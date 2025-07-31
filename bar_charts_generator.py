import matplotlib.pyplot as plt
import pandas as pd
from utility_functions import save_plot # Import the shared utility function

def generate_bar_charts(df: pd.DataFrame, num_achievers: int = 5):
    """
    Generates four bar charts:
    1. Top N counties by Revenue Collection.
    2. Bottom N counties by Revenue Collection.
    3. Top N counties by Budget Absorption Rate.
    4. Bottom N counties by Budget Absorption Rate.

    Args:
        df (pd.DataFrame): The DataFrame containing 'Revenue Collection (Million KES)',
                           'Budget Absorption Rate', and 'County' columns.
        num_achievers (int): The number of top/bottom counties to display in each chart.
    """
    print(f"\n--- Starting Bar Chart Generation for Top/Bottom {num_achievers} Achievers ---")
    print("This module generates bar charts to highlight counties with highest and lowest performance.")

    # --- Top and Bottom Achievers by Revenue Collection ---
    print(f"Preparing data for top and bottom {num_achievers} counties by Revenue Collection...")
    df_sorted_revenue = df.sort_values('Revenue Collection (Million KES)', ascending=False)
    top_revenue = df_sorted_revenue.head(num_achievers)
    bottom_revenue = df_sorted_revenue.tail(num_achievers)

    # Plotting Top Revenue Collection
    print(f"Generating bar chart for Top {num_achievers} Revenue Collection...")
    fig_top_rev, ax_top_rev = plt.subplots(figsize=(10, 6))
    ax_top_rev.bar(top_revenue['County'], top_revenue['Revenue Collection (Million KES)'], color='lightgreen')
    ax_top_rev.set_xlabel('County', fontsize=12)
    ax_top_rev.set_ylabel('Revenue Collection (Million KES)', fontsize=12)
    ax_top_rev.set_title(f'Top {num_achievers} Counties by Revenue Collection', fontsize=14)
    plt.xticks(rotation=45, ha='right') # Rotate labels for readability
    plt.tight_layout()
    save_plot(fig_top_rev, f'top_{num_achievers}_revenue_collection.png')

    # Plotting Bottom Revenue Collection
    print(f"Generating bar chart for Bottom {num_achievers} Revenue Collection...")
    fig_bottom_rev, ax_bottom_rev = plt.subplots(figsize=(10, 6))
    ax_bottom_rev.bar(bottom_revenue['County'], bottom_revenue['Revenue Collection (Million KES)'], color='salmon')
    ax_bottom_rev.set_xlabel('County', fontsize=12)
    ax_bottom_rev.set_ylabel('Revenue Collection (Million KES)', fontsize=12)
    ax_bottom_rev.set_title(f'Bottom {num_achievers} Counties by Revenue Collection', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    save_plot(fig_bottom_rev, f'bottom_{num_achievers}_revenue_collection.png')

    # --- Top and Bottom Achievers by Budget Absorption Rate ---
    print(f"Preparing data for top and bottom {num_achievers} counties by Budget Absorption Rate...")
    df_sorted_budget = df.sort_values('Budget Absorption Rate', ascending=False)
    top_budget = df_sorted_budget.head(num_achievers)
    bottom_budget = df_sorted_budget.tail(num_achievers)

    # Plotting Top Budget Absorption Rate
    print(f"Generating bar chart for Top {num_achievers} Budget Absorption Rate...")
    fig_top_bud, ax_top_bud = plt.subplots(figsize=(10, 6))
    ax_top_bud.bar(top_budget['County'], top_budget['Budget Absorption Rate'], color='lightgreen')
    ax_top_bud.set_xlabel('County', fontsize=12)
    ax_top_bud.set_ylabel('Budget Absorption Rate (%)', fontsize=12)
    ax_top_bud.set_title(f'Top {num_achievers} Counties by Budget Absorption Rate', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    save_plot(fig_top_bud, f'top_{num_achievers}_budget_absorption.png')

    # Plotting Bottom Budget Absorption Rate
    print(f"Generating bar chart for Bottom {num_achievers} Budget Absorption Rate...")
    fig_bottom_bud, ax_bottom_bud = plt.subplots(figsize=(10, 6))
    ax_bottom_bud.bar(bottom_budget['County'], bottom_budget['Budget Absorption Rate'], color='salmon')
    ax_bottom_bud.set_xlabel('County', fontsize=12)
    ax_bottom_bud.set_ylabel('Budget Absorption Rate (%)', fontsize=12)
    ax_bottom_bud.set_title(f'Bottom {num_achievers} Counties by Budget Absorption Rate', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    save_plot(fig_bottom_bud, f'bottom_{num_achievers}_budget_absorption.png')

    print(f"--- Bar Chart Generation for Top/Bottom {num_achievers} Achievers Complete ---\n")

if __name__ == '__main__':
    # Example usage for testing bar_charts_generator.py independently.
    # In a full workflow, the DataFrame would come from `data_preparation.py`.
    print("Executing `bar_charts_generator.py` directly for testing purposes.")
    # Create a dummy DataFrame for standalone testing
    test_data = pd.DataFrame({
        'County': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Budget Absorption Rate': [70, 85, 60, 75, 90, 50, 55, 65, 45, 40],
        'Revenue Collection (Million KES)': [250, 400, 200, 350, 500, 100, 150, 300, 80, 120]
    })
    generate_bar_charts(test_data, num_achievers=3)
    print("Test bar chart generation function executed. Check the 'plots/' directory.")