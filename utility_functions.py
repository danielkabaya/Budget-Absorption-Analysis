import matplotlib.pyplot as plt
import os

def save_plot(figure: plt.Figure, filename: str, directory: str = 'plots', dpi: int = 300):
    """
    Saves a given Matplotlib figure to a specified file.

    Args:
        figure (plt.Figure): The Matplotlib figure object to save.
        filename (str): The name of the file (e.g., 'my_plot.png').
        directory (str): The directory where the plot should be saved.
                         Defaults to 'plots'. This directory will be created if it doesn't exist.
        dpi (int): The resolution of the saved image in dots per inch.
                   Higher DPI results in a clearer image. Defaults to 300.
    """
    print(f"Attempting to save plot '{filename}' to directory '{directory}'...")
    # Ensure the output directory exists
    os.makedirs(directory, exist_ok=True)
    full_path = os.path.join(directory, filename)

    try:
        figure.savefig(full_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully saved to: {full_path}")
    except Exception as e:
        print(f"Error saving plot '{filename}': {e}")
        print("Please check file path, permissions, and ensure the figure object is valid.")
    finally:
        # Close the plot to free up memory, important for batch processing many plots
        plt.close(figure)
        print(f"Figure for '{filename}' closed.")

if __name__ == '__main__':
    # Example usage for testing utility_functions.py independently
    print("Executing `utility_functions.py` directly for testing purposes.")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    ax.set_title("Test Plot")
    save_plot(fig, 'test_plot_from_utilities.png')
    print("Test plot saving function executed. Check 'plots/test_plot_from_utilities.png'.")