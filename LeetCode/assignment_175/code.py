import pandas as pd


def combine_two_tables(person_tab: pd.DataFrame, address_tab: pd.DataFrame):
    result = pd.merge(person_tab, address_tab, on="personId", how="left")
    result = result[["firstName", "lastName", "city", "state"]]
    return result
