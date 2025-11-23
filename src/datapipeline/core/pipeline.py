from typing import Any
from .interfaces import Source, Transformer, Sink

class DataPipeline:
    def __init__(self, source: Source, transformers: list[Transformer], sink: Sink):
        self.source = source
        self.transformers = transformers
        self.sink = sink

    def run(self) -> None:
        # Extract data from the source
        data = self.source.extract()
        
        for transformer in self.transformers:
            data = transformer.transform(data)
          
        self.sink.load(data)

