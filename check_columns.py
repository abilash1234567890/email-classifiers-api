import pandas as pd

df = pd.read_csv("support_emails.csv")  # Corrected name
print("Available columns:", df.columns.tolist())
