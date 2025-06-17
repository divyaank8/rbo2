import streamlit as st
import time

# Static data

rm_daily_nudge_rbo3 = """
🏦 RM Daily Nudge – RBO-2 <br>

🚀 <strong>Room to Improve</strong><br>

Your region is currently ranked <strong>3rd</strong> in your AO (out of 5 RBOs), <strong>10th</strong> in your Network, and <strong>20th</strong> in your Circle.    

Performance has been mixed – CASA and Loan achievements hover around 60% of MTD targets. NPA is marginally above threshold, and there are multiple improvement opportunities across segments.<br>

📈 <strong>Performance Overview</strong><br>
💰 Deposits: Moderate CASA achievement, but several branches with <50% performance.<br>
⬆️ Advances: Housing and SME Loans are lagging with low conversion and sourcing issues.<br>
⚠️ NPA: Slightly elevated NPA levels with increasing stress in SME segments.<br>
⚙️ Operational: No major issues of ATM outages or availablity.<br>

📌 <strong>Suggested Focus</strong><br>
Boost CASA via localized outreach and focused acquisition from salary & institutional segments.<br>
Improve loan sourcing and reduce rejections by strengthening lead quality, documentation support, and TAT.<br>
Contain NPA through early alerts and segment-wise resolution strategies.<br>

🌟 <strong>Top Performing Branches</strong>:<br>
Preet Vihar, Nehru Place<br>
🔻 <strong>Bottom Performing Branches</strong>:<br>
Laxmi Nagar, Shastri Nagar, Nangloi, Rani Bagh
"""

rm_daily_nudge_rbo3_deposits = """
💰 <strong>Deposits (CASA)</strong><br>
MTD: ₹10.8 Cr vs Target ₹18 Cr 🔹 60% Achieved – Room for growth.<br>
⭐ <strong>Top Branches:</strong>  <br>
Preet Vihar, Nehru Place, Krishna Nagar  <br>
🔻<strong>Bottom Branches:</strong>  <br>
Laxmi Nagar, Rani Bagh, Nangloi, Shastri Nagar <br>
📌 <strong>Snapshot:</strong><br>
 • 12 branches <50% budget achievement<br>
 • <strong>Persistent Laggards:</strong> <br>
 Laxmi Nagar, Shastri Nagar, Rani Bagh  <br>
 • <strong>New Declines:</strong> <br>
 Nangloi – drop due to salary account shift<br>
🛠️ <strong>Actions:</strong><br>
 • <strong>All Laggards</strong>: <br>
Map nearby corporates/intitutions and pitch bulk account onboarding with dedicated. <br>
 • <strong>New Declines:</strong><br>
Nangloi: Engage lost corporate tie-up, offer relationship-led win-back strategy  
"""



