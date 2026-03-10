import json
import os
from colorama import Fore, Style

def export_json(report):

    os.makedirs("output", exist_ok=True)

    with open("output/report.json", "w") as f:
        json.dump(report, f, indent=4)

    print(Fore.CYAN +"Report exported to output/report.json"+ Style.RESET_ALL)