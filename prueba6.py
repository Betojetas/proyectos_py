import matplotlib.pyplot as plt


def generar_grafico_barras():
    # Datos ficticios sobre la incidencia de cáncer en diferentes regiones del mundo
    regiones = ["América", "Europa", "Asia", "África", "Oceania"]
    incidencia_cancer = [
        3792000,
        4230000,
        8751000,
        1055000,
        252000,
    ]  # Números ficticios, reemplaza con datos reales

    # Crear el gráfico de barras
    plt.bar(regiones, incidencia_cancer, color="blue")
    plt.xlabel("Regiones del Mundo")
    plt.ylabel("Incidencia de Cáncer (por cada 100,000 personas)")
    plt.title("Incidencia de Cáncer en el Mundo")
    plt.show()


def generar_grafico_pastel():
    # Datos ficticios sobre la incidencia de cáncer en diferentes regiones del mundo
    regiones = ["América", "Europa", "Asia", "África", "Oceania"]
    incidencia_cancer = [
        3792000,
        4230000,
        8751000,
        1055000,
        252000,
    ]  # Números ficticios, reemplaza con datos reales

    # Crear el gráfico de pastel
    plt.pie(
        incidencia_cancer,
        labels=regiones,
        autopct="%1.1f%%",
        startangle=90,
        colors=["red", "green", "blue", "yellow", "purple"],
    )
    plt.axis("equal")  # Hace que el gráfico de pastel sea circular
    plt.title("Proporción de Incidencia de Cáncer en el Mundo")
    plt.show()


# Llamar a las funciones para generar los gráficos
generar_grafico_barras()
generar_grafico_pastel()