rm_daily_nudge_rbo3_advances = """

⬆️ <strong>Advances (Total)</strong><br>
MTD: ₹8.2 Cr vs Target ₹14 Cr 🔹 59% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
Nehru Place, Preet Vihar<br>
🔻 <strong>Bottom Branches:</strong><br>
Nangloi, Rani Bagh, Laxmi Nagar, Shastri Nagar<br><br>

💼 <strong>SME Loans</strong><br>
MTD: ₹3.4 Cr vs Target ₹6 Cr 🔹 56% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
Nehru Place, Preet Vihar<br>
🔻 <strong>Bottom Branches:</strong><br>
Nangloi, Laxmi Nagar, Rani Bagh<br>
📌 <strong>Snapshot:</strong><br>
 • 4 branches <30% budget achievement; 15 >60%<br>
 • <strong>Persistent Laggards:</strong><br>
   Nangloi, Rani Bagh<br>
 • <strong>New Issues:</strong><br>
   Laxmi Nagar: Delays in collateral valuation, slow TAT<br>
🛠️ <strong>Actions:</strong><br>
• <strong>All Laggards:</strong><br>
Suggest tailored loan products for distinct SME segments 
(e.g., working capital finance, machinery loans, startup credit).<br>
Proactively deepen client relationships.<br>
• <strong>New Issues:</strong><br>
 Laxmi Nagar: Engage approved valuers to reduce bottlenecks<br>

🏠 <strong>Housing Loans</strong><br>
MTD: ₹3.9 Cr vs Target ₹7 Cr 🔹 55% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
Preet Vihar, Krishna Nagar<br>
🔻 <strong>Bottom Branches:</strong><br>
Rani Bagh, Laxmi Nagar, Shastri Nagar<br>
📌 <strong>Snapshot:</strong><br>
 • 3 branches <40% of target; 10 >65%<br>
 • <strong>Persistent Laggards:</strong><br>
   Shastri Nagar + 3 others<br>
 • <strong>New Issues:</strong><br>
 Rani Bagh: Multiple CIBIL-based rejections (<680 scores)<br>
🛠️ <strong>Actions:</strong><br>
• <strong>All Laggards:</strong><br>
Partner with real estate expos, attend project launches and enable digital onboarding for quicker processing. 
<br><strong>New Issues:</strong><br>
Rani Bagh: Run credit education + pre-check CIBIL <br>

🚗 <strong>Auto Loans</strong><br>
MTD: ₹1.65 Cr vs Target ₹3.5 Cr 🔹 47% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
Preet Vihar, Nehru Place<br>
🔻 <strong>Bottom Branches:</strong><br>
Nangloi, Seelampur, Laxmi Nagar<br>
📌 <strong>Snapshot:</strong><br>
 • 4 branches <30% of target; 12 >55%<br>
 • <strong>Persistent Laggards:</strong><br>
   Laxmi Nagar + 3 others<br>
 • <strong>New Issues:</strong><br>
   Nangloi: Disbursement delays post-sanction<br>
   Seelampur: Inconsistent presence of on-site officers at dealerships hampering lead sourcing.<br>
🛠️ <strong>Actions:</strong><br>
• <strong>All Laggards:</strong><br>
  Re-engage dealers with improved incentives.<br>
• <strong>New Issues:</strong><br>
Nangloi: Streamline post-sanction disbursement<br>
Seelampur: Enforce presence of on-site officers to ensure timely, real-time lead sourcing.
<br>
"""





rm_daily_nudge_rbo3_npa = """
⚠️ <strong>NPA Management</strong><br>
Current NPA: 1.91% 🔺 +12 bps vs Target 1.65% → ₹2.7 Cr total NPA<br>
📌 <strong>Key Branches:</strong><br>
Nangloi: ₹0.72 Cr SME NPA<br>
Rani Bagh: ₹0.28 Cr SME NPA<br>
Shastri Nagar: ₹0.15 Cr HL NPA<br>
🛠️ <strong>Actions:</strong><br>
Launch aggressive recovery drives in SME, using early-warning signals.<br>
Proactive restructuring for eligible borrowers (esp. SME), intensify post-disbursal checks.<br>
"""

rm_daily_nudge_rbo3_ops = """
🏧 <strong>ATM & Operational Performance</strong><br>
Uptime: 97% vs Target 95%<br>
⭐ <strong>Top ATMs:</strong> <br>Vasant Vihar, Malviya Nagar<br>
🔻 <strong>Low Performing ATMs:</strong><br>
Laxmi Nagar, Shastri Nagar, Seelampur<br>
📌 <strong>Issues:</strong><br>
Cashouts: Poor cash load forecasting in 4 branches<br>
🛠️ <strong>Actions:</strong><br>
Optimize cash forecasting using volume trends; tighten vendor oversight.<br>
"""





rm_daily_nudge_agent ="""
  <p>
    This RM Daily Nudge was auto-generated by <strong>IntelliAI</strong>, a custom <strong>agentic GenAI system</strong> designed for SBI RBO performance reporting.
  </p>

  <h6>🧠 What Powers It:</h6>
  <ul>
    <li><strong>LLMs (Large Language Models):</strong> Generate clear, human-readable summaries, insights, and coaching actions across CASA, Loans, NPA, and Operations.</li>
    <li><strong>GenAI Agents:</strong> Modular agents act autonomously—pulling data, identifying issues, comparing peers, and drafting tailored recommendations for each branch.</li>
    <li><strong>Prompt Engineering:</strong> Smart templates adapt to context (performance, ranking, gaps) and generate personalized nudges for every RBO.</li>
  </ul>

  <h6>🔗 How It Works:</h6>
  <ul>
    <li>Ingests structured <strong>branch-level performance data</strong> (MTD/YTD, targets, baselines, issues).</li>
    <li>Applies <strong>rule-based logic and prioritization</strong> (e.g., flag low achievers, rising NPAs, operational lapses).</li>
    <li>Uses <strong>multi-agent collaboration</strong> (e.g., CASA Agent, Loan Agent, NPA Agent) to break down data by segment.</li>
    <li>Synthesizes all outputs into a <strong>single coherent markdown report</strong>, optimized for regional managers.</li>
  </ul>

</div>

""" 







