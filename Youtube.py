from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st
from generate_video_id import get_youtube_video_id
from get_title import get_youtube_metadata

load_dotenv()
import json
model =  ChatOpenAI(model='gpt-4')


st.header('Youtube Video Summarizer')
video_link = st.text_input('Paste the youtube video link')
if video_link:
    meta = get_youtube_metadata(video_link)
    st.write("🎬 Title:", meta["title"])
    st.write("📺 Channel:", meta["channel"])
    if st.button('Summarize'):
        try:
            video_id = get_youtube_video_id(video_link)
            generate_transcript = YouTubeTranscriptApi()
            transcript =generate_transcript.fetch(video_id)
            text_formatter = TextFormatter()
            text_formatted = text_formatter.format_transcript(transcript)
            with open('transcript.txt', 'w', encoding='utf-8') as txt_file:
                txt_file.write(text_formatted)
            transcript_String = ""
            with open('firstpost.txt', 'r') as file:
                for line in file:
                    transcript_String+=line

            template = load_prompt('yt_template.json')
            chain = template | model
            result = chain.invoke({'text_file_content':transcript_String})
            st.write(result.content)
        except Exception as e:
            st.error(f"Error: {str(e)}")

else:
    st.info("👆 Paste a valid YouTube link above to begin.")




