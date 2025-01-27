import streamlit as st
import base64
from io import BytesIO
import time
import os
from pathlib import Path
import shutil
from extract_text import PDFToAudio

class PDFToAudioWeb(PDFToAudio):
    def __init__(self):
        super().__init__()
        self.setup_session_state()

    def setup_session_state(self):
        """Initialize session state variables"""
        if 'audio_files' not in st.session_state:
            st.session_state.audio_files = []
        if 'extracted_text' not in st.session_state:
            st.session_state.extracted_text = ""
        if 'conversion_done' not in st.session_state:
            st.session_state.conversion_done = False

    def get_audio_player_html(self, audio_path):
        """Create HTML audio player"""
        audio_placeholder = f"""
        <audio controls style="width: 100%">
            <source src="{audio_path}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        """
        return audio_placeholder

    def get_download_link(self, file_path, filename):
        """Generate download link for file"""
        with open(file_path, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        button_html = f'''
            <a href="data:audio/mpeg;base64,{b64}" 
               download="{filename}" 
               style="text-decoration: none;">
                <button style="
                    background-color: #4CAF50;
                    border: none;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 4px;">
                    Download {filename}
                </button>
            </a>
        '''
        return button_html

def create_zip_of_audio_files(audio_files, zip_path):
    """Create a ZIP file containing all audio files"""
    import zipfile
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for audio_file in audio_files:
            zipf.write(audio_file, os.path.basename(audio_file))
    return zip_path

def main():
    st.set_page_config(
        page_title="PDF to Audio Converter",
        page_icon="🔊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Sidebar
    with st.sidebar:
        st.title("Settings")
        lang = st.selectbox(
            "Select Language",
            options=['en', 'es', 'fr', 'de', 'it'],
            format_func=lambda x: {
                'en': 'English',
                'es': 'Spanish',
                'fr': 'French',
                'de': 'German',
                'it': 'Italian'
            }[x]
        )
        chunk_size = st.slider(
            "Chunk Size (characters)",
            min_value=1000,
            max_value=5000,
            value=3000,
            step=500
        )

    # Main content
    st.title("📚 PDF to Audio Converter")
    st.write("Transform your PDF documents into audio files with ease!")

    # Initialize converter
    converter = PDFToAudioWeb()

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload a PDF file to convert it to audio"
    )

    if uploaded_file is not None:
        # Save uploaded file temporarily
        pdf_path = f"temp_{uploaded_file.name}"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Create tabs
        tab1, tab2 = st.tabs(["📝 Text", "🔊 Audio"])

        with tab1:
            if not st.session_state.extracted_text:
                with st.spinner("Extracting text from PDF..."):
                    st.session_state.extracted_text = converter.extract_text_from_pdf(pdf_path)
            
            st.text_area(
                "Extracted Text",
                st.session_state.extracted_text,
                height=400
            )

        with tab2:
            if not st.session_state.conversion_done:
                if st.button("🎵 Convert to Audio", use_container_width=True):
                    with st.spinner("Converting to audio..."):
                        output_dir = "audio_output"
                        st.session_state.audio_files = converter.convert_pdf_to_audio(
                            pdf_path=pdf_path,
                            output_dir=output_dir,
                            play_audio=False
                        )
                        st.session_state.conversion_done = True

            if st.session_state.conversion_done and st.session_state.audio_files:
                # Create ZIP file of all audio files
                zip_path = "audio_files.zip"
                create_zip_of_audio_files(st.session_state.audio_files, zip_path)
                
                # Download all button
                with open(zip_path, "rb") as f:
                    bytes = f.read()
                    st.download_button(
                        label="📥 Download All Audio Files (ZIP)",
                        data=bytes,
                        file_name="audio_files.zip",
                        mime="application/zip",
                        use_container_width=True
                    )

                # Display individual audio players and download buttons
                for i, audio_file in enumerate(st.session_state.audio_files):
                    st.markdown(f"### Part {i+1}")
                    st.markdown(converter.get_audio_player_html(audio_file), unsafe_allow_html=True)
                    st.markdown(converter.get_download_link(audio_file, f"audio_part_{i+1}.mp3"), 
                              unsafe_allow_html=True)

        # Cleanup
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Made with ❤️ by Your Name</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()