# RBO 1

rm_daily_nudge_rbo1 = """
🏦 RM Daily Nudge – RBO-1<br>

🎉 <strong>Congratulations!</strong> 🏆  <br>

Your Region is ranked <strong>2nd</strong> in your AO (out of 5 RBOs), <strong>3rd</strong> in your Network, and <strong>6th</strong> in your Circle.<br>
 <br>Your team has shown strong, consistent performance this month, maintaining steady CASA (89%) and Loan (65%) MTD budget achievements. However, the rising NPA trend (+18 bps) needs your urgent attention.<br>

📈 <strong>Performance Overview</strong><br>
💰 Deposits: You're at the highest budget achievement in your AO and Network.<br>
⬆️ Advances: Achievements are close to being on track and should reach targets.<br>
⚠️ NPA: The increase is a concern and is slightly above the peer average.<br>
⚙️ Operational: Some ATMs reported service lapses.<br>

📌 <strong>Suggested Focus</strong><br>
Maintain momentum in CASA and Loans.<br>
Aggressively tackle NPA management.  <br>

🌟 <strong>Top Performing Branches</strong>: <br>
New Delhi Main Branch (Parliament Street), Connaught Place<br>
🔻 <strong>Bottom Performing Branches</strong>: <br>
Saket, Janakpuri, Dwarka Sector 10<br>
"""

# 📊 Category-wise Deep Dive  

rm_daily_nudge_rbo1_deposits = """
💰 <strong>Deposits (CASA)</strong><br>
MTD: ₹16.02 Cr vs Target ₹18 Cr 🔹 89% Achieved – Strong performance.<br>
⭐ <strong>Top Branches:</strong><br>
New Delhi Main, Connaught Place, Daryaganj<br>
🔻<strong>Bottom Branches:</strong><br>
Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Pitam Pura  <br>
📌 <strong>Snapshot:</strong><br>
 • 8 branches <40% budget achievement; 28 branches >90%<br>
 • <strong>Persistent Laggards:</strong><br>
 Badarpur, Connaught Place, Karol Bagh + 3 others<br>
 • <strong>New Declines:</strong><br>
   Patel Nagar: Lost major institutional account<br>
   Pitam Pura: Salaried accounts moved due to better competitor package  <br>
🛠️ <strong>Actions:</strong><br>
 • <strong>All Laggards</strong>: <br>
 Run hyper-local campaigns, targeted customer engagement drives, and specialized relationship management efforts<br>
 • <strong>New Declines:</strong><br>
 Patel Nagar: Review & strengthen institutional client ties<br>
 Pitam Pura: Deepen corporate engagement to retain Corporate Salary Package (CSP) accounts<br>

"""

