import pandas as pd
from collections import Counter

"""Assignment 181: Employees Earning More Than Their Managers"""


def find_employees(employee: pd.DataFrame):
    df = employee.merge(right=employee, how="inner", left_on="managerId", right_on="id")
    emp = df[df["salary_x"] > df["salary_y"]]["name_x"]
    return pd.DataFrame({"Employee": emp})


data = {
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "salary": [5000, 7000, 6000, 8000],
    "managerId": [None, 1, 1, 2],
}
employee_df = pd.DataFrame(data)
result = find_employees(employee_df)

"""Assignment 182: Duplicate Emails"""
def duplicate_emails(person: pd.DataFrame):
    emails = person["email"].to_list()
    email_freq = Counter(emails)
    duplicate_emails = set()
    for email, freq in email_freq.items():
        if freq >= 2: 
            duplicate_emails.add(email)
    duplicate_emails = list(duplicate_emails)
    df_result = pd.DataFrame({'Email': duplicate_emails})
    return df_result

