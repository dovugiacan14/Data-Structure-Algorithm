import pandas as pd
from collections import Counter



def duplicate_emails(person: pd.DataFrame):
    emails = person["email"].to_list()
    email_freq = Counter(emails)
    duplicate_emails = set()
    for email, freq in email_freq.items():
        if freq >= 2:
            duplicate_emails.add(email)
    duplicate_emails = list(duplicate_emails)
    df_result = pd.DataFrame({"Email": duplicate_emails})
    return df_result
