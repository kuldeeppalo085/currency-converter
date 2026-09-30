
exchange_rates = {
    "INR": 1.0,
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.0095,
    "JPY": 1.78
}


def show_currencies():
    print("\nSupported currencies:")
    for currency in exchange_rates:
        print("-", currency)
    print()


def convert_currency(amount, from_currency, to_currency):

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return None

    amount_in_inr = amount / exchange_rates[from_currency]

    converted_amount = amount_in_inr * exchange_rates[to_currency]

    return converted_amount


def main():
    print("===== SIMPLE CURRENCY CONVERTER =====")

    while True:
        show_currencies()

        from_currency = input("Convert FROM (currency code): ").strip().upper()
        to_currency = input("Convert TO (currency code): ").strip().upper()

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.\n")
            continue

        result = convert_currency(amount, from_currency, to_currency)

        if result is None:
            print("Invalid currency code. Please choose from the supported list.\n")
        else:
            print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}\n")

        again = input("Convert another amount? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()