def mijn_pensioen(pensioenleeftijd, werkstatus, wekelijks_bedrag):
    mijnLeeftijd = int(input("Wat is je leeftijd? Voer het aantal jaren in:"))
    
    if mijnLeeftijd < pensioenleeftijd:
        Resterende_leeftijd = pensioenleeftijd - mijnLeeftijd
        uitvoer = (f"Van werken word je gelukkig, je mag nog {Resterende_leeftijd} jaar genieten van je baan.")
        print (uitvoer)
        
    else:
        mijn_werkstatus =str(input("Wat is je werkstatus? Voer in: medewerker, zelfstandige of ambtenaar:"))
        mijnbedrag = "?"
        if mijn_werkstatus == werkstatus[0]:
            mijnbedrag = wekelijks_bedrag[0]
        elif mijn_werkstatus == werkstatus[1]:
            mijnbedrag = wekelijks_bedrag[1]
        elif mijn_werkstatus == werkstatus[2]:
            mijnbedrag = wekelijks_bedrag[2]
        uitvoer = (f"Je krijgt € {mijnbedrag} per week.")
        print (uitvoer)
        return uitvoer

pensioenleeftijd = 65
mijn_werkstatus = ["medewerker", "zelfstandige", "ambtenaar"]
wekelijks_bedrag = [350, 300, 370]

mijn_pensioen(pensioenleeftijd, mijn_werkstatus, wekelijks_bedrag)