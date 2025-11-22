import pandas as pd
from ..core.interfaces import Transformer
from typing import Any



class BasicTransform(Transformer):
    def transform(self, data: Any) -> Any:
        
        # Example transformation: Fill missing values and convert temperature to Fahrenheit
        df: pd.DataFrame = pd.DataFrame(data)
        df.columns = [c.strip().lower() for c in df.columns]
        return df