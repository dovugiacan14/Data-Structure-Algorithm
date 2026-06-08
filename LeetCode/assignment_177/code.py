

def nth_highest_salary(employee: pd.DataFrame, N: int):
    unique_salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)
    n_salary = unique_salaries.iloc[N - 1] if len(unique_salaries) >= N else None
    return pd.DataFrame({f"getNthHighestSalary({N})": [n_salary]})
