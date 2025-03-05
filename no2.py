import pandas as pd

# Function to load currency data from CSV file with different encodings
def load_currency_data(file_path):
    encodings = ["latin1", "ISO-8859-1", "windows-1252"]
    for enc in encodings:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except UnicodeDecodeError:
            continue
    return None

# Function to convert USD to the desired currency
def convert_currency(amount, currency_code, df):
    row = df[df['code'] == currency_code]
    if row.empty:
        print("Currency not found.")
        return None
    rate = row['rate'].values[0]
    return amount * rate

if __name__ == "__main__":
    file_path = "currency.csv"
    df = load_currency_data(file_path)

    if df is not None:
        # Get user input for USD amount and target currency
        amount = float(input("How much dollar do you have? "))
        currency_code = input("What currency do you want to have? ").strip().upper()

        # Convert and display the result
        converted_amount = convert_currency(amount, currency_code, df)

        if converted_amount is not None:
            print(f"\nDollar: {amount} USD")
            print(f"{currency_code}: {converted_amount}")
    else:
        print("Failed to load currency data. Make sure 'currency.csv' is in the correct directory.")
