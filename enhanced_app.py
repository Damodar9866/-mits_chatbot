from flask import Flask, request, jsonify, render_template
import json
import re
from datetime import datetime, timedelta
import os
from scraper import MITSScraper

app = Flask(__name__)

# MITS College Information Database (Static fallback data)
MITS_INFO = {
    "about": {
        "name": "Madanapalle Institute of Technology & Science (MITS)",
        "established": "1998",
        "location": "Madanapalle, Andhra Pradesh, India",
        "campus_size": "26.17 acres",
        "highway": "Madanapalle - Anantapur Highway (NH-205)",
        "distance_from_madanapalle": "10km",
        "founder": "Late Sri. N. Krishna Kumar M.S. (U.S.A)",
        "secretary": "Dr. N. Vijaya Bhaskar Choudary, Ph.D.",
        "academy": "Ratakonda Ranga Reddy Educational Academy"
    },
    "vision": "To develop as one of the best centers of Academic Excellence in India",
    "mission": "Learning, Expression, Discourse & Innovation",
    "values": [
        "Amazing freedom to explore",
        "Freedom to experiment",
        "Freedom to collaborate",
        "Real-World perspective",
        "Innovation spirit",
        "Empathy and Humanity",
        "Technology-powered learning"
    ],
    "departments": [
        "Computer Science and Engineering",
        "Artificial Intelligence and Machine Learning",
        "Electronics and Communication Engineering",
        "Electrical and Electronics Engineering",
        "Mechanical Engineering",
        "Civil Engineering"
    ],
    "facilities": [
        "Student Activity Centre (SAC)",
        "Yoga & Meditation Club",
        "Tech Club",
        "Library",
        "Laboratories",
        "Sports facilities",
        "Hostels"
    ],
    "recent_activities": [
        "Tech Intellect Challenge by Tech Club",
        "AI and Machine Learning Workshop by CSE(AI&ML) Department",
        "MoU signed with Aizu University, Japan",
        "Various programs organized by Student Activity Centre"
    ],
    "contact": {
        "website": "https://mits.ac.in",
        "location": "Near Angallu, Madanapalle - Anantapur Highway (NH-205)"
    }
}

