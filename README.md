# MITS Chatbot - Your Virtual Assistant

🎓 **Madanapalle Institute of Technology & Science (MITS) Chatbot** - An intelligent virtual assistant providing comprehensive information about MITS college.

## 🌟 Features

### 🎨 Multiple UI Versions
- **Original UI**: Classic chatbot interface
- **Enhanced UI**: Modern design with advanced features
- **Unique UI**: Premium experience with dark mode, voice input, and animations

### 🚀 Advanced Capabilities
- **Voice Input**: Speak your questions using Web Speech API
- **Dark/Light Mode**: Toggle between themes
- **Real-time Typing Indicator**: Shows when bot is processing
- **Message Timestamps**: Track conversation history
- **Persistent Chat History**: Conversations saved in local storage
- **Custom Avatars**: User and bot avatars for better UX
- **Smooth Animations**: Beautiful slide-in effects for messages
- **Emoji Support**: Add emojis to your messages
- **Responsive Design**: Works on all devices

### 🏫 MITS Information Available
- College overview and history
- Academic departments and courses
- Campus facilities and infrastructure
- Recent activities and events
- Location and contact information
- Admission procedures
- AI/ML department details

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with CSS Variables, Font Awesome icons
- **Features**: Web Speech API, Local Storage, Responsive Design

## 📁 Project Structure

```
mits_chatbot/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Original UI
│   ├── enhanced_index.html    # Enhanced UI
│   ├── unique_index.html      # Unique UI with advanced features
│   └── test_unique.html       # Test UI for debugging
├── mits_data.json            # College information database
├── scraper.py                # Web scraping utilities
├── run_chatbot.bat           # Windows batch file to run server
├── run_unique_chatbot.bat    # Batch file with multiple UI options
└── README.md                 # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mits-chatbot.git
   cd mits-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```
   
   Or use the batch file (Windows):
   ```bash
   run_unique_chatbot.bat
   ```

### 🌐 Access the Application

- **Original UI**: http://localhost:5000/
- **Enhanced UI**: http://localhost:5000/unique
- **Test UI**: http://localhost:5000/test

## 🎯 Usage

### Basic Queries
- "Tell me about MITS"
- "What courses are available?"
- "What are the facilities?"
- "How do I apply for admission?"
- "Where is MITS located?"
- "What are the latest news?"

### Advanced Features (Unique UI)
- **Voice Input**: Click the microphone icon and speak
- **Dark Mode**: Click the moon/sun icon in the header
- **Clear Chat**: Click the trash icon to reset conversation
- **Emoji**: Click the smile icon to add emojis
- **Refresh Data**: Click the refresh icon to update information

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV`: Set to 'development' for debug mode
- `FLASK_APP`: Set to 'app.py'

### Customization
- **Update College Info**: Modify `MITS_INFO` dictionary in `app.py`
- **Styling**: Edit CSS variables in template files
- **Add New Routes**: Extend `app.py` with additional endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 API Endpoints

- `GET /`: Original chatbot interface
- `GET /unique`: Advanced UI with premium features
- `GET /test`: Test interface for debugging
- `POST /chat`: Send message to chatbot
- `POST /refresh_data`: Refresh college information
- `GET /health`: Health check endpoint

## 🎨 UI Themes

### Light Theme (Default)
- Clean, modern design
- Blue and green color scheme
- Optimized for readability

### Dark Theme
- Easy on the eyes
- Dark background with light text
- Perfect for low-light environments

## 📱 Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

**Note**: Voice input requires browsers with Web Speech API support

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Integration with college database
- [ ] Push notifications
- [ ] Mobile app version
- [ ] Advanced NLP capabilities
- [ ] File upload support
- [ ] Video chat integration

## 🐛 Known Issues

- Voice input may not work in all browsers
- Some features require modern browser support
- Local storage has size limitations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- MITS College for providing the information
- Font Awesome for icons
- Flask community for the excellent framework
- Web Speech API for voice functionality

## 📞 Support

For support, email your.email@example.com or create an issue in the GitHub repository.

---

**Made with ❤️ for MITS Community**

# MITS Chatbot - College Information Assistant

A user-friendly chatbot/agent for Madanapalle Institute of Technology & Science (MITS) that provides comprehensive information about the college by scraping data from mits.ac.in and combining it with curated knowledge.

## Features

- **Real-time Information**: Scrapes latest data from mits.ac.in
- **Comprehensive Knowledge Base**: Covers all aspects of MITS including:
  - General information and history
  - Academic programs and departments
  - Campus facilities and infrastructure
  - Latest news and events
  - Admission procedures
  - Location and contact information
  - Student activities and clubs
- **User-Friendly Interface**: Modern, responsive web interface
- **Quick Suggestions**: Pre-built questions for easy interaction
- **Auto-refresh**: Automatically updates data from website
- **Typing Indicators**: Real-time chat experience

## Project Structure

```
mits_chatbot/
├── app.py                 # Basic Flask application
├── enhanced_app.py        # Enhanced version with web scraping
├── scraper.py            # Web scraper for mits.ac.in
├── requirements.txt      # Python dependencies
├── templates/
│   ├── index.html        # Basic UI template
│   └── enhanced_index.html # Enhanced UI template
└── README.md            # This file
```

## Installation

1. **Clone or create the project directory**:
   ```bash
   mkdir mits_chatbot
   cd mits_chatbot
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Required packages**:
   - Flask==2.3.3
   - requests==2.31.0
   - python-dotenv==1.0.0
   - beautifulsoup4==4.12.2
   - lxml==4.9.3

