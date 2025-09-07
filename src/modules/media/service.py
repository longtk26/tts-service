from fastapi import Depends
from typing import Annotated
from src.providers.tts import ATTSProvider

class MediaService:
    def __init__(self, tts_provider: ATTSProvider):
        self.media_items = []
        self.tts_provider = tts_provider

    def get_media(self):
        return self.media_items
    
    def generate_audio_from_subtitle(self, subtitle: str):
        audio_data = self.tts_provider.synthesize_speech(subtitle)
        return audio_data

AMediaService = Annotated[MediaService, Depends(MediaService)]