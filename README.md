# my-portfolio-website

A full-stack portfolio website with a **Python Flask backend** and a modern front-end.

## 🚀 Features

### Frontend
- Beautiful responsive design with gradient header
- Smooth scrolling navigation
- Scroll animations for project cards
- Modern UI with hover effects

### Backend (Python + Flask)
- RESTful API endpoints
- CORS-enabled for cross-origin requests
- Project management endpoints
- Contact form handling
- Portfolio statistics API

## 📂 Project Structure

```
my-portfolio-website/
├── index.html          # Main HTML file
├── styles.css          # CSS styling
├── script.js           # Frontend JavaScript
├── app.py              # Flask Python backend
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3 (with gradients and animations)
- JavaScript (ES6+)

**Backend:**
- Python 3.x
- Flask 2.3.3
- Flask-CORS 4.0.0
- Gunicorn (for production)

## 🔧 Installation & Setup

### Frontend (GitHub Pages)
The website is already deployed at: `https://gaganoctrl.github.io/my-portfolio-website/`

### Backend (Local Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gaganoctrl/my-portfolio-website.git
   cd my-portfolio-website
   ```

2. **Create a Python virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

   The API will be available at `http://localhost:5000`

## 📡 API Endpoints

### GET `/`
Welcome message with all available endpoints

### GET `/api/projects`
Get all projects
```json
{
  "success": true,
  "count": 3,
  "projects": [...]
}
```

### GET `/api/projects/<id>`
Get a specific project by ID

### POST `/api/contact`
Submit a contact form
```json
{
  "name": "Your Name",
  "email": "your@email.com",
  "message": "Your message"
}
```

### GET `/api/stats`
Get portfolio statistics
```json
{
  "total_projects": 3,
  "technologies_used": ["Python", "HTML", "CSS", ...],
  "last_updated": "2025-12-12T..."
}
```

## 🚀 Deployment

### Deploy Backend to Heroku (Free)
1. Create a `Procfile`
   ```
   web: gunicorn app:app
   ```

2. Push to Heroku
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Deploy Backend to Vercel
Create `api/index.py` for Vercel serverless functions

## 💡 Usage Examples

### Fetch projects from frontend
```javascript
fetch('http://localhost:5000/api/projects')
  .then(res => res.json())
  .then(data => console.log(data.projects))
```

### Submit contact form
```javascript
fetch('http://localhost:5000/api/contact', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'John',
    email: 'john@example.com',
    message: 'Hello!'
  })
})
```

## 📝 Customization

### Add More Projects
Edit `app.py` and add to the `projects` list:
```python
{
  "id": 4,
  "title": "My New Project",
  "description": "...",
  "technologies": [...],
  "link": "...",
  "date": "2025-12-12"
}
```

### Connect to Database
Replace the in-memory `projects` list with a database like MongoDB or PostgreSQL

## 📸 Screenshots

Visit the live site: [Portfolio Website](https://gaganoctrl.github.io/my-portfolio-website/)

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📄 License

MIT License - feel free to use this project for your own portfolio!

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [GitHub Pages Guide](https://pages.github.com/)

---

**Created with ❤️ by Gagan**
