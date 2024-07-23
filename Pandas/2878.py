# Get the size of a DataFrame
import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list([players.index.size, players.columns.size])