import pandas as pd
from ..core.interfaces import Transformer
from typing import Any
from rich import print



class BasicTransform(Transformer):
    def __init__(self, debug: bool = False, verbose: bool = False) -> None:
        self.debug = debug
        self.verbose = verbose
    
    def transform(self, data: Any) -> Any:
        

        df: pd.DataFrame = pd.DataFrame(data)
        
        df.columns = [c.strip().lower() for c in df.columns]
        
        if self.debug:
            print(f"[yellow]Data after transforming name columns to lowercase and stripping whitespace:[/yellow] {df.columns.to_list()}")
            
        
        if self.verbose:
            print(f"[green]Returning df after transformer[/green]")
        
        return df
    

        
        