import os
import io
import pydub
from pydub import AudioSegment
from wit import Wit, wit
from config import *

pydub.AudioSegment.ffmpeg = ""


class SpeechConvereter:
    def __init__(self):
        pass

    def to_text(self, file_path) -> str:
        pass


class WitSpeechConvereter(SpeechConvereter):
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = WitSpeechConvereter()
        return cls._instance

    def __init__(self):
        super().__init__()
        self.client = Wit(WITAI_TOKEN)
        if not os.path.exists(PATH_TO_VOICE_MESSAGES):
            os.mkdir(PATH_TO_VOICE_MESSAGES)

    def to_text(self, input_file_path) -> str:
        try:
            dest_song = os.path.splitext(input_file_path)[0] + '.wav'
            song = AudioSegment.from_ogg(input_file_path)
            song.export(dest_song, format="wav")
            with open(dest_song, 'rb') as f:
                data = self.client.speech(f, {'Content-Type': 'audio/wav'})
            text = data.get('text', '')
            if text == '':
                raise ValueError
        except Exception:
            raise ValueError
        return text