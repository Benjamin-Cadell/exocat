import pandas as pd
import numpy as np
from exocat import read_tepcat_csv

def test_tepcat_csv():
    # Test the tepcat_csv function with the default URL
    df = read_tepcat_csv.tepcat_csv()
    assert isinstance(df, pd.DataFrame), "Output should be a pandas DataFrame"
    assert not df.empty, "DataFrame should not be empty"
    assert 'System' in df.columns, "DataFrame should contain 'System' column"
    assert 'Type' in df.columns, "DataFrame should contain 'Type' column"
    
def test_tepcat_tidy():
    # Test the tepcat_tidy function with a sample DataFrame
    sample_data = {
        'System': ['System1', 'System2'],
        'Type': ['Type1', 'Type2'],
        'Teq': [300, 400],
        'Teq_errup': [10, 20],
        'Teq_errdn': [5, 15]
    }
    df = pd.DataFrame(sample_data)
    tidied_df = read_tepcat_csv.tepcat_tidy(df)
    
    assert isinstance(tidied_df, pd.DataFrame), "Output should be a pandas DataFrame"
    assert not tidied_df.empty, "Tidied DataFrame should not be empty"
    assert 'Teq' in tidied_df.columns, "Tidied DataFrame should contain 'Teq' column"
    assert tidied_df['Teq'].dtype == float, "'Teq' column should be of type float"
    
if __name__ == "__main__":
    test_tepcat_csv()
    test_tepcat_tidy()