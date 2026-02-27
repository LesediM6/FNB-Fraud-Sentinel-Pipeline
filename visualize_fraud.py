import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_fraud_charts(fact_file):
    print("📊 Generating Fraud Analysis Charts...")
    df = pd.read_csv(fact_file)

    # Filter to see only the actual fraud cases
    fraud_df = df[df['is_fraud'] == 1]

    # Set the visual style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Create a bar chart: Fraud occurrences by Transaction Type
    chart = sns.countplot(data=fraud_df, x='trans_type', palette='magma')
    
    # Add titles and labels
    plt.title('FNB Fraud Sentinel: Confirmed Fraud by Transaction Type', fontsize=16)
    plt.xlabel('Transaction Type', fontsize=12)
    plt.ylabel('Number of Fraud Cases', fontsize=12)

    # Save the chart as an image for your presentation
    plt.savefig('fraud_analysis_report.png', bbox_inches='tight')
    print("✅ Success! Chart saved as 'fraud_analysis_report.png'")

if __name__ == "__main__":
    create_fraud_charts('fact_transactions.csv')