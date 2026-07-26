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


print("---------------------------------------------------------" )


print(dataframe.describe())
