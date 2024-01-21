import streamlit as st

def main():
    st.title("Audio Player App")
    audio_file_path = "ilakana-kavithai.mp3"
    st.audio(audio_file_path, format='audio/mp3')
if __name__ == "__main__":
    main()
