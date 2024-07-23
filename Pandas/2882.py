# Drop duplicate rows
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers_unique = customers.drop_duplicates(subset=['email'])
    return customers_unique