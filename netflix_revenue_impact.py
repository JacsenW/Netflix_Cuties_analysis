
#Revenue Impact 
subs_q2 = 192.95  # Q2 2020 subscribers in millions
subs_q3 = 195.15  # Q3 2020 subscribers in millions
actual_net_adds_q3 = subs_q3 - subs_q2  # Actual net adds in millions

# Conservative baseline growth assumption (Netflix grew bby 10.1M in Q2)
expected_growth_q3 = 6.0 # Expected net adds in millions
missed_signups = expected_growth_q3 - actual_net_adds_q3  # Missed signups in millions (3.8M)

# Revenue assumptions from Q3 2020 report
ARPU = 11.00  # Average Revenue Per User in USD
LTV = ARPU * 12  # Lifetime Value in USD (assuming 1 year)

# Calculate revenue impact
missed_monthly_revenue = missed_signups * 1_000_000 * ARPU  # Missed monthly revenue in USD
missed_annual_revenue = missed_signups * 1_000_000 * LTV  # Missed annual revenue in USD

print("=== Netflix Revenue Impact from Reduced Q3 Subscriber Growth ===")
print(f"Expected Subscription Growth (Q3): {expected_growth_q3:.2f}M")
print(f"Actual Subscription Growth (Q3): {actual_net_adds_q3:.2f}M")
print(f"Estimated Missed Subscribers: {missed_signups:.2f}M")
print()
print(f"Monthly Revenue Lost (Global ARPU ${ARPU}): ${missed_monthly_revenue:,.2f}")
print(f"Annual Revenue Lost (Estimated LTV ${LTV}): ${missed_annual_revenue:,.2f}")
