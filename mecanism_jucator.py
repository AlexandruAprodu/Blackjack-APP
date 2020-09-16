import random as r

total_blackjack_jucator = 0



class MecanismJucator():
    def mecanism(self):
        while True:
            global total_blackjack_jucator
            choice_card = int(input('Apasa 1 pentru hit si 2 pentru stand: '))
            if choice_card == 1:
                self.carte_jucator = r.randrange(1, 11)
                print(self.carte_jucator)
                total_blackjack_jucator += self.carte_jucator
                print(f'Totalul cartilor este {total_blackjack_jucator}')
                if total_blackjack_jucator == 21:
                    print(f'Felicitari ai facut {total_blackjack_jucator} puncte si ai castigat !')
                    break
                elif total_blackjack_jucator > 21:
                    print(f'Din pacate ai facut {total_blackjack_jucator} si ai pierdut !')
                    break
            elif choice_card == 2:
                print(f'Ai ales sa stai, totalul tau este: {total_blackjack_jucator}.')
                break


mecanismjucator = MecanismJucator()
mecanismjucator.mecanism()