rm_daily_nudge_rbo1_advances = """

⬆️ <strong>Advances (Total)</strong><br>
MTD: ₹9.75 Cr vs Target ₹15 Cr 🔹 65% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
New Delhi Main, Rohini Sec-7, Vasant Kunj<br>
🔻 <strong>Bottom Branches:</strong><br>
Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Dwarka Sec-10   <br><br>
💼 <strong>SME Loans</strong><br>
MTD: ₹5.2 Cr vs Target ₹8 Cr 🔹 65% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
New Delhi Main Branch, Rohini Sec-7, Vasant Kunj<br>
🔻 <strong>Bottom Branches:</strong><br>
Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Dwarka Sec-10<br>
📌 <strong>Snapshot:</strong> <br>
 • 5 branches <30% budget achievement; 20 >70% budget achievement<br>
 • <strong>Persistent Laggards:</strong><br>
 Badarpur, Karol Bagh + 2 others<br>
 • <strong>New Issues:</strong> <br>
   Dwarka Sec-10: High rejection rate (collateral/document gaps)<br>
   Patel Nagar: TAT delays, disbursals lagging by 5 days<br>
🛠️ <strong>Actions:</strong><br>
• <strong>All Laggards</strong>: <br>
Suggest tailored loan products for distinct SME segments 
(e.g., working capital finance, machinery loans, startup credit).<br>
Proactively deepen client relationships.
 <br>• <strong>New Issues:</strong><br>
 Dwarka: Push CGTMSE-backed options<br>
 Patel Nagar: Fast-track high-ticket loans, optimize approval flow    <br><br>
🏠 <strong>Housing Loans</strong><br>
MTD: ₹4.88 Cr vs Target ₹7.55 Cr 🔹 65% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
New Delhi Main, Rohini Sec-7, Vasant Kunj<br>
🔻 <strong>Bottom Branches:</strong><br>
Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Dwarka Sec-10<br>
📌 <strong>Snapshot:</strong><br>
 • 6 branches <35% budget achievement<br>
 • <strong>Persistent Laggards:</strong><br>
 Connaught Place, Laxmi Nagar + 1 (low market demand)<br>
 • <strong>New Issues:</strong><br>
   Green Park: High rejections from poor credit scores, weak lead quality.<br>
   Tilak Nagar: Competitor edge (rate & speed), 15% drop in applications<br>
🛠️ <strong>Actions:</strong><br>
• <strong>All Laggards</strong><br>
Partner with real estate expos, attend project launches and enable digital onboarding for quicker processing.
<br><strong>New Issues:</strong><br>
Green Park: Pre-screen leads, run credit camps, align with quality builders.<br>
Tilak Nagar: Highlight transparent pricing, eliminate hidden charges, and streamline documentation to reduce TAT  <br><br>

🚗 <strong>Auto Loans</strong><br>
MTD: ₹1.89 Cr vs Target ₹4.5 Cr 🔹 42% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
New Delhi Main, Rohini Sec-7, Vasant Kunj<br>
🔻 <strong>Bottom Branches:</strong> Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Dwarka Sec-10<br>
 📌 <strong>Key Issues:</strong><br>
Lost key dealers to competitors offering better incentives and faster disbursals.<br>
Delayed approvals (2-day lag) causing dealer dissatisfaction.
🛠️ <strong>Actions:</strong><br>
Re-engage dealers with improved incentives.<br>
Enforce presence of on-site officers to ensure timely, real-time loan sourcing.
"""

rm_daily_nudge_rbo1_npa = """
⚠️ <strong>NPA Management</strong><br>
Current NPA: 1.83% 🔺 +18 bps vs Target 1.65% → ₹1.5 Cr total NPA  <br>
⭐ <strong>Top Branches:</strong><br>
New Delhi Main, Rohini Sec-7, Vasant Kunj<br>
🔻 <strong>Bottom Branches:</strong><br>
Saket, Narela, Dwarka Sec-10, Connaught Place<br>
📌 <strong>Snapshot:</strong><br>
 Saket: High NPA ₹0.18 Cr – recovery/appraisal gaps<br>
 Janakpuri: Personal Loan NPA ↑ ₹0.15 Cr<br>
 Connaught Place: NPA% down, but actuals up ₹0.20 Cr – disbursement spike masking risk<br>
🛠️ <strong>Actions:</strong><br>
 Rapid reviews, restructure viable cases, recover others<br>
 Boost early warning triggers & intensify collections, legal action, post-disbursal checks<br>
"""

rm_daily_nudge_rbo1_ops = """
🏧 <strong>ATM Availability</strong><br>
Uptime: 93.9% vs Target 95%<br>
⭐ <strong>Top ATMs:</strong><br>
New Delhi Main Branch, Karol Bagh, Civil Lines<br>
🔻 <strong>Bottom ATMs:</strong><br>
Laxmi Nagar, Uttam Nagar<br>
📌 <strong>Snapshot:</strong><br>
 Laxmi Nagar: poor connectivity, old hardware<br>
 Sarojini Nagar, Shastri Nagar: Major cash-outs due to poor forecasting<br>
🛠️ <strong>Actions:</strong><br>
Optimize cash forecasting using volume trends; tighten vendor oversight.<br>
Audit and upgrade outdated ATMs to minimize outages.
"""

# RBO 2

