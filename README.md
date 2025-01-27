# PDF to Audio Converter 🔊

A powerful Python application that converts PDF documents into high-quality audio files. This tool uses state-of-the-art text extraction and text-to-speech technologies to create natural-sounding audio from any PDF document.

## 🌟 Features

- **PDF Text Extraction**: Accurate text extraction using PyMuPDF
- **High-Quality Text-to-Speech**: Natural voice synthesis using Google Text-to-Speech
- **User-Friendly Interface**: Clean and intuitive web interface built with Streamlit
- **Multi-Language Support**: Support for multiple languages including English, Spanish, French, German, and Italian
- **Chunk Processing**: Smart text splitting for optimal audio generation
- **Download Options**: Download individual audio files or complete ZIP package
- **Audio Preview**: Built-in audio player for immediate playback
- **Progress Tracking**: Real-time progress indicators for all operations

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/codeliveyou/pdf-reader.git
cd pdf-reader
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Streamlit web interface:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

## 📖 Usage

1. **Upload PDF**
   - Click the "Choose a PDF file" button
   - Select your PDF document

2. **View Extracted Text**
   - The extracted text will appear in the "Text" tab
   - Review the text for accuracy

3. **Convert to Audio**
   - Click the "Convert to Audio" button
   - Wait for the conversion process to complete

4. **Listen and Download**
   - Use the built-in audio player to preview the audio
   - Download individual parts or the complete ZIP file

## ⚙️ Configuration

### Language Settings
Select your preferred language from the sidebar:
- English (default)
- Spanish
- French
- German
- Italian

### Chunk Size
Adjust the text chunk size (1000-5000 characters) from the sidebar to optimize audio generation.

## 🛠️ Technical Details

### Project Structure
```
pdf-reader/
├── app.py                 # Main Streamlit web application
├── pdf_to_audio.py        # Core conversion logic
├── requirements.txt       # Project dependencies
├── audio_output/         # Generated audio files
└── README.md             # Project documentation
```

### Dependencies

- `PyMuPDF`: PDF text extraction
- `gTTS`: Google Text-to-Speech
- `pygame`: Audio playback
- `streamlit`: Web interface
- `tqdm`: Progress bars
- Additional utilities: `pathlib`, `logging`

## 📝 API Reference

### PDFToAudio Class

```python
converter = PDFToAudio()
audio_files = converter.convert_pdf_to_audio(
    pdf_path="document.pdf",
    output_dir="audio_output",
    play_audio=False
)
```

### Key Methods

- `extract_text_from_pdf(pdf_path)`: Extract text from PDF
- `text_to_speech(text, output_path, lang='en')`: Convert text to speech
- `convert_pdf_to_audio(pdf_path, output_dir, play_audio)`: Complete conversion process

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) for PDF processing
- [gTTS](https://github.com/pndurette/gTTS) for text-to-speech conversion
- [Streamlit](https://streamlit.io/) for the web interface

## 📧 Contact

Codeliveyou - codetankstn@gmail.com

Project Link: [https://github.com/codeliveyou/pdf-reader](https://github.com/codeliveyou/pdf-reader)

## 🐛 Known Issues

- Large PDFs may take longer to process
- Some complex PDF layouts might affect text extraction
- Internet connection required for Google Text-to-Speech

## 🚀 Future Improvements

- [ ] Add support for more languages
- [ ] Implement offline text-to-speech option
- [ ] Add batch processing for multiple PDFs
- [ ] Improve text extraction for complex layouts
- [ ] Add custom voice options
- [ ] Implement audio speed control
- [ ] Add text highlighting during playback

## 📊 Version History

* 0.2
    * Add web interface
    * Improve text extraction
    * Add multi-language support
* 0.1
    * Initial Release

## 💡 Tips for Best Results

1. Use PDFs with clear, well-formatted text
2. Ensure stable internet connection for TTS
3. Split large documents into smaller parts
4. Use appropriate chunk sizes for better audio quality

## ⚠️ Requirements

```
pip install -r requirements.txt
```

---
Made with ❤️ by [Codeliveyou]