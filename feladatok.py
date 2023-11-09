import random
import math
#1.	feladat:     
def elso():
    a:int = int(input("Kérek egy páros számot!: "))
    while not (a % 2 ==0):
        a:int = int(input("Ez nem páros! Kérek egy páros számot!: "))
        
    print(a)

#2. feladat:
def masodik():
    i:int = 0
    a:int = 0
    while i != 13:
        b:int=math.floor(random.random()*141+10)
        if b % 3 == 0:
            a+=1
        i+=1
    print(f"A számok között {a} db 3-mal osztható van!")

#3.feladat
def harmadik(text,N):
    hossz:int=len(text)

    if N > hossz:
        print("Nincs N. karakter!”")
    elif hossz >= N:
        print(f"A szöveg {N}. karaktere: {text[N-1]} - {text.upper()[N-1]*3}")

#4.feladat
def negyedik():
    b:int = 0
    a:str = str(input("Kérek egy nevet!:"))
    while a != "@":
        a:str = str(input("Kérek egy nevet!:"))
        b += 1
    print(f"A felhasználó {b} nevet adott meg.")

#5.feladat
def otodik():
    a:str = str(input("Kő/Papír/Olló?: "))
    felhasznalo_tippje = a.lower()
    while not (felhasznalo_tippje == "kő" or felhasznalo_tippje == "papír" or felhasznalo_tippje == "olló"):
        print("Nem jó szót adtál meg!")
        a:str = str(input("Kő/Papír/Olló?: "))
        felhasznalo_tippje = a.lower()
        

    b:int = math.floor(random.random()*3+1)
    gep_tippje:str = ""
    if b == 1:
        gep_tippje = "kő"
    if b == 2:
        gep_tippje = "papír"
    if b == 3:
        gep_tippje = "olló"

    print(f"A Felhasználó tippje: {felhasznalo_tippje.capitalize()}")
    print(f"A Gép tippje: {gep_tippje.capitalize()}")   
    print("---------------------") 

    #döntetlen:

    if gep_tippje == felhasznalo_tippje:
        print("Döntetlen")
    #gép vesztes esetei:

    elif gep_tippje == "kő" and felhasznalo_tippje == "papír":
        print("A felhasználó nyert\nA gép vesztett")
    elif gep_tippje == "papír" and felhasznalo_tippje == "olló":
        print("A felhasználó nyert\nA gép vesztett")
    elif gep_tippje == "olló" and felhasznalo_tippje == "kő":
        print("A felhasználó nyert\nA gép vesztett")
    #gép nyertes esetei:

    elif gep_tippje == "kő" and felhasznalo_tippje == "olló":
        print("A gép nyert\nA felhasználó vesztett")
    elif gep_tippje == "papír" and felhasznalo_tippje == "kő":
        print("A gép nyert\nA felhasználó vesztett")
    elif gep_tippje == "olló" and felhasznalo_tippje == "papír":
        print("A gép nyert\nA felhasznéó vesztett")
    
    
        

