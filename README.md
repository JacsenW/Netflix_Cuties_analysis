# 📉 Netflix Cuties Controversy: Business, Subscriber, and Revenue Impact Analysis

## 📖 What Happened?

In August 2020, Netflix released a trailer for the film *Cuties* — and instantly faced global backlash. Accusations of exploitation swept across social media, with hashtags like **#CancelNetflix** trending worldwide.

But did this controversy really hurt Netflix’s business?

As a data analyst, I asked:
- Was there a **financial hit**?
- Did **fewer people sign up**?
- Did **subscriber churn increase**?
- Did the controversy shake **investor confidence**?
- Was it just noise, or a real business risk?

---

## 📊 Project Overview

This **end-to-end analytics project** analyzes Netflix’s stock performance, subscriber trends, revenue impact, and a simulated lead-to-quote-to-cash funnel — before, during, and after the Cuties backlash.

Leveraging real earnings data and simulated user behavior, this report answers key business questions and provides insight into:
- 📈 Subscriber acquisition trends
- 📉 Churn and retention patterns
- 💸 Revenue impact modeling
- 🧲 Funnel breakdown during PR crisis
- 🧠 Strategic lessons for brand trust

---

## 💰 Stock Market Reaction

**Did Stock Performance Reflect the Backlash?**  
✅ Yes — but only briefly.

| 📅 Date             | Event                     | Price Impact      |
|--------------------|---------------------------|-------------------|
| Aug 18, 2020       | *Cuties* Trailer Released | 📈 $500 → $550     |
| Sept 9, 2020       | Film Released             | 📉 $500 → $450     |
| Q4 2020 Close      | Post-Recovery             | 🔄 ~$482           |

![netlfix stock price plotlib](https://github.com/user-attachments/assets/39355723-6c55-4577-8d95-8ecb2d6b2e5f)


**📌 Conclusion**: Investors responded to the backlash, but didn’t panic. The stock quickly rebounded, signaling **confidence in Netflix’s long-term strength**.

---

## 👥 Subscriber Trends

**Did Users Cancel in Large Numbers?**  
🚫 No.

| Quarter | Global Subscribers |
|---------|--------------------|
| Q1 2020 | ~183M              |
| Q2 2020 | ~193M              |
| Q3 2020 | ~195M              |
| Q4 2020 | 200M+              |

![netflix subs plotlib](https://github.com/user-attachments/assets/21ccf3a1-ed21-4a9a-b83d-df1762b3b384)

![Simluted Subscriber Counts](https://github.com/user-attachments/assets/14abcf93-629f-4566-bd12-d4a5e92a447b)

**📌 Conclusion**: Netflix retained its base. Churn remained low — even with simulated churn as high as 8%, numbers didn’t realistically dip.  
**The problem wasn't retention. It was acquisition.**

---

## 🚪 Lead-to-Quote Funnel Breakdown

**Did Fewer People Sign Up?**  
✅ Yes — *this is where the damage was clear*.

| Stage              | July   | August | **September** | October |
|-------------------|--------|--------|---------------|---------|
| Site Visitors      | 10,000 | 12,000 | 11,000        | 12,500  |
| Engaged Users      | 8,000  | 9,500  | **6,000**     | 10,000  |
| Pricing Page Views | 5,000  | 7,000  | **4,000**     | 8,000   |
| Signups            | 2,000  | 4,500  | **2,500**     | 6,000   |

![netflix lead to quote ](https://github.com/user-attachments/assets/c1927086-6d68-4870-aac2-20cf58f13b34)


**📉 September Drop-Off**:
- 37% decrease in engaged users  
- 43% decrease in pricing views  
- 44% decrease in signups  

📌 **Conclusion**: Traffic remained steady, but **trust was broken**. Users came, browsed — and bounced. The brand couldn’t convert.

---

## 💸 Revenue Impact

**What Was the Estimated Revenue Loss?**  
Using average revenue per user (ARPU) and missed conversion estimates:

![estimated netflix lost ](https://github.com/user-attachments/assets/d1161aa6-60bb-4256-9001-645fc1f6d133)


> 💰 Estimated long-term revenue loss in Q3 2020: **$500 million**

**📌 Why?**
- Churn was low → no immediate loss  
- Acquisition plummeted → **future revenue gone**

📌 **Conclusion**: No cancellations ≠ no damage.  
The controversy caused a **silent opportunity cost**.

---

## 💬 Sentiment & Behavior Correlation

Though not NLP-modeled in this version, real-world sentiment showed:

- Social media was flooded with outrage  
- “#CancelNetflix” trended globally  
- User signups dropped in the same month  

📌 **Conclusion**: Brand sentiment **directly affected user behavior**.  
Conversion rates fell as negative headlines rose.

---

## 🔁 Business Process Impact

Analyzing the lead-to-quote-to-cash model:

✅ **Lead Generation**: Strong  
❌ **Quote/Signup Conversion**: Broken  
✅ **Billing/Retention**: Stable

📌 **Conclusion**: The **middle stages collapsed**. Awareness wasn’t the issue — conversion trust was.

---

## 🧠 Strategic Business Takeaways

This project highlights how **public controversies** affect more than headlines:

- 👁 Watch middle-funnel metrics, not just churn
- 🧠 Sentiment impacts trust → trust affects conversion
- 🔄 Controversy delays growth more than it causes loss
- 📣 Crisis response must preserve brand integrity + UX

---

## 🛠 Tools & Technologies

| Tool       | Use Case                          |
|------------|-----------------------------------|
| `Python`   | ETL, data simulation, modeling    |
| `Pandas`   | Data wrangling & transformation   |
| `NumPy`    | Numeric computations              |
| `Matplotlib` | Data visualization (stock trends, churn) |
| `Power BI` | Funnel charts, KPI dashboards     |
| `GitHub`   | Version control & documentation   |

![netflix preview](https://github.com/user-attachments/assets/86124179-1942-44dc-8a62-d390f55631e5)

---
