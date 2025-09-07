from fastapi import APIRouter
from .service import AMediaService
from base64 import b64encode

media_route = APIRouter(prefix="/media", tags=["media"])

@media_route.get("")
def get_media(media_service: AMediaService):
    return {
        "message": "List of media items",
        "data": media_service.get_media()
    }

@media_route.post("/generate-audio")
def gen_audio_from_subtitle(media_service: AMediaService):
    audio_bytes = media_service.generate_audio_from_subtitle("Sample subtitle text")
    return {
        "message": "Generated audio from subtitle",
        "data": b64encode(audio_bytes).decode('utf-8')  
    }