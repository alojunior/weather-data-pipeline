import typer 
from rich import print
from .core.pipeline import DataPipeline
from .sources.open_meteo import OpenMeteoSource
from .processing.basic_transform import BasicTransform
from .storage.csv_sink import CSVSink

app = typer.Typer(help="Data Pipeline CLI")

@app.callback()
def main():
    pass

@app.command("pipeline")
def run():
    print("[blue]Running the data pipeline...[/blue]")
    
    print("[gray]Setting up data source...[/gray]")
    
    print("[red]This is only a test...[/red]")    
    
if __name__ == "__main__":
    app()
