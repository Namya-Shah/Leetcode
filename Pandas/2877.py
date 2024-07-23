# Create a dataframe from the list
import pandas as pd
from typing import List # Just to remove error

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    student_data = pd.DataFrame(student_data, columns=["student_id", "age"])
    return student_data