import matplotlib.pyplot as plt
import pandas as pd

pharma = pd.read_csv("./Farmacos_Producto_Comercial.csv", index_col=0)
print(pharma.info())

pharma_sort = pharma.sort_values("Laboratorio_Comercial", ascending=False)
pharma_lab = pharma[ (pharma["Laboratorio_Comercial"] == "Europharma") | (pharma["Laboratorio_Comercial"] == "Laboratorio Saval S.A.") ]
pharma_formA = pharma[pharma["glosa_FFE"] == "supositorio"]
pharma_formB = pharma[pharma["glosa_FFE"] == "gel tópico"]

# Get proportion for each type
pharma_per_type = ([pharma_formA, pharma_formB])
print(pharma_per_type)

form_by_type = pharma.groupby(["glosa_FFE", "Laboratorio_Comercial"])
print(form_by_type.first())

print(pharma.sort_index(level=["glosa_FFE"]))
# pharma_pivot = pharma.pivot_table(values="glosa_FFE", index=["PC_Término_Preferido","Preferido_Fármacos_Familia_de_Productos"], columns="id_Bioequivalente")
# print(pharma_pivot)

print(pharma_sort)
print(pharma_lab)
print(pharma.head())
print(pharma.values)
print(pharma.columns)
print(pharma.index)
print(pharma[["PC_Término_Preferido", "Laboratorio_Comercial"]])