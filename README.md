# 🛠️ Omni-Tools | Dev Utilities

A curated collection of automation scripts and high-performance utilities built in **Python, C, and JavaScript**. This repository serves as my "Swiss Army Knife" for streamlining development workflows and automating repetitive tasks.

---

## 📂 Project Structure


| Folder | Language | Description |
| :--- | :--- | :--- |
| `thor/transcription/` | **Python** | AI-powered speech-to-text using OpenAI Whisper/APIs. |
| `thor/kaggle-ops/` | **Python** | Automated dataset searching and downloading via Kaggle API. |
| `tools-c/sys-utils/` | **C** | High-performance system monitoring and memory utilities. |
| `ruud-js/web-automations/` | **JS (Node)** | Custom scrapers and browser-based workflow automations. |
| `notebooks/` | **Python/C/JS** | Contains python, C and JS experiments. |

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.+**
- **Node.js 16+**
- **GCC** (for compiling C utilities)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Osei-OwusuENG/omni-tools

2. For Python tools, install dependencies:
bash
pip install -r requirements.txt


3. For JS tools, install packages:
bash
npm install


🛠️ Individual Tools
1. Kaggle Downloader (Python)
Purpose: Search and fetch datasets directly to your local environment.
Usage: python kfetch.py --search "titanic"
2. Performance Monitor (C)
Purpose: Real-time system resource tracking with minimal overhead.
Compile: gcc monitor.c -o monitor

---

📈 Future Roadmap
1. Add Docker support for consistent environments.
2. Integrate a GUI for the transcription tool.
3. Add more low-level C utilities for file management.

---

📜 License
-This project is licensed under the MIT License - see the LICENSE file for details.