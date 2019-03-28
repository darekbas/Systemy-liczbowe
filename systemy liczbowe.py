# -*- encoding: utf-8

def tekst_na_wartosc( x, podst ):
    wartLiczby=0
    # ... konwersja x(podst) na liczbę y
    # (obsługiwane mają być cyfry, małe litery i duże litery)
    for i in range(len(x)):                               # pętla iterująca po znakach wprowadzonej liczby x
        znak = x[i]
        if znak >='0' and znak <= '9':                    # jeżeli znak zawiera się od 0 do 9
            wartCyfry = ord(znak) - ord('0')              # zamiana zmiennej typu string na integer
        elif znak >= 'A' and znak < 'a':                  # jeżeli znak jest literą zawierającą się od A do a
            wartCyfry = 10 + ord(znak) - ord('A')         # zamiana litery na odpowiadającą jej wartość
                                                          # w systemie dziesiątkowym typu integer
        wartZnaku = wartCyfry * podst ** (len(x) - 1 - i) # przemnożenie zmiennych przez odpowiadające im wagi
        wartLiczby += wartZnaku                           # dodanie wartości znaku do końcowej wartości liczby
    return wartLiczby                                     # zwrócenie skonwertowanej liczby

def wartosc_na_tekst(val, podst):
    wynik=''                                               # val w docelowym systemie liczbowym
    listaReszt = []                                        # zmienna w której będą przechowaywane reszty z dzielenia
    while(val >= 1):                                       # pętla wykonuje się dopóki val jest większe lub równe 1
        reszta = val % podst                               # zapisanie reszty z dzielenia do zmiennej
        dziel = val
        val = int(val/podst)                               # przypisanie zmiennej val wartości całkowitej
                                                           # wyniku z dzielenia val/podst
        print("%d/%d = %d reszty %d" % (dziel, podst ,val, reszta))
        listaReszt.append(reszta)                          # zapisanie reszty z dzielenia val/podst do listyReszt

    for reszta in reversed(listaReszt):                    # pętla iterująca od końca listyReszt
        if reszta >= 0 and reszta <= 9:                    # jeżeli reszta zawiera się od 0 do 9
            wynik = wynik + str(reszta)                    # dopisanie ctfry typy string do wyniku
        else:                                              # jeżeli reszta nie zawiera sie w przedziale od 0 do 10
            wynik = wynik + chr(reszta - 10 + ord('A'))    # zamiana reszty typu integer na string
                                                           # i dopisanie jej do wyniku
    return wynik                                           # zwraca przekonwertowaną liczbę

# program konwersji:

P_We = input("Podstawa systemu liczby wejsciowej: ")
P_We = int(P_We)
# tu można sprawdzić czy L_We nie jest pustym łańcuchem oraz czy zawiera znaki w prawidłowym zakresie
L_We = input("Liczba wejsciowa: ")
check = True
while(check):
    if not L_We:
        print('Zły zapis liczby, wpisz jeszcze raz')
        L_We = input("Liczba wejsciowa: ")
    for i in range(len(L_We)):
        if L_We[i] >= 'a':
            print('Zły zapis liczby, wpisz jeszcze raz')
            L_We = input("Liczba wejsciowa: ")
        else:
            check = False
P_Wy = input("Podstawa systemu liczby wyjsciowej: ")
P_Wy = int(P_Wy)
# tu można wprowadzić sprawdzenie czy P_Wy jest liczbą oraz czy jest w zakresie 2<=P_We<=36

# wywołanie funkcji konwertujących
wartosc = tekst_na_wartosc( L_We, P_We )
print( "Liczba {}({}) ma wartość: {}(10)".format( L_We, P_We, wartosc ) )
L_Wy = wartosc_na_tekst( wartosc, P_Wy )
print( "-> Po konwersji: {}({})".format( L_Wy, P_Wy ) )
input()
