import matplotlib.pyplot as plt

# Quarterly subscriber numbers (in millions)
subscribers = [182.86, 192.95, 195.15, 203.66]  # Q1 to Q4 2020
quarters = ['Q1 2020', 'Q2 2020', 'Q3 2020', 'Q4 2020']

#Monthly churn rates to simulate
churn_rates = {
    'low': 0.02, # 2% churn rate
    'moderate': 0.05, # 5% churn rate
    'high': 0.08  # 8% churn rate
}

# Simulate subscriber growth with churn
def simulate_churn(start_subs, churn_rate, months=3):
    subs = start_subs
    subs_over_time = []
    for month in range(months):
        subs = subs * (1 - churn_rate)
        subs_over_time.append(subs)
    return subs_over_time

# Simulate churn for Q3 2020 starting at Q2 subs 
start_subs = subscribers[1]  # Q2 subs: 192.95 million

low_churn = simulate_churn(start_subs, churn_rates['low'])
moderate_churn = simulate_churn(start_subs, churn_rates['moderate'])
high_churn = simulate_churn(start_subs, churn_rates['high'])

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(range(1, 4), low_churn, marker='o', label='Low Churn (2%)',)
plt.plot(range(1, 4), moderate_churn, marker='o', label='Moderate Churn (5%)')
plt.plot(range(1, 4), high_churn, marker='o', label='High Churn (8%)')
plt.axhline(subscribers[2], color='gray', linestyle='--', label='Actual Q3 Subs')
plt.title('Simulated Subscriber Counts Over Q3 2020 with Different Churn Rates')
plt.xlabel('Month')
plt.ylabel('Subscribers (millions)')
plt.legend()
plt.grid(True)
plt.show()
