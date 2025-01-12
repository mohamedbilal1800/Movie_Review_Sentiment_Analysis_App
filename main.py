import google.generativeai as genai
import streamlit as st


# load api key from secrets.toml file
GOOGLE_API_KEY = st.secrets["Google_API_Key"]


if not GOOGLE_API_KEY:
    raise ValueError("API key is not set in the secrets.toml file")


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(
    'gemini-1.5-flash-001',
    generation_config=genai.GenerationConfig(
        temperature=0.1,
        top_p=1,
        max_output_tokens=200,
    ))


# sentiment analysis function
def analyze_sentiment(review_text):
    """
    Analyzes the sentiment of the given review text.
    Args: review_text (str): The input movie review.
    Returns: dict: A dictionary containing the sentiment and explanation.
    """

    prompt = f"""Classify movie reviews as POSITIVE, NEUTRAL or NEGATIVE.
    Review: {review_text}
    Sentiment: 
    Explanation: """

    response = model.generate_content(prompt)
    print(response, type(response))
    sentiment = response.text.strip("Sentiment: ").split()[0]
    explanation = response.text.split("Explanation: ", 2)[1]
    return {"sentiment": sentiment, "explanation": explanation}


# Streamlit App
st.title("🎥 Movie Review Sentiment Analysis App")


st.sidebar.title("About the App")
st.sidebar.info(
    """
    This app analyzes movie reviews to determine their sentiment 
    (Positive, Negative, or Neutral) and provides an explanation 
    for the chosen sentiment. Created using the Google gemini-1.5-flash-001 model, 
    it combines advanced natural language understanding with an 
    intuitive interface to help you evaluate reviews effectively.
    """
)


# User input
st.write("#### Enter your movie review below:")
review = st.text_area("Your Review", placeholder="Type your movie review here...", height=150)

# Predicting Output
if st.button("Analyze Sentiment"):
    if review.strip():
        # Call the sentiment analysis method
        result = analyze_sentiment(review)

        # Displaying results
        st.write("## Sentiment Analysis Result:")
        st.success(f"**Sentiment:** {result['sentiment']}")
        st.write("### Explanation:")
        st.info(result['explanation'])
    else:
        st.warning("Please enter a valid review to analyze.")
