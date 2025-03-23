# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Primera llamada: solo mostrar el monto total con el descuento aplicado (por defecto 10%)
monto1 = 300
descuento1 = calcular_descuento(monto1)
total1 = monto1 - descuento1
print("Primera compra:")
print(f"  Total con descuento aplicado: ${total1}\n")

# Segunda llamada: mostrar todo (monto, descuento, total)
monto2 = 1800
porcentaje2 = 20
descuento2 = calcular_descuento(monto2, porcentaje2)
total2 = monto2 - descuento2
print("Segunda compra:")
print(f"  Monto original: ${monto2}")
print(f"  Descuento aplicado ({porcentaje2}%): ${descuento2}")
print(f"  Total a pagar con descuento: ${total2}")