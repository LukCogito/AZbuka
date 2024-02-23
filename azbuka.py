# Program na trénování azbuky / ruské cyrilice
import random
from termcolor import colored


# do slovníku si dám ruská písmena a jejich českou výslovnost

azbuka = [
    {"А а" : "a"},
    {"Б б" : "b"},
    {"В в" : "v"},
    {"Г г" : "g"},
    {"Д д" : "d"},
    {"Е е" : "je"},
    {"Ё ё" : "jo"},
    {"Ж ж" : "ž"},
    {"З з" : "z"},
    {"И и" : "i"},
    {"Й й" : "j"},
    {"К к" : "k"},
    {"Л л" : "l"},
    {"M м" : "m"},
    {"Н н" : "n"},
    {"О о" : "o"},
    {"П п" : "p"},
    {"Р р" : "r"},
    {"C с" : "s"},
    {"Т т" : "t"},
    {"У у" : "u"},
    {"Ф ф" : "f"},
    {"Х х" : "ch"},
    {"Ц ц" : "c"},
    {"Ч ч" : "č"},
    {"Ш ш" : "š"},
    {"Щ щ" : "šč"},
    {"Ъ ъ" : "tvrdý znak"},
    {"Ы ы" : "y"},
    {"Ь ь" : "měkký znak"},
    {"Э э" : "e"},
    {"Ю ю" : "ju"},
    {"Я я" : "já"},
    ]


# Definice fce pro náhodný výběr prvku z pole.
def vyber_nahodne(pole_vyberu):
  nahodny_vyber = pole_vyberu[random.randint(0, len(pole_vyberu) - 1)]
  return nahodny_vyber

azbuka_trenink = azbuka

# Uvedení.
print("Toto je program na trénování ruské cyrilice.")

# vytvoření proměnné (pole) pro uchovávání chyb
chyby = []

# Začátek nekonečného cyklu, nutno ukončit příkazem 'break' nebo přerušit program za běhu.
while True:
    
    while len(azbuka_trenink) != 0:
        aktualni = vyber_nahodne(azbuka_trenink)
        vypis_klic = list(aktualni.keys())[0]
        print(f"Písmeno v azbuce: \033[1m{vypis_klic}\033[0m")
        ukol = input("Zadejte výslovnost v české latince: ")

        vypis_hodnota = list(aktualni.values())[0]
        print(vypis_hodnota)

        if ukol == vypis_hodnota:
            print(colored("\033[1mSprávně!\033[0m\n", 'green'))
            azbuka_trenink.remove(aktualni)

        else:
            print(colored("\033[1mŠpatně.\033[0m\n", 'red'))
            chyby.append(aktualni)
            
    # Po dokončení dojde ke kontrole chyb.
    # Pokud je pole s chybami prázdné, dojde k ukončení.
    if len(chyby) == 0:
        # Program gratuluje uživateli.
        print("\033[1mGratuluji, splnili jste celý úkol bez chyb.\033[0m")
        # A ukončí se.
        break
        
    # V opačném případě dojde k procvičení chyb.
    else:
        print("Nyní si pojďme zopakovat ty písmena, u kterých jste udělali chybu.", "\n")

        
        # deklaruji proměnnou pro index
        i = 0
        # Procházím pole s chybami cyklem for.
        while True:
            # Náhodně vyberu chybu k zopakování.
            chyba = vyber_nahodne(chyby)
            # Klíč této položky (slovníku) přiřadím do proměnné a kvůli jednodušímu výpisu převedu na 'list'.
            vypis_klic = list(chyba.keys())
            # A tím, že jej přepíšu nultým indexem ze sebe samého získám hodnotu typu 'str', kterou mohu hezky vypisiovat.
            vypis_klic = vypis_klic[0]
            # Vypíšu jej (klíč je vždy písmeno v azbuce a hodnota prvku přepis výslovnosti v latince).
            print(f"Písmeno v azbuce: \033[1m{vypis_klic}\033[0m")
            # Po uživateli vyžaduji, aby zadal přepis výslovnosti v latince, ten pokud je správně je shodný s hodnotou prvku.
            ukol = input("Zadejte výslovnost v české latince: ")

            # Pro účely porovnání, a tedy vyhodnocení správnosti uživatelova vstupu, uložím do proměnné a převedu na
            # datový typ list, kvůli hezčímu výpisu.
            vypis_hodnota = list(chyba.values())
            vypis_hodnota = vypis_hodnota[0]
            # Rovnou také vypíšu správný výsledek.
            print(vypis_hodnota)

            # A nakonec provedu již zméněné porovnání.
            if ukol == vypis_hodnota:
                print(colored("\033[1mSprávně!\033[0m\n", 'green'))
                chyby.remove(chyba)

            else:
                print(colored("\033[1mŠpatně.\033[0m\n", 'red'))

            # Nakonec ověřím, jestli pole s chybami už bylo vyprázdněno.
            if len(chyby) == 0:
                break
    break               
print("Hotovo.")    