prijzen = {
    "aardbei" : int(3),
    "vanille" : int(4),
    "chocolade": int(5)
    }

aanbieding = prijzen['vanille'] * 0.8

reclame_tekst= f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

reclametekst2= reclame_tekst[:62]
reclametekst3= reclametekst2.upper()
reclametekst4= [el.lower() if len(el) <=4 else el.upper() for el in list(reclametekst3)]


for el in reclametekst4:
     print(el)