rm_daily_nudge_rbo2 = """
🏦 RM Daily Nudge – RBO‑2<br>

📉 <strong>Alert!</strong> <br>
Your Region is ranked <strong>5th</strong> in your AO (out of 5 RBOs), <strong>12th</strong> in your Network, and <strong>18th</strong> in your Circle.  

<br>Performance is lagging behind—CASA at 62%, Loan at 48% of MTD budgets. NPA is rising (+32 bps). Significant operational issues noted.  

<br>📈 <strong>Performance Overview</strong>
💰 Deposits: Deep underperformance—many branches below 50% CASA achievement.<br>
⬇️ Advances: Loan targets are far from being met.<br>
⚠️ NPA: Worrying uptick, well above peer average.<br>

⚙️ Operational: Widespread ATM outages and Re‑KYC compliance issues.  <br>
📌 <strong>Suggested Focus</strong><br>
🚨 Rapid recovery campaigns for deposits and loans.<br>
🔧 Immediate fixes on ATMs & KYC compliance.<br>
👥 Reinforce branch-level accountability.  <br>

🌟 <strong>Top Performing Branches</strong>:<br>
Vasant Vihar, Malviya Nagar<br>
🔻 <strong>Bottom Performing Branches</strong>:<br>
Badarpur, Narela, Trilokpuri<br>
"""

# 📊 Category‑wise Deep Dive  

rm_daily_nudge_rbo2_deposits = """
💰 <strong>Deposits (CASA)</strong><br>
MTD: ₹11.5 Cr vs Target ₹18.5 Cr 🔹 62% Achieved – Underwhelming <br>
⭐ <strong>Top Branches:</strong>  <br>
Vasant Vihar, Malviya Nagar  <br>
🔻 <strong>Bottom Branches:</strong>  <br>
Badarpur, Narela, Trilokpuri, Ghazipur, Shaheen Bagh  <br>
📌 <strong>Snapshot:</strong>  <br>
 • 6 branches <45% budget achievement  <br>
 • <strong>Persistent Underperformance:</strong>  <br>
Badarpur, Narela, Ghazipur  <br>
 • <strong>New Declines:</strong>  <br>
Trilokpuri: Lost a large corporate account  <br>
Shaheen Bagh: Salaried accounts shifting due to competitor offers  <br>
🛠️ <strong>Actions:</strong>  <br>
 • <strong>Persistent Laggards:</strong> <br>
Micro‑market campaigns, targeted relationship management  <br>
 • <strong>New Declines:</strong>  <br>
Trilokpuri: Re‑negotiate with institution, offer customized CASA benefits <br> 
Shaheen Bagh: Run CSP retention drives and promote digital salary credits  <br>
"""

