from abc import ABC, abstractmethod

class TTSProvider(ABC):
    @abstractmethod
    def synthesize_speech(self, text: str) -> bytes:
        print("Abstract method called")
        pass


