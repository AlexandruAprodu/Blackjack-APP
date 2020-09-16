import random as r
import time as t
from blackjack_module.mecanism_jucator import total_blackjack_jucator

total_blackjack_dealer = 0


class MecanismDealer():

    def mecanism(self):
        while True:
            t.sleep(3)
            global total_blackjack_dealer
            self.carte_dealer = r.randrange(1, 11)
            print(self.carte_dealer)
            total_blackjack_dealer += self.carte_dealer
            print(f'Totalul cartilor dealerului : {total_blackjack_dealer}')
            if (total_blackjack_dealer == 18) or (total_blackjack_dealer == 19) or (total_blackjack_dealer == 20):
                print(f'Dealerul a ales stea si are {total_blackjack_dealer} puncte!')
                break
            elif total_blackjack_dealer == 21:
                print(f'Dealerul are {total_blackjack_dealer} puncte! Casa a castigat')
                break
            elif total_blackjack_dealer > 21:
                print(f'Dealerul are {total_blackjack_dealer} puncte. Ai castigat, felicitari !')
                break
            else:
                continue

def formula_castigatoare():
    if (21 > total_blackjack_jucator > 1) and (21 > total_blackjack_dealer > 1):
        if total_blackjack_jucator > total_blackjack_dealer:
            print(f'Felicitari! Ai castigat mana aceasta !Jucator > {total_blackjack_jucator}, casa > {total_blackjack_dealer}')

        elif total_blackjack_jucator < total_blackjack_dealer:
            print(f'Din pacate casa a castigat ! totalul casei {total_blackjack_dealer}')

        elif total_blackjack_jucator == total_blackjack_dealer:
            print(f'Aceasta partida s-a terminat la egalitate ! Jucator > {total_blackjack_jucator}, casa > {total_blackjack_dealer}')


mecanismdealer = MecanismDealer()

if total_blackjack_jucator > 21:
    pass
elif (total_blackjack_jucator < 21) and (total_blackjack_dealer < 21):
    mecanismdealer.mecanism()
    formula_castigatoare()


