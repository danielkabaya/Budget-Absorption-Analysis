# Budget-Absorption-Analysis
# County Performance Analysis and Visualization

This repository contains Python code for analyzing and visualizing county-level performance data, specifically focusing on the relationship between revenue collection and budget absorption rates. The project is designed with modularity in mind, making it easy to understand, maintain, and extend.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Data Source](#data-source)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Potential Enhancements](#potential-enhancements)
- [License](#license)

## Project Overview

This project aims to provide insightful visualizations of county performance. It uses a provided dataset containing various metrics, with a particular focus on how well counties collect revenue and absorb their allocated budgets. The visualizations include scatter plots to show correlations and bar charts to highlight top and bottom performing counties.

## Features

- **Data Loading & Preparation:** Reads raw data, cleans "Revenue Collection" figures, and transforms them into a more manageable format (Millions KES).
- **Correlation Visualization:** Generates a scatter plot to illustrate the relationship between Revenue Collection and Budget Absorption Rate, including a linear regression line and confidence interval. County names are annotated on the plot for easy identification.
- **Top/Bottom Achievers Analysis:** Creates bar charts to showcase the top 5 and bottom 5 counties based on both Revenue Collection and Budget Absorption Rate.
- **Modular Codebase:** Organized into separate Python files for data handling, plotting specific chart types, and utility functions, promoting readability and reusability.
- **Automated Plot Saving:** Automatically saves all generated plots to a dedicated `plots/` directory.

## Project Structure

The project is organized into the following Python files:

-   `main.py`: The entry point of the application. It orchestrates the entire workflow by calling functions from other modules.
-   `data_preparation.py`: Contains functions responsible for loading the raw dataset (currently hardcoded for demonstration but easily adaptable for file input) and performing necessary data cleaning and transformations.
-   `scatter_plot_generator.py`: Encapsulates the logic for creating the scatter plot that visualizes the relationship between revenue collection and budget absorption, complete with a regression line and individual county labels.
-   `bar_charts_generator.py`: Houses the functions that generate bar charts to identify and display the top and bottom performing counties based on specified metrics (Revenue Collection and Budget Absorption Rate).
-   `utility_functions.py`: A collection of reusable helper functions, such as `save_plot()`, which handles the saving of Matplotlib figures to disk.
-   `plots/`: (Automatically created directory) This directory will store all the generated plot images (e.g., PNG files).
