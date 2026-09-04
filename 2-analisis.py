#¿Qué puesto tiene el salario promedio más alto?

import pandas as pd
dataframe=pd.read_csv("ds_salaries_mejorado.csv")

promedio_por_puesto=dataframe.groupby("job_title")["salary_in_usd"].mean()
print(promedio_por_puesto.sort_values(ascending=False).head())

"""Resultado
job_title
Data Analytics Lead         405000.000000
Principal Data Engineer     328333.333333
Financial Data Analyst      275000.000000
Principal Data Scientist    215242.428571
Director of Data Science    195074.000000
Name: salary_in_usd, dtype: float64"""

""" El puesto con el salario mas alto  es Data Analytics Lead, comn un salario promedio de 405000 USD"""
print("--------------conigna 2----------------------------------")
#¿Qué nivel de experiencia gana más?

promedio_experiencia=dataframe.groupby("experience_level")["salary_in_usd"].mean()
print(promedio_experiencia.sort_values(ascending=False))
"""Respuesta
experience_level
EX    199392.038462
SE    138617.292857
MI     87996.056338
EN     61643.318182
el Nivel de experiencia con mayor salario promedio es EX(ejecutivo), con 199392 USD"""

print("---------consiga 3-------------------")

#¿Qué países pagan mejores salarios?

promedio_pais=dataframe.groupby("company_location")["salary_in_usd"].mean()
print(promedio_pais.sort_values(ascending=False).head())

"""Respuesta
company_location
RU    157500.000000
US    144055.261972
NZ    125000.000000
IL    119059.000000
JP    114127.333333
Name: salary_in_usd, dtype: float64
el pais con mayor salario promedio es Rusia(RU),Estados Unidos(US),Nueva Zelanda(NZ),Israel(IL),Japon(Jp) 
"""
print("--------------------conigna 4---------------")

#¿Existe diferencia entre trabajo remoto y presencial?

promedio_modalidad=dataframe.groupby("remote_ratio")["salary_in_usd"].mean()
print(promedio_modalidad.sort_values(ascending=False))

"""Respuesta
remote_ratio
100    122457.454068
0      106354.622047
50      80823.030303
Name: salary_in_usd, dtype: float64
existe diferencia entre trabajo remoto y presencial en cuanto al salario, trabajo remoto presenta un trabajo promedio mayor consueldo 122457 USD"""

print("----------------consigna 5--------------------------")

#¿Qué tamaño de empresa paga mejor?

promedio_tamaño=dataframe.groupby("company_size")["salary_in_usd"].mean()
print(promedio_tamaño.sort_values(ascending=False))

"""respuesta
company_size
L    119242.994949
M    116905.466258
S     77632.674699
Name: salary_in_usd, dtype: float64
las empresas Grandes(L)son las que tienen el mayor salario promedio con  119242 USD"""

print("----------------consigna 6-----------------")
#¿Qué moneda aparece con mayor frecuencia?

Frecuencia_Moneda=dataframe["salary_currency"].value_counts()
print(Frecuencia_Moneda.head(1))
"""Respuesta
la Moneda que aparece con mayor frecuencia es el USD 398 veces"""

print("------consigna 7-------------")

#¿Qué tendencias observan?
"""Respuesta:
las tendencias son las siguientes:
Ejecutivos=EX tivo el promedio mas alto (199.392 USD)
Empresas Grandes= L tubo el promedio mas alto (119.243 USD)
Trabajo remoto=100% remoto tuvo mayor promedio(122.457 USD)
USD= fue la moneda con amyor frecuencia(398 veces)

se observa que los salarios mas altos estan relacionados con niveles de experiencia ejecutivos, empresas grandes
y trabajos remotos.Tambien se observan que el USD es la moneda que aparece con mayor frecuencia"""