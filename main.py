import fitz  # PyMuPDF
import os
from gtts import gTTS
import pygame
from pathlib import Path
import logging
from tqdm import tqdm
import time

class PDFToAudio:
    def __init__(self):
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text from PDF using PyMuPDF (best method for text extraction)
        """
        try:
            text = ""
            # Open PDF
            with fitz.open(pdf_path) as doc:
                # Iterate through pages
                for page in tqdm(doc, desc="Extracting text from PDF"):
                    text += page.get_text()
            return text.strip()
        except Exception as e:
            self.logger.error(f"Error extracting text from PDF: {str(e)}")
            return ""

    def split_text_into_chunks(self, text, max_chars=3000):
        """
        Split text into smaller chunks for better TTS processing
        """
        chunks = []
        current_chunk = ""
        
        # Split by sentences to maintain natural breaks
        sentences = text.split('.')
        for sentence in sentences:
            if len(current_chunk) + len(sentence) < max_chars:
                current_chunk += sentence + '.'
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + '.'
        
        if current_chunk:
            chunks.append(current_chunk.strip())
            
        return chunks

    def text_to_speech(self, text, output_path, lang='en'):
        """
        Convert text to speech using Google Text-to-Speech
        """
        try:
            tts = gTTS(text=text, lang=lang)
            tts.save(output_path)
            return True
        except Exception as e:
            self.logger.error(f"Error in TTS conversion: {str(e)}")
            return False

    def play_audio(self, audio_path):
        """
        Play the generated audio using pygame
        """
        try:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except Exception as e:
            self.logger.error(f"Error playing audio: {str(e)}")

    def convert_pdf_to_audio(self, pdf_path, output_dir="audio_output", play_audio=False):
        """
        Main method to convert PDF to audio
        """
        try:
            # Create output directory
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            # Extract text from PDF
            self.logger.info("Extracting text from PDF...")
            text = self.extract_text_from_pdf(pdf_path)
            
            if not text:
                raise Exception("No text could be extracted from the PDF")

            # Split text into chunks
            chunks = self.split_text_into_chunks(text)
            self.logger.info(f"Split text into {len(chunks)} chunks")

            # Convert each chunk to audio
            audio_files = []
            for i, chunk in enumerate(tqdm(chunks, desc="Converting text to speech")):
                output_path = os.path.join(output_dir, f"audio_part_{i+1}.mp3")
                
                if self.text_to_speech(chunk, output_path):
                    audio_files.append(output_path)
                    
                    # Optional: Play each chunk as it's created
                    if play_audio:
                        self.logger.info(f"Playing audio part {i+1}")
                        self.play_audio(output_path)
                        time.sleep(1)  # Pause between chunks

            self.logger.info(f"Created {len(audio_files)} audio files")
            return audio_files

        except Exception as e:
            self.logger.error(f"Error in PDF to audio conversion: {str(e)}")
            return []

def main():
    # Example usage
    converter = PDFToAudio()
    
    # Configure paths
    pdf_path = "a.pdf"  # Replace with your PDF path
    output_dir = "audio_output"
    
    # Convert PDF to audio
    print(f"\nConverting PDF: {pdf_path}")
    print("This process may take some time depending on the PDF size...")
    
    audio_files = converter.convert_pdf_to_audio(
        pdf_path=pdf_path,
        output_dir=output_dir,
        play_audio=False  # Set to False to disable automatic playback
    )
    
    if audio_files:
        print(f"\nConversion completed successfully!")
        print(f"Audio files created: {len(audio_files)}")
        print(f"Output directory: {output_dir}")
        
        # List all created files
        print("\nCreated audio files:")
        for audio_file in audio_files:
            print(f"- {audio_file}")
    else:
        print("\nConversion failed. Check the logs for details.")

if __name__ == "__main__":
    main()