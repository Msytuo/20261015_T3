"""
#Vamos a calcular la altura a la que se encuentra un objeto cuando lo dejamos caer en caida libre.
#Tendras como constante la gravedad y debera introducirse la altura inicial y tiempo.
#Con esto calcularemos la velocidad final, el tiempo y la altura final
#Todas variables introducidas, constantes y calculos se haran en unidades del SI

y0 = altura_inicial
v0 = velocidad_final (Es 0 , porque estamos en caida libre)
t = tiempo 
g = gravedad
y = altura_final

y = y0 + v0*t - (0,5*g)*(t**2)
"""
#primero la cte.

GRAVEDADES = {
    "tierra": 9.81,
    "marte": 3.7,
    "luna": 1.68,
    "jupiter": 24.79 ,
    "sol": 274

}
VELOCIDAD_INICIAL = 0

#Pedimos las variables inicials

altura_inicial = float(input("A que altura inicial esta el objeto? (m): "))
tiempo = float(input("A que tiempo quieres medir la altura? (s): "))
ubicacion = input("En que planeta estas? (Tierra, Marte, Luna, Jupiter, Sol): ")
#pasamos la ubi. a minisculas
ubicacion = ubicacion.lower()

#Comprobamos si la ubi. es valida

if ubicacion in GRAVEDADES:
    #tenemos esta ubicion
    GRAVEDAD = GRAVEDADES[ubicacion]
else:

        print(f"Ese planeta, {ubicacion}, no es valido, te asigno la Tierra")
        GRAVEDAD = GRAVEDADES["tierra"]

#Comenzamos el codigo en python para resolver la funcion

altura_final = round(altura_inicial +  (VELOCIDAD_INICIAL * tiempo) - (0.5 * GRAVEDAD * (tiempo ** 2)),2)

#Devolvemos el codigo con un print y comprobamos si ha llegado al suelo.
if altura_final <= 0:
    print(f"El objeto está en el suelo")
else:

    print(f"El objeto se encuentra a una altura de {altura_final} metros tras {tiempo} segundos")
