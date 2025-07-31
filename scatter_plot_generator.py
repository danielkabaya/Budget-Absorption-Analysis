import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utility_functions import save_plot # Import the shared utility function

def generate_scatter_plot(df: pd.DataFrame, output_filename: str = 'influence_scatter_plot.png'):
    """
    Generates a scatter plot showing the influence of Revenue Collection
    on Budget Absorption, including a regression line and county names.

    Args:
        df (pd.DataFrame): The DataFrame containing 'Revenue Collection (Million KES)',
                           'Budget Absorption Rate', and 'County' columns.
        output_filename (str): The base name of the file to save the plot (e.g., 'my_plot.png').
                               The plot will be saved in the 'plots/' directory by default.
    """
    print(f"\n--- Starting Scatter Plot Generation: {output_filename} ---")
    print("This module generates a scatter plot to visualize the relationship between revenue and budget absorption.")

    # Create a Matplotlib figure and axes for the plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Use Seaborn's regplot to draw the scatter plot with a linear regression model fit
    # scatter_kws for scatter point properties (e.g., transparency)
    # line_kws for regression line properties (e.g., color)
    print("Creating scatter plot with regression line and confidence interval...")
    sns.regplot(x='Revenue Collection (Million KES)', y='Budget Absorption Rate', data=df,
                scatter_kws={'alpha':0.8}, line_kws={'color':'navy'}, ax=ax)

    # Add county names as labels to each data point for detailed identification
    print("Annotating each data point with its respective county name...")
    for i, row in df.iterrows():
        ax.annotate(row['County'], (row['Revenue Collection (Million KES)'], row['Budget Absorption Rate']),
                    textcoords="offset points", xytext=(5,-5), ha='left', fontsize=8)

    # Set informative plot titles and axis labels
    ax.set_title('Influence of Revenue Collection on Budget Absorption with County Names', fontsize=14, pad=15)
    ax.set_xlabel('Revenue Collected (Million KES)', fontsize=12)
    ax.set_ylabel('Budget Absorption Rate (%)', fontsize=12)

    # Enhance readability with a grid
    ax.grid(True, linestyle='--', alpha=0.7)

    # Adjust layout to ensure all elements, especially labels, fit within the figure area
    plt.tight_layout()

    # Save the generated plot using the utility function
    save_plot(fig, output_filename)

    print("--- Scatter Plot Generation Complete ---\n")

if __name__ == '__main__':
    # Example usage for testing scatter_plot_generator.py independently.
    # In a full workflow, the DataFrame would come from `data_preparation.py`.
    print("Executing `scatter_plot_generator.py` directly for testing purposes.")
    # Create a dummy DataFrame for standalone testing
    test_data = pd.DataFrame({
        'County': ['CountyX', 'CountyY', 'CountyZ', 'CountyA', 'CountyB'],
        'Budget Absorption Rate': [72.5, 80.1, 65.0, 78.9, 88.3],
        'Revenue Collection (Million KES)': [300, 450, 250, 400, 550]
    })
    generate_scatter_plot(test_data, 'test_scatter_plot_standalone.png')
    print("Test scatter plot generation function executed. Check 'plots/test_scatter_plot_standalone.png'.")