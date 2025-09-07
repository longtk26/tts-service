from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    google_cloud_tts_key: str

    model_config = SettingsConfigDict(env_file=".env")

config = Config()