import requests
from typing import Dict, Any
from ..core.interfaces import Source
import pandas as pd


class OpenMeteoSource(Source):
    def __init__(self, latitude: float, longitude: float, hourly: str) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.hourly = hourly
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def extract(self) -> Dict[str, Any]:
        
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "hourly": self.hourly,
        }
        
        response = requests.get(self.base_url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        df = pd.DataFrame({
            "time": data["hourly"]["time"],
            "temp": data["hourly"]["temperature_2m"],
            "humidity": data["hourly"]["relativehumidity_2m"],
        })
        
        return df