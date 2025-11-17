import time

def menu():
    global producte, preu, quantitat, opcio, comanda_creada
    print("__________________________________________________\n")
    print("=========== GESTIÓ COMANDES RESTAURANT ===========")
    print("__________________________________________________\n")
    print("1. Crear nova comanda")
    print("2. Actualitzar comanda anterior")
    print("3. Visualitzar últim tiquet")
    print("4. Sortir")

    try:
        opcio = int(input("> Tria una opció: "))
    except:
        print("Opció no vàlida")
        return menu()

    match opcio:
        case 1:
            crear()

        case 2:
            if not comanda_creada:
                print("No hi ha cap comanda enregistrada")
                time.sleep(2)
                return menu()
            actualizar()

        case 3:
            if not comanda_creada:
                print("No hi ha cap comanda enregistrada")
                time.sleep(2)
                return menu()
            visualitzar()

        case 4:
            sortir()

        case _:
            print("Opció no vàlida")
            time.sleep(1)
            return menu()


def crear():
    global nom, producte, preu, quantitat, opcio, linea_producte, total, iva, total_iva, comanda_creada
    print("__________________________________________________\n")
    print("================= NOVA COMANDA ===================")
    print("__________________________________________________\n")
    
    linea_producte = ""
    total = 0
    afegir=''

    nom=str(input("> Introdueix el nom del client: "))

    while afegir != 'n':
        producte=str(input("> Introdueix el producte: "))
        preu=float(input("> Preu unitari (€): " ))
        quantitat=int(input("> Quantitat: " ))
        afegir=str(input("> Vols afegir un altre producte? (s/n)" )).lower()
        
        subtotal=preu*quantitat
        total+=subtotal

        linea_producte += f"{producte}        {quantitat}           {preu:.2f}€       {subtotal:.2f}€\n"

    print("S’està generant el tiquet…\n")
    time.sleep(2)
    print("__________________________________________________\n")
    print("===================== TIQUET =====================")
    print("__________________________________________________\n")
    print(f"Client: {nom}")
    print("Producte        Quantitat   Preu unit.   Subtotal")
    print("--------------------------------------------------")
    print(linea_producte)

    iva = total/10
    total_iva = total + iva
    print("--------------------------------------------------")
    print(f"Total sense IVA:                          {total:.2f} €")
    print(f"IVA (10%):                                {iva:.2f} €")
    print(f"TOTAL A PAGAR:                            {total_iva:.2f} €")
    print("==================================================")
    comanda_creada = True
    time.sleep(2)
    menu()

def actualizar():
    global nom, producte, preu, quantitat, opcio, linea_producte, total, iva, total_iva
    afegir=''

    print("> Actualitzant comanda de:", nom)

    while afegir != 'n':
        producte=str(input("> Introdueix el producte: "))
        preu=float(input("> Preu unitari (€): " ))
        quantitat=int(input("> Quantitat: " ))
        afegir=str(input("> Vols afegir un altre producte? (s/n)" )).lower()

        subtotal=preu*quantitat
        total+=subtotal

        linea_producte += f"{producte}        {quantitat}           {preu:.2f}€       {subtotal:.2f}€\n" 

    print("S'està actualitzant la comanda…\n")
    time.sleep(2)
    print("__________________________________________________\n")
    print("=============== TIQUET ACTUALITZAT ===============")
    print("__________________________________________________\n")
    print(f"Client: {nom}")
    print("Producte        Quantitat   Preu unit.   Subtotal")
    print("--------------------------------------------------")
    print(linea_producte)
    iva=total/10
    total_iva=total + iva
    print("--------------------------------------------------")
    print(f"Total sense IVA:                          {total:.2f} €")
    print(f"IVA (10%):                                {iva:.2f} €")
    print(f"TOTAL A PAGAR:                            {total_iva:.2f} €")
    print("==================================================")
    print("Comanda actualitzada correctament.\n")
    time.sleep(2)
    menu()

def visualitzar():
    global nom, producte, preu, quantitat, opcio
    print("__________________________________________________\n")
    print("================= ÚLTIM TIQUET ==================")
    print("__________________________________________________\n")
    print(f"Client: {nom}")
    print("Producte        Quantitat   Preu unit.   Subtotal")
    print("--------------------------------------------------")
    print(linea_producte)
    print("--------------------------------------------------")
    print(f"Total sense IVA:                          {total:.2f} €")
    print(f"IVA (10%):                                {iva:.2f} €")
    print(f"TOTAL A PAGAR:                            {total_iva:.2f} €")
    print("==================================================")
    time.sleep(2)
    menu()

def sortir():
    print("__________________________________________________\n")
    print("================ FINS LA PROPERA! ================")
    print("__________________________________________________\n")

if __name__=='__main__':
    nom = ""
    producte = ""
    preu = 0.0
    quantitat = 0
    opcio = ""
    linea_producte = ""
    total = 0
    iva = 0
    total_iva = 0
    comanda_creada = False

    menu()
