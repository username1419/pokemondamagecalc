import tkinter as tk
from tkinter import ttk
from csv import reader

# secret pokemon code: # + national dex number + regional variant + additional form

def limfour(entry):
    if entry.get() != "" and not entry.get().isnumeric():
        entry.set("")
    try:
        if int(entry.get()) > 1010:
            entry.set("1010")
    except:
        pass

def limthree(entry):
    if entry.get() != "" and not entry.get().isnumeric():
        entry.set("")
    try:
        if len(entry.get()) > 2:
            entry.set("100")
    except:
        pass
    
def limevs(entry):
    if entry.get() != "" and not entry.get().isnumeric():
        entry.set("252")
    try:
        if len(entry.get()) == 0:
            entry.set("0")
        if int(entry.get()) > 252:
            entry.set("252")
    except:
        pass

def limivs(entry):
    if entry.get() != "" and not entry.get().isnumeric():
        entry.set("31")
    try:
        if len(entry.get()) == 0:
            entry.set("0")
        if int(entry.get()) > 31:
            entry.set("31")
    except:
        pass

def atrue_stat_calc(basestat : list):
    hp = [int(ahpivvar.get()),int(ahpevvar.get())]
    atk = [int(aativvar.get()),int(aatevvar.get())]
    def1 = [int(adefivvar.get()),int(adefevvar.get())]
    spatk = [int(spaatkivvar.get()),int(spaatkevvar.get())]
    spdef = [int(spadefivvar.get()),int(spadefevvar.get())]
    sped = [int(aspeivvar.get()),int(aspeevvar.get())]
    level = int(alevelvar.get())
    anaturemod = [1,1,1,1,1,1] # index 0 is kinda useless ngl
    with open('C:/Users/Admin/Desktop/projects/misc/natures.csv') as file:
        a = reader(file) # figure out a better name for this
        for i in a:
            if i[0] == anature.get():
                if i[1] == 'Attack':
                    anaturemod[1] = 0.9
                elif i[1] == 'Defense':
                    anaturemod[2] = 0.9
                elif i[1] == 'SpAtk':
                    anaturemod[3] = 0.9
                elif i[1] == 'SpDef':
                    anaturemod[4] = 0.9
                elif i[1] == 'Speed':
                    anaturemod[5] = 0.9

                if i[2] == 'Attack':
                    anaturemod[1] = 1.1
                elif i[2] == 'Defense':
                    anaturemod[2] = 1.1
                elif i[2] == 'SpAtk':
                    anaturemod[3] = 1.1
                elif i[2] == 'SpDef':
                    anaturemod[4] = 1.1
                elif i[2] == 'Speed':
                    anaturemod[5] = 1.1

                break
    truestat = []
    for i in basestat:
        if i == basestat[0]:
            truestat.append(i)
            continue
        truestat.append(int(i))

    # hp
    truestat[1] = (2*truestat[1]+hp[0]+int(hp[1]/4))*level
    truestat[1] = int(truestat[1]/100)+level+10

    # attack
    truestat[2] = (2*truestat[2]+atk[0]+int(atk[1]/4))*level
    truestat[2] = int(truestat[2]/100)+5
    truestat[2] = int(truestat[2]*anaturemod[1])

    # defense
    truestat[3] = (2*truestat[3]+def1[0]+int(def1[1]/4))*level
    truestat[3] = int(truestat[3]/100)+5
    truestat[3] = int(truestat[3]*anaturemod[2])

    # special attack
    truestat[4] = (2*truestat[4]+spatk[0]+int(spatk[1]/4))*level
    truestat[4] = int(truestat[4]/100)+5
    truestat[4] = int(truestat[4]*anaturemod[3])

    # special defense
    truestat[5] = (2*truestat[5]+spdef[0]+int(spdef[1]/4))*level
    truestat[5] = int(truestat[5]/100)+5
    truestat[5] = int(truestat[5]*anaturemod[4])

    # speed
    truestat[6] = (2*truestat[6]+sped[0]+int(sped[1]/4))*level
    truestat[6] = int(truestat[6]/100)+5
    truestat[6] = int(truestat[6]*anaturemod[5])
    
    return truestat

def btrue_stat_calc(basestat : list):
    hp = [int(bhpivvar.get()),int(bhpevvar.get())]
    atk = [int(bativvar.get()),int(batevvar.get())]
    def1 = [int(bdefivvar.get()),int(bdefevvar.get())]
    spatk = [int(spbatkivvar.get()),int(spbatkevvar.get())]
    spdef = [int(spbdefivvar.get()),int(spbdefevvar.get())]
    sped = [int(bspeivvar.get()),int(bspeevvar.get())]
    level = int(blevelvar.get())
    bnaturemod = [1,1,1,1,1,1] # index 0 is kinda useless ngl
    with open('C:/Users/Admin/Desktop/projects/misc/natures.csv') as file:
        b = reader(file) # figure out a better name for this as well
        for i in b:
            if i[0] == bnature.get():
                if i[1] == 'Attack':
                    bnaturemod[1] = 0.9
                elif i[1] == 'Defense':
                    bnaturemod[2] = 0.9
                elif i[1] == 'SpAtk':
                    bnaturemod[3] = 0.9
                elif i[1] == 'SpDef':
                    bnaturemod[4] = 0.9
                elif i[1] == 'Speed':
                    bnaturemod[5] = 0.9

                if i[2] == 'Attack':
                    bnaturemod[1] = 1.1
                elif i[2] == 'Defense':
                    bnaturemod[2] = 1.1
                elif i[2] == 'SpAtk':
                    bnaturemod[3] = 1.1
                elif i[2] == 'SpDef':
                    bnaturemod[4] = 1.1
                elif i[2] == 'Speed':
                    bnaturemod[5] = 1.1

                break
    truestat = []
    for i in basestat:
        if i == basestat[0]:
            truestat.append(i)
            continue
        truestat.append(int(i))

    # hp
    truestat[1] = (2*truestat[1]+hp[0]+int(hp[1]/4))*level
    truestat[1] = int(truestat[1]/100)+level+10

    # attack
    truestat[2] = (2*truestat[2]+atk[0]+int(atk[1]/4))*level
    truestat[2] = int(truestat[2]/100)+5
    truestat[2] = int(truestat[2]*bnaturemod[1])

    # defense
    truestat[3] = (2*truestat[3]+def1[0]+int(def1[1]/4))*level
    truestat[3] = int(truestat[3]/100)+5
    truestat[3] = int(truestat[3]*bnaturemod[2])

    # special attack
    truestat[4] = (2*truestat[4]+spatk[0]+int(spatk[1]/4))*level
    truestat[4] = int(truestat[4]/100)+5
    truestat[4] = int(truestat[4]*bnaturemod[3])

    # special defense
    truestat[5] = (2*truestat[5]+spdef[0]+int(spdef[1]/4))*level
    truestat[5] = int(truestat[5]/100)+5
    truestat[5] = int(truestat[5]*bnaturemod[4])

    # speed
    truestat[6] = (2*truestat[6]+sped[0]+int(sped[1]/4))*level
    truestat[6] = int(truestat[6]/100)+5
    truestat[6] = int(truestat[6]*bnaturemod[5])
    
    return truestat

