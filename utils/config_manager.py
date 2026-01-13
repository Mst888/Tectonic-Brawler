import json
import os
from typing import Any, Optional

class ConfigManager:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = self._load_config()
    
    def _load_config(self) -> dict:
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return self._create_default_config()
    
    def _create_default_config(self) -> dict:
        default_config = {
            "welcome_channel_id": None,
            "leave_channel_id": None,
            "youtube_notification_channel_id": None,
            "youtube_channel_id": None,
            "last_video_id": None,
            "check_interval_minutes": 10
        }
        self._save_config(default_config)
        return default_config
    
    def _save_config(self, config: dict) -> None:
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        self.config[key] = value
        self._save_config(self.config)
    
    def reload(self) -> None:
        self.config = self._load_config()
