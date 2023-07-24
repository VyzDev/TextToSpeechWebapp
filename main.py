import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="Text to Speech", page_icon=":speech_balloon:")

with st.container():
    ttsTitleText = st.title("Text to Speech!")
    st.caption("Created by [@VyzDev](https://twitter.com/VyzDev)")
    textInput = st.text_area("Input text here!")
    outputLanguageSelect = st.selectbox("Output Accent", ["English", "Spanish", "French", "Russian", "German", "Japanese", "Chinese", "Vietnamese"])
    downloadButton = st.button("Speechify!")

    if downloadButton:
        with st.spinner("Working..."):
            if len(textInput) > 0:
                if outputLanguageSelect == "English":
                    languageCode = "en"
                elif outputLanguageSelect == "Spanish":
                    languageCode = "es"
                elif outputLanguageSelect == "French":
                    languageCode = "fr"
                elif outputLanguageSelect == "Russian":
                    languageCode = "ru"
                elif outputLanguageSelect == "German":
                    languageCode = "de"
                elif outputLanguageSelect == "Japanese":
                    languageCode = "ja"
                elif outputLanguageSelect == "Chinese":
                    languageCode = "zh"
                elif outputLanguageSelect == "Vietnamese":
                    languageCode = "vi"

                myobj = gTTS(text=textInput, lang=languageCode, slow=False)
                myobj.save("ttsFile.mp3")
                #https://docs.streamlit.io/library/api-reference/media/st.audio
                audio_file = open('ttsFile.mp3', 'rb')
                audio_bytes = audio_file.read()

                st.audio(audio_bytes, format='audio/mp3')
            else:
                st.error("No text to speak!")