def afindpokemon():
    try:
        with open('C:/Users/Admin/Desktop/projects/misc/pokemons.csv') as pokemonfile:
            csvreader = reader(pokemonfile)
            for i in csvreader:
                if anatdexno.get() in i[0]:
                    try:
                        alabel.grid_forget()
                        aform.set("")
                        aregionalform.set("")
                        for y in aframe.grid_slaves(row=13):
                            y.grid_forget()
                    except:
                        pass
                    alabel.config(text=i[1])
                    alabel.grid(column=2,row=12)
                    if i[1] == "Meowth":
                        tk.Label(aframe,text="Form: ",bg="red").grid(column=0,row=13)
                        ameowth.grid(column=1,row=13)
                    elif i[1] == "Tauros":
                        tk.Label(aframe,text="Form: ",bg="red").grid(column=0,row=13)
                        ataurosform.grid(column=1,row=13)
                    elif i[1] in alolan:
                        tk.Label(aframe,text="Form: ",bg="red").grid(column=0,row=13)
                        aalolanform.grid(column=1,row=13)
                    elif i[1] in galarian:
                        tk.Label(aframe,text="Form: ",bg="red").grid(column=0,row=13)
                        agalarianform.grid(column=1,row=13)
                    elif i[1] in paldean:
                        tk.Label(aframe,text="Form: ",bg="red").grid(column=0,row=13)
                        apaldeanform.grid(column=1,row=13)
                    if i[1] in otherforms:
                        tk.Label(aframe,text="Form: ",bg="red").grid(column=0,row=13)
                        if i[1] == "Groudon" or i[1] == "Kyogre":
                            aprimalform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Deoxys":
                            adeoxysform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Burmy" or i[1] == "Wormadam":
                            aburmyandwormadamform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Rotom":
                            arotomform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Giratina":
                            agiratinaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Dialga" or i[1] == "Palkia":
                            aoriginform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Shaymin":
                            ashayminform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Darmanitan":
                            adarmaditanform.grid(column=2,row=13,columnspan=2)
                        elif i[1] in ("Tornadus","Thundurus","Landorus","Enamorus"):
                            aformce_of_nature.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Kyurem":
                            akyuremform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Meloetta":
                            ameloettaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Greninja":
                            agreninjaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Aegislash":
                            aaegislashform.grid(column=2,row=13,columnspan=2)
                        elif i[1] in ("Pumpkaboo","Gourgeist"):
                            apumpkinform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Zygarde":
                            azygardeform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Hoopa":
                            ahoopaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Oricorio":
                            aoricorioform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Lycanroc":
                            alycanrocform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Wishiwashi":
                            awishiwashiform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Minior":
                            aminiorform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Necrozma":
                            anecrozmaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Eiscue":
                            aeiscueform.grid(column=2,row=13,columnspan=2)
                        elif i[1] in ["Zacian","Zamazenta"]:
                            adaugform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Urishifu":
                            aurshifuform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Calyrex":
                            acalyrexform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Palafin":
                            apalafinform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Indeedee":
                            aindeedeeform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Oinkologne":
                            aoinkologneform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Castform":
                            acastFORM.grid(column=2,row=13,columnspan=2)
                    break
                
    except:
        pass

def bfindpokemon():
    try:
        with open('C:/Users/Admin/Desktop/projects/misc/pokemons.csv') as pokemonfile:
            csvreader = reader(pokemonfile)
            for i in csvreader:
                if bnatdexno.get() in i[0]:
                    try:
                        blabel.grid_forget()
                        bform.set("")
                        bregionalform.set("")
                        for y in bframe.grid_slaves(row=13):
                            y.grid_forget()
                    except:
                        pass
                    blabel.config(text=i[1])
                    blabel.grid(column=2,row=12)
                    if i[1] == "Meowth":
                        tk.Label(bframe,text="Form: ",bg="blue").grid(column=0,row=13)
                        bmeowth.grid(column=1,row=13)
                    elif i[0] == "Tauros":
                        tk.Label(bframe,text="Form: ",bg="blue").grid(column=0,row=13)
                        btaurosform.grid(column=1,row=13)
                    elif i[1] in alolan:
                        tk.Label(bframe,text="Form: ",bg="blue").grid(column=0,row=13)
                        balolanform.grid(column=1,row=13)
                    elif i[1] in galarian:
                        tk.Label(bframe,text="Form: ",bg="blue").grid(column=0,row=13)
                        bgalarianform.grid(column=1,row=13)
                    elif i[1] in paldean:
                        tk.Label(bframe,text="Form: ",bg="blue").grid(column=0,row=13)
                        bpaldeanform.grid(column=1,row=13)
                    if i[1] in otherforms:
                        tk.Label(bframe,text="Form: ",bg="blue").grid(column=0,row=13)
                        if i[1] == "Groudon" or i[1] == "Kyogre":
                            bprimalform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Deoxys":
                            bdeoxysform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Burmy" or i[1] == "Wormadam":
                            bburmyandwormadamform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Rotom":
                            brotomform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Giratina":
                            bgiratinaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Dialga" or i[1] == "Palkia":
                            boriginform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Shaymin":
                            bshayminform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Darmanitan":
                            bdarmaditanform.grid(column=2,row=13,columnspan=2)
                        elif i[1] in ("Tornadus","Thundurus","Landorus","Enamorus"):
                            bformce_of_nature.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Kyurem":
                            bkyuremform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Meloetta":
                            bmeloettaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Greninja":
                            bgreninjaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Aegislash":
                            baegislashform.grid(column=2,row=13,columnspan=2)
                        elif i[1] in ("Pumpkaboo","Gourgeist"):
                            bpumpkinform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Zygarde":
                            bzygardeform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Hoopa":
                            bhoopaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Oricorio":
                            boricorioform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Lycanroc":
                            blycanrocform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Wishiwashi":
                            bwishiwashiform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Minior":
                            bminiorform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Necrozma":
                            bnecrozmaform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Eiscue":
                            beiscueform.grid(column=2,row=13,columnspan=2)
                        elif i[1] in ["Zacian","Zamazenta"]:
                            bdaugform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Urishifu":
                            burshifuform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Calyrex":
                            bcalyrexform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Palafin":
                            bpalafinform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Indeedee":
                            bindeedeeform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Oinkologne":
                            boinkologneform.grid(column=2,row=13,columnspan=2)
                        elif i[1] == "Castform":
                            bcastFORM.grid(column=2,row=13,columnspan=2)
                    break
    except:
        pass

