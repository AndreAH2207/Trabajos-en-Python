def computerPay(horas, tarifa):
  extras = 0
  if horas >40 :
    extras = horas-40
    pagar =  40*tarifa + extras*1.5*tarifa;
  else:
    pagar = horas*tarifa
  return pagar
  
  horas = int(input("Ingrese horas:"))
  tarifa = float(input("Ingrese tarifa:"))
  print(f"Total a pagar {computerPay(horas, tarifa)} soles")
