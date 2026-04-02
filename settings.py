#
#  Import LIBRARIES
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

#  Import FILES
#  ______________________
#


#  Import FILES
#  ______________________
#


# Settings model definition
class Settings(BaseSettings):
    # Use validation_alias to map the .env name to your Python variable name
    # We use Field(default=...) to stop Pylance from complaining about missing arguments
    google_api_key: str = Field(validation_alias="GOOGLE_API_KEYgit st")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # This prevents the "Extra inputs not permitted" error
    )


# Instantiate the settings
# If GOOGLE_API_KEY is missing, the script will instantly fail here with a Pydantic ValidationError.
settings = Settings()  # type: ignore


print("✅ Settings loaded successfully!\n")
