import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # id_vars: Columns to use as identifier variables
    # value_vars: Columns to unpivot
    # var_name: Name to use for the variable column
    # value_name: name to use for the value column
    return pd.melt(report, id_vars='product', value_vars=['quarter_1','quarter_2','quarter_3','quarter_4'], var_name='quarter', value_name='sales')