def afindstats():
    try:
        atemp = anatdexno.get()
        while len(atemp) != 4:
            atemp = "0"+atemp
        asecretvalue = "#" + atemp
        if aregionalform.get() == "alolan":
            asecretvalue += "A"
        elif aregionalform.get() == "galarian":
            asecretvalue += "G"
        elif aregionalform.get() == "normal":
            asecretvalue += "N"
        elif aregionalform.get() == "hisuian":
            asecretvalue += "H"

        if aform.get() == "normal":
            asecretvalue += "N"
        elif aform.get() in taurosforms:
            if aform.get() == "combat":
                asecretvalue += "C"
            elif aform.get() == "blaze":
                asecretvalue += "F"
            elif aform.get() == "aqua":
                asecretvalue += "A"
        elif aform.get() in deoxysforms:
            if aform.get() == "attack":
                asecretvalue += "A"
            elif aform.get() == "defense":
                asecretvalue += "D"
            elif aform.get() == "speed":
                asecretvalue += "S"
        elif aform.get() in rotomforms:
            if aform.get() == "heat":
                asecretvalue += "H"
            elif aform.get() == "wash":
                asecretvalue += "W"
            elif aform.get() == "frost":
                asecretvalue += "I"
            elif aform.get() == "fan":
                asecretvalue += "F"
            elif aform.get() == "mow":
                asecretvalue += "M"
        elif aform.get() in giratinaforms:
            if aform.get() == "altered":
                asecretvalue += "A"
            elif aform.get() == "origin":
                asecretvalue += "O"
        elif aform.get() in shayminforms:
            if aform.get() == "land":
                asecretvalue += "L"
            elif aform.get() == "sky":
                asecretvalue += "S"
        elif aform.get() in darmaditanforms:
            if aform.get() == "zen":
                asecretvalue += "Z"
        elif aform.get() in formces_of_nature:
            if aform.get() == "incarnate":
                asecretvalue += "I"
            elif aform.get() == "therian":
                asecretvalue += "T"
        elif aform.get() in meloettaforms:
            if aform.get() == "aria":
                asecretvalue += "A"
            elif aform.get() == "pirouette":
                asecretvalue += "P"
        elif aform.get() in kyuremforms:
            if aform.get() == "black":
                asecretvalue += "B"
            elif aform.get() == "white":
                asecretvalue += "W"
        elif aform.get() in greninja:
            if aform.get() == "ash":
                asecretvalue += "A"
        elif aform.get() in aegislashforms:
            if aform.get() == "blade":
                asecretvalue += "B"
            elif aform.get() == "shield":
                asecretvalue += "S"
        elif aform.get() in zygardeforms:
            if aform.get() == "10%":
                asecretvalue += "D"
            elif aform.get() == "50%":
                asecretvalue += "S"
            elif aform.get() == "complete":
                asecretvalue += "C"
        elif aform.get() in hoopaforms:
            if aform.get() == "confined":
                asecretvalue += "C"
            elif aform.get() == "unbound":
                asecretvalue += "U"
        elif aform.get() in lycanrocforms:
            if aform.get() == "midday":
                asecretvalue += "MD"
            elif aform.get() == "midnight":
                asecretvalue += "MN"
            elif aform.get() == "dusk":
                asecretvalue += "DU"
        elif aform.get() in wishiwashiforms:
            if aform.get() == "school":
                asecretvalue += "S"
        elif aform.get() in miniorforms:
            if aform.get() == "meteor":
                asecretvalue += "M"
            elif aform.get() == "core":
                asecretvalue += "C"
        elif aform.get() in necrozmaforms:
            if aform.get() == "dawn wings":
                asecretvalue += "DW"
            elif aform.get() == "dusk mane":
                asecretvalue += "DM"
            elif aform.get() == "ultra":
                asecretvalue += "U"
        elif aform.get() in eiscueforms:
            if aform.get() == "ice face":
                asecretvalue += "I"
            elif aform.get() == "noice face":
                asecretvalue += "N"
        elif int(anatdexno.get()) in (876,902,916):
            if aform.get() == "male":
                asecretvalue += "M"
            elif aform.get() == "female":
                asecretvalue += "F"
        elif aform.get() in daugforms:
            if aform.get() == "hero of many battles":
                asecretvalue += "H"
            elif aform.get() == "crowned":
                asecretvalue += "C"
        elif aform.get() in urshifuforms:
            if aform.get() == "rapid strike style":
                asecretvalue += "R"
            elif aform.get() == "single strike style":
                asecretvalue += "S"
        elif aform.get() in calyrexforms:
            if aform.get() == "ice rider":
                asecretvalue += "I"
            elif aform.get() == "shadow rider":
                asecretvalue += "S"
        elif aform.get() in palafinforms:
            if aform.get() == "zero":
                asecretvalue += "Z"
            elif aform.get() == "hero":
                asecretvalue += "H"
        elif aform.get() in gimighoulforms:
            if aform.get() == "chest":
                asecretvalue += "C"
            elif aform.get() == "roaming":
                asecretvalue += "R"
        elif int(anatdexno.get()) in (382,383):
            if aform.get() == "primal":
                asecretvalue += "P"
        elif aform.get() in castFORMS:
            if aform.get() == "rain":
                asecretvalue += "R"
            elif aform.get() == "sun":
                asecretvalue += "S"
            elif aform.get() == "hail":
                asecretvalue += "H"
        elif int(anatdexno.get()) in (412,413):
            if aform.get() == "plant cloak":
                asecretvalue += "P"
            elif aform.get() == "sand cloak":
                asecretvalue += "S"
            elif aform.get() == "trash cloak":
                asecretvalue += "T"
        elif int(anatdexno.get()) in (710,711):
            if aform.get() == "small":
                asecretvalue += "S"
            elif aform.get() == "average":
                asecretvalue += "M"
            elif aform.get() == "large":
                asecretvalue += "L"
            elif aform.get() == "super":
                asecretvalue += "XL"
        elif aform.get() in oricorioforms:
            if aform.get() == "baile":
                asecretvalue += "B"
            elif aform.get() == "pom-pom":
                asecretvalue += "P"
            elif aform.get() == "p'au":
                asecretvalue += "P'"
            elif aform.get() == "sensu":
                asecretvalue += "S"
        elif int (anatdexno.get()) in (483,484):
            if aform.get() == "origin":
                asecretvalue += "O"

        flag = True
        with open('C:/Users/Admin/Desktop/projects/misc/pokemons base stats.csv') as pokemonstatfile:
            csvreader = reader(pokemonstatfile)
            for i in csvreader:
                if i[0] == asecretvalue:
                    
                    abasestats.config(state=tk.NORMAL)
                    abasestats.delete(1.0,tk.END)
                    abasestats.insert(tk.END,f"""HP: {i[1]}
Atk: {i[2]}
Def: {i[3]}
Sp.Atk: {i[4]}
Sp.Def: {i[5]}
Sped: {i[6]}""")
                    abasestats.config(state=tk.DISABLED)
                    truestat = atrue_stat_calc(i)
                    atruestats.config(state=tk.NORMAL)
                    atruestats.delete(1.0,tk.END)
                    atruestats.insert(tk.END,f"""HP: {truestat[1]}
Atk: {truestat[2]}
Def: {truestat[3]}
Sp.Atk: {truestat[4]}
Sp.Def: {truestat[5]}
Sped: {truestat[6]}""")
                    atruestats.config(state=tk.DISABLED)
                    flag = False
                    break

        if flag:

            with open('C:/Users/Admin/Desktop/projects/misc/pokemons base stats.csv') as pokemonstatfile:
                csvreader = reader(pokemonstatfile)
                for i in csvreader:
                    if i[0] == asecretvalue[:-1]:
                        
                        abasestats.config(state=tk.NORMAL)
                        abasestats.delete(1.0,tk.END)
                        abasestats.insert(tk.END,f"""HP: {i[1]}
Atk: {i[2]}
Def: {i[3]}
Sp.Atk: {i[4]}
Sp.Def: {i[5]}
Sped: {i[6]}""")
                        abasestats.config(state=tk.DISABLED)
                        truestat = atrue_stat_calc(i)
                        atruestats.config(state=tk.NORMAL)
                        atruestats.delete(1.0,tk.END)
                        atruestats.insert(tk.END,f"""HP: {truestat[1]}
Atk: {truestat[2]}
Def: {truestat[3]}
Sp.Atk: {truestat[4]}
Sp.Def: {truestat[5]}
Sped: {truestat[6]}""")
                        atruestats.config(state=tk.DISABLED)
                        flag = False
                        break
    except:
        global nothingtoseeheremoveon
        if nothingtoseeheremoveon:
            abasestats.config(state="normal")
            abasestats.delete(1.0,tk.END)
            abasestats.insert(tk.END,"Really?")
            abasestats.config(state="disabled")
            nothingtoseeheremoveon = False
        else:
            abasestats.config(state="normal")
            abasestats.delete(1.0,tk.END)
            abasestats.insert(tk.END,"Really?")
            abasestats.config(state="disabled")

            atruestats.config(state="normal")
            atruestats.delete(1.0,tk.END)
            atruestats.insert(tk.END,"Are you fucking kidding me?")
            atruestats.config(state="disabled")

