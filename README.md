# 🔑 Keyword Extraction System

A powerful AI-powered keyword extraction system for **Journalism and Research** domain. Built with KeyBERT, YAKE, and RAKE algorithms with a beautiful, clean UI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.2+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Multiple Extraction Methods:**
  - 🧠 **KeyBERT** - BERT-based semantic keyword extraction
  - 📊 **YAKE** - Statistical keyword extraction
  - 🔗 **RAKE** - Graph-based keyword extraction
  - 🎯 **Ensemble** - Combined method for best accuracy

- **Domain Optimized:** Specifically tuned for journalism and research texts
- **Beautiful UI:** Clean, modern interface with unique fonts
- **Real-time Processing:** Fast keyword extraction with progress feedback
- **Sample Texts:** Pre-loaded examples for quick testing

## 📁 Project Structure

```
keyword-extraction-system/
├── backend/
│   ├── app.py                 # Flask backend server
│   ├── requirements.txt       # Python dependencies
│   ├── model/
│   │   ├── extractor.py       # Keyword extraction module
│   │   ├── config.json        # Model configuration
│   │   └── __init__.py
│   ├── templates/
│   │   └── index.html         # Frontend UI
│   └── static/                # Static assets (optional)
├── Keyword_Extraction_Training.ipynb  # Google Colab training notebook
└── README.md
```

## 🚀 Quick Start

### 1. Clone/Download the Project

### 2. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Download NLTK Data

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
```

### 4. Run the Server

```bash
python app.py
```

### 5. Open in Browser

Navigate to `http://localhost:5000`

## 📓 Google Colab Training

The `Keyword_Extraction_Training.ipynb` notebook allows you to:

1. Load and explore news datasets (AG News)
2. Train/test all extraction models
3. Benchmark performance
4. Export the model as a ZIP file

### To Use Colab Notebook:

1. Upload `Keyword_Extraction_Training.ipynb` to Google Colab
2. Run all cells
3. Download the generated `keyword_extraction_model.zip`
4. Extract and place in the `backend/model/` directory

## 🔧 API Reference

### Extract Keywords

**POST** `/api/extract`

```json
{
    "text": "Your text here...",
    "method": "ensemble",
    "top_n": 10
}
```

**Response:**

```json
{
    "success": true,
    "method": "ensemble",
    "keywords": [
        {"keyword": "federal reserve", "score": 0.95},
        {"keyword": "interest rate", "score": 0.87}
    ],
    "count": 10,
    "processing_time": 0.5
}
```

### Available Methods

| Method | Description | Speed |
|--------|-------------|-------|
| `keybert` | Semantic BERT-based extraction | Medium |
| `yake` | Statistical extraction | Fast |
| `rake` | Graph-based extraction | Fast |
| `ensemble` | Weighted combination | Slower |

## 🎨 Frontend Features

- 🌙 Dark theme with gradient accents
- 📱 Fully responsive design
- ⌨️ Keyboard shortcuts (Ctrl+Enter to extract)
- 📋 Copy keywords with one click
- 📝 Sample texts for quick testing
- 📊 Real-time statistics display

## 📊 Dataset Reference

The models are optimized using:

- **AG News Dataset**: 120,000 news articles across 4 categories
  - World News
  - Sports
  - Business
  - Science/Technology

Source: [HuggingFace AG News](https://huggingface.co/datasets/ag_news)

## 🛠️ Configuration

Edit `model/config.json` to customize:

```json
{
    "models": {
        "keybert": {"model_name": "all-MiniLM-L6-v2"},
        "ensemble": {
            "weights": {
                "keybert": 0.5,
                "yake": 0.3,
                "rake": 0.2
            }
        }
    },
    "default_params": {
        "top_n": 10,
        "diversity": 0.5
    }
}
```

## 📦 Production Deployment

Using Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

---

Made with ❤️ for Journalism & Research
