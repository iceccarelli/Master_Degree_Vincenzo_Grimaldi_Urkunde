import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

def generate_plots(csv_path, plots_path):
    key_details_df = pd.read_csv(csv_path)

    # Plot 1: Grades Distribution
    grades_df = key_details_df[
        (key_details_df["detail_key"].str.contains("Grade", na=False)) &
        (~key_details_df["detail_value"].isin(["passed", "X", "ausreichend", "befriedigend", "gut", "sehr gut"]))
    ]
    grades_df["detail_value"] = pd.to_numeric(grades_df["detail_value"], errors=\'coerce\')
    grades_df = grades_df.dropna(subset=["detail_value"])

    plt.figure(figsize=(12, 7))
    sns.histplot(grades_df["detail_value"], bins=np.arange(1, 5.5, 0.5), kde=True, color=\'skyblue\')
    plt.title(\'Distribution of Module Grades (M.Sc. RWTH)\')
    plt.xlabel(\'Grade (1.0 = best, 5.0 = worst)\')
    plt.ylabel(\'Number of Modules\')
    plt.xticks(np.arange(1, 5.5, 0.5))
    plt.grid(True, linestyle=\'--\', alpha=0.7)
    plt.savefig(os.path.join(plots_path, \'grades_distribution.png\'))
    plt.close()

    # Plot 2: Degree Timeline
    enrollment_date = pd.to_datetime(\'2022-10-01\') # Assuming typical start of winter semester
    # Safely get graduation date, fallback if not found
    graduation_date_str = key_details_df[key_details_df["detail_key"] == "Graduation Date"]["detail_value"].iloc[0] if not key_details_df[key_details_df["detail_key"] == "Graduation Date"].empty else "08. August 2025" # Fallback to hardcoded value
    graduation_date = pd.to_datetime(graduation_date_str, format=\'%d. %B %Y\', errors=\'coerce\')
    if pd.isna(graduation_date):
        graduation_date = pd.to_datetime(\'2025-08-08\') # Fallback if parsing fails

    thesis_start_date = pd.to_datetime(\'2024-02-01\') # Conceptual start of thesis work

    dates = [enrollment_date, thesis_start_date, graduation_date]
    events = [\'Enrollment\', \'Thesis Focus\', \'Graduation\']

    plt.figure(figsize=(12, 4))
    plt.plot(dates, np.zeros(len(dates)), \'o\', markersize=10, color=\'blue\')
    plt.vlines(dates, -0.5, 0.5, color=\'gray\', linestyle=\'--\')
    for i, (date, event) in enumerate(zip(dates, events)):
        plt.text(date, 0.1 + (i % 2) * 0.2, event, horizontalalignment=\'center\', verticalalignment=\'bottom\', rotation=15)
    plt.ylim(-1, 1)
    plt.axis(\'off\')
    plt.title(\'Master\\\\'s Degree Timeline: Enrollment to Graduation\')
    plt.savefig(os.path.join(plots_path, \'degree_timeline.png\'))
    plt.close()

    print(f"Generated plots in {plots_path}")

if __name__ == "__main__":
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    output_csv_path = os.path.join(base_path, \'data\', \'key_details.csv\')
    plots_path = os.path.join(base_path, \'plots\')

    os.makedirs(plots_path, exist_ok=True)

    generate_plots(output_csv_path, plots_path)
