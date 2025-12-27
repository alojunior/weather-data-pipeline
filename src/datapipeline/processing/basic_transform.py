import pandas as pd
from ..core.interfaces import Transformer
from typing import Any
from rich import print
import numpy as np



class BasicTransform(Transformer):
    def __init__(self, debug: bool = False, verbose: bool = False) -> None:
        self.debug = debug
        self.verbose = verbose
    
    def transform(self, data: Any) -> Any:
        
        df: pd.DataFrame = pd.DataFrame(data)
        
        # 1. Temperatura em Fahrenheit (vetorizado)
        df['temp_f'] = df['temp'] * 1.8 + 32
        
        # 2. Categorias de temperatura (vetorizado com np.select!)
        
        conditions = [
            df['temp'] < 15,
            df['temp'] < 25,
        ]
        choices = ['Frio', 'Morno']
        df['temp_category'] = np.select(conditions, choices, default='Quente')
        
        # 3. Features temporais (vetorizado)
        df['time'] = pd.to_datetime(df['time'])
        df['hour'] = df['time'].dt.hour
        df['day_of_week'] = df['time'].dt.dayofweek  # 0=Monday, 6=Sunday
        df['is_daytime'] = ((df['hour'] >= 6) & (df['hour'] <= 18)).astype(int)
        
        # 4. Heat Index simplificado (sensação térmica) (vetorizado)
        # Fórmula simplificada: temp + (umidade * 0.05)
        df['heat_index'] = df['temp'] + (df['humidity'] * 0.05)
        
        # Normaliza nomes de colunas
        df.columns = [c.strip().lower() for c in df.columns]
        
        if self.debug:
            print(f"[yellow]Data after transforming column names:[/yellow] {df.columns.to_list()}")
        
        if self.debug:
            print(f"[yellow]Added features:[/yellow] temp_f, temp_category, hour, day_of_week, is_daytime, heat_index")
        
        if self.verbose:
            print(f"[green]Returning transformed df with {len(df.columns)} columns[/green]")
        
        return df

        
        