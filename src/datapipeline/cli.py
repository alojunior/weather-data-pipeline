import typer 
from rich import print
from typing import Literal
from .core.pipeline import DataPipeline
from .sources.open_meteo import OpenMeteoSource
from .processing.basic_transform import BasicTransform
from .storage.csv_sink import CSVSink
from .core.config import PipelineConfig

app = typer.Typer(help="Data Pipeline CLI")

@app.callback()
def main():
    pass

@app.command("pipeline")
def run(
    debug: bool = typer.Option(False, "--debug", help="Enable debug mode"),
    verbose: bool = typer.Option(False, "--verbose", help="Enable verbose output"),
    output_format: Literal["csv", "json", "postgres"] = typer.Option("csv", "--output-format", help="Output format: csv, json, or postgres"),
    batch_size: int = typer.Option(32, "--batch-size", help="Batch size for processing")
):
    
    config = PipelineConfig(
        debug=debug,
        verbose=verbose,
        output_format=output_format,
        batch_size=batch_size
    )
    
    print(f"[yellow]Pipeline Configuration:[/yellow] {config}")
    
    print("[blue]Running the data pipeline...[/blue]")
    
    print("[gray]Setting up data source...[/gray]")
    
    print("[red]This is only a test...[/red]")    
    
if __name__ == "__main__":
    app()