class EnhancedMITSChatbot:
    def __init__(self):
        self.conversation_history = []
        self.scraper = MITSScraper()
        self.scraped_data = {}
        self.last_update = None
        self.update_interval = timedelta(hours=6)  # Update every 6 hours
        
    def update_scraped_data(self):
        """Update scraped data if needed"""
        if (not self.last_update or 
            datetime.now() - self.last_update > self.update_interval):
            try:
                self.scraped_data = self.scraper.load_data()
                if not self.scraped_data:
                    print("No cached data found, scraping fresh data...")
                    self.scraped_data = self.scraper.scrape_all_data()
                    self.scraper.save_data(self.scraped_data)
                self.last_update = datetime.now()
            except Exception as e:
                print(f"Error updating scraped data: {e}")
                self.scraped_data = {}
        
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Update scraped data if needed
        self.update_scraped_data()
        
        # Store conversation
        self.conversation_history.append({
            "user": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # Greeting responses
        if any(greeting in user_input for greeting in ["hi", "hello", "hey", "good morning", "good afternoon"]):
            return """
            🎓 **Welcome to MITS Chatbot!**
            
            Hello! I'm your virtual assistant for Madanapalle Institute of Technology & Science (MITS). 
            I can help you with information about our college, including:
            
            • General information about MITS
            • Academic programs and departments
            • Campus facilities and infrastructure
            • Recent news and events
            • Admission procedures
            • Contact information
            
            What would you like to know about MITS?
            """
        
        # News and recent updates
        if any(word in user_input for word in ["news", "latest", "recent", "updates", "announcements"]):
            response = "**Latest News & Updates from MITS:**\n\n"
            
            # Add scraped news if available
            if self.scraped_data.get('homepage', {}).get('news'):
                response += "📰 **Recent News:**\n"
                for news_item in self.scraped_data['homepage']['news'][:3]:
                    response += f"• {news_item}\n"
                response += "\n"
            
            # Add scraped events if available
            if self.scraped_data.get('homepage', {}).get('events'):
                response += "🎉 **Recent Events:**\n"
                for event_item in self.scraped_data['homepage']['events'][:3]:
                    response += f"• {event_item}\n"
                response += "\n"
            
            # Add static recent activities as fallback
            response += "🏆 **Recent Activities:**\n"
            for activity in MITS_INFO['recent_activities']:
                response += f"• {activity}\n"
            
            if self.scraped_data.get('last_updated'):
                response += f"\n*Last updated: {self.scraped_data['last_updated'][:19]}*"
            
            return response
        
        # About MITS
        if any(word in user_input for word in ["about", "tell me about", "what is", "information"]):
            return f"""
            🏫 **About MITS:**
            
            {MITS_INFO['about']['name']} was established in {MITS_INFO['about']['established']} in the picturesque environs of {MITS_INFO['about']['location']}.
            
            📍 **Campus:** {MITS_INFO['about']['campus_size']} sprawling campus on {MITS_INFO['about']['highway']}, near Angallu
            🎯 **Vision:** {MITS_INFO['vision']}
            🎪 **Mission:** {MITS_INFO['mission']}
            
            **Leadership:**
            • Founder: {MITS_INFO['about']['founder']}
            • Secretary & Correspondent: {MITS_INFO['about']['secretary']}
            • Academy: {MITS_INFO['about']['academy']}
            
            MITS offers amazing freedom to explore, experiment, and collaborate with a real-world perspective, powered by technology and driven by innovation.
            """
        
        # Courses/Departments
        if any(word in user_input for word in ["courses", "departments", "programs", "branches", "streams"]):
            dept_list = "\n".join([f"• {dept}" for dept in MITS_INFO['departments']])
            response = f"""
            🎓 **Academic Programs at MITS:**
            
            {dept_list}
            
            We offer B.Tech programs in these departments with a focus on:
            • Innovation and real-world applications
            • Hands-on learning experience
            • Industry-relevant curriculum
            • Research and development opportunities
            """
            
            # Add scraped department info if available
            if self.scraped_data.get('departments'):
                response += "\n\n📚 **Additional Department Information:**\n"
                for dept_name, dept_url in list(self.scraped_data['departments'].items())[:3]:
                    response += f"• {dept_name}\n"
            
            return response
        
        # Facilities
        if any(word in user_input for word in ["facilities", "infrastructure", "campus life", "clubs"]):
            facilities_list = "\n".join([f"• {facility}" for facility in MITS_INFO['facilities']])
            return f"""
            🏢 **Campus Facilities at MITS:**
            
            {facilities_list}
            
            **Campus Life:**
            • State-of-the-art laboratories and equipment
            • Modern library with digital resources
            • Sports and recreational facilities
            • Active student clubs and societies
            • Comfortable hostel accommodation
            • Cafeteria and dining facilities
            
            Our campus provides a comprehensive environment for learning, research, and personal development.
            """
        
        # Admissions
        if any(word in user_input for word in ["admission", "apply", "eligibility", "entrance"]):
            response = """
            🎓 **Admissions at MITS:**
            
            **B.Tech Programs Available:**
            • Computer Science and Engineering
            • Artificial Intelligence and Machine Learning
            • Electronics and Communication Engineering
            • Electrical and Electronics Engineering
            • Mechanical Engineering
            • Civil Engineering
            
            **General Information:**
            • Visit our website: https://mits.ac.in
            • Contact the admissions office directly
            • Check eligibility criteria for specific programs
            • Application deadlines and procedures
            
            We welcome students who are passionate about technology and innovation!
            """
            
            # Add scraped admission info if available
            if self.scraped_data.get('admissions', {}).get('admission_info'):
                response += "\n\n📋 **Latest Admission Updates:**\n"
                for info in self.scraped_data['admissions']['admission_info'][:2]:
                    response += f"• {info}\n"
            
            return response
        
        # Location/Contact
        if any(word in user_input for word in ["location", "address", "contact", "where", "how to reach"]):
            return f"""
            📍 **MITS Location & Contact:**
            
            **Address:** Near Angallu, Madanapalle - Anantapur Highway (NH-205)
            **Distance:** About 10km from Madanapalle
            **Campus Size:** 26.17 acres
            **Website:** {MITS_INFO['contact']['website']}
            
            **How to Reach:**
            • Located on National Highway NH-205
            • Easily accessible from Madanapalle
            • Well-connected by road transport
            • Serene environment ideal for learning
            
            The campus offers a peaceful and conducive atmosphere for academic excellence.
            """
        
        # AI/ML specific
        if any(word in user_input for word in ["ai", "artificial intelligence", "machine learning", "ml"]):
            return """
            🤖 **AI & Machine Learning at MITS:**
            
            **Department:** Computer Science and Engineering (Artificial Intelligence and Machine Learning)
            
            **Programs & Activities:**
            • Dedicated AI/ML curriculum
            • Regular workshops on AI and ML technologies
            • Hands-on projects and research opportunities
            • Industry collaboration and internships
            • Latest tools and technologies
            
            **Recent Highlights:**
            • AI and Machine Learning Workshop organized by CSE(AI&ML) Department
            • Focus on cutting-edge research and practical applications
            • Preparing students for the future of technology
            
            Our AI/ML program is designed to create skilled professionals ready for the digital transformation era.
            """
        
        # International collaborations
        if any(word in user_input for word in ["international", "collaboration", "mou", "japan", "aizu"]):
            return """
            🌍 **International Collaborations:**
            
            **Recent Achievement:**
            • MITS has signed a prestigious Memorandum of Understanding (MoU) with Aizu University, Japan
            • This marks a significant milestone in international academic collaboration
            
            **Benefits:**
            • Student exchange programs
            • Joint research opportunities
            • Faculty collaboration
            • Enhanced global exposure
            • International academic standards
            
            This collaboration opens new avenues for our students and faculty to engage with international academic communities.
            """
        
        # Tech Club
        if any(word in user_input for word in ["tech club", "technical", "competition", "challenge"]):
            return """
            💻 **Tech Club at MITS:**
            
            **Recent Activities:**
            • Tech Intellect Challenge - An exciting competition to test and sharpen technical and analytical skills
            • Regular technical workshops and seminars
            • Coding competitions and hackathons
            • Industry expert sessions
            
            **Focus Areas:**
            • Programming and software development
            • Emerging technologies
            • Innovation and problem-solving
            • Skill development
            
            The Tech Club provides an excellent platform for students to enhance their technical skills and stay updated with latest technologies.
            """
        
        # Help/Commands
        if any(word in user_input for word in ["help", "commands", "what can you do"]):
            return """
            🤝 **How I Can Help You:**
            
            **Information Available:**
            • **About MITS** - History, vision, mission, and general information
            • **Academic Programs** - Departments, courses, and curriculum
            • **Campus Facilities** - Infrastructure, labs, library, hostels
            • **Admissions** - Procedures, eligibility, and requirements
            • **News & Events** - Latest updates and announcements
            • **Location & Contact** - Address, directions, and contact details
            • **Special Programs** - AI/ML, international collaborations
            • **Student Life** - Clubs, activities, and campus culture
            
            **How to Ask:**
            Just type your question naturally! For example:
            • "Tell me about MITS"
            • "What courses are available?"
            • "How do I apply for admission?"
            • "What are the latest news?"
            
            I'm here to help you with any information about MITS!
            """
        
        # Default response
        return """
        🤔 **I'm here to help you learn about MITS!**
        
        I can provide information about:
        • About MITS and its history
        • Academic programs and departments
        • Campus facilities and infrastructure
        • Latest news and events
        • Admission procedures
        • Location and contact details
        • Student activities and clubs
        
        **Try asking me:**
        • "What is MITS?"
        • "Tell me about the courses"
        • "What facilities are available?"
        • "How can I apply for admission?"
        • "What's the latest news?"
        
        What would you like to know about MITS?
        """

# Initialize enhanced chatbot
chatbot = EnhancedMITSChatbot()

@app.route('/')
def index():
    return render_template('enhanced_index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = chatbot.get_response(user_message)
    return jsonify({'response': response})

@app.route('/refresh_data', methods=['POST'])
def refresh_data():
    """Endpoint to manually refresh scraped data"""
    try:
        chatbot.scraped_data = chatbot.scraper.scrape_all_data()
        chatbot.scraper.save_data(chatbot.scraped_data)
        chatbot.last_update = datetime.now()
        return jsonify({'status': 'success', 'message': 'Data refreshed successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy', 
        'service': 'Enhanced MITS Chatbot',
        'last_data_update': chatbot.last_update.isoformat() if chatbot.last_update else None
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
