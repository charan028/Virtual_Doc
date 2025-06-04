import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
# ffmpeg,portaudio,pyaudio

from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(audio_file_path,timeout=20,phrase_time_limit=None):
    recognizer=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source,duration=1)
            logging.info("speaking...")
#audio recording
            audio_data=recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete...")
            wav_data= audio_data
            audio_Segment = AudioSegment.from_wav(BytesIO(wav_data.get_wav_data()))
            audio_Segment.export(audio_file_path, format="mp3",bitrate="128k")
            logging.info(f"Audio saved to {audio_file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
audio_filepath="patient_voice_test_for_patient.mp3"
# recognize_speech_from_audio(audio_file_path="patient_voice.mp3")

# part2
# GROQ_API_KEY = os.environ.get("GROQ_API_KEY") # Replace with your actual API key

api_key=os.environ.get("GROQ_API_KEY")
GROQ_API_KEY=api_key
from groq import Groq
client=Groq(api_key=GROQ_API_KEY)  
# query="Is there something wrong with my face?"
model = "whisper-large-v3"
audio_file_path = "patient_voice.mp3"
audio_file=open(audio_file_path, "rb")
def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
    
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )
    return transcription.text
# transcription=client.audio.transcriptions.create(
#         file=audio_file,
#         model=model,
#         language="en",
#         response_format="text"
#     )
# print(transcription)
