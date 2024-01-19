
GB = int(input("Ingrese los GB que consume: "))
if GB <= 4 and GB != 0:
   pago = 50
elif GB <= 8:
   pago = 85
else:
   pago = 85 + (GB - 8) * 4.50
print("El pago es:", pago)

GB = int(input("Ingrese su consumo: "))
try:
  consumo= float(0)
  consumo_extra = float(0)
  pago = float()
  if 4 >= GB > 0:
    pago=50
  elif 8 >= GB > 4:
    pago=85
  elif GB > 8:
    consumo = GB - 8
    consumo_extra = consumo * 4.5
    pago = 85 + consumo_extra
  print("Debe pagar", pago, "soles")
except:
  print("Valor equivocado")
