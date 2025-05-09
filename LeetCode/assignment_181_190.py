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

"""Assignment 183: Customers Who Never Order"""
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    need_order_name = []
    ordered_id = orders["customerId"].to_list()
    customers_dict = customers.set_index('id')["name"].to_dict()
    for id, name in customers_dict.items(): 
        if id not in ordered_id:
            need_order_name.append(name)
    df_result = pd.DataFrame({'Customers': need_order_name})
    return df_result

