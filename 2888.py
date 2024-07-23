# Reshape Data: Concatenate
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    joined_df = pd.concat([df1, df2],ignore_index=True)
    return joined_df