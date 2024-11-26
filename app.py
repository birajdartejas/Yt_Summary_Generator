import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()  # Ensure GOOGLE_API_KEY is set in your environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt template
prompt = """You are a professional video summarizer specializing in creating clear, engaging, and precise summaries for YouTube audiences. Given the transcript of a video, your goal is to extract the most relevant and interesting points while maintaining the essence of the speaker's message. The summary should be:

Concise: Use bullet points and limit the total word count to 2500 words.
Engaging: Highlight key themes, emotions, and significant moments.
Informative: Summarize key takeaways and memorable insights.
Audience-Friendly: Ensure it is easy to read and understand for a general audience.
Use the transcript below to craft a compelling summary. """

# Extract transcript from YouTube
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[1].split("&")[0]
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item["text"] for item in transcript_data])
        return transcript
    except Exception as e:
        st.error(f"Error fetching transcript: {str(e)}")
        return None

# Generate summary using Gemini
def generate_gemini_content(transcript_text, prompt):
    try:
        # Truncate input to fit API limits
        max_tokens = 2000  # Adjust based on Gemini's limit
        truncated_text = transcript_text[:max_tokens]

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + truncated_text)

        # # Debugging response structure
        # st.write("API Response:", response)

        # Extract content text from the response
        if hasattr(response, "candidates") and len(response.candidates) > 0:
            parts = response.candidates[0].content.parts
            # Combine all text parts using the `text` attribute
            summary = "".join(part.text for part in parts)
            return summary
        else:
            st.error("Unexpected response format.")
            return None
    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")
        return None




# Streamlit app
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    try:
        video_id = youtube_link.split("v=")[1].split("&")[0]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
    except IndexError:
        st.error("Invalid YouTube URL format. Please try again.")

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)


    summary = generate_gemini_content(transcript_text, prompt)
    if summary:
        st.markdown("## Detailed Notes:")
        st.write(summary)
