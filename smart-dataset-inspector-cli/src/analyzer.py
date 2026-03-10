import numpy as np

def dataset_overview(df):

    overview = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict()
    }

    return overview


def missing_values(df):

    return df.isnull().sum().to_dict()


def numeric_summary(df):

    numeric_df = df.select_dtypes(include=[np.number])

    return numeric_df.describe().to_dict()


def category_counts(df):

    categorical_cols = df.select_dtypes(include=["object"]).columns

    results = {}

    for col in categorical_cols:
        results[col] = df[col].value_counts().head(5).to_dict()

    return results