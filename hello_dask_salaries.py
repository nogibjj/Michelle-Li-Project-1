import py_compile
from dblib import salaries
ddf = salaries.load_data_dask()
print("one record from dask dataframe without compute:")
print(ddf['experience_level'][0])
print("one record from dask dataframe with compute:")
print(ddf['experience_level'][0].compute())