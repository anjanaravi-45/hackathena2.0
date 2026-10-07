<p align="center">
  <img src="https://github.com/Runa8147/Hackathena_Readme_Template/blob/d0add823684f0ac28b76a99636c729f80b0ca8ff/hackathena_banner.png" alt="Hackathena '26 2.0" width="100%">
</p>

<h1 align="center">ShopShield AI</h1>

<p align="center">
  <strong>ShopShield AI is an ML-powered solution that analyzes e-commerce website URLs and detects potentially fake or fraudulent websites before users interact with them.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Hackathena-'26%202.0-black?style=for-the-badge" alt="Hackathena">
  <img src="https://img.shields.io/badge/Theme-AI%20Fraud%20Detection-red?style=for-the-badge" alt="Theme">
  <img src="https://img.shields.io/badge/Status-Prototype-white?style=for-the-badge&labelColor=black" alt="Status">
</p>

---

## 👥 Team

**Team Name:** `Neural Trace`

|      Member          |    Role       |       Institution            |
|    ----------        | ---------     |   -------------------        |
| **Adhya Krishnan**   | Team Lead     | Jyothi Engineering College   |
| **Aleena Rose Joji** | Team Member   | Jyothi Engineering College   |
| **Amrita Shinod**    | Team Member   | Jyothi Engineering College   |
| **Anjana Ravi**      | Team Member   | Jyothi Engineering College   |

---

## 🎯 Problem Statement

The rapid advancement of generative AI has made it increasingly difficult to distinguish authentic content from artificially generated or manipulated content.

Deepfakes, cloned voices, synthetic images, fabricated documents, and other AI-assisted techniques can enable **impersonation, misinformation, identity theft, financial fraud, and social engineering attacks**.

**Fake e-commerce websites often imitate genuine shopping platforms using attractive offers, copied designs, and suspicious URLs. Users may find it difficult to identify these fraudulent websites before sharing personal or payment information. Therefore, a reliable system is needed to detect suspicious websites and provide users with an early warning about potential risks.**

---

## 💡 Solution

### ShopShield AI

** ShopShield AI** is a **web-based AI/ML solution** solution designed to detect **potentially fraudulent and suspicious e-commerce websites.**.

The system takes **website URL as input**, analyzes it using **machine learning and website feature extraction techniques**, and produces **website classification and risk assessment** to help users identify potentially fraudulent content.

### Key Features

* 🔴 **URL Analysis** — Accepts an e-commerce website URL and analyzes its characteristics.
* ⚪ **Machine Learning Detection** — Uses a trained ML model to classify websites as legitimate or suspicious.
* ⚫ **Risk Assessment** — Provides a clear risk level based on the analysis.
* 🔴 **Feature Extraction** — Extracts relevant URL and webpage security features for prediction.
* ⚪ **User-Friendly Interface** — Provides an attractive and simple interface for submitting URLs and viewing results.

---

## 🔄 How It Works

```text
      User enters Website URL
               │
               ▼
        React Frontend
               │
               ▼
         Flask Backend
               │
               ▼
       Feature Extraction
               │
               ▼
       Trained ML Model
               │
               ▼
       Website Prediction
               │
     ┌─────────┴─────────┐
     ▼                   ▼
LEGITIMATE           SUSPICIOUS
     │                   │
     └─────────┬─────────┘
               ▼
          Risk Result
               │
               ▼
          User Display
```

![System Architecture](ARCHITECTURE_IMAGE_URL)

*System architecture and processing workflow.*

---

## 🛠️ Technology Stack

### Software

| Layer          | Technologies                              |
| -------------- | ----------------------------------------  |
| **Frontend**   | React.js, HTML, CSS, JavaScript           |
| **Backend**    | Python, Flask, Flask-CORS                 |
| **AI / ML**    | Scikit-learn, trained classification model|
| **Database**   | Not used                                  |
| **Processing** | Pandas, NumPy, Requests, BeautifulSoup    |
| **Deployment** | Localhost / Netlify                       |

### Tools

* Git & GitHub
* Python
* Node.js & npm
* PowerShell
* Browser Developer Tools

---

## 📸 Project Preview

### Main Interface

