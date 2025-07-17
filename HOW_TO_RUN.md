# How to Run the MITS Chatbot

## 📋 **Complete Step-by-Step Guide**

### **Method 1: Using Batch Files (Easiest)**

1. **Double-click** `run_chatbot.bat` for the enhanced version with web scraping
   - OR -
2. **Double-click** `run_basic_chatbot.bat` for the basic version with static data

### **Method 2: Using Command Line**

#### **Step 1: Open Command Prompt or PowerShell**
- Press `Win + R`, type `cmd`, and press Enter
- Or press `Win + X` and select "Windows PowerShell"

#### **Step 2: Navigate to the Project Directory**
```bash
cd "C:\Users\damod\mits_chatbot"
```

#### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 4: Run the Chatbot**

**For Enhanced Version (with Web Scraping):**
```bash
python enhanced_app.py
```

**For Basic Version (Static Data):**
```bash
python app.py
```

#### **Step 5: Access the Chatbot**
1. Open your web browser
2. Go to: `http://localhost:5000`
3. Start chatting!

---

## 🚀 **Quick Start Commands**

```bash
# Navigate to project
cd "C:\Users\damod\mits_chatbot"

# Install dependencies
pip install -r requirements.txt

# Run enhanced chatbot
python enhanced_app.py
```

---

## 🌐 **Accessing the Chatbot**

Once running, the chatbot will be available at:
- **Primary URL:** http://localhost:5000
- **Alternative:** http://127.0.0.1:5000

---

## 🛠️ **Available Options**

### **Enhanced Version** (`enhanced_app.py`)
- ✅ Real-time data from mits.ac.in
- ✅ Beautiful modern interface
- ✅ Auto-refresh capability
- ✅ Latest news and events
- ✅ Comprehensive information

### **Basic Version** (`app.py`)
- ✅ Static information about MITS
- ✅ Fast and reliable
- ✅ Simple interface
- ✅ No internet required

---

## 🧪 **Testing the Scraper**

To test the web scraper separately:
```bash
python scraper.py
```

This will create/update `mits_data.json` with the latest data from the website.

---

## 💬 **Sample Questions to Try**

- "Tell me about MITS"
- "What courses are available?"
- "What are the facilities?"
- "How do I apply for admission?"
- "What's the latest news?"
- "Where is MITS located?"
- "Tell me about AI and Machine Learning"

---

## 🔧 **Troubleshooting**

### **Common Issues:**

1. **"Module not found" error:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Port already in use:**
   - Stop any running Python processes
   - Or change port in the `.py` files

3. **Web scraping not working:**
   - Check internet connection
   - Run basic version instead

4. **Browser not opening:**
   - Manually go to http://localhost:5000
   - Check if server is running

---

## 📱 **Features You Can Use**

- **Quick Questions:** Click the suggestion buttons
- **Refresh Data:** Click the refresh button in enhanced version
- **Mobile Friendly:** Works on phones and tablets
- **Real-time Chat:** Typing indicators and smooth interface

---

## 🛑 **To Stop the Server**

Press `Ctrl + C` in the command prompt/terminal where the server is running.

---

## 📂 **Project Files**

- `enhanced_app.py` - Main chatbot with web scraping
- `app.py` - Basic chatbot with static data
- `scraper.py` - Web scraper for mits.ac.in
- `templates/` - HTML templates for the interface
- `requirements.txt` - Python dependencies
- `run_chatbot.bat` - Easy launcher for enhanced version
- `run_basic_chatbot.bat` - Easy launcher for basic version

---

## 🎯 **Success Indicators**

You'll know it's working when you see:
```
* Running on http://127.0.0.1:5000
* Running on http://192.168.1.27:5000
```

Then open your browser and go to `http://localhost:5000`

---

**Need help?** Check the README.md file for more detailed information!
