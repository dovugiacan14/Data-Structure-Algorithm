def consecutive_numbers(logs):
    logs["var"] = logs.num.rolling(window= 3).var()
    return pd.DataFrame(data = {'ConsecutiveNums' : logs.query('var == 0').num.unique()})
