import pandas as pd

dataframe = pd.read_csv("ds_salaries.csv")

print(dataframe.isnull().sum())
"""Unnamed: 0            0
work_year             0
experience_level      0
employment_type       0
job_title             0
salary                0
salary_currency       0
salary_in_usd         0
employee_residence    0
remote_ratio          0
company_location      0
company_size          0"""

#no se encontraron dotos nulos o faltantes


print(dataframe.duplicated().sum())
print("Duplicados")
"""Unnamed: 0            0
work_year             0
experience_level      0
employment_type       0
job_title             0
salary                0
salary_currency       0
salary_in_usd         0
employee_residence    0
remote_ratio          0
company_location      0
company_size          0
dtype: int64
0
Duplicados"""
# NO se encontraron registros Duplicados 

dataframe.rename(columns={
    "wor_year":"Año_de_trabajo",
    "experience_level ":"nivel_de_experiencia",
    "employment_type":"tipo_de_empleo",
    "job_title ":"título profesional",
    "salary ":"salario",
    "salary_currency  ":"moneda_del_salario",
    "salary_in_usd ":"salario_en_USD",
    "employee_residence  ":"residencia del empleado",
    "remote_ratio  ":"relación_remota",
    "company_location ": "ubicación_de_la_empresa",
    "company_size " : "tamaño_de_la_empresa"
}, inplace=True)

print(dataframe.head())
"""   Unnamed: 0  work_year  ... company_location company_size
0           0       2020  ...               DE            L
1           1       2020  ...               JP            S
2           2       2020  ...               GB            M
3           3       2020  ...               HN            S
4           4       2020  ...               US            L

[5 rows x 12 columns]"""
print(dataframe.tail())

"""     Unnamed: 0  work_year  ... company_location company_size
602         602       2022  ...               US            M
603         603       2022  ...               US            M
604         604       2022  ...               US            M
605         605       2022  ...               US            M
606         606       2022  ...               US            L

[5 rows x 12 columns]"""

print("-----------------------------------------------------")

print(dataframe.info())
"""RangeIndex: 607 entries, 0 to 606
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   Unnamed: 0          607 non-null    int64
 1   work_year           607 non-null    int64
 2   experience_level    607 non-null    str  
 3   tipo_de_empleo      607 non-null    str  
 4   job_title           607 non-null    str  
 5   salary              607 non-null    int64
 6   salary_currency     607 non-null    str  
 7   salary_in_usd       607 non-null    int64
 8   employee_residence  607 non-null    str  
 9   remote_ratio        607 non-null    int64
 10  company_location    607 non-null    str  
 11  company_size        607 non-null    str  
dtypes: int64(5), str(7)
memory usage: 57.0 KB
None"""
# los datos eran correctos y no fue necesario modificarlos
# ademas  la colimna " Unnamed 0", se elimino por que fue un indice generado al exportar el archivo
print("---------------------------------------------------------" )

print(dataframe.describe())

"""       Unnamed: 0    work_year        salary  salary_in_usd  remote_ratio
count  607.000000   607.000000  6.070000e+02     607.000000     607.00000
mean   303.000000  2021.405272  3.240001e+05  112297.869852      70.92257
std    175.370085     0.692133  1.544357e+06   70957.259411      40.70913
min      0.000000  2020.000000  4.000000e+03    2859.000000       0.00000
25%    151.500000  2021.000000  7.000000e+04   62726.000000      50.00000
50%    303.000000  2022.000000  1.150000e+05  101570.000000     100.00000
75%    454.500000  2022.000000  1.650000e+05  150000.000000     100.00000
max    606.000000  2022.000000  3.040000e+07  600000.000000     100.00000

"""
print("---------------------------------------------------------------------")

print(dataframe.dtypes)

"""Unnamed: 0            int64
work_year             int64
experience_level        str
tipo_de_empleo          str
job_title               str
salary                int64
salary_currency         str
salary_in_usd         int64
employee_residence      str
remote_ratio          int64
company_location        str
company_size            str
dtype: object"""
print("------------------------------------------------------------------")

dataframe.drop("Unnamed: 0", axis=1,inplace=True)
"""<class 'pandas.DataFrame'>
RangeIndex: 607 entries, 0 to 606
Data columns (total 11 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   work_year           607 non-null    int64
 1   experience_level    607 non-null    str  
 2   tipo_de_empleo      607 non-null    str  
 3   job_title           607 non-null    str  
 4   salary              607 non-null    int64
 5   salary_currency     607 non-null    str  
 6   salary_in_usd       607 non-null    int64
 7   employee_residence  607 non-null    str  
 8   remote_ratio        607 non-null    int64
 9   company_location    607 non-null    str  
 10  company_size        607 non-null    str  
dtypes: int64(4), str(7)
memory usage: 52.3 KB
None"""


print(dataframe.info())