![Main Interface](https://drive.google.com/drive/folders/1uO8V_0e2TZYgFf0kyZTAEXksIBwziQHo)

*Main interface of the application.*

### Detection / Analysis

![Detection](https://drive.google.com/drive/folders/1GbI1jU2727gQpBY67G5BaOeEND9jB4A_)

*AI fraud detection and analysis workflow.*

### Results

![Results](https://drive.google.com/drive/folders/16O2i7OlUc1ti3Lp2W0X8uBRVBlXE5K_k)

*Detection result, risk assessment, and supporting information.*

---

## 📊 Results

| Metric                     | Result                                      |
| ----------------------     | ------------------------------------------- |
| **Legitimate Probability** | 90%                                         |
| **Phishing Risk Score**    | 10%                                         |
| **Phishing Probability**   | 10%                                         |
| **Security Verdict**       | Legitimate (Low Risk)                       |
| **Detected Indicators**    | 3 Threat Signals                            |
| **Supported Input**        | URL / Domain                                |

> **Note:** Replace the above values with measured results from the final prototype. Remove metrics that are not applicable.

---

## 🚀 Getting Started

### Prerequisites

* * Python 3.12
* Node.js and npm
* Git
* Visual Studio Code
* A modern web browser
* 
### Installation

```bash
git clone [REPOSITORY_URL]
cd Hackethena

[INSTALL_COMMAND]
cd backend
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

cd frontend
npm install
```

### Environment Variables

Create a `.env` file:

```env
[VARIABLE_NAME]=[VALUE]
[API_KEY]=[YOUR_API_KEY]
```

### Run

```bash
cd backend
.\venv\Scripts\Activate.ps1
python app.py
http://127.0.0.1:5000

cd frontend
npm run dev
http://localhost:5173
```

The application will be available at:

```text
[LOCALHOST / DEPLOYMENT URL]
```

---

## 🎥 Demo

### Live Demo

**[LIVE DEMO URL]**

### Demo Video

**[https://drive.google.com/drive/folders/1yemkCp7h7nwBV_UGqbBPTxxodYcMprzh]**

> The demo demonstrates the complete workflow from input submission to fraud detection, analysis, and final result.

---

## 🧪 Example

**Input**

```text
https://example-shopping-site.com
```

**System Analysis**

```text
URL Length: Analyzed
IP Address Usage: Checked
HTTPS Token: Checked
URL Shortening: Checked
Domain Information: Analyzed
Webpage Features: Extracted
ML Model: Prediction generated
```

**Result**

```text
Unable to analyze website
```

---

## 🔐 Security & Privacy

The system is designed with user privacy and responsible AI usage in mind.

* URL-Based Analysis — The system requires only the website URL for detection.
* No Password Collection — Users are not required to provide passwords, payment details, or other sensitive credentials.
* Secure API Communication — The frontend communicates with the backend through the application API.
* Minimal Data Collection — The system focuses on website-related features required for ML-based detection.
* Credential Protection — If external API credentials are added in the future, they should be stored using environment variables rather than hard-coded in the    source code.
* Responsible Detection — Detection results are intended to help users assess potentially suspicious websites and should not be considered a guaranteed security verdict.

---

## 🔮 Future Scope

* Browser Extension – automatically checks a shopping website while browsing.
* Real-Time Detection – analyzes websites instantly before users interact with them.
* Threat Intelligence Integration – checks domain reputation and known malicious websites.
* Explainable AI – tells users why a website was classified as suspicious.
* Continuous Model Training – improves detection as new fake websites appear.

---

## 👨‍💻 Team Contributions

* **Adhya Krishnan** — Architecture & AI model development
* **Aleena Rose Joji** — Frontend & UI Integration 
* **Amrita Shinod** — Dataset & model Testing 
* ***Anjana Ravi** — Research & Documentation 

---

## 🏆 Hackathena '26 2.0

This project was developed as part of **Hackathena '26 2.0**, organized by the **Department of Computer Science & Engineering and CESA, Jyothi Engineering College**.

### Theme

> **Detection and Prevention of AI-Based Frauds**

The project focuses on addressing emerging forms of fraud enabled or amplified by generative artificial intelligence, including **deepfakes, cloned voices, synthetic media, fabricated documents, and AI-assisted impersonation**.

---

## 📄 Repository Structure

```text
.
├── frontend/              # Frontend application
├── backend/               # Backend services
├── models/                # AI/ML models
├── data/                  # Datasets / sample data
├── docs/                  # Documentation
├── screenshots/           # Project screenshots
├── .env.example           # Environment variables template
├── requirements.txt       # Python dependencies
├── package.json           # Node dependencies
└── README.md
```

---

## 📬 Contact

For questions, collaboration, or further information:

**Team:** Neural Trace
**Team Lead:** Adhya Krishnan
**Email:** aadhyahkrishnan@gmail.com
**GitHub:** [GITHUB REPOSITORY]

---

<p align="center">

<strong>Hackathena '26 2.0</strong>

<br>

Detection & Prevention of AI-Based Frauds

<br><br>

<img src="https://img.shields.io/badge/Built%20at-Jyothi%20Engineering%20College-black?style=flat-square">
<img src="https://img.shields.io/badge/Hackathena-2026-red?style=flat-square">

</p>
