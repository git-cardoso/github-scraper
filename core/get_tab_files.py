import pandas as pd


def get_tab_files(list_tab_files):
    # Calculate sum and percentage with pandas
    temp_tab_files = pd.DataFrame(list_tab_files, columns=[
                                  'extensions', 'lines', 'bytes']).groupby('extensions').sum()

    tab_files = (temp_tab_files.groupby('extensions')
                 .agg({'lines': ['sum', lambda x: x.sum() / temp_tab_files['lines'].sum() * 100],
                       'bytes': ['sum', lambda x: x.sum() / temp_tab_files['bytes'].sum() * 100]
                       })
                 )
    tab_files.columns = tab_files.columns.map(
        '_'.join).str.replace('<lambda>', '%')

    return tab_files
