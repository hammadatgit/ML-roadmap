import os
import matplotlib.pyplot as plt


def category_plot(df, column):

    os.makedirs("output", exist_ok=True)

    counts = df[column].value_counts()

    plt.figure()
    counts.plot(kind="bar")

    plt.title(f"{column} Distribution")
    plt.ylabel("Count")

    plt.savefig(f"output/{column}_distribution.png")
    plt.close()


def numeric_histogram(df, column):

    os.makedirs("output", exist_ok=True)

    plt.figure()
    df[column].plot(kind="hist", bins=10)

    plt.title(f"{column} Distribution")

    plt.savefig(f"output/{column}_histogram.png")
    plt.close()