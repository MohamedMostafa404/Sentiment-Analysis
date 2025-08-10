#  Twitter Sentiment Analysis  
---

A sophisticated Twitter sentiment analysis application powered by a fine-tuned **BERT-base-uncased** model. This project provides real-time sentiment classification for text with an intuitive Streamlit web interface.

---

## 🚀 Features

- 🎯 **Multi-class Classification:** Accurately classifies text into Positive, Negative, Neutral, or Irrelevant categories  
- ⚡ **Real-time Analysis:** Instant sentiment prediction with confidence scores  
- 🖥️ **User-friendly Interface:** Clean, responsive Streamlit web application  
- 🤖 **Advanced NLP:** Built on BERT-base-uncased architecture fine-tuned for Twitter data  
- 📊 **Confidence Metrics:** Visual confidence scores with progress bars  
- 🔧 **Easy Deployment:** Simple setup and deployment process  

---

## 🛠️ Installation & Setup

### Prerequisites  
- Python 3.8 or higher  
- pip package manager  

### 1. Clone the Repository

```bash
git clone https://github.com/MohamedMostafa404/Sentiment-Analysis.git
cd twitter-sentiment-analysis

```
2. Install Dependencies
```bash
pip install -r requirements.txt

```
3. Run the Application

```bash
streamlit run app.py

```
🎮 Usage
Launch the app:
streamlit run app.py

Enter text:
Type or paste the text you want to analyze

Get results:
Click "Analyze Sentiment" to see predictions

View confidence:
Check the confidence score and visual indicators

---------------------------------------------------------------------------------------------

## 🧠 Model Details

| Feature       | Details                        |
|---------------|-------------------------------|
| Architecture  | BERT-base-uncased             |
| Base Model    | bert-base-uncased             |
| Training Data | Twitter sentiment dataset     |
| Classes       | 4 (Positive, Negative, Neutral, Irrelevant) |
| Model Size    | ~255MB                       |
| Framework     | 🤗 Transformers, PyTorch      |

---------------------------------------------------------------------------------------------

🔧 Configuration
The model uses the following key configurations:

Max Length: 512 tokens

Truncation: Enabled

Padding: Dynamic

Return Tensors: PyTorch

----------------------------------------------------------------------------------------------------------

🔧 Configuration
The model uses the following key configurations:

Max Length: 512 tokens

Truncation: Enabled

Padding: Dynamic

Return Tensors: PyTorch

--------------------------------------------------------------------------------------------

🚀 Deployment Options
Local Development

```bas
streamlit run app.py

```

⭐ Star this repository if you found it helpful! ⭐








