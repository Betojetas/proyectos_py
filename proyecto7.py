import matplotlib.pyplot as plt
import random

# Datos ficticios para el ejemplo
tipos_cancer = [
    "Pulmón",
    "Mama",
    "Colon",
    "Próstata",
    "Estómago",
    "Hígado",
    "Ovario",
    "Leucemia",
    "Cervical",
    "Cerebro",
    "Tiroides",
    "Páncreas",
    "Esófago",
    "Riñón",
    "Linfoma",
    "Melanoma",
    "Sarcoma",
    "Testicular",
    "Gástrico",
    "Oral",
]
casos_por_tipo = [
    250000,
    180000,
    150000,
    120000,
    95000,
    80000,
    75000,
    70000,
    60000,
    55000,
    50000,
    45000,
    40000,
    35000,
    30000,
    25000,
    20000,
    15000,
    10000,
    5000,
]
tasas_supervivencia = [
    0.35,
    0.75,
    0.65,
    0.80,
    0.30,
    0.25,
    0.60,
    0.50,
    0.70,
    0.55,
    0.40,
    0.20,
    0.45,
    0.55,
    0.75,
    0.85,
    0.65,
    0.80,
    0.90,
    0.30,
]

# Gráfico de dispersión para el desglose por tipo de cáncer
plt.figure(figsize=(10, 6))
plt.scatter(tipos_cancer, casos_por_tipo, color="skyblue", label="Número de casos")
plt.title("Desglose por tipo de cáncer (Gráfico de dispersión)")
plt.xlabel("Tipo de cáncer")
plt.ylabel("Número de casos")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.show()

# Gráfico de dispersión para la tasa de supervivencia global
plt.figure(figsize=(10, 6))
plt.scatter(
    tipos_cancer, tasas_supervivencia, color="lightcoral", label="Tasa de supervivencia"
)
plt.title("Tasa de supervivencia global por tipo de cáncer (Gráfico de dispersión)")
plt.xlabel("Tipo de cáncer")
plt.ylabel("Tasa de supervivencia")
plt.xticks(rotation=45, ha="right")
plt.ylim(
    0, 1
)  # Establecer el rango del eje y entre 0 y 1 para representar la tasa de supervivencia
plt.legend()
plt.tight_layout()
plt.show()