def bfindstats():
    try:
        btemp = bnatdexno.get()
        while len(btemp) != 4:
            btemp = "0"+btemp
        bsecretvalue = "#" + btemp
        if bregionalform.get() == "alolan":
            bsecretvalue += "A"
        elif bregionalform.get() == "galarian":
            bsecretvalue += "G"
        elif bregionalform.get() == "normal":
            bsecretvalue += "N"
        elif bregionalform.get() == "hisuian":
            bsecretvalue += "H"

        if bform.get() == "normal":
            bsecretvalue += "N"
        elif bform.get() in taurosforms:
            if bform.get() == "combat":
                bsecretvalue += "C"
            elif bform.get() == "blaze":
                bsecretvalue += "F"
            elif bform.get() == "aqua":
                bsecretvalue += "A"
        elif bform.get() in deoxysforms:
            if bform.get() == "attack":
                bsecretvalue += "A"
            elif bform.get() == "defense":
                bsecretvalue += "D"
            elif bform.get() == "speed":
                bsecretvalue += "S"
        elif bform.get() in rotomforms:
            if bform.get() == "heat":
                bsecretvalue += "H"
            elif bform.get() == "wash":
                bsecretvalue += "W"
            elif bform.get() == "frost":
                bsecretvalue += "I"
            elif bform.get() == "fan":
                bsecretvalue += "F"
            elif bform.get() == "mow":
                bsecretvalue += "M"
        elif bform.get() in giratinaforms:
            if bform.get() == "altered":
                bsecretvalue += "A"
            elif bform.get() == "origin":
                bsecretvalue += "O"
        elif bform.get() in shayminforms:
            if bform.get() == "land":
                bsecretvalue += "L"
            elif bform.get() == "sky":
                bsecretvalue += "S"
        elif bform.get() in darmaditanforms:
            if bform.get() == "zen":
                bsecretvalue += "Z"
        elif bform.get() in formces_of_nature:
            if bform.get() == "incarnate":
                bsecretvalue += "I"
            elif bform.get() == "therian":
                bsecretvalue += "T"
        elif bform.get() in meloettaforms:
            if bform.get() == "aria":
                bsecretvalue += "A"
            elif bform.get() == "pirouette":
                bsecretvalue += "P"
        elif bform.get() in kyuremforms:
            if bform.get() == "black":
                bsecretvalue += "B"
            elif bform.get() == "white":
                bsecretvalue += "W"
        elif bform.get() in greninja:
            if bform.get() == "ash":
                bsecretvalue += "A"
        elif bform.get() in aegislashforms:
            if bform.get() == "blade":
                bsecretvalue += "B"
            elif bform.get() == "shield":
                bsecretvalue += "S"
        elif bform.get() in zygardeforms:
            if bform.get() == "10%":
                bsecretvalue += "D"
            elif bform.get() == "50%":
                bsecretvalue += "S"
            elif bform.get() == "complete":
                bsecretvalue += "C"
        elif bform.get() in hoopaforms:
            if bform.get() == "confined":
                bsecretvalue += "C"
            elif bform.get() == "unbound":
                bsecretvalue += "U"
        elif bform.get() in lycanrocforms:
            if bform.get() == "midday":
                bsecretvalue += "MD"
            elif bform.get() == "midnight":
                bsecretvalue += "MN"
            elif bform.get() == "dusk":
                bsecretvalue += "DU"
        elif bform.get() in wishiwashiforms:
            if bform.get() == "school":
                bsecretvalue += "S"
        elif bform.get() in miniorforms:
            if bform.get() == "meteor":
                bsecretvalue += "M"
            elif bform.get() == "core":
                bsecretvalue += "C"
        elif bform.get() in necrozmaforms:
            if bform.get() == "dawn wings":
                bsecretvalue += "DW"
            elif bform.get() == "dusk mane":
                bsecretvalue += "DM"
            elif bform.get() == "ultra":
                bsecretvalue += "U"
        elif bform.get() in eiscueforms:
            if bform.get() == "ice face":
                bsecretvalue += "I"
            elif bform.get() == "noice face":
                bsecretvalue += "N"
        elif int(bnatdexno.get()) in (876,902,916):
            if bform.get() == "male":
                bsecretvalue += "M"
            elif bform.get() == "female":
                bsecretvalue += "F"
        elif bform.get() in daugforms:
            if bform.get() == "hero of many battles":
                bsecretvalue += "H"
            elif bform.get() == "crowned":
                bsecretvalue += "C"
        elif bform.get() in urshifuforms:
            if bform.get() == "rapid strike style":
                bsecretvalue += "R"
            elif bform.get() == "single strike style":
                bsecretvalue += "S"
        elif bform.get() in calyrexforms:
            if bform.get() == "ice rider":
                bsecretvalue += "I"
            elif bform.get() == "shadow rider":
                bsecretvalue += "S"
        elif bform.get() in palafinforms:
            if bform.get() == "zero":
                bsecretvalue += "Z"
            elif bform.get() == "hero":
                bsecretvalue += "H"
        elif bform.get() in gimighoulforms:
            if bform.get() == "chest":
                bsecretvalue += "C"
            elif bform.get() == "roaming":
                bsecretvalue += "R"
        elif int(bnatdexno.get()) in (382,383):
            if bform.get() == "primal":
                bsecretvalue += "P"
        elif bform.get() in castFORMS:
            if bform.get() == "rain":
                bsecretvalue += "R"
            elif bform.get() == "sun":
                bsecretvalue += "S"
            elif bform.get() == "hail":
                bsecretvalue += "H"
        elif int(bnatdexno.get()) in (412,413):
            if bform.get() == "plant cloak":
                bsecretvalue += "P"
            elif bform.get() == "sand cloak":
                bsecretvalue += "S"
            elif bform.get() == "trash cloak":
                bsecretvalue += "T"
        elif int(bnatdexno.get()) in (710,711):
            if bform.get() == "small":
                bsecretvalue += "S"
            elif bform.get() == "average":
                bsecretvalue += "M"
            elif bform.get() == "large":
                bsecretvalue += "L"
            elif bform.get() == "super":
                bsecretvalue += "XL"
        elif bform.get() in oricorioforms:
            if bform.get() == "baile":
                bsecretvalue += "B"
            elif bform.get() == "pom-pom":
                bsecretvalue += "P"
            elif bform.get() == "p'au":
                bsecretvalue += "P'"
            elif bform.get() == "sensu":
                bsecretvalue += "S"
        elif int (bnatdexno.get()) in (483,484):
            if bform.get() == "origin":
                bsecretvalue += "O"
        
        flag = True
        with open('C:/Users/Admin/Desktop/projects/misc/pokemons base stats.csv') as pokemonstatfile:
            csvreader = reader(pokemonstatfile)
            for i in csvreader:
                if i[0] == bsecretvalue:
                    
                    bbasestats.config(state=tk.NORMAL)
                    bbasestats.delete(1.0,tk.END)
                    bbasestats.insert(tk.END,f"""HP: {i[1]}
Atk: {i[2]}
Def: {i[3]}
Sp.Atk: {i[4]}
Sp.Def: {i[5]}
Sped: {i[6]}""")
                    bbasestats.config(state=tk.DISABLED)
                    truestat = btrue_stat_calc(i)
                    btruestats.config(state=tk.NORMAL)
                    btruestats.delete(1.0,tk.END)
                    btruestats.insert(tk.END,f"""HP: {truestat[1]}
Atk: {truestat[2]}
Def: {truestat[3]}
Sp.Atk: {truestat[4]}
Sp.Def: {truestat[5]}
Sped: {truestat[6]}""")
                    btruestats.config(state=tk.DISABLED)
                    flag = False
                    break

        if flag:

            with open('C:/Users/Admin/Desktop/projects/misc/pokemons base stats.csv') as pokemonstatfile:
                csvreader = reader(pokemonstatfile)
                for i in csvreader:
                    if i[0] == bsecretvalue[:-1]:
                        
                        bbasestats.config(state=tk.NORMAL)
                        bbasestats.delete(1.0,tk.END)
                        bbasestats.insert(tk.END,f"""HP: {i[1]}
Atk: {i[2]}
Def: {i[3]}
Sp.Atk: {i[4]}
Sp.Def: {i[5]}
Sped: {i[6]}""")
                        bbasestats.config(state=tk.DISABLED)
                        truestat = atrue_stat_calc(i)
                        btruestats.config(state=tk.NORMAL)
                        btruestats.delete(1.0,tk.END)
                        btruestats.insert(tk.END,f"""HP: {truestat[1]}
Atk: {truestat[2]}
Def: {truestat[3]}
Sp.Atk: {truestat[4]}
Sp.Def: {truestat[5]}
Sped: {truestat[6]}""")
                        btruestats.config(state=tk.DISABLED)
                        flag = False
                        break
    except:
        global nothingtoseeheremoveon
        if nothingtoseeheremoveon:
            bbasestats.config(state="normal")
            bbasestats.delete(1.0,tk.END)
            bbasestats.insert(tk.END,"Really?")
            bbasestats.config(state="disabled")
            nothingtoseeheremoveon = False
        else:
            bbasestats.config(state="normal")
            bbasestats.delete(1.0,tk.END)
            bbasestats.insert(tk.END,"Really?")
            bbasestats.config(state="disabled")

            btruestats.config(state="normal")
            btruestats.delete(1.0,tk.END)
            btruestats.insert(tk.END,"Are you fucking kidding me?")
            btruestats.config(state="disabled")
    
