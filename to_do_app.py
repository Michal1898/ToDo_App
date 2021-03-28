import pymysql
import cryptography

possible_options=["1", "2", "3", "4", "E", "e"]

selector_switch=""
while str.lower(selector_switch) !="e":
    while selector_switch not in possible_options:
        print("    Menu:")
        print("*"*13)
        print("Zobraz seznam ukolu: stiskni 1")
        print("Vypis seznam ukolu: stiskni 2")
        print("Oznac ukol jako splneny: stiskni 3")
        print("Zadej novy ukol:  stiskni 4")
        print("Ukonci program: stiskni E")
        selector_switch=input("Zadej svoji volbu:")

print("Program bude ukoncen")