rm_daily_nudge_rbo2_advances = """

⬆️ <strong>Advances (Total)</strong><br>
MTD: ₹7.2 Cr vs Target ₹15 Cr 🔹 48% Achieved – Lagging<br>
⭐ <strong>Top Branches:</strong><br>
Vasant Vihar, Malviya Nagar<br>
🔻 <strong>Bottom Branches:</strong><br>
Badarpur, Narela, Trilokpuri, Ghazipur, Shaheen Bagh   <br><br>
💼 <strong>SME Loans</strong><br>
MTD: ₹2.8 Cr vs Target ₹7 Cr 🔹 40% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
Vasant Vihar, Malviya Nagar, Janakpuri<br>
🔻 <strong>Bottom Branches:</strong><br>
Badarpur, Karol Bagh (persistent), Dwarka Sec-10, Patel Nagar<br>
📌 <strong>Snapshot:</strong><br>
 • 5 branches <30% budget achievement; 20 >70% budget achievement<br>
 • <strong>Persistent Laggards:</strong><br>
Badarpur, Karol Bagh + 2 others<br>
 • <strong>New Issues:</strong><br>
Dwarka Sec-10: High rejection rate (collateral/document gaps)<br>
Patel Nagar: TAT delays, disbursals lagging by 5 days<br>
🛠️ <strong>Actions:</strong><br>
 • <strong>All Laggards</strong>: <br>
Run cluster-based outreach (e.g., “Loan Melas”), trade body engagement<br>
 • <strong>New Issues:</strong><br>
Dwarka: Push CGTMSE-backed options<br>
Patel Nagar: Fast-track high-ticket loans, optimize approval flow  <br><br>

🏠 <strong>Housing Loans</strong><br>
MTD: ₹3.1 Cr vs Target ₹8 Cr 🔹 39% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
Vasant Vihar, Malviya Nagar, Lajpat Nagar<br>
🔻 <strong>Bottom Branches:</strong><br>
Ghazipur, Narela (persistent); Karol Bagh, Dwarka Sec-10<br>
📌 <strong>Snapshot:</strong><br>
 • 5 branches <30% budget achievement; 4 branches >70%<br>
 • <strong>Persistent Laggards:</strong><br>
Ghazipur, Narela + 2 others<br>
 • <strong>New Issues:</strong><br>
   Karol Bagh: Builder tie-up fallout<br>
   Dwarka Sec-10: Slow approvals due to back-office overload<br>
🛠️ <strong>Actions:</strong><br>
 • <strong>All Laggards</strong>: <br>
Run on-ground housing loan camps with local builders<br>
 • <strong>New Issues:</strong><br>
Karol Bagh: Rebuild developer relations, offer rate-matching<br>
Dwarka: Augment back-office team; set SLA-based routing  <br><br>

🚗 <strong>Auto Loans</strong><br>
MTD: ₹1.5 Cr vs Target ₹4 Cr 🔹 38% Achieved<br>
⭐ <strong>Top Branches:</strong><br>
Vasant Vihar, Malviya Nagar, Connaught Place<br>
🔻 <strong>Bottom Branches:</strong><br>
Badarpur, Narela (persistent); Shaheen Bagh, Patel Nagar<br>
📌 <strong>Snapshot:</strong><br>
 • 6 branches <35% achievement; 19 >70%<br>
 • <strong>Persistent Laggards:</strong><br>
   Badarpur, Narela + 2 others<br>
 • <strong>New Issues:</strong><br>
Shaheen Bagh: Dealership tie-up expired<br>
Patel Nagar: Disbursement delays post-sanction<br>
🛠️ <strong>Actions:</strong><br>
 • <strong>All Laggards</strong>: <br>
 Organize "Drive SBI" weekend camps with top dealers<br>
 • <strong>New Issues:</strong><br>
Shaheen Bagh: Renew dealer tie-ups, offer bundled schemes<br>
Patel Nagar: Streamline post-sanction disbursement with SLA tracking<br>
"""

rm_daily_nudge_rbo2_npa = """
⚠️<strong>NPA Management:</strong><br>
Current NPA: 1.82% 🔺 +32 bps vs Target 1.50%  <br>
⭐ <strong>Top:</strong> Vasant Vihar, Malviya Nagar<br>
🔻 <strong>Bottom:</strong> Badarpur, Narela, Trilokpuri, Ghazipur<br>
📌 <strong>Snapshot:</strong><br>
 • Badarpur: SME & Personal loan defaults rising sharply<br>
 • Trilokpuri: Agri‑NPA up ₹0.12 Cr (seasonal stress)<br>
 • Ghazipur: Decline in NPA% but a rise in absolute NPA amounts  <br>
🛠️ <strong>Actions:</strong>  <br>
 • Finalize restructuring for viable borrowers, escalate recovery  <br>
 • Publish monthly Early Warning reports  <br>
 • Boost legal recovery team and set target SLAs  <br>
"""

rm_daily_nudge_rbo2_ops = """
🏧 <strong>ATM Availability</strong><br>
Uptime: 94% vs Target 95%  25 outages 🔺 Target <20<br>
⭐ <strong>Top ATMs:</strong> Vasant Vihar, Malviya Nagar<br>
🔻 <strong>Bottom ATMs:</strong> Badarpur, Narela, Ghazipur, Trilokpuri<br>
📌 <strong>Snapshot:</strong><br>
 • Badarpur: Recurrent hardware failures, no backup<br>
 • Ghazipur: Frequent cash‑outs, forecasting errors <br>
🛠️ <strong>Actions:</strong><br>
 • Install backup UPS and upgrade failing ATMs<br>
 • Conduct power and network diagnostics<br>
<br>
🗂️ <strong>Re‑KYC Compliance</strong><br>
Re‑KYC Backlog: 350+ accounts pending<br>
🛑 <strong>Issues:</strong><br>
 • Understaffed branches leading to documentation delays<br>
 • Low online KYC uptake<br>
🛠️ <strong>Actions:</strong><br>
 • Launch branch‑assisted digital KYC camps<br>
 • Train staff teams to guide customers through digital process<br>
"""




