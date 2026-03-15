import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_plots():
    """Generate two simple plots from key_details.csv."""
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    csv_path = os.path.join(base_path, 'data', 'key_details.csv')
    plots_path = os.path.join(base_path, 'plots')
    
    os.makedirs(plots_path, exist_ok=True)
    df = pd.read_csv(csv_path)
    
    # Plot 1: Grades Distribution
    grades = pd.to_numeric(
        df[df['detail_key'].str.contains('Grade', na=False)]['detail_value'], 
        errors='coerce'
    ).dropna()
    
    plt.figure(figsize=(10, 6))
    sns.histplot(grades, bins=8, kde=True, color='steelblue')
    plt.title("Distribution of My Master's Module Grades")
    plt.xlabel("Grade (1.0 = best)")
    plt.ylabel("Number of Modules")
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(plots_path, 'grades_distribution.png'))
    plt.close()
    
    # Plot 2: Simple Degree Timeline
    grad_date_str = df[df['detail_key'] == 'Graduation Date']['detail_value'].iloc[0]
    plt.figure(figsize=(10, 3))
    plt.plot([2023, 2025], [0, 0], marker='o', linewidth=3, color='darkblue')
    plt.text(2023, 0.12, 'Start of Studies', ha='center')
    plt.text(2025, 0.12, f'Graduation\n{grad_date_str}', ha='center')
    plt.title("My Master's Degree Timeline")
    plt.yticks([])
    plt.grid(True, axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_path, 'degree_timeline.png'))
    plt.close()
    
    print(f"Plots saved in {plots_path}")

if __name__ == "__main__":
    generate_plots()
