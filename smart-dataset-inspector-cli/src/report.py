from colorama import Fore, Style
def generate_report(overview, missing, numeric, categories, suggestions):

    print(Fore.CYAN +"\n========== DATASET REPORT ==========\n"+ Style.RESET_ALL)

    print(f"Rows: {overview['rows']}")
    print(f"Columns: {overview['columns']}\n")

    print("Column Names:")
    for col in overview["column_names"]:
        print(f"- {col}")

    print("\nMissing Values:")
    for col, val in missing.items():
        print(f"{col}: {val}")

    print("\nNumeric Statistics:")

    for col in numeric:
        if "mean" in numeric[col]:
            print(f"{col} mean: {round(numeric[col]['mean'],2)}")

    print("\nTop Categories:")

    for col in categories:
        print(f"\n{col}")

        for k,v in categories[col].items():
            print(f" {k}: {v}")

    print("\nCleaning Suggestions:")

    for s in suggestions:
        print("-", s)

    print(Fore.CYAN +"\n====================================\n"+ Style.RESET_ALL)