import streamlit as st
from gtts import gTTS

languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Russian": "ru",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh",
    "Vietnamese": "vi",
}

st.set_page_config(page_title="Text to Speech", page_icon=":speech_balloon:")

with st.container():
    ttsTitleText = st.title("Text to Speech!")
    textInput = st.text_area("Input text here!")
    outputLanguageSelect = st.selectbox("Output Accent", ["English", "Spanish", "French", "Russian", "German", "Japanese", "Chinese", "Vietnamese"])
    downloadButton = st.button("Speechify!")

    if downloadButton:
        with st.spinner("Working..."):
            if len(textInput) > 0:
                myobj = gTTS(text=textInput, lang=languages[outputLanguageSelect], slow=False)
                myobj.save("ttsFile.mp3")
                #https://docs.streamlit.io/library/api-reference/media/st.audio
                audio_file = open('ttsFile.mp3', 'rb')
                audio_bytes = audio_file.read()

                st.audio(audio_bytes, format='audio/mp3')
            else:
                st.error("No text to speak!")
