from .tts import TTSProvider
import boto3

class AwsTTS(TTSProvider):
    def __init__(self):
        self.client = boto3.client("polly")

    def synthesize_speech(self, text) -> bytes:
        print('Synthesizing speech using AWS Polly...')
        speed = 1.5
        if speed != 1.0:
            text = f'<speak><prosody rate="{speed*100}%">{text}</prosody></speak>'

        response = self.client.synthesize_speech(
            Text=text,
            TextType="ssml",
            OutputFormat="pcm",
            VoiceId="Joanna"
        )
        return response["AudioStream"].read()