# declarations
font = ("Courier", 12)
natures = ('Hardy', 'Docile', 'Bashful', 'Quirky', 'Serious', 'Lonely', 'Adamant', 'Naughty', 'Brave', 'Bold', 'Impish', 'Lax', 'Relaxed', 'Modest', 'Mild', 'Rash', 'Quiet', 'Calm', 'Gentle', 'Careful', 'Sassy', 'Timid', 'Hasty', 'Jolly', 'Naive')
nothingtoseeheremoveon = True
alolan = ["Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetales","Diglett","Dugtrio","Meowth","Persian","Geodude","Graveler","Golem","Grimer","Muk","Exeggutor","Marowak"]
galarian = ["Meowth","Ponyta","Rapidash","Farfetch'd","Weezing","Mr.Mime","Corsola","Zigzagoon","Linoone","Darumaka","Darmanitan","Yamask","Stunfisk","Slowpoke","Slowbro","Articuno","Zapdos","Moltres","Slowking"]
paldean = ["Tauros","Wooper"]
otherforms = ["Kyogre","Groudon","Deoxys","Burmy","Wormadam","Rotom","Giratina","Dialga","Plakia","Shaymin","Darmanitan","Tornadus","Thundurus","Landorus","Enamorus","Kyurem","Meloetta","Greninja","Aegislash","Pumpkaboo","Gourgeist","Zygarde","Hoopa","Oricorio","Lycanroc","Wishiwashi","Minior","Necrozma","Eiscue","Zacian","Zamazenta","Urshifu","Calyrex","Palafin","Indeedee","Oinkologne","Castform"]

