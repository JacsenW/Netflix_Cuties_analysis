import matplotlib.pyplot as plt

# Simulated monthly funnel data (in thousands)
months = ['July', 'August', 'September', 'October']

# Each step in the funnel
leads = [10000, 12000, 11000, 12500]
engaged = [8000, 9500, 6000, 10000]
viewed_pricing = [5000, 7000, 4000, 8000]
signed_up = [3000, 4500, 2500, 6000]

# Plotting the funnel over time
plt.figure(figsize=(12,6))
plt.plot(months, leads, marker='o', label='Website Visitors (Leads)')
plt.plot(months, engaged, marker='o', label='Engaged Users')
plt.plot(months, viewed_pricing, marker='o', label='Viewed Pricing Page')
plt.plot(months, signed_up, marker='o', label='Signed Up')

plt.title('Simulated Netflix Lead-to-Quote Funnel (Jul–Oct 2020)')
plt.xlabel('Month')
plt.ylabel('Users (Thousands)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
