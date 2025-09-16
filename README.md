# 🌍 AlertMap – Disaster Explorer

🚀 Built for the NASA International Space Apps Challenge (24-hour national-level hackathon).

AlertMap is a 3D interactive disaster visualization tool that lets users explore, analyze, and report disasters such as fires, floods, and meteorite impacts on a global scale.


# ✨ Features

🌐 CesiumJS 3D Globe – immersive visualization of Earth
🔥 Disaster Layers – toggle between Fires, Floods, and Meteorites
📍 Interactive Popups – click on markers to see detailed event info (location, date, intensity, etc.)
📑 Instant PDF Reports – generate reports for:
  A single clicked disaster
  The overall global view
⚡ Client-side only – no backend required
🗂 GeoJSON datasets – cleaned and processed using Python


# 🛠 Tech Stack

Frontend: HTML, CSS, JavaScript
Visualization: CesiumJS
Reporting: jsPDF
Data Processing: Python (for cleaning + converting datasets to GeoJSON)


# 📊 Datasets Used

🔥 NASA FIRMS (Fire Information for Resource Management System)
🌊 Global Flood datasets
☄️ NASA Meteorite Landings dataset
(All datasets processed and converted to GeoJSON for easy visualization.)


# 🚀 How to Run Locally

Clone this repo
git clone https://github.com/saiminghanaa/Alert-Map.git
cd Alert-Map

Start a local server (important for loading GeoJSON):

Python 3
python -m http.server 8000

Open in browser:
http://localhost:8000


# 🌍 Deployment

This project is live on GitHub Pages:
👉 https://saiimeghanaaa.github.io/Alert-Map/


# 📌 Future Scope

Add more disasters: Earthquakes, Volcanoes, Hurricanes
Integrate with real-time APIs for live updates
Support alerts/notifications for specific regions
Enhance clustering & performance for massive datasets

# 🏆 About the Hackathon

This project was developed in just 24 hours for the NASA International Space Apps Challenge.
The goal: build solutions that help communities worldwide understand and respond to Earth’s biggest challenges.


# 📷 Demo

Link: https://drive.google.com/file/d/1_WR390HG2h0u_6_LmV2ar_HwhVk3wMCX/view?usp=sharing


