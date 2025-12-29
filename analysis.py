import pandas as pd
df = pd.read_csv("data/purchases.csv")
# new column total amount
df["TotalAmount"] = df["Quantity"] * df["Price"]
print(df)
customer_spending = df.groupby("CustomerName")["TotalAmount"].sum()
print(customer_spending)

import matplotlib.pyplot as plt

customer_spending.plot(kind="bar", title="Total spending by customer")
plt.xlabel("custoemr Name")
plt.ylabel("Total amount spend")
plt.show()