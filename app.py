from flask import Flask, request, jsonify, render_template
import json
import re
from datetime import datetime
import os

app = Flask(__name__)

# MITS College Information Database
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

class MITSChatbot:
    def __init__(self):
        self.conversation_history = []
        
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Store conversation
        self.conversation_history.append({
            "user": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # Greeting responses
        if any(greeting in user_input for greeting in ["hi", "hello", "hey", "good morning", "good afternoon"]):
            return "Hello! Welcome to MITS (Madanapalle Institute of Technology & Science). I'm here to help you with information about our college. How can I assist you today?"
        
        # About MITS
        if any(word in user_input for word in ["about", "tell me about", "what is", "information"]):
            return f"""
            **About MITS:**
            
            {MITS_INFO['about']['name']} was established in {MITS_INFO['about']['established']} in the picturesque environs of {MITS_INFO['about']['location']}. 
            
            🏫 **Campus:** {MITS_INFO['about']['campus_size']} sprawling campus
            📍 **Location:** {MITS_INFO['about']['highway']}, near Angallu
            🎯 **Vision:** {MITS_INFO['vision']}
            
            MITS originated under the Ratakonda Ranga Reddy Educational Academy and offers amazing freedom to explore, experiment, and collaborate with a real-world perspective.
            """
        
        # Courses/Departments
        if any(word in user_input for word in ["courses", "departments", "programs", "branches", "streams"]):
            dept_list = "\n".join([f"• {dept}" for dept in MITS_INFO['departments']])
            return f"""
            **Departments at MITS:**
            
            {dept_list}
            
            We offer B.Tech programs in these departments with a focus on innovation and real-world applications.
            """
        
        # Facilities
        if any(word in user_input for word in ["facilities", "infrastructure", "campus life", "clubs"]):
            facilities_list = "\n".join([f"• {facility}" for facility in MITS_INFO['facilities']])
            return f"""
            **Facilities at MITS:**
            
            {facilities_list}
            
            Our campus provides a comprehensive environment for learning and personal development.
            """
        
        # Recent activities/events
        if any(word in user_input for word in ["events", "activities", "recent", "news", "updates"]):
            activities_list = "\n".join([f"• {activity}" for activity in MITS_INFO['recent_activities']])
            return f"""
            **Recent Activities at MITS:**
            
            {activities_list}
            
            We regularly organize various technical and cultural events to enhance student experience.
            """
        
        # Location/Contact
        if any(word in user_input for word in ["location", "address", "contact", "where", "how to reach"]):
            return f"""
            **MITS Location & Contact:**
            
            📍 **Address:** Near Angallu, Madanapalle - Anantapur Highway (NH-205)
            📏 **Distance:** About 10km from Madanapalle
            🌐 **Website:** {MITS_INFO['contact']['website']}
            
            The campus is easily accessible via the national highway and offers a serene environment for learning.
            """
        
        # Admissions
        if any(word in user_input for word in ["admission", "apply", "eligibility", "entrance"]):
            return """
            **Admissions at MITS:**
            
            For detailed admission information:
            • Visit our website: https://mits.ac.in
            • Contact the admissions office directly
            • Check eligibility criteria for B.Tech programs
            
            We welcome students who are passionate about technology and innovation!
            """
        
        # AI/ML specific
        if any(word in user_input for word in ["ai", "artificial intelligence", "machine learning", "ml"]):
            return """
            **AI & Machine Learning at MITS:**
            
            🤖 We have a dedicated Computer Science and Engineering (Artificial Intelligence and Machine Learning) department
            🔬 Regular workshops on AI and ML technologies
            💡 Focus on cutting-edge research and practical applications
            
            Our AI/ML program is designed to prepare students for the future of technology.
            """
        
        # Default response
        return """
        I'm here to help you with information about MITS! You can ask me about:
        
        • About MITS and its history
        • Courses and departments
        • Campus facilities
        • Recent events and activities
        • Location and contact information
        • Admissions process
        
        What would you like to know?
        """

# Initialize chatbot
chatbot = MITSChatbot()

@app.route('/')
def index():
    return render_template('demo.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = chatbot.get_response(user_message)
    return jsonify({'response': response})

@app.route('/refresh_data', methods=['POST'])
def refresh_data():
    # Simulate data refresh (you can implement actual data refresh logic here)
    try:
        # Here you could refresh your MITS_INFO data from an external source
        # For now, we'll just return success
        return jsonify({'status': 'success', 'message': 'Data refreshed successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'MITS Chatbot'})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
