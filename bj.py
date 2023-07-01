import random
import time
from colorama import Fore, Back, Style

print(Fore.GREEN)
print(" - Quartzz Blackjack - ")
print(Style.RESET_ALL)
print(" ")

i = 0

# Kartları tanımla
KARTLAR = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Vale', 'Kız', 'Papaz']
DEĞERLER = {'As': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Vale': 10, 'Kız': 10, 'Papaz': 10}

# Oyuncunun elini hesapla
def hesapla_el(el):
    toplam = sum([DEĞERLER[kart] for kart in el])
    if 'As' in el and toplam <= 11:
        toplam += 10
    return toplam

# Oyun döngüsü
while i < 1:

    print("  ")


    deste = KARTLAR * 4
    random.shuffle(deste)

    oyuncu_el = [deste.pop(), deste.pop()]
    krupiye_el = [deste.pop(), deste.pop()]

    krupiye_gösterilen = krupiye_el[0]

    print("--------------------------------------")
    print(Fore.MAGENTA)
    print('Kurpiye gösterilen kart:', krupiye_gösterilen)
    print(Style.RESET_ALL)
    print(Fore.YELLOW)
    print('Oyuncu eli:', oyuncu_el)
    print(Style.RESET_ALL)
    print("--------------------------------------")

    while True:
        oyuncu_skoru = hesapla_el(oyuncu_el)
        if oyuncu_skoru == 21:
            time.sleep(1)
            print(Fore.GREEN)
            print('Oyuncu Blackjack yaptı! Kazandın!')
            print(Style.RESET_ALL)
            i += 1
            break
        elif oyuncu_skoru > 21:
            time.sleep(1)
            print(Fore.RED)
            print('Oyuncunun eli 21\'den büyük. Kaybettin!')
            print(Style.RESET_ALL)
            i += 1
            break
        
        seçim = input('Kart ister misin? [E/H]: ')
        print("--------------------------------------")
        if seçim.lower() == 'e':
            print("Hesaplanıyor . . .")
            time.sleep(1)
            oyuncu_el.append(deste.pop())
            print('Oyuncu eli:', oyuncu_el)
        else:
            break

    krupiye_skoru = hesapla_el(krupiye_el)
    while krupiye_skoru < 17:
        krupiye_el.append(deste.pop())
        krupiye_skoru = hesapla_el(krupiye_el)

    print("Hesaplanıyor . . .")
    time.sleep(1)
    print('Kurpiye eli:', krupiye_el)

    if oyuncu_skoru > 21:
        continue
    elif oyuncu_skoru == krupiye_skoru:
        time.sleep(1)
        print(Fore.WHITE)
        print('Berabere! Oyunu tekrar oyna.')
        print(Style.RESET_ALL)
        i += 1
        time.sleep(3)
    elif oyuncu_skoru > krupiye_skoru:
        time.sleep(1)
        print(Fore.CYAN)
        print('Oyuncu kazandı!')
        print(Style.RESET_ALL)
        i += 1         
        time.sleep(3)
    else:
        time.sleep(1)
        print(Fore.MAGENTA)
        print('Kurpiye kazandı!') 
        print(Style.RESET_ALL)
        i += 1
        time.sleep(3)
