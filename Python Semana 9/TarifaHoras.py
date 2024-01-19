def computepay(hours,rate):
    if hours>40:
        pago = 40*rate + (hours-40)*(1.5*rate)
    else:
        pago = 40*rate
    return pago

hours = input("Ingresar horas: ")
rate = input("Tarifa: ")
hours = int(hours)
rate = int(rate)
pago = computepay(hours, rate)
print("Pago: ", pago)

