# 🛠️ Omni-Tools | Dev Utilities

A curated collection of automation scripts and high-performance utilities built in **Python, C, and JavaScript**. This repository serves as my "Swiss Army Knife" for streamlining development workflows and automating repetitive tasks.


📂 Project Structure
Folder	            Language	    Description
transcription/	    Python	        AI-powered speech-to-text using OpenAI Whisper/APIs.
kaggle-ops/	        Python	        Automated dataset searching and downloading via Kaggle API.
sys-utils/	        C	            High-performance system monitoring and memory utilities.
web-automations/	JS (Node)	    Custom scrapers and browser-based workflow automations.


🚀 Getting Started
Prerequisites
Python 3.8+
Node.js 16+
GCC (for compiling C utilities)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Osei-OwusuENG/omni-tools

2. For Python tools, install dependencies:
bash
pip install -r requirements.txt
Use code with caution.

3. For JS tools, install packages:
bash
npm install
Use code with caution.

🛠️ Individual Tools
1. Kaggle Downloader (Python)
Purpose: Search and fetch datasets directly to your local environment.
Usage: python kfetch.py --search "titanic"
2. Performance Monitor (C)
Purpose: Real-time system resource tracking with minimal overhead.
Compile: gcc monitor.c -o monitor

📈 Future Roadmap
Add Docker support for consistent environments.
Integrate a GUI for the transcription tool.
Add more low-level C utilities for file management.


📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
