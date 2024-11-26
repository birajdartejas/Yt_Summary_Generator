
# YouTube Transcript to Summary Generator

A Streamlit-based web application that extracts transcripts from YouTube videos and generates engaging, concise, and audience-friendly summaries using Google's Gemini generative AI.

## Features

- **Transcript Extraction:** Automatically fetches transcripts for YouTube videos with subtitles.
- **AI-Generated Summaries:** Uses Google's Gemini generative AI to create high-quality summaries from video transcripts.
- **Streamlined User Interface:** Upload a YouTube video link and receive detailed notes instantly.
- **Customizable Summaries:** Leverages a tailored prompt to ensure concise, engaging, and informative outputs.

## Technology Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** Python
- **APIs:** 
  - [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) for fetching video transcripts.
  - [Google Generative AI (Gemini)](https://developers.generativeai.google/) for generating summaries.
- **Environment Variables:** [python-dotenv](https://pypi.org/project/python-dotenv/) for secure API key management.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShreyasGandhi0607/yttranscribe_summary_generator.git
   cd yttranscribe_summary_generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with the following variables:
   ```env
   GOOGLE_API_KEY=<your_google_api_key>
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Enter the YouTube video URL in the provided text box.

3. Click on **"Get Detailed Notes"** to extract the transcript and generate a summary.

4. View the transcript and generated summary directly in the app.

## Application Workflow

1. **YouTube Transcript Extraction:**
   - Extracts the video ID from the YouTube URL.
   - Fetches the transcript using the YouTube Transcript API.

2. **Summary Generation:**
   - Uses a predefined prompt to guide Gemini generative AI for summary creation.
   - Processes transcript text into concise, audience-friendly summaries.

3. **Output:**
   - Displays the video thumbnail for context.
   - Shows the generated summary in Markdown format for easy readability.


## Limitations

- The app requires YouTube videos with accessible transcripts.
- The generated summary length depends on API token limits (2000 tokens currently).

## Future Enhancements

- Support for videos without captions using audio-to-text conversion.
- Option to download the transcript and summary as a text file.
- Improved UI/UX for mobile responsiveness.
#
