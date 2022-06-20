## Shahnawaz Anwar @ Bergmeyer
## 6/17/2021
## Scanning Master Laptop List to return owner of a laptop given Service Tag

import pandas as pd
from datetime import date

data = pd.read_excel (r'Master Laptop List.xlsx', sheet_name="Working")
df = pd.DataFrame(data)


def GiveSTGetUser(service_tag):
    for i in range(len(df)):
        if df['ServiceTag'][i] == service_tag:
            return df['Employee/Current User'][i]

user = GiveSTGetUser(input("Input Service Tag: "))
print(user)