# ohh boy here goes nothin
deoxysforms = ['normal','attack','defense','speed']
rotomforms = ['normal','heat','wash','fan','mow']# did you know rotom backwards is motor
giratinaforms = ['altered','origin'] # fuck you for wasting my time, past self
shayminforms = ['land','sky']
darmaditanforms = ['normal','zen']
formces_of_nature = ['incarnate','therian']
meloettaforms = ['aria','pirouette']
kyuremforms = ['normal','black','white']
greninja = ['normal','ash'] # rip ash greninja you will most likely not be remembered(2015-2022)
aegislashforms = ['blade','shield']
zygardeforms = ['10%','50%','complete']
hoopaforms = ['confined','unbound']
lycanrocforms = ['midday','midnight','dusk']
wishiwashiforms = ['normal','school']
miniorforms = ['meteor','core']
necrozmaforms = ['normal','dawn wings','dusk mane','ultra']
eiscueforms = ['ice face','noice face']
indeedeeforms = ['male','female']
daugforms = ['hero of many battles','crowned'] # wait is zacian a girl
urshifuforms = ['single strike style','rapid strike style']
calyrexforms = ['normal','ice rider','shadow rider']
basculegionforms = ['male','female']
oinkologneforms = ['male','female']
palafinforms = ['zero','hero']
gimighoulforms = ['chest','roaming']
primalforms = ['normal','primal']
castFORMS = ['normal','rain','sun','hail']
burmyandwormadamforms = ['plant cloak','sandy cloak','trash cloak']
pumpkinforms = ['average','small','large','super'] # why the fuck is there 4 forms for pumpkin pokemon
oricorioforms = ['baile','pom-pom',"pa'u",'sensu']
originforms = ['normal','origin']
taurosforms = ['normal','combat','blaze','aqua']

alolanforms = ['normal','alolan']
galarianforms = ['normal','galarian']
paldeanforms = ['normal','paldean']
meowthregionals = ['normal','alolan','galarian']


# root window
root = tk.Tk()
mainframe = tk.Frame(root,padx=5,pady=5)
mainframe.grid()
root.title("Pokemon Damage? Calculator")

# main stuff

# attacking
aframe = tk.Frame(mainframe, bg="red", relief="raised",padx = 10,pady = 5,borderwidth=2)
aframe.grid(column=0,row=0)

tk.Label(aframe,text="Pokemon level: ",bg="red").grid(column=0,row=0,columnspan=2)
alevel = tk.Entry(aframe,bg="pink",exportselection=0,width=4)
alevel.grid(column=2,row=0,columnspan=2)
alevelvar = tk.StringVar(alevel)
alevelvar.trace("w",lambda *args: limthree(alevelvar))
alevel.config(textvariable=alevelvar)

tk.Label(aframe, text="Pokemon National\nPokeDex Number: ",bg="red").grid(column=0,row=1,columnspan=2)
anatdexno = tk.Entry(aframe,bg="pink",exportselection=0,width=4)
anatdexno.grid(column=2,row=1,columnspan=2)
anatdexvar = tk.StringVar(anatdexno)
anatdexvar.trace("w",lambda *args: limfour(anatdexvar))
anatdexno.config(textvariable=anatdexvar)

tk.Label(aframe, text="HP EVs: ",bg="red").grid(column=0,row=2)
ahpev = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
ahpev.grid(column=1,row=2)
ahpevvar = tk.StringVar(ahpev,"0")
ahpevvar.trace("w",lambda *args: limevs(ahpevvar))
ahpev.config(textvariable=ahpevvar)

tk.Label(aframe, text="Attack EVs: ",bg="red").grid(column=0,row=3)
aatkev = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
aatkev.grid(column=1,row=3)
aatevvar = tk.StringVar(aatkev,"0")
aatevvar.trace("w",lambda *args: limevs(aatevvar))
aatkev.config(textvariable=aatevvar)

tk.Label(aframe, text="Defense EVs: ",bg="red").grid(column=0,row=4)
adefev = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
adefev.grid(column=1,row=4)
adefevvar = tk.StringVar(adefev,"0")
adefevvar.trace("w",lambda *args: limevs(adefevvar))
adefev.config(textvariable=adefevvar)

tk.Label(aframe, text="SpAttack EVs: ",bg="red").grid(column=0,row=5)
spaatkev = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
spaatkev.grid(column=1,row=5)
spaatkevvar = tk.StringVar(spaatkev,"0")
spaatkevvar.trace("w",lambda *args: limevs(spaatkevvar))
spaatkev.config(textvariable=spaatkevvar)

tk.Label(aframe, text="SpDefense EVs: ",bg="red").grid(column=0,row=6)
spadefev = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
spadefev.grid(column=1,row=6)
spadefevvar = tk.StringVar(spadefev,"0")
spadefevvar.trace("w",lambda *args: limevs(spadefevvar))
spadefev.config(textvariable=spadefevvar)

tk.Label(aframe, text="Sped EVs: ",bg="red").grid(column=0,row=7)
aspev = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
aspev.grid(column=1,row=7)
aspeevvar = tk.StringVar(aspev,"0")
aspeevvar.trace("w",lambda *args: limevs(aspeevvar))
aspev.config(textvariable=aspeevvar)

tk.Label(aframe, text="HP IVs: ",bg="red").grid(column=2,row=2)
ahpiv = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
ahpiv.grid(column=3,row=2)
ahpivvar = tk.StringVar(ahpiv,"0")
ahpivvar.trace("w",lambda *args: limivs(ahpivvar))
ahpiv.config(textvariable=ahpivvar)

tk.Label(aframe, text="Attack IVs: ",bg="red").grid(column=2,row=3)
aatkiv = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
aatkiv.grid(column=3,row=3)
aativvar = tk.StringVar(aatkiv,"0")
aativvar.trace("w",lambda *args: limivs(aativvar))
aatkiv.config(textvariable=aativvar)

tk.Label(aframe, text="Defense IVs: ",bg="red").grid(column=2,row=4)
adefiv = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
adefiv.grid(column=3,row=4)
adefivvar = tk.StringVar(adefiv,"0")
adefivvar.trace("w",lambda *args: limivs(adefivvar))
adefiv.config(textvariable=adefivvar)

tk.Label(aframe, text="SpAttack IVs: ",bg="red").grid(column=2,row=5)
spaatkiv = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
spaatkiv.grid(column=3,row=5)
spaatkivvar = tk.StringVar(spaatkiv,"0")
spaatkivvar.trace("w",lambda *args: limivs(spaatkivvar))
spaatkiv.config(textvariable=spaatkivvar)

tk.Label(aframe, text="SpDefense IVs: ",bg="red").grid(column=2,row=6)
spadefiv = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
spadefiv.grid(column=3,row=6)
spadefivvar = tk.StringVar(spadefiv,"0")
spadefivvar.trace("w",lambda *args: limivs(spadefivvar))
spadefiv.config(textvariable=spadefivvar)

tk.Label(aframe, text="Sped IVs: ",bg="red").grid(column=2,row=7)
aspiv = tk.Entry(aframe, bg="pink",exportselection=0,width=4)
aspiv.grid(column=3,row=7)
aspeivvar = tk.StringVar(aspiv,"0")
aspeivvar.trace("w",lambda *args: limivs(aspeivvar))
aspiv.config(textvariable=aspeivvar)

tk.Label(aframe,text="Nature: ",bg="red").grid(column=0,row=8,columnspan=2)
anature = tk.StringVar(aframe,"0")
anaturelist = ttk.OptionMenu(aframe,anature,*natures)
anaturelist.config(textvariable=anature)
anaturelist.grid(column=2,row=8,columnspan=2)

