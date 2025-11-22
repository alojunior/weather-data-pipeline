from pathlib import Path
import pandas as pd
from ..core.interfaces import Sink
from typing import Any


class CSVSink(Sink):
    def __init__(self, path: str = "output/data.csv") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self, data: Any) -> None:
        df: pd.DataFrame = pd.DataFrame(data)