# Dictionary mapping for easy handling
rbo_summaries = {
    "RBO-1": rm_daily_nudge_rbo1,
    #"RBO-2": rm_daily_nudge_rbo2,
    "RBO-2": rm_daily_nudge_rbo3,
}

rbo_deep_dives = {
    "RBO-2": {
        "Deposits": rm_daily_nudge_rbo3_deposits,
        "Advances": rm_daily_nudge_rbo3_advances,
        "Operations": rm_daily_nudge_rbo3_ops,
        "NPA": rm_daily_nudge_rbo3_npa,
        "How this works?": rm_daily_nudge_agent,


    },
        "RBO-1": {
        "Deposits": rm_daily_nudge_rbo1_deposits,
        "Advances": rm_daily_nudge_rbo1_advances,
        "Operations": rm_daily_nudge_rbo1_ops,
        "NPA": rm_daily_nudge_rbo1_npa,
                "How this works?": rm_daily_nudge_agent,


    },

}

# 💡 Icon mapping for deep dive sections
deep_dive_icons = {
    "Deposits": "💰",
    "Advances": "⬆️",
    "NPA & Ops": "🛠️",
    "NPA": "📉",
    "Cross-Sell & Digital": "📱",
    "Compliance": "✅",
    "How this works?": "🤖"
}




# --- Page Configuration ---
st.set_page_config(
    page_title="SBI RBO-2 IntelliAI",
    page_icon=":bank:",
    layout="wide"
)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #edf4fa;
            color: #002B5B;
            font-family: 'Segoe UI', sans-serif;
            margin: 0 !important;
            padding: 0 !important;
        }


        .sbi-header {
            background-color: #002B5B;
            padding: 12px 40px; /* Added horizontal padding */
            border-radius: 0; /* Remove border radius for full-width block */
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 5px;
            width: 100vw; /* Full viewport width */
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .sbi-header img {
            height: 60px;
            margin-right: 20px;
        }

        .sbi-header-title {
            font-size: 30px;
            font-weight: 700;
            color: #ffffff;
        }

        .sbi-subtitle {
            font-size: 16px;
            color: #cce6ff;
            margin-top: 4px;
        }

        .stButton>button {
            background-color: #0072BC;
            color: white;
            font-weight: 600;
            font-size: 15px;
            padding: 12px 20px;
            border-radius: 8px;
            border: none;
            width: 100%;
        }

        .stButton>button:hover {
            background-color: #005A96;
        }
        .stButton {
        margin-bottom: 2px; /* 👈 Controls spacing between buttons */
        }

        .centered-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            margin-top: 0px;
        }

        h1, h2, h3 {
            color: #002B5B;
        }

        .chat-container {
            padding: 10px 15px;
            background-color: #ffffff;
            border: 1px solid #dbe4f0;
            border-radius: 5px;
            margin-top: 5px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        }

        .chat-bubble.bot {
            background-color: #eef5fc;
            color: #002B5B;
            padding: 10px 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            font-size: 15px;
        }

        .back-btn-container {
            display: flex;
            justify-content: flex-start;
            margin-bottom: 1rem;
        }
        .back-btn-container button {
            width: auto !important;
            min-width: 120px;
            padding: 0.3rem 0.75rem;
            font-size: 0.9rem;
            border-radius: 6px;
        }
        
        
        
            button span {
        display: inline-block;
        width: 100%;
        text-align: center;
    }
    
        

        </style>

        
    

""", unsafe_allow_html=True)
# --- SBI Header Block ---
import base64

# Read and encode local image (lll.png) as base64
with open("logo_sbi.png", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

# Inject into your HTML block
st.markdown(f"""
    <div class="sbi-header" style="display: flex; align-items: center; gap: 1rem;">
        <img src="data:image/png;base64,{encoded}" class="header-img" style="height: 65px;">
        <div>
            <div class="sbi-header-title">SBI RBO IntelliAI</div>
            <div class="sbi-subtitle">Data-driven GenAI intelligence</div>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- Page Routing with Session State ---
#if "page" not in st.session_state:
#    st.session_state.page = "home"

