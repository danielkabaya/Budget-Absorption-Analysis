# main.py
import data_preparation
import scatter_plot_generator
import bar_charts_generator
import os

def run_analysis_workflow():
    """
    Orchestrates the entire data analysis and plotting workflow.
    Steps include:
    1. Loading and preparing the data.
    2. Generating the scatter plot with county names.
    3. Generating bar charts for top and bottom achievers.
    """
    print("--- Starting Overall Data Analysis Workflow ---")
    print(f"Current working directory: {os.getcwd()}")

    # Step 1: Load and prepare data
    print("Calling `data_preparation.load_and_prepare_data()` to get the DataFrame.")
    df_county_data = data_preparation.load_and_prepare_data()
    if df_county_data.empty:
        print("Error: No data loaded. Exiting analysis workflow.")
        return

    # Step 2: Generate the scatter plot
    print("Calling `scatter_plot_generator.generate_scatter_plot()` to create the scatter plot.")
    scatter_plot_generator.generate_scatter_plot(df_county_data, 'influence_revenue_on_budget_absorption_with_names.png')

    # Step 3: Generate the top/bottom achievers bar charts
    print("Calling `bar_charts_generator.generate_bar_charts()` to create bar charts for achievers.")
    bar_charts_generator.generate_bar_charts(df_county_data, num_achievers=5)

    print("\n--- Overall Data Analysis Workflow Complete ---")
    print("All plots should be saved in the 'plots/' directory.")

if __name__ == '__main__':
    run_analysis_workflow()