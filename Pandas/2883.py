# Drop missing data

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students_unique = students.dropna(subset=['name'])
    return students_unique