if "page" not in st.session_state:
    st.session_state.page = "chat"  # 👈 Open chat page by default
    st.session_state.selected_rbo = "RBO-2"  # 👈 Hardcoded RBO
    st.session_state.show_spinner = True



# --- Navigation: Homepage ---
if st.session_state.page == "home":
    st.markdown("""
        <div style="text-align: center; padding-top: 10px; padding-bottom: 20px;">
            <h3>👋 Welcome to your <br> RBO IntelliAI Assistant</h3>
            <h5>💡 Start your day with data-driven intelligence!</h5>
            <p style="font-size: 16px;">
                Choose a Regional Business Office to start a smart, insight-driven conversation about its performance and opportunities.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- Horizontally aligned RBO Buttons with Equal Width ---
    col1, col2 = st.columns(2)
    rbo_names = ["RBO-1", "RBO-2"]
    rbo_cols = [col1, col2]

    for col, rbo in zip(rbo_cols, rbo_names):
        with col:
            if st.button(rbo):
                st.session_state.selected_rbo = rbo
                st.session_state.page = "chat"
                st.session_state.show_spinner = True  # 🔁 Reset spinner every time

                st.rerun()
                
                
                
                
                
                
                
                
  # --- CHAT PAGE ---
  
  
# --- CHAT PAGE ---
elif st.session_state.page == "chat":

    rbo = st.session_state.get("selected_rbo", "RBO-1")

    st.markdown(f"#### 💬 IntelliAI Chat for {rbo}")

    if st.session_state.get("show_spinner", True):
        with st.spinner(f"Generating insights for {rbo}..."):
            time.sleep(2)
        st.session_state.show_spinner = False
        st.rerun()

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    if "selected_deep_dives" not in st.session_state:
        st.session_state.selected_deep_dives = []

    # --- Inject styles ---
    st.markdown("""
    <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            padding: 15px 20px;
            background-color: #ffffff;
            border: 1px solid #dbe4f0;
            border-radius: 10px;
            margin-top: 10px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        }

        .chat-bubble {
            padding: 10px 15px;
            border-radius: 12px;
            max-width: 85%;
            word-wrap: break-word;
            font-size: 15px;
        }

        .chat-bubble.bot {
            align-self: flex-start;
            background-color: #eef5fc;
            color: #002B5B;
        }

        .chat-bubble.user {
            align-self: flex-end;
            background-color: #d9fdd3;
            color: #002B5B;
        }

        .stButton > button {
            padding: 0.4rem 0.6rem;
            font-size: 0.83rem;
            margin: 2px;
            border-radius: 6px;

        }
        .stButton {
            margin-bottom: 2px; /* 👈 Controls spacing between buttons */
        }

    </style>
    """, unsafe_allow_html=True)

    # --- Display RBO summary as first bot message ---
    with st.container():
        st.markdown(f"""
            <div class="chat-container">
                <div class="chat-bubble bot">
                    {rbo_summaries.get(rbo, 'No summary available.')}

        """, unsafe_allow_html=True)
    



    # --- Display chat log for each selected deep dive ---
    for dive in st.session_state.chat_log:
        icon = deep_dive_icons.get(dive, "📂")
        response = rbo_deep_dives[rbo].get(dive, "No insights available.")
        st.markdown(f"""
            <div class="chat-container">
                <div class="chat-bubble user">{icon} {dive}</div>
                <div class="chat-bubble bot">{response}</div>
            </div>
        """, unsafe_allow_html=True)

    # --- Show deep dive buttons at the bottom ---
    if rbo in rbo_deep_dives:

        deep_dive_options = list(rbo_deep_dives[rbo].keys())
        remaining_dive_options = [d for d in deep_dive_options if d not in st.session_state.chat_log]

        if remaining_dive_options:
            st.markdown(f"""
                <div class="chat-container">
                    <div class="chat-bubble bot">
                        Select a segment to explore insights:
                    </div>
                </div>
            """, unsafe_allow_html=True)

            cols = st.columns(len(remaining_dive_options), gap="small")

            for i, dive in enumerate(remaining_dive_options):
                with cols[i]:
                    icon = deep_dive_icons.get(dive, "📂")
                    label = f"{icon} {dive}"
                    if st.button(label, key=f"btn_{dive}", use_container_width=True):
                        st.session_state.chat_log.append(dive)
                        st.rerun()
