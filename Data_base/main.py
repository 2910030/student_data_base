#Student data base, Ludniewski Bartas, peace
import os

studenci=[]

class Student:
    def __init__(self, imie, nazwisko, pesel):
        self.imie=imie
        self.nazwisko=nazwisko
        self.pesel=pesel

def add(lista):
    lista.append(student)
    return lista

def delete(pesel):
    with open('dane.txt') as f:
        lista=f.readlines()
    plik_danych = open('dane.txt','w')
    for x in range(0,len(lista)):
        if pesel in lista[x]:
            pass
        else:
            plik_danych.write(lista[x])
    plik_danych.close()

def check(nazw):
    with open('dane.txt') as f:
        datafile = f.readlines()
    for line in datafile:
        if nazw in line:
            print(line)

while 1:
    print("1. Dodaj")
    print("2. Usun PESEL")
    print("3. Szukaj PESEL")
    print("4. Wyswietl")
    print("0: Koniec")

    w = int(input("Wybór: "))

    if w == 1:
        print("Dodaj studenta: ")
        imie = str(input("Podaj imie: "))
        nazwisko = str(input("Podaj nazwisko: "))
        pesel = int(input("Podaj PESEL: "))
        student = Student(imie, nazwisko, pesel)
        add(studenci)
        zap = str(input('Zapisac do pliku?: '))
        if zap == 'TAK' or 'tak':
            plik_danych=open('dane.txt', "a")
            plik_danych.write("{} {} {}\n".format(student.imie, student.nazwisko, student.pesel))
            plik_danych.close()
        elif zap == 'NIE' or 'nie':
            pass

    if w == 2:
        do_usuniecia = str(input("PESEL do usuniecia?: "))
        delete(do_usuniecia)

    if w == 3:
        szukaj = str(input("Wyszukaj pesel: "))
        check(szukaj)

    if w == 4:

        if (os.path.isfile('dane.txt')) == 0:
            print("Lista jest pusta")
        else:
            print("\nLista studentow")
            plik_danych=open('dane.txt', "r+")
            for line in plik_danych:
                    print(line, end="")
            plik_danych.close()

    if w == 0:
        break
