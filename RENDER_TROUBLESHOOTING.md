# 🔧 Render Deployment Troubleshooting Guide

## Common Issues and Solutions

### 1. **Update Render Configuration**

In your Render dashboard:

1. **Go to your service settings**
2. **Update Build Command**: `pip install -r requirements.txt`
3. **Update Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
4. **Set Environment Variables**:
   - `PYTHON_VERSION`: `3.9.16`
   - `FLASK_ENV`: `production`
   - `PORT`: `10000`

### 2. **Check Build Logs**

Look for these common errors:

**Error**: `ModuleNotFoundError: No module named 'gunicorn'`
**Solution**: Updated requirements.txt includes Gunicorn now

**Error**: `Port binding issues`
**Solution**: App now uses `PORT` environment variable

**Error**: `Template not found`
**Solution**: Verify templates folder structure

### 3. **Force Redeploy**

1. **Go to Render dashboard**
2. **Click your service**
3. **Click "Manual Deploy"**
4. **Select "Deploy latest commit"**

### 4. **Check Your URLs**

After deployment, test these URLs:
- `https://your-app-name.onrender.com/` (Basic UI)
- `https://your-app-name.onrender.com/unique` (Unique UI)
- `https://your-app-name.onrender.com/test` (Test UI)
- `https://your-app-name.onrender.com/health` (Health check)

### 5. **Common Fixes Applied**

✅ **Added Gunicorn** for better production server
✅ **Updated requirements.txt** with all dependencies
✅ **Fixed port binding** to use environment variables
✅ **Added Procfile** for alternative deployment
✅ **Improved render.yaml** configuration

### 6. **If Still Not Working**

**Check Browser Console** (F12):
- Look for JavaScript errors
- Check for failed network requests
- Verify CDN resources are loading

**Test Different Routes**:
- Try `/test` route first (simpler UI)
- Then try `/unique` route (advanced UI)
- Check if `/health` returns JSON

**Verify Flask App**:
- Ensure `app.py` is in root directory
- Check that templates folder exists
- Verify all imports are correct

### 7. **Manual Deployment Steps**

If automatic deployment fails:

1. **Clone your repo locally**
2. **Test locally first**:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
3. **If local works, push to GitHub**
4. **Trigger manual deploy in Render**

### 8. **Alternative Start Commands**

If current doesn't work, try:
- `python app.py`
- `gunicorn --bind 0.0.0.0:$PORT app:app`
- `python -m flask run --host=0.0.0.0 --port=$PORT`

### 9. **Check Service Status**

In Render dashboard:
- **Service Status**: Should be "Live"
- **Build Status**: Should be "Build successful"
- **Deploy Status**: Should be "Deploy successful"

### 10. **Contact Support**

If issues persist:
- Check Render status page
- Review deployment logs completely
- Contact Render support with specific error messages

## Quick Test Script

Run this locally to verify your app works:

```bash
# Test all routes
curl http://localhost:5000/
curl http://localhost:5000/unique
curl http://localhost:5000/test
curl http://localhost:5000/health

# Test chat functionality
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "hello"}'
```

## Expected Behavior

**Working Demo Should Show**:
- ✅ Responsive chatbot interface
- ✅ Dark/light mode toggle
- ✅ Voice input button (microphone)
- ✅ Emoji support
- ✅ Smooth animations
- ✅ Real-time chat functionality
- ✅ Multiple UI versions accessible

---

**After pushing these fixes, your Render deployment should work perfectly! 🚀**
