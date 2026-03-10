# Smart Dataset Inspector CLI

A lightweight **Command Line Interface (CLI) tool** for quickly inspecting and analyzing datasets before using them in data science or machine learning pipelines.

The tool automatically analyzes **CSV and Excel datasets**, detects **missing values**, computes **numeric statistics**, shows **category distributions**, generates **visualizations**, and exports a **structured JSON report**.

---

## Features

* Load **CSV** and **Excel** datasets
* Dataset overview (rows, columns, column names)
* Missing value detection
* Numeric statistics summary
* Category frequency analysis
* Data cleaning suggestions
* Automatic data visualizations
* Export analysis report to **JSON**
* Professional CLI interface
* Colored terminal output
* Automatic output folder creation

---

## Project Structure

```
dataset-inspector-cli
│
├── data                # Sample datasets
│
├── notebooks           # Optional experimentation notebooks
│
├── output              # Generated charts and reports
│
├── src
│   ├── loader.py       # Dataset loading
│   ├── analyzer.py     # Dataset analysis functions
│   ├── cleaner.py      # Cleaning suggestions
│   ├── visualizer.py   # Chart generation
│   ├── exporter.py     # Export JSON report
│   └── report.py       # CLI report formatting
│
├── inspect_dataset.py  # Main CLI script
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/dataset-inspector-cli.git
cd dataset-inspector-cli
```

Create a virtual environment (recommended):

```bash
conda create -n dataset-cli python=3.10
conda activate dataset-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Dependencies

Main libraries used:

* **Pandas** – data analysis
* **NumPy** – numerical operations
* **Matplotlib** – visualization
* **Colorama** – colored CLI output

---

## Usage

Basic dataset inspection:

```bash
python inspect_dataset.py --file data/titanic.csv
```

Generate visualizations:

```bash
python inspect_dataset.py --file data/titanic.csv --visualize
```

Export JSON analysis report:

```bash
python inspect_dataset.py --file data/titanic.csv --export
```

Full analysis with charts and export:

```bash
python inspect_dataset.py --file data/titanic.csv --visualize --export
```

---

## CLI Help

Run:

```bash
python inspect_dataset.py --help
```

Example output:

```
usage: inspect_dataset.py [-h] --file FILE [--visualize] [--export]

Smart Dataset Inspector CLI

Options:
  --file         Path to CSV or Excel dataset
  --visualize    Generate automatic visualizations
  --export       Export analysis report to JSON
```

---

## Example Output

```
========== DATASET REPORT ==========

Rows: 891
Columns: 12

Missing Values:
Age: 177
Cabin: 687
Embarked: 2

Numeric Statistics:
Age mean: 29.7
Fare mean: 32.2

Cleaning Suggestions:
Column 'Cabin' has many missing values → consider filling or dropping
```

---

## Generated Output

When visualization and export options are enabled, the tool automatically creates an **output folder** containing:

```
output/
├── category_distribution.png
├── numeric_distribution.png
└── report.json
```

---

## Example Dataset

The project can analyze datasets such as:

* Titanic dataset
* Sales data
* Customer data
* Any CSV or Excel dataset

---

## Why This Project

This project demonstrates:

* CLI tool development in Python
* Modular project architecture
* Data analysis automation
* Visualization integration
* Exportable data reports

It is designed as a **beginner-friendly data engineering / machine learning utility tool**.

---

## Future Improvements

Possible enhancements:

* Interactive CLI menu
* Dataset profiling (similar to Pandas Profiling)
* Support for larger datasets
* Additional visualizations
* Web dashboard version

---

## License

This project is open-source and available under the **MIT License**.

---

## Author

Created as part of a **Data Science / Machine Learning learning roadmap**.

If you found this useful, feel free to ⭐ the repository.
