# datos.simples formas de concatenar en python

apodo = "beto jetas"
concatenar_forma_1 = "hola " + apodo + " como estas"
concatenar_forma_2 = f"hola {apodo} como estas"

print(concatenar_forma_1)
print(concatenar_forma_2)

# operadores de perdtenencia
# si hay un caracter paresido en la variable arroja true si no false
print("hola" in concatenar_forma_1)
# si no existe la cadena "hola beto jetas" arroja un true pero si existe arroja false
print("Hola" not in concatenar_forma_2)
