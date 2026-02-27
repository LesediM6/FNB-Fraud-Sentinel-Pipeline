import pandas as pd
import hashlib
import os

def mask_pii(text):
    """Hashing function to hide customer names/IDs."""
    return hashlib.sha256(str(text).encode()).hexdigest()[:12]

def process_banking_data(input_file, output_file):
    # Check if the file exists before starting
    if not os.path.exists(input_file):
        print(f"❌ ERROR: I can't find '{input_file}'. Make sure you renamed the Kaggle file!")
        return

    print(f"🚀 Starting ETL Pipeline for: {input_file}")
    
    # Load data (Reading only 100k rows to save time/memory)
    df = pd.read_csv(input_file, nrows=100000)
    print(f"📊 Data loaded. Total records to process: {len(df)}")

    # 1. PII Masking: Anonymizing account names
    print("🔐 Masking PII (Account IDs)...")
    df['nameOrig'] = df['nameOrig'].apply(mask_pii)
    df['nameDest'] = df['nameDest'].apply(mask_pii)
    
    # 2. Data Integrity: Removing transactions <= 0
    print("⚖️ Validating Transaction Integrity...")
    df = df[df['amount'] > 0]
    
    # 3. Save the result
    df.to_csv(output_file, index=False)
    print(f"✅ Success! Cleaned data saved as: {output_file}")

if __name__ == "__main__":
    # We tell the script to look for 'transactions.csv'
    process_banking_data('transactions.csv', 'cleaned_transactions.csv')