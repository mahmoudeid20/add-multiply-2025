# ⚡ Add & Multiply Calculator — 2025 Edition

A futuristic web application built with Python (Flask) and Docker, allowing users to input two numbers and instantly get their Sum and Product in a smooth, animated interface.  
Designed with a 2025-level UI, it combines clean aesthetics, responsive layout, and a lightweight backend for high performance.
---
🖥️ Live Demo
> *(Add your deployment link here once hosted — e.g. Render / Railway / GitHub Pages)*
---
✨ Features
- 🧮 Real-time addition and multiplication  
- 🎨 Modern animated interface (HTML + CSS)  
- ⚙️ Fully containerized using Docker  
- 💻 Responsive design for desktop & mobile  
- 🔒 Lightweight, fast, and production-ready  
---

🧩 Project Structure

add-multiply-2025/
│
├── Dockerfile # Docker build configuration
├── requirements.txt # Python dependencies
├── app.py # Flask web app
│
├── templates/
│ └── index.html # HTML user interface
│
└── static/
└── style.css # Styling and animations

---
🐳 Run the App Locally with Docker

1️⃣ Build the Docker image
   bash:
   docker build -t add-multiply-2025 .
   docker run -p 8080:5000 add-multiply-2025
2️⃣ Run the container
   bash:
   docker run -p 8080:5000 add-multiply-2025

Then open your browser and visit:
👉 http://localhost:8080
![App Screenshot]<img width="1365" height="731" alt="image" src="https://github.com/user-attachments/assets/5d3bc54e-094d-4d7f-a0b9-6eae4d08637d" />


