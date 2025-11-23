from dataclasses import dataclass
from typing import Literal


@dataclass
class PipelineConfig:
    debug: bool = False
    verbose: bool = False
    output_format: Literal["csv", "json", "postgres"] = "csv"  # opções podem ser 'csv', 'json', 'postgres'
    batch_size: int = 32 # Irmão adicionei isso como exemplo de nova configuração porém não entendo muito bem o que faz
    
    
    def __post_init__(self):
        valid_formats = ('csv', 'postgres', 'json')
        if self.output_format not in valid_formats:
            raise ValueError(f"output_format must be one of: {valid_formats}")