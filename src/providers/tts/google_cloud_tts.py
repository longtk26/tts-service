from fastapi import Depends
from typing import Annotated
from.tts import TTSProvider
from google.cloud import texttospeech as gcp_tts
from google.oauth2 import service_account
from src.config import config
import base64, json

class GoogleCloudTTS(TTSProvider):
    def __init__(self):
        json_key_b64 = config.google_cloud_tts_key
        print("Encoded JSON Key:", json_key_b64)  # Debugging line
        json_key = base64.b64decode(json_key_b64).decode('utf-8')
        print("Decoded JSON Key:", json_key)  # Debugging line
        credentials = service_account.Credentials.from_service_account_info(
            json.loads(json_key)
        )
        self.client = gcp_tts.TextToSpeechClient(credentials=credentials)
        print("Google Cloud TTS client initialized.")

    def synthesize_speech(self, text) -> bytes:
        response = self.client.synthesize_speech(
            input=gcp_tts.SynthesisInput(text=text),
            voice=gcp_tts.VoiceSelectionParams(
                language_code="en-US",
                ssml_gender=gcp_tts.SsmlVoiceGender.NEUTRAL,
            ),
            audio_config=gcp_tts.AudioConfig(
                audio_encoding=gcp_tts.AudioEncoding.MP3
            )
        )
        return response.audio_content

        
AGoogleCloudTTS  = Annotated[GoogleCloudTTS, Depends(GoogleCloudTTS)]