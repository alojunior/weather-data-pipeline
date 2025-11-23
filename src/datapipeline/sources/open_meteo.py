import requests
from typing import Dict, Any
from ..core.interfaces import Source
import pandas as pd
from rich import print


class OpenMeteoSource(Source):
    def __init__(self, latitude: float, longitude: float, hourly: str, debug: bool = False, verbose: bool = False) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.hourly = hourly
        self.debug = debug
        self.verbose = verbose
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def extract(self) -> Dict[str, Any]:
        
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "hourly": self.hourly,
        }
        
        if self.verbose:
            print(f"[green]Fetching data from Open-Meteo API with params:[/green] {params}")
                    
        response = requests.get(self.base_url, params=params, timeout=30)
        response.raise_for_status()
        
        if self.verbose:
            print(f"[green]Response content:[/green] ({len(response.content)} bytes)")  # Print length of content to avoid huge outputs
        
        data = response.json()
        
        if self.debug:
            print(f"[yellow]Raw API response:[/yellow] {data}")
        
        
        df = pd.DataFrame({
            "time": data["hourly"]["time"],
            "temp": data["hourly"]["temperature_2m"],
            "humidity": data["hourly"]["relativehumidity_2m"],
        })
        
        return df