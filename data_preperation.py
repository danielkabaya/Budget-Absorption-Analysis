import pandas as pd
import io
# The spss and spssaux imports are commented out as they are specific to
# running within an SPSS environment. Data is hardcoded for general Python use.
# import spss
# import spssaux

def load_and_prepare_data():
    """
    Loads the county data from a hardcoded string and prepares it for analysis.
    This function handles:
    1. Reading the raw data into a pandas DataFrame.
    2. Cleaning the 'Revenue Collection' column by removing commas and converting to float.
    3. Creating a new 'Revenue Collection (Million KES)' column for easier plotting.

    Returns:
        pd.DataFrame: A DataFrame with cleaned and prepared data,
                      ready for plotting and further analysis.
    """
    print("--- Starting Data Loading and Preparation Phase ---")
    print("This module is designed to load and preprocess the raw county data.")

    # Raw data as a multi-line string. In a real-world scenario, this would likely
    # come from a CSV file, a database, or an SPSS dataset.
    raw_data_string = """
    County,Budget Absorption Rate,Revenue Collection,Clean Water Access,Clean Energy Technologies,Under-5 Mortality,Under-5 Stunting Rate,Teenage Pregnancy Rates,Under-5 Enrolled in School
    Mombasa,53.7,"3,608,672,111",72.6,42.2,50,13.5,9.4,92.6
    Kwale,76.7,"302,688,593",68.1,7.5,30,22.7,14.8,76.3
    Kilifi,67.7,"827,496,951",47.2,9,40,37,12.5,86.4
    Tana River,84.5,"72,260,813",42.8,2.1,45,21.1,17.2,50.2
    Lamu,74.8,"126,995,226",43.2,10.6,50,16.1,13.7,83.8
    Taita Taveta,74.3,"315,575,986",53,11.5,29,19.2,18.4,91.7
    Garissa,74.9,"65,624,500",22.8,4.6,44,9,14.8,18.6
    Wajir,80.4,"52,415,625",30.8,1.7,57,12.4,10.8,29.5
    Mandera,87.3,"132,899,851",33.5,1.3,21,20.5,13.9,16.7
    Marsabit,83.2,"99,563,452",42.2,2.1,15,18.9,29.4,59.1
    Isiolo,77.4,"107,832,875",30.6,13.1,33,14.1,16.7,80
    Meru,79.8,"385,391,541",54.6,9.4,35,25.2,23.6,98.8
    Tharaka-Nithi,72.9,"234,293,360",58.6,9,25,20.5,9.9,92.2
    Embu,77.1,"394,540,728",65.8,14.6,44,19.9,14.4,97.5
    Kitui,82.7,"361,271,342",53.3,6.3,27,25.1,9.2,93.9
    Machakos,76.3,"1,118,461,753",85.9,29.4,41,16.2,11.3,97.9
    Makueni,73.2,"749,406,507",86,7.4,38,19.8,11.1,97
    Nyandarua,73.2,"473,061,809",62,7.1,45,17.8,5.2,96.8
    Nyeri,82.7,"948,313,629",61.1,28.4,52,12.5,4.5,94.2
    Kirinyaga,77.3,"364,653,724",57,30.6,56,11.2,7.3,100
    Murang'a,75.6,"520,317,425",62.7,15,47,10.1,7.4,96.2
    Kiambu,73.2,"3,149,182,552",62.4,56.6,40,15.3,11.9,96.4
    Turkana,60.4,"204,349,844",44.3,2.4,55,23,18.5,59
    West Pokot,85.2,"113,444,832",81.3,2.3,46,33.5,36.3,70
    Samburu,79.8,"120,049,011",44.1,2.4,38,31.4,50.1,64.7
    Trans Nzoia,83.9,"379,991,105",78.2,6.7,42,21.3,17.8,93.4
    Uasin Gishu,77.1,"858,341,720",70.9,18.5,37,14.2,10.7,95.3
    Elgeyo Marakwet,77.8,"162,252,071",74.6,2.4,33,21.8,12.1,95.2
    Nandi,84.9,"275,658,466",75.4,7.7,39,15.1,10.5,96.3
    Baringo,72.7,"264,898,800",44,2.1,55,21.2,20.3,87.4
    Laikipia,70,"894,884,655",60.5,15.5,50,12.6,9.1,94.3
    Nakuru,66.2,"1,707,447,685",55.5,19.8,51,18.5,16.5,94.7
    Narok,79.5,"1,334,563,666",67.3,5.2,26,21.5,28.1,84.7
    Kajiado,69.8,"527,943,689",71,49.3,32,14,21.8,84.6
    Kericho,81.9,"566,821,704",88.6,5.5,31,19.3,14.5,94
    Bomet,78.1,"202,430,010",71.5,4,28,22.1,9,97.1
    Kakamega,84.5,"1,226,076,737",80.8,7,45,11.5,15.1,97
    Vihiga,67.4,"236,265,160",89.7,5.2,51,16.6,7.7,98.3
    Bungoma,73.1,"368,035,218",61.1,5.5,55,19,18.6,93.1
    Busia,62.8,"292,736,456",68.8,6.7,53,15,18.3,91.9
    Siaya,79.2,"434,376,276",65.4,5.9,63,19.2,20.9,94.5
    Kisumu,61.5,"982,789,204",68.1,14.7,45,9.1,11.1,96
    Homa Bay,81.4,"146,642,418",47.1,5.1,61,12.5,23.2,94.6
    Migori,83.7,"386,872,946",76.9,5.5,73,14.8,22.4,83.7
    Kisii,76.2,"404,554,620",89.6,9.9,40,16.3,14.2,95.5
    Nyamira,85.5,"166,487,465",71.4,3.4,42,13.5,15.5,91
    Nairobi,71.5,"9,238,804,878",63.1,76.4,44,11.1,8.4,94.3
    """

    # Read the data into a pandas DataFrame using io.StringIO for string input
    try:
        df = pd.read_csv(io.StringIO(raw_data_string), sep=',', quotechar='"', skipinitialspace=True)
        print("Raw data loaded successfully into DataFrame.")
        print("Initial DataFrame head:")
        print(df.head())
    except Exception as e:
        print(f"Error loading raw data: {e}")
        raise

    # Clean the 'Revenue Collection' column: remove commas and convert to float
    print("Cleaning 'Revenue Collection' column (removing commas and converting to numeric)...")
    if 'Revenue Collection' in df.columns and df['Revenue Collection'].dtype == 'object':
        df['Revenue Collection'] = df['Revenue Collection'].str.replace(',', '').astype(float)
        print("'Revenue Collection' column cleaned and converted to float.")
    else:
        print("'Revenue Collection' column already numeric or not found. Skipping cleaning.")

    # Create 'Revenue Collection (Million KES)' for better plot readability
    print("Creating 'Revenue Collection (Million KES)' column for scaled values...")
    df['Revenue Collection (Million KES)'] = df['Revenue Collection'] / 1_000_000
    print("New column 'Revenue Collection (Million KES)' created.")

    print("\nData preparation complete. Prepared DataFrame info:")
    df.info()
    print("\n--- Data Loading and Preparation Phase Complete ---\n")
    return df

if __name__ == '__main__':
    # This block allows this script to be run independently for testing.
    # In a full workflow, `main.py` would call this function.
    print("Executing `data_preparation.py` directly for testing purposes.")
    prepared_data = load_and_prepare_data()
    print(f"Prepared data shape: {prepared_data.shape}")
    print("This script has finished its standalone execution.")