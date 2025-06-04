# setup text to speech with gTTs

# setup etxt to speech-tts with eleven labs
#  use model for text output to voice
from dotenv import load_dotenv
import os

load_dotenv() 
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"
    audioobj=gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

input_text = "Hi this is Ai with charan!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")
# text_to_Speech_with_gtts(input_text,output_file="output.mp3")    



# from elevenlabs.client import ElevenLabs
# from elevenlabs import play

# api_elevn="sk_601eb27bab8c58cd480478b1dab8a3ee32d00ade8bc95bd2"
# def text_to_speech_with_elevenlabs(text,output_filepath):
#     api_elevn="sk_601eb27bab8c58cd480478b1dab8a3ee32d00ade8bc95bd2"
#     client = ElevenLabs(api_key=api_elevn)
#     audio = client.text_to_speech.convert(text=text,
#                                    voice_id="JBFqnCBsd6RMkjVDRZzb",
#     model_id="eleven_multilingual_v2",
#     output_format="mp3_44100_128")
#     # ElevenLabs.play_audio(audio)  # Play the audio
#     ElevenLabs.save_audio(audio, output_filepath)

# text_to_speech_with_elevenlabs(input_text,output_filepath="output_eleven.mp3")
import elevenlabs
from elevenlabs.client import ElevenLabs
api_elevn=os.getenv("api_eleven") 
# print(api_elevn) # Ensure you have set this in your .env file

ELEVENLABS_API_KEY=api_elevn

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id= "onwK4e9ZLuTAKqWW03F9",
        output_format= "mp3_22050_32",
        model_id= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 


import subprocess
import platform
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id= "onwK4e9ZLuTAKqWW03F9",
        output_format= "mp3_22050_32",
        model_id= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")