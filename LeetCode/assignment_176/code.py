

def second_highes_salary(employee: pd.DataFrame):
    unique_employee = employee["salary"].drop_duplicates().nlargest(2)
    return unique_employee.iloc[-1] if len(unique_employee) > 1 else None
