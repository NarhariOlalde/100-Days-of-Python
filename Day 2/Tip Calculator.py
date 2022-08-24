bill = input("Cuanto debe de la cuenta?")
tip = input("Cuando quiere dejar de propina? 10, 15, 20")
personas = input("Cuantas personas estan en la mesa?")


propina = int(tip)/100

billTotal = float(bill) + float(bill) * float(propina )
billPer = float(billTotal)/float(personas)

print(f"La cuenta total es: {billTotal} y por persona es: {round(billPer, 2)}")
