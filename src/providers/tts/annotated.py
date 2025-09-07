
from fastapi import Depends
from typing import Annotated
from .google_cloud_tts import GoogleCloudTTS
from .tts import TTSProvider

ATTSProvider = Annotated[TTSProvider, Depends(GoogleCloudTTS)]
