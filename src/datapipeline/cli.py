import typer 
from rich import print
from typing import Literal
from .core.pipeline import DataPipeline
from .sources.open_meteo import OpenMeteoSource
from .processing.basic_transform import BasicTransform
from .storage.csv_sink import CSVSink
from .storage.postgres_sink import PostgresSink
from .core.config import PipelineConfig
import os
from dotenv import load_dotenv


app = typer.Typer(help="Data Pipeline CLI")

@app.callback()
def main():
    pass

@app.command("pipeline")
def run(
    debug: bool = typer.Option(False, "--debug", help="Enable debug mode"),
    verbose: bool = typer.Option(False, "--verbose", help="Enable verbose output"),
    output_format: Literal["csv", "json", "postgres"] = typer.Option("csv", "--output-format", help="Output format: csv, json, or postgres")
    #batch_size: int = typer.Option(32, "--batch-size", help="Batch size for processing")
):
    load_dotenv()  
    
    config = PipelineConfig(
        debug=debug,
        verbose=verbose,
        output_format=output_format
    )
    
    if verbose:
        print(f"[blue] Starting weather data pipeline...[/blue]")
    
    source = OpenMeteoSource(
        latitude=23.0,
        longitude=49.0,
        hourly="temperature_2m,relativehumidity_2m",
        debug=config.debug,
        verbose=config.verbose
    )
    
    transformer = [BasicTransform(
        debug=config.debug,
        verbose=config.verbose
    )]
    
    if config.output_format == "postgres":
        
        sink = PostgresSink(
            host=os.getenv("DB_HOST", "localhost"), # getenv com fallback padrão em caso de erro
            port=int(os.getenv("DB_PORT", 5432)),   # getenv com fallback padrão em caso de erro
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            debug=config.debug,
            verbose=config.verbose
        )
    else:
        sink = CSVSink(
            output_dir="output",
            filename="weather_data.csv",
            debug=config.debug,
            verbose=config.verbose
        )
    pipeline = DataPipeline(
        source=source,
        transformers=transformer,
        sink=sink
    )
    
    pipeline.run()
    
    if verbose:
        print(f"[bold green] Weather data pipeline completed.[/bold green]")
    

if __name__ == "__main__":
    app()
