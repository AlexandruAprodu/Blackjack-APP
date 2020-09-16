


def meniu():
    intrebare_inceput = input('Bine ai venit la masa de BlackJack! Cum te numesti ? ')
    bani_total_jucator = int(input('Cati bani doresti sa cheltui in seara asta ?'))
    print('Dealerul din aceasta seara este Costica! Enjoy!')
    while True:
        bani_joc_curent = int(input('Cati bani doresti sa cheltui pentru aceasta partida? '))
        if bani_joc_curent > bani_total_jucator:
            print('Din pacate nu dispui de fonduri suficiente!')
            continue
        elif bani_joc_curent <= bani_total_jucator:
            print('Sa inceapa jocul !')
            break


meniu()



