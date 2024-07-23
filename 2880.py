# Select data
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student101 = students.loc[students['student_id']==101, ['name', 'age']]
    return student101