import argparse
from colorama import Fore, Style
from src.loader import load_data
from src.analyzer import dataset_overview, missing_values, numeric_summary, category_counts
from src.cleaner import cleaning_suggestions
from src.report import generate_report
from src.visualizer import category_plot, numeric_histogram
from src.exporter import export_json


def main():

    parser = argparse.ArgumentParser(
    description="""
    Smart Dataset Inspector CLI

    Quickly inspect CSV or Excel datasets before using them in
    data science or machine learning pipelines.

    Example Usage:
    python inspect_dataset.py --file data/sample_sales.csv
    python inspect_dataset.py --file data/sample_sales.csv --visualize
    python inspect_dataset.py --file data/sample_sales.csv --visualize --export
"""
)

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to CSV or Excel dataset"
    )

    # NEW FLAG → visualization
    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Generate charts for dataset"
    )

    # NEW FLAG → export JSON
    parser.add_argument(
        "--export",
        action="store_true",
        help="Export report to JSON"
    )

    args = parser.parse_args()

    df = load_data(args.file)

    if df is None:
        return

    # analysis
    overview = dataset_overview(df)
    missing = missing_values(df)
    numeric = numeric_summary(df)
    categories = category_counts(df)

    suggestions = cleaning_suggestions(missing)

    # print report
    generate_report(overview, missing, numeric, categories, suggestions)

    # NEW FEATURE → Visualization
    if args.visualize:

        for col in df.select_dtypes(include=["object"]).columns:
            category_plot(df, col)

        for col in df.select_dtypes(include=["number"]).columns:
            numeric_histogram(df, col)

        print(Fore.CYAN +"Charts saved in output/ folder"+ Style.RESET_ALL)

    # NEW FEATURE → Export JSON
    if args.export:

        report = {
            "overview": overview,
            "missing_values": missing,
            "numeric_summary": numeric,
            "categories": categories,
            "cleaning_suggestions": suggestions
        }

        export_json(report)


if __name__ == "__main__":
    main()