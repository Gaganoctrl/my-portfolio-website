from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# Sample projects data
projects = [
    {
        "id": 1,
        "title": "Portfolio Website",
        "description": "A beautiful portfolio website built with HTML, CSS, and JavaScript",
        "technologies": ["HTML", "CSS", "JavaScript"],
        "link": "https://github.com/Gaganoctrl/my-portfolio-website",
        "date": "2025-12-12"
    },
    {
        "id": 2,
        "title": "Interactive Web App",
        "description": "A responsive web application with Python backend",
        "technologies": ["Python", "Flask", "JavaScript"],
        "link": "#",
        "date": "2025-12-12"
    },
    {
        "id": 3,
        "title": "AI Chat Assistant",
        "description": "An intelligent chatbot powered by machine learning",
        "technologies": ["Python", "NLP", "React"],
        "link": "#",
        "date": "2025-12-11"
    }
]

# Routes
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Portfolio API",
        "version": "1.0",
        "endpoints": {
            "projects": "/api/projects",
            "project": "/api/projects/<id>",
            "contact": "/api/contact",
            "stats": "/api/stats"
        }
    })

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Get all projects"""
    return jsonify({
        "success": True,
        "count": len(projects),
        "projects": projects
    })

@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Get a specific project by ID"""
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return jsonify({"success": True, "project": project})
    return jsonify({"success": False, "error": "Project not found"}), 404

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    data = request.json
    
    # Validate required fields
    required = ['name', 'email', 'message']
    if not all(field in data for field in required):
        return jsonify({"success": False, "error": "Missing required fields"}), 400
    
    # Log the message (in real app, send email or save to database)
    print(f"New message from {data['name']} ({data['email']}): {data['message']}")
    
    return jsonify({
        "success": True,
        "message": "Thank you for your message! I'll get back to you soon.",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/stats', methods=['GET'])
def stats():
    """Get portfolio statistics"""
    return jsonify({
        "total_projects": len(projects),
        "technologies_used": list(set(tech for p in projects for tech in p['technologies'])),
        "last_updated": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
