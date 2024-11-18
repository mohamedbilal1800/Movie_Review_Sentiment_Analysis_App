# 🎥 Movie Review Sentiment Analysis App

Analyze movie reviews effortlessly with this sentiment analysis app! This application uses the **Google Gemini-1.5-flash-001 model** for advanced natural language understanding to classify reviews as **Positive**, **Negative**, or **Neutral**. It also provides an explanation for the chosen sentiment, helping users better understand the analysis.

---

## 🌟 Features

- **Sentiment Classification**: Classifies movie reviews into Positive, Neutral, or Negative.
- **Explanations**: Provides clear reasoning for the sentiment classification.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.
- **Powered by AI**: Leverages the state-of-the-art Google Gemini-1.5-flash-001 model for robust natural language understanding.

---

## 🛠️ Technologies Used

- **Python**: Backend logic and integration.
- **Streamlit**: Interactive web interface.
- **Google Gemini Model**: Advanced AI for sentiment analysis.
- **dotenv**: Securely load API keys.
- **Google Generative AI SDK**: Access Google Gemini APIs.

---

## 🚀 Getting Started

### Prerequisites

1. Python 3.9 or later.
2. A Google Cloud account with access to the **Gemini-1.5-flash-001 model**.
3. Streamlit installed on your machine.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-review-sentiment-analysis.git
   cd movie-review-sentiment-analysis
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your **Google API key** to a `.env` file

---

## 💻 Usage

1. Run the app locally:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Enter a movie review in the text box and click **"Analyze Sentiment"** to see the sentiment and explanation.
