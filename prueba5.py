from faker import Faker
import pandas as pd

# Crea una instancia de Faker
faker = Faker()

# Genera datos ficticios
num_muestras = 1000  # Número de muestras que deseas generar
data = []
for _ in range(num_muestras):
    nombre = faker.name()
    dirección = faker.address()
    correo = faker.email()
    teléfono = faker.phone_number()
    data.append([nombre, dirección, correo, teléfono])

# Convierte los datos en un DataFrame de Pandas
columnas = ["Nombre", "Dirección", "Correo", "Teléfono"]
df = pd.DataFrame(data, columns=columnas)

# Muestra el DataFrame
print(df)

# Guardar el DataFrame en un archivo CSV
df.to_csv("datos_ficticios.csv", index=False)
