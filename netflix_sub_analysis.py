import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
sub_df = pd.read_csv("netflix_subs.csv")

# Don't convert to datetime, keep quarters as strings for plotting


# Plot subscriber growth
plt.figure(figsize=(10,5))
plt.plot(sub_df['Quarter'], sub_df['Subscribers'], marker='o', color='teal')
plt.title('Netflix Global Subscribers (Q1–Q4 2020)')
plt.xlabel('Quarter')
plt.ylabel('Subscribers (millions)')
plt.grid(True)
plt.tight_layout()
plt.show()
