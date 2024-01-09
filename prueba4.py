from faker import Faker

# Crea una instancia de Faker
fake = Faker()

# Genera datos de personas ficticias
for _ in range(1000):  # Genera datos para 10 personas ficticias
    nombre = fake.name()
    edad = fake.random_int(min=18, max=80)  # Edad entre 18 y 80 años
    direccion = fake.address()
    correo = fake.email()
    numero_telefono = fake.phone_number()

    # Imprime los datos generados
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Dirección: {direccion}")
    print(f"Correo: {correo}")
    print(f"Teléfono: {numero_telefono}")
    print("\n")
