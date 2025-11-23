from pathlib import Path
import pandas as pd
from ..core.interfaces import Sink
from typing import Any
from rich import print


class CSVSink(Sink):
    def __init__(self, output_dir: str = "output", debug: bool = False, verbose: bool = False, filename: str = "data.csv") -> None:
        self.output_dir = Path.cwd() / output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.debug = debug
        self.verbose = verbose
        self.filename = filename
    
    def load(self, data: Any) -> None:
        
        df: pd.DataFrame = pd.DataFrame(data)
        
        output_file = self.output_dir / self.filename
        
        df.to_csv(output_file, index=False)
        
        if self.verbose:
            print(f"[green]Data saved to:[/green] {output_file}")
        
        if self.debug:
            print(f"[yellow]Saved {len(df)} row and {len(df.columns)} columns to CSV.[/yellow]")
