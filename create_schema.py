import pandas as pd

def build_star_schema(input_file):
    print(f"🏗️ Building Star Schema from {input_file}...")
    df = pd.read_csv(input_file)

    # 1. Create Dim_Customers (Unique list of all accounts)
    # We combine origin and destination names to get a master list of all unique customers
    all_customers = pd.concat([df['nameOrig'], df['nameDest']]).unique()
    dim_customers = pd.DataFrame(all_customers, columns=['customer_id'])
    
    # 2. Create Fact_Transactions (The core event table)
    # We select only the columns needed for transaction analysis
    fact_transactions = df[['step', 'type', 'amount', 'nameOrig', 'nameDest', 'isFraud']]
    fact_transactions.columns = ['step', 'trans_type', 'amount', 'origin_id', 'dest_id', 'is_fraud']

    # Save these as separate tables
    dim_customers.to_csv('dim_customers.csv', index=False)
    fact_transactions.to_csv('fact_transactions.csv', index=False)
    
    print(f"✅ Star Schema Complete!")
    print(f"📁 Created 'dim_customers.csv' ({len(dim_customers)} unique customers)")
    print(f"📁 Created 'fact_transactions.csv' ({len(fact_transactions)} transactions)")

if __name__ == "__main__":
    build_star_schema('cleaned_transactions.csv')