tk.Label(aframe,bg="red",text="Base Stats").grid(column=0,row=9,columnspan=2)
tk.Label(aframe,bg="red",text="True Stats").grid(column=2,row=9,columnspan=2)

abasestats = tk.Text(aframe,bg="pink",state=tk.DISABLED,height=6,width=15)
abasestats.grid(column=0,row=10,columnspan=2)
atruestats = tk.Text(aframe,bg="pink",state=tk.DISABLED,height=6,width=15)
atruestats.grid(column=2,row=10,columnspan=2)

tk.Button(aframe, text="Check Pokemon",command=afindpokemon).grid(column=0,row=11,columnspan=4)
tk.Label(aframe,text="Chosen Pokemon: ",bg="red").grid(column=0,row=12,columnspan=2)
alabel = tk.Label(aframe,text="",bg="red")

aform = tk.StringVar(aframe)
adeoxysform = tk.OptionMenu(aframe,aform,*deoxysforms)
arotomform = tk.OptionMenu(aframe,aform,*rotomforms)
agiratinaform = tk.OptionMenu(aframe,aform,*giratinaforms)
ashayminform = tk.OptionMenu(aframe,aform,*shayminforms)
adarmaditanform = tk.OptionMenu(aframe,aform,*darmaditanforms)
aformce_of_nature = tk.OptionMenu(aframe,aform,*formces_of_nature)
ameloettaform = tk.OptionMenu(aframe,aform,*meloettaforms)
akyuremform = tk.OptionMenu(aframe,aform,*kyuremforms)
agreninjaform = tk.OptionMenu(aframe,aform,*greninja)
aaegislashform = tk.OptionMenu(aframe,aform,*aegislashforms)
azygardeform = tk.OptionMenu(aframe,aform,*zygardeforms)
ahoopaform = tk.OptionMenu(aframe,aform,*hoopaforms)
alycanrocform = tk.OptionMenu(aframe,aform,*lycanrocforms)
awishiwashiform = tk.OptionMenu(aframe,aform,*wishiwashiforms)
aminiorform = tk.OptionMenu(aframe,aform,*miniorforms)
anecrozmaform = tk.OptionMenu(aframe,aform,*necrozmaforms)
aeiscueform = tk.OptionMenu(aframe,aform,*eiscueforms)
aindeedeeform = tk.OptionMenu(aframe,aform,*indeedeeforms)
adaugform = tk.OptionMenu(aframe,aform,*daugforms)
aurshifuform = tk.OptionMenu(aframe,aform,*urshifuforms)
acalyrexform = tk.OptionMenu(aframe,aform,*calyrexforms)
abasculegionform = tk.OptionMenu(aframe,aform,*basculegionforms)
aoinkologneform = tk.OptionMenu(aframe,aform,*oinkologneforms)
apalafinform = tk.OptionMenu(aframe,aform,*palafinforms)
agimighoulform = tk.OptionMenu(aframe,aform,*gimighoulforms)
aprimalform = tk.OptionMenu(aframe,aform,*primalforms)
acastFORM = tk.OptionMenu(aframe,aform,*castFORMS)
aburmyandwormadamform = tk.OptionMenu(aframe,aform,*burmyandwormadamforms)
apumpkinform = tk.OptionMenu(aframe,aform,*pumpkinforms)
aoricorioform = tk.OptionMenu(aframe,aform,*oricorioforms)
aoriginform = tk.OptionMenu(aframe,aform,*originforms)
ataurosform = tk.OptionMenu(aframe,aform,*taurosforms)

aregionalform = tk.StringVar(aframe)
aalolanform = tk.OptionMenu(aframe,aregionalform,*alolanforms)
agalarianform = tk.OptionMenu(aframe,aregionalform,*galarianforms)
apaldeanform = tk.OptionMenu(aframe,aregionalform,*paldeanforms)
ameowth = tk.OptionMenu(aframe,aregionalform,*meowthregionals)

tk.Button(aframe,text="Check Stats",command=afindstats).grid(column=0,row=14,columnspan=4)

# the side that takes damage- pokemon
bframe = tk.Frame(root,relief="raised",bg="blue",padx=10,pady=5,borderwidth=2)
bframe.grid(column=1,row=0)

tk.Label(bframe,text="Pokemon level: ",bg="blue").grid(column=0,row=0,columnspan=2)
blevel = tk.Entry(bframe,bg="cyan",exportselection=0,width=4)
blevel.grid(column=2,row=0,columnspan=2)
blevelvar = tk.StringVar(blevel)
blevelvar.trace("w",lambda *args: limthree(blevelvar))
blevel.config(textvariable=blevelvar)

tk.Label(bframe, text="Pokemon National\nPokeDex Number: ",bg="blue").grid(column=0,row=1,columnspan=2)
bnatdexno = tk.Entry(bframe,bg="cyan",exportselection=0,width=4)
bnatdexno.grid(column=2,row=1,columnspan=2)
bnatdexvar = tk.StringVar(bnatdexno)
bnatdexvar.trace("w",lambda *args: limfour(bnatdexvar))
bnatdexno.config(textvariable=bnatdexvar)

tk.Label(bframe, text="HP EVs: ",bg="blue").grid(column=0,row=2)
bhpev = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
bhpev.grid(column=1,row=2)
bhpevvar = tk.StringVar(bhpev,"0")
bhpevvar.trace("w",lambda *args: limevs(bhpevvar))
bhpev.config(textvariable=bhpevvar)

tk.Label(bframe, text="Attack EVs: ",bg="blue").grid(column=0,row=3)
batkev = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
batkev.grid(column=1,row=3)
batevvar = tk.StringVar(batkev,"0")
batevvar.trace("w",lambda *args: limevs(batevvar))
batkev.config(textvariable=batevvar)

tk.Label(bframe, text="Defense EVs: ",bg="blue").grid(column=0,row=4)
bdefev = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
bdefev.grid(column=1,row=4)
bdefevvar = tk.StringVar(bdefev,"0")
bdefevvar.trace("w",lambda *args: limevs(bdefevvar))
bdefev.config(textvariable=bdefevvar)

tk.Label(bframe, text="SpAttack EVs: ",bg="blue").grid(column=0,row=5)
spbatkev = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
spbatkev.grid(column=1,row=5)
spbatkevvar = tk.StringVar(spbatkev,"0")
spbatkevvar.trace("w",lambda *args: limevs(spbatkevvar))
spbatkev.config(textvariable=spbatkevvar)

tk.Label(bframe, text="SpDefense EVs: ",bg="blue").grid(column=0,row=6)
spbdefev = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
spbdefev.grid(column=1,row=6)
spbdefevvar = tk.StringVar(spbdefev,"0")
spbdefevvar.trace("w",lambda *args: limevs(spbdefevvar))
spbdefev.config(textvariable=spbdefevvar)

