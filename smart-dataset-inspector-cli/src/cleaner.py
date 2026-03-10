def cleaning_suggestions(missing):

    suggestions = []

    for column, value in missing.items():

        if value > 0:

            suggestions.append(
                f"Column '{column}' has {value} missing values → consider filling or dropping."
            )

    if not suggestions:
        suggestions.append("No missing values detected.")

    return suggestions