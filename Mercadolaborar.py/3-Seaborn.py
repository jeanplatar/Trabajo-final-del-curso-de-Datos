import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

dataframe = pd.read_csv("ds_salaries_mejorado.csv")

#Histograma de salarios.

sns.histplot(data=dataframe, x="salary_in_usd")
plt.title("Salarios")
plt.savefig("histograma_Salarios.jpg")

plt.clf()


print("----------Boxplot por experiencia.----------------")

sns.boxplot(data=dataframe, x="experience_level",y="salary_in_usd")
plt.title("salario por nivel de experiencia")
plt.savefig("boxplot Experiencia.jpg")
plt.clf()

print("-----------Barplot por país.----------------------")


promedio_pais=dataframe.groupby("company_location")["salary_in_usd"].mean()
promedio_pais=promedio_pais.sort_values(ascending=False).head(10)
print(promedio_pais)
sns.barplot(x=promedio_pais.index, y=promedio_pais.values)
plt.title("Top 10 paises por salario promedio")
plt.xticks(rotation=45)
plt.savefig("barplot_pais.jpg")
plt.clf()

print("-----------Countplot por tamaño de empresa.------------")

sns.countplot(data=dataframe, x="company_size")
plt.title("Registro por Tamaño de Empresa")
plt.savefig("countplot tamaño_empresas.jpg")

plt.clf()

print("------------Boxplot por modalidad remota-----------------")

sns.boxplot(data=dataframe, x="remote_ratio",y="salary_in_usd")
plt.title("salario por modalida_remota")
plt.savefig("boxplot Modalida .jpg")
plt.clf()

print("--------------Heatmap----------------")

plt.figure(figsize=(10,7))
corr = dataframe.drop(columns=["Unnamed: 0"]).corr(numeric_only=True)
plt.title("mapa de calor")
sns.heatmap(corr, annot=True)

plt.savefig("heatmap.jpg")
plt.clf()