import pandas as pd
from colorama import Fore, Style
def load_data(filepath):
    """
    Load CSV or Excel dataset
    """

    try:

        if filepath.endswith(".csv"):
            df = pd.read_csv(filepath)
            print(Fore.GREEN + "Dataset loaded successfully\n" + Style.RESET_ALL)
        elif filepath.endswith(".xlsx"):
            df = pd.read_excel(filepath)
            print(Fore.GREEN + "Dataset loaded successfully\n" + Style.RESET_ALL)
        else:
            print("Unsupported file format")
            return None

        return df  
         
    

    except Exception as e:
        print(f"Error loading file: {e}")
        return None