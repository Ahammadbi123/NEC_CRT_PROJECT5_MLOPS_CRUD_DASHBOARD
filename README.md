
# 🚀 NEC_CRT_PROJECT5: MLOps CRUD Dashboard (People Manager)

[![Python Version](https://img.shields.com/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Flask Framework](https://img.shields.com/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.com/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



**🔗 Live Demo:** [![Live Demo](https://img.shields.com/badge/Live-Demo-brightgreen?style=for-the-badge&logo=render)](https://nec-crt-project5-mlops-crud-dashboard.onrender.com)

---

## 🌌 Project Overview
**MLOps Nexus** is a professional-grade dataset management dashboard designed for machine learning pipelines. It provides an intuitive, futuristic interface to manage metadata records used by training algorithms. Beyond simple CRUD (Create, Read, Update, Delete) operations, it features a direct integration with an automated retraining engine to ensure your models are always updated with the latest data.

### 🎯 Objective
To bridge the gap between manual data handling and automated ML training by providing a high-performance web interface for data scientists and MLOps engineers.

---

## ✨ Key Features

### 🖥️ High-End Futuristic UI
- **Neon Glassmorphism**: A frosted glass effect with deep-space mesh gradients.
- **Cyber-Glow Components**: Interactive elements with neon cyan, purple, and pink accents.
- **Shimmering AI Buttons**: Dynamic, glowing call-to-action buttons for critical operations.
- **Responsive Layout**: Optimized for both desktop and mobile orchestrators.

### 🛠️ Core Functionalities (CRUD)
- **Create**: Inject new subject identities and feature vectors into the pipeline.
- **Read**: Explore the active dataset through a real-time synchronized data stream.
- **Update**: Modify existing record metadata with a single-click modification portal.
- **Delete**: Purge obsolete or corrupted data from the training stream.

### 🤖 MLOps Integration
- **One-Click Retraining**: Trigger the `train.py` script directly from the UI to update the `model.pkl`.
- **Live Metrics**: Real-time computation of dataset size and mean feature values.
- **System Status**: Visual indicators for engine health and pipeline activity.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Backend** | Python 3, Flask |
| **Data Processing** | Pandas (CSV Engine) |
| **Machine Learning** | Scikit-Learn (Linear Regression) |
| **UI/UX Styling** | Tailwind CSS (v3), Glassmorphism |
| **Typography** | Orbitron & Plus Jakarta Sans |
| **Deployment** | Gunicorn (Production Ready) |

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Ahammadbi123/NEC_CRT_PROJECT5_MLOPS_CRUD_DASHBOARD.git
cd NEC_CRT_PROJECT5_MLOPS_CRUD_DASHBOARD
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize Training Pipeline
Run the initial training to generate the ML model artifacts:
```bash
python train.py
```

### 4. Launch the Dashboard
```bash
python app.py
```
Access the terminal at: `http://127.0.0.1:5000`

---

## 📋 Usage Guide
1. **Inject Data**: Use the left-side panel to add new names and ages.
2. **Monitor**: View the dataset update in the right-side explorer.
3. **Optimize**: Click **"INITIATE RETRAIN"** on the header after adding new data.
4. **Deploy**: The system automatically saves the updated `model.pkl` for production use.

---

## 🤝 Contribution
Contributions are welcome! Feel free to open an issue or submit a pull request if you want to add more ML algorithms or enhance the UI glow effects.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---
**Developed with ❤️ by [Ahammadbi123](https://github.com/Ahammadbi123)**
