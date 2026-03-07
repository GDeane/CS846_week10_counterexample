from payment_processor import process_payments


def print_results(totals):
    print("Processed totals:")
 
    for i, total in enumerate(totals, start=1):
        print(f"Payment {i}: {total}")



def calculate_statistics(totals):
    if not totals:
        print("No valid payments processed.")
        return

    total_sum = sum(totals)
    average = total_sum / len(totals)
    maximum = max(totals)
    minimum = min(totals)

    print("Summary Statistics")
    
    print("Total transactions:", len(totals))
    print("Sum of totals:", total_sum)
    print("Average payment:", average)
    print("Highest payment:", maximum)
    print("Lowest payment:", minimum)
   


def main():
    file_path = "payments.txt"

    print("Running payment processor test")
   

    try:
        totals = process_payments(file_path)
    except Exception as e:
        print("Program crashed with error:", e)
        return

    print_results(totals)
    calculate_statistics(totals)


if __name__ == "__main__":
    main()
