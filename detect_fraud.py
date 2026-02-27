import pandas as pd

def run_fraud_detection(fact_file):
    print(f"🕵️ Analyzing transactions for fraud in {fact_file}...")
    df = pd.read_csv(fact_file)

    # Rule 1: High-Value Flag (Transactions > 200,000)
    high_value_threshold = 200000
    df['high_value_flag'] = df['amount'] > high_value_threshold

    # Rule 2: Suspicious Type (Flagging all 'TRANSFER' and 'CASH_OUT' as higher risk)
    # These are the most common types used in fraud
    risk_types = ['TRANSFER', 'CASH_OUT']
    df['risk_type_flag'] = df['trans_type'].isin(risk_types)

    # Combine flags into a 'Final Suspicion Score'
    # If it's high value AND a risky type, we flag it for urgent review
    df['urgent_review'] = df['high_value_flag'] & (df['is_fraud'] == 1)

    # Create a summary report
    fraud_cases = df[df['is_fraud'] == 1]
    print(f"🚨 ANALYSIS COMPLETE")
    print(f"Total Transactions Scanned: {len(df)}")
    print(f"Confirmed Fraud Cases Found: {len(fraud_cases)}")
    print(f"High-Value Transactions Flagged: {df['high_value_flag'].sum()}")

    # Save the alerts to a file for the FNB 'Forensics Team'
    df[df['urgent_review']].to_csv('fraud_alerts.csv', index=False)
    print("📁 Alerts saved to 'fraud_alerts.csv'")

if __name__ == "__main__":
    run_fraud_detection('fact_transactions.csv')