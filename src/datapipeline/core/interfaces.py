from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Source(ABC):
    @abstractmethod
    def extract(self) -> any:
        """Read data from the source and return it as a list of dictionaries."""



class Transformer(ABC):
    @abstractmethod
    def transform(self, data: Any) -> Any:
        """Transform the input data and return the transformed data."""
        
        
        
class Sink(ABC):
    @abstractmethod
    def load(self, data: Any) -> None:
        """Load the data into the sink destination."""