## Usage

### Option 1: Basic Chatbot (Static Data)

Run the basic version with static information:

```bash
python app.py
```

### Option 2: Enhanced Chatbot (With Web Scraping)

Run the enhanced version with real-time data from mits.ac.in:

```bash
python enhanced_app.py
```

### Option 3: Run Web Scraper Separately

To scrape data manually:

```bash
python scraper.py
```

## Accessing the Chatbot

1. Open your web browser
2. Navigate to `http://localhost:5000`
3. Start chatting with the MITS Chatbot!

## Available Endpoints

- `/` - Main chatbot interface
- `/chat` - POST endpoint for chat messages
- `/refresh_data` - POST endpoint to refresh scraped data
- `/health` - Health check endpoint

## Sample Questions

Try asking the chatbot:

- "Tell me about MITS"
- "What courses are available?"
- "What are the facilities?"
- "How do I apply for admission?"
- "What are the latest news?"
- "Where is MITS located?"
- "Tell me about AI and Machine Learning at MITS"
- "What are the recent activities?"

## Features Highlights

### 🎓 Comprehensive Information
- Detailed information about MITS history, vision, and mission
- Complete list of departments and programs
- Campus facilities and infrastructure details
- Latest news and events from the website

### 🌐 Real-time Updates
- Automatic data scraping from mits.ac.in
- Cached data for better performance
- Manual refresh option for latest information

### 💬 User-Friendly Interface
- Modern, responsive design
- Quick suggestion buttons
- Typing indicators for better UX
- Mobile-friendly layout

### 🔍 Smart Responses
- Context-aware responses
- Keyword-based matching
- Fallback responses for unknown queries
- Formatted output with emojis and structure

## Technical Details

### Web Scraping
- Uses BeautifulSoup4 and requests for scraping
- Handles news, events, and department information
- Graceful error handling for network issues
- Respects website structure and performance

### Data Management
- JSON-based data storage
- Automatic data refresh every 6 hours
- Fallback to static data if scraping fails
- Conversation history tracking

### Security
- Input validation and sanitization
- Rate limiting considerations
- Error handling and logging
- Safe HTML rendering

## Customization

### Adding New Topics
To add new topics or improve responses:

1. Edit the `get_response()` method in `enhanced_app.py`
2. Add new keywords and response patterns
3. Update the static `MITS_INFO` dictionary for fallback data

### Modifying Scraping
To scrape additional information:

1. Edit the `scraper.py` file
2. Add new scraping methods
3. Update the data structure in `enhanced_app.py`

### UI Customization
To modify the interface:

1. Edit `templates/enhanced_index.html`
2. Update CSS styles for appearance
3. Add new features or buttons

## Troubleshooting

### Common Issues

1. **Port already in use**: Change port in app.py/enhanced_app.py
2. **Scraping errors**: Check internet connection and website availability
3. **Dependencies missing**: Run `pip install -r requirements.txt`
4. **Template not found**: Ensure templates folder exists

### Performance Optimization

- Data is cached to reduce server load
- Automatic updates every 6 hours
- Lightweight responses for better speed
- Efficient HTML parsing

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make improvements
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes and is designed to help students and prospective students get information about MITS.

## Support

For issues or questions:
- Check the troubleshooting section
- Review the code comments
- Test with different browsers
- Verify all dependencies are installed

## Future Enhancements

Potential improvements:
- Natural Language Processing for better understanding
- Multi-language support
- Voice interaction capabilities
- Integration with college databases
- Mobile app version
- Analytics and usage tracking

---

**Note**: This chatbot is designed to provide general information about MITS. For official and detailed information, please visit the official MITS website at https://mits.ac.in
