import requests
import csv
import numpy as np
import pandas as pd

#TEPCat fetching csv data, generalised to any links
def tepcat_csv(dat_url:str="https://www.astro.keele.ac.uk/jkt/tepcat/allinfo-csv.csv") -> pd.DataFrame:
    """
    Fetches TEPCat CSV data from a specified URL.

    Parameters
    ----------
    dat_url : str, optional
        The URL of the TEPCat CSV data. The default is "https://www.astro.keele.ac.uk/jkt/tepcat/allinfo-csv.csv".
    
    Returns
    -------
    dat : pandas.DataFrame
        A DataFrame containing the TEPCat data fetched from the specified URL.
    """
    
    with requests.Session() as s:
        # Get the CSV data from the specified URL
        download = s.get(dat_url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        
    dat = pd.DataFrame(my_list[1:], columns=my_list[0])
    return dat


#Data cleaning function for TEPCat tables
def tepcat_tidy(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and tidies the TEPCat DataFrame by renaming columns, converting data types, and handling missing values.
    
    Parameters
    ----------
    dat : pandas.DataFrame
        The TEPCat DataFrame to be tidied up.
        
    Returns
    -------
    new_dat : pandas.DataFrame
        A DataFrame containing the tidied, NaN-replaced TEPCat data.
    """
    
    #Storing  'System' & 'Type' columns as separate list to be re-added later
    System = dat['System'].values.tolist()
    Type = dat['Type'].values.tolist()

    #Rename all column headers to avoid duplicate 'err' names
    new_tepcat_colnames = ['System', 'Type', 'RA(deg)', 'Dec(deg)', 'Vmag', 'Kmag', 'length', 'depth', 'T0(HJDorBJD)', 'T0err',
                           'Period(day)', 'Perioderr', 'Teff', 'Teff_errup', 'Teff_errdn', '[Fe/H]', '[Fe/H]_errup', '[Fe/H]_errdn',
                           'M_A', 'M_A_errup', 'M_A_errdn', 'R_A', 'R_A_errup', 'R_A_errdn', 'loggA', 'loggA_errup', 'loggA_errdn', 
                           'rho_A', 'rho_A_errup', 'rho_A_errdn', 'e', 'e_errup', 'e_errdn', 'a(AU)', 'a(AU)_errup', 'a(AU)_errdn',
                           'M_b', 'M_b_errup', 'M_b_errdn', 'R_b', 'R_b_errup', 'R_b_errdn', 'g_b', 'g_b_errup', 'g_b_errdn',
                           'rho_b', 'rho_b_errup', 'rho_b_errdn', 'Teq', 'Teq_errup', 'Teq_errdn', 'Lambda', 'Lambda_errup', 'Lambda_errdn',
                           'Psi', 'Psi_errup', 'Psi_errdn']
    new_dat = dat.set_axis(new_tepcat_colnames, axis=1)
    
    #Dropping the two string columns at the start to make changing the data types easier
    new_dat.drop('System', axis=1, inplace=True)
    new_dat.drop('Type', axis=1, inplace=True)
    
    # Convert data types of all columns to float
    tot_col_no = len(new_dat.columns)

    for col in new_dat.columns:
        new_dat[col] = pd.to_numeric(new_dat[col], errors='coerce')
        new_dat[col].replace(-1, np.nan, inplace=True)
        new_dat[col].replace(-999, np.nan, inplace=True)
        
    #Re-inserting 'System' & 'Type' columns back into the dataframe and return new tidied up table
    new_dat.insert(0, "System", System)
    new_dat.insert(1, "Type", Type)
    
    return new_dat