tk.Label(bframe, text="Sped EVs: ",bg="blue").grid(column=0,row=7)
bspev = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
bspev.grid(column=1,row=7)
bspeevvar = tk.StringVar(bspev,"0")
bspeevvar.trace("w",lambda *args: limevs(bspeevvar))
bspev.config(textvariable=bspeevvar)

tk.Label(bframe, text="HP IVs: ",bg="blue").grid(column=2,row=2)
bhpiv = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
bhpiv.grid(column=3,row=2)
bhpivvar = tk.StringVar(bhpiv,"0")
bhpivvar.trace("w",lambda *args: limivs(bhpivvar))
bhpiv.config(textvariable=bhpivvar)

tk.Label(bframe, text="Attack IVs: ",bg="blue").grid(column=2,row=3)
batkiv = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
batkiv.grid(column=3,row=3)
bativvar = tk.StringVar(batkiv,"0")
bativvar.trace("w",lambda *args: limivs(bativvar))
batkiv.config(textvariable=bativvar)

tk.Label(bframe, text="Defense IVs: ",bg="blue").grid(column=2,row=4)
bdefiv = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
bdefiv.grid(column=3,row=4)
bdefivvar = tk.StringVar(bdefev,"0")
bdefivvar.trace("w",lambda *args: limivs(bdefivvar))
bdefiv.config(textvariable=bdefivvar)

tk.Label(bframe, text="SpAttack IVs: ",bg="blue").grid(column=2,row=5)
spbatkiv = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
spbatkiv.grid(column=3,row=5)
spbatkivvar = tk.StringVar(spbatkev,"0")
spbatkivvar.trace("w",lambda *args: limivs(spbatkivvar))
spbatkiv.config(textvariable=spbatkivvar)

tk.Label(bframe, text="SpDefense IVs: ",bg="blue").grid(column=2,row=6)
spbdefiv = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
spbdefiv.grid(column=3,row=6)
spbdefivvar = tk.StringVar(spbdefiv,"0")
spbdefivvar.trace("w",lambda *args: limivs(spbdefivvar))
spbdefiv.config(textvariable=spbdefivvar)

tk.Label(bframe, text="Sped IVs: ",bg="blue").grid(column=2,row=7)
bspiv = tk.Entry(bframe, bg="cyan",exportselection=0,width=4)
bspiv.grid(column=3,row=7)
bspeivvar = tk.StringVar(bspiv,"0")
bspeivvar.trace("w",lambda *args: limivs(bspeivvar))
bspiv.config(textvariable=bspeivvar)

tk.Label(bframe,text="Nature: ",bg="blue").grid(column=0,row=8,columnspan=2)
bnature = tk.StringVar(bframe,"0")
bnaturelist = ttk.OptionMenu(bframe,bnature,*natures)
bnaturelist.config(textvariable=bnature)
bnaturelist.grid(column=2,row=8,columnspan=2)

tk.Label(bframe,bg="blue",text="Base Stats").grid(column=0,row=9,columnspan=2)
tk.Label(bframe,bg="blue",text="True Stats").grid(column=2,row=9,columnspan=2)

bbasestats = tk.Text(bframe,bg="cyan",state=tk.DISABLED,height=6,width=15)
bbasestats.grid(column=0,row=10,columnspan=2)
btruestats = tk.Text(bframe,bg="cyan",state=tk.DISABLED,height=6,width=15)
btruestats.grid(column=2,row=10,columnspan=2)

tk.Button(bframe, text="Check Pokemon",command=bfindpokemon).grid(column=0,row=11,columnspan=4)
tk.Label(bframe,text="Chosen Pokemon: ",bg="blue").grid(column=0,row=12,columnspan=2)
blabel = tk.Label(bframe,text="",bg="blue")

# individual forms
bform = tk.StringVar(bframe)
bdeoxysform = tk.OptionMenu(bframe,bform,*deoxysforms)
brotomform = tk.OptionMenu(bframe,bform,*rotomforms)
bgiratinaform = tk.OptionMenu(bframe,bform,*giratinaforms)
bshayminform = tk.OptionMenu(bframe,bform,*shayminforms)
bdarmaditanform = tk.OptionMenu(bframe,bform,*darmaditanforms)
bformce_of_nature = tk.OptionMenu(bframe,bform,*formces_of_nature)
bmeloettaform = tk.OptionMenu(bframe,bform,*meloettaforms)
bkyuremform = tk.OptionMenu(bframe,bform,*kyuremforms)
bgreninjaform = tk.OptionMenu(bframe,bform,*greninja)
baegislashform = tk.OptionMenu(bframe,bform,*aegislashforms)
bzygardeform = tk.OptionMenu(bframe,bform,*zygardeforms)
bhoopaform = tk.OptionMenu(bframe,bform,*hoopaforms)
blycanrocform = tk.OptionMenu(bframe,bform,*lycanrocforms)
bwishiwashiform = tk.OptionMenu(bframe,bform,*wishiwashiforms)
bminiorform = tk.OptionMenu(bframe,bform,*miniorforms)
bnecrozmaform = tk.OptionMenu(bframe,bform,*necrozmaforms)
beiscueform = tk.OptionMenu(bframe,bform,*eiscueforms)
bindeedeeform = tk.OptionMenu(bframe,bform,*indeedeeforms)
bdaugform = tk.OptionMenu(bframe,bform,*daugforms)
burshifuform = tk.OptionMenu(bframe,bform,*urshifuforms)
bcalyrexform = tk.OptionMenu(bframe,bform,*calyrexforms)
bbasculegionform = tk.OptionMenu(bframe,bform,*basculegionforms)
boinkologneform = tk.OptionMenu(bframe,bform,*oinkologneforms)
bpalafinform = tk.OptionMenu(bframe,bform,*palafinforms)
bgimighoulform = tk.OptionMenu(bframe,bform,*gimighoulforms)
bprimalform = tk.OptionMenu(bframe,bform,*primalforms)
bcastFORM = tk.OptionMenu(bframe,bform,*castFORMS)
bburmyandwormadamform = tk.OptionMenu(bframe,bform,*burmyandwormadamforms)
bpumpkinform = tk.OptionMenu(bframe,bform,*pumpkinforms)
boricorioform = tk.OptionMenu(bframe,bform,*oricorioforms)
boriginform = tk.OptionMenu(bframe,bform,*originforms)
btaurosform = tk.OptionMenu(bframe,bform,*taurosforms)

# regional forms
bregionalform = tk.StringVar(bframe)
balolanform = tk.OptionMenu(bframe,bregionalform,*alolanforms)
bgalarianform = tk.OptionMenu(bframe,bregionalform,*galarianforms)
bpaldeanform = tk.OptionMenu(bframe,bregionalform,*paldeanforms)
bmeowth = tk.OptionMenu(bframe,bregionalform,*meowthregionals)

tk.Button(bframe,text="Check Stats",command=bfindstats).grid(column=0,row=14,columnspan=4)

root.mainloop()