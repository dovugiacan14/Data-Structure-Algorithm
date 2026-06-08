import pandas as pd
from collections import Counter



def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    need_order_name = []
    ordered_id = orders["customerId"].to_list()
    customers_dict = customers.set_index("id")["name"].to_dict()
    for id, name in customers_dict.items():
        if id not in ordered_id:
            need_order_name.append(name)
    df_result = pd.DataFrame({"Customers": need_order_name})
    return df_result
