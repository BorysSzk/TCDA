import os
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

dane_titanic = pd.read_csv(r'train.csv')

ofiary = dane_titanic[dane_titanic['Survived'] == 0]
ocal = dane_titanic[dane_titanic['Survived'] == 1]



def tabela_titanic():
    '''
    Próba wyświetlenia ogólnej tabeli zbioru danych Titanic'a (kolejna funkcja już lepsza)
    '''

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    #pd.set_option('display.max_colwidth', 1000)
    #pd.set_option('display.width', 1000)
    print(dane_titanic)

    return ""


def tabela_titanic_max():
    '''
    Funkcja wyświetla ogólną tabelę (w ramcę) zbioru danych Titanic'a
    '''

    print(f"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"| PassengerId | Name                                                      | Sex     | Age   | Pclass | Survived | SibSp  | Parch | Ticket      | Fare     | Cabin            | Embarked |")
    print(f"-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    for index, rows in dane_titanic.iterrows():
        print(f"| {rows['PassengerId']:<11} | {rows['Name'][:56]:<57} | {rows['Sex']:<7} | {rows['Age']:<5} | {rows['Pclass']:<6} | {rows['Survived']:<8} | {rows['SibSp']:<6} | {rows['Parch']:<5} | {rows['Ticket'][:10]:<11} | {rows['Fare']:<8}" \
                f" | {rows['Cabin']:<16} | {rows['Embarked']:<8} |")

    print(f"-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def slownik_danych():
    '''
    Funkcja wyświetla słownik danych ogólnej tabeli pasażerów
    '''

    print("\n________________________________________"\
    "\nSłownik danych ogólnej tabeli pasażerów: \n" \
    "\n_____________________________________________________________________________________________________________________________________________________________________________________" \
    "\n| PassengerId - Passenger Identification                                              (pl. Identyfikator Pasażera (ten identyfikator odnosi się do numeracji w tym zbiorze danych)) |" \
    "\n| Survived    - Survived  0 = No, 1 = Yes                                             (pl. Przeżycie 0 - Nie, 1 - Tak)                                                              |" \
    "\n| Pclass      - Ticket class  1 = 1st, 2 = 2nd, 3 = 3rd                               (pl. Klasa biletu, 1st - pierwsza, 2nd - druga, 3rd - trzecia)                                |" \
    "\n| Sex         - Sex  (male, female)                                                   (pl. Płeć (mężczyzna, kobieta))                                                               |" \
    "\n| Age         - Age in years                                                          (pl. Wiek w latach)                                                                           |" \
    "\n| SibSp       - Number of siblings / spouses aboard the Titanic                       (pl. Liczba rodzeństwa / małżonków na pokładzie Titanic'a)                                    |" \
    "\n| Parch       - Number of parents / children aboard the Titanic                       (pl. Liczba rodziców / dzieci na pokładzie Titanic'a)                                         |" \
    "\n| Ticket      - Ticket number                                                         (pl. Numer biletu)                                                                            |" \
    "\n| Fare        - Passenger fare                                                        (pl. Opłata za przejazd pasażera)                                                             |" \
    "\n| Cabin       - Cabin number                                                          (pl. Numer kabiny)                                                                            |" \
    "\n| Embarked    - Port of Embarkation - C = Cherbourg, Q = Queenstown, S = Southampton  (pl. Port zaokrętowania (wejścia na pokład)                                                   |" \
    "\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def wiek_ofiar():
    '''
    Funkcja wyświetla histogram wieku ofiar Titanic'a
    '''
    sns.set_style('whitegrid')

    w_o = sns.histplot(ofiary['Age'], discrete = True, shrink = .8, alpha = 1, color = '#b82a20')

    plt.xlabel('Wiek')
    plt.ylabel('Liczba ofiar')
    w_o.set(title="Wiek ofiar")

    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74])
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

    widocznosc = True
    if (widocznosc):
        xticks = w_o.xaxis.get_major_ticks()
        xticks[4].label1.set_visible(False)
        xticks[11].label1.set_visible(False)
        xticks[12].label1.set_visible(False)
        xticks[52].label1.set_visible(False)
        xticks[62].label1.set_visible(False)
        xticks[66].label1.set_visible(False)
        xticks[67].label1.set_visible(False)
        xticks[68].label1.set_visible(False)
        xticks[71].label1.set_visible(False)
        xticks[72].label1.set_visible(False)

    plt.show()

    return ""


def wiek_ocalałych():
    '''
    Funkcja wyświetla histogram wieku ocalałych Titanic'a
    '''
    sns.set_style('whitegrid')

    w_oc = sns.histplot(ocal['Age'], discrete = True, shrink = .8, alpha = 1, binrange = [1, 80], color = '#20b848')

    plt.xlabel('Wiek')
    plt.ylabel('Liczba ocalałych')
    w_oc.set(title="Wiek ocalałych")
    
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80])
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

    widocznosc = True
    if (widocznosc):
        xticks = w_oc.xaxis.get_major_ticks()
        xticks[9].label1.set_visible(False)
        xticks[45].label1.set_visible(False)
        xticks[56].label1.set_visible(False)
        xticks[58].label1.set_visible(False)
        xticks[60].label1.set_visible(False)
        xticks[63].label1.set_visible(False)
        xticks[64].label1.set_visible(False)
        xticks[65].label1.set_visible(False)
        xticks[66].label1.set_visible(False)
        xticks[67].label1.set_visible(False)
        xticks[68].label1.set_visible(False)
        xticks[69].label1.set_visible(False)
        xticks[70].label1.set_visible(False)
        xticks[71].label1.set_visible(False)
        xticks[72].label1.set_visible(False)
        xticks[73].label1.set_visible(False)
        xticks[74].label1.set_visible(False)
        xticks[75].label1.set_visible(False)
        xticks[76].label1.set_visible(False)
        xticks[77].label1.set_visible(False)
        xticks[78].label1.set_visible(False)

    plt.show()

    return ""


def wiek_pasażerów():
    '''
    Funkcja wyświetla histogram wieku pasażerów Titanic'a
    '''
    sns.set_style('whitegrid')

    w_p = sns.histplot(dane_titanic['Age'], shrink = 0.8, discrete = True, alpha = 1, binrange = [1, 80], color = '#208fb8')

    plt.xlabel('Wiek')
    plt.ylabel('Liczba pasażerów')
    w_p.set(title = "Wiek pasażerów")

    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80])
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32])

    widocznosc = True
    if (widocznosc):
        xticks = w_p.xaxis.get_major_ticks()
        xticks[66].label1.set_visible(False)
        xticks[67].label1.set_visible(False)
        xticks[68].label1.set_visible(False)
        xticks[71].label1.set_visible(False)
        xticks[72].label1.set_visible(False)
        xticks[74].label1.set_visible(False)
        xticks[75].label1.set_visible(False)
        xticks[76].label1.set_visible(False)
        xticks[77].label1.set_visible(False)
        xticks[78].label1.set_visible(False)
    
    plt.show()

    return ""


def wiek_all():
    '''
    Funkcja wyświetla wszystkie wykresy kategorii wieku ofiar (itd.) Titanic'a - naraz w tym samym momencie
    '''
    plt.figure(1)

    sns.set_style('whitegrid')

    w_o = sns.histplot(ofiary['Age'], discrete = True, shrink = .8, alpha = 1, color = '#b82a20')

    plt.xlabel('Wiek')
    plt.ylabel('Liczba ofiar')
    w_o.set(title="Wiek ofiar")

    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74])
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

    widocznosc = True
    if (widocznosc):
        xticks = w_o.xaxis.get_major_ticks()
        xticks[4].label1.set_visible(False)
        xticks[11].label1.set_visible(False)
        xticks[12].label1.set_visible(False)
        xticks[52].label1.set_visible(False)
        xticks[62].label1.set_visible(False)
        xticks[66].label1.set_visible(False)
        xticks[67].label1.set_visible(False)
        xticks[68].label1.set_visible(False)
        xticks[71].label1.set_visible(False)
        xticks[72].label1.set_visible(False)

    plt.figure(2)

    sns.set_style('whitegrid')

    w_oc = sns.histplot(ocal['Age'], discrete = True, shrink = .8, alpha = 1, binrange = [1, 80], color = '#20b848')

    plt.xlabel('Wiek')
    plt.ylabel('Liczba ocalałych')
    w_oc.set(title="Wiek ocalałych")
    
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80])
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

    widocznosc = True
    if (widocznosc):
        xticks = w_oc.xaxis.get_major_ticks()
        xticks[9].label1.set_visible(False)
        xticks[45].label1.set_visible(False)
        xticks[56].label1.set_visible(False)
        xticks[58].label1.set_visible(False)
        xticks[60].label1.set_visible(False)
        xticks[63].label1.set_visible(False)
        xticks[64].label1.set_visible(False)
        xticks[65].label1.set_visible(False)
        xticks[66].label1.set_visible(False)
        xticks[67].label1.set_visible(False)
        xticks[68].label1.set_visible(False)
        xticks[69].label1.set_visible(False)
        xticks[70].label1.set_visible(False)
        xticks[71].label1.set_visible(False)
        xticks[72].label1.set_visible(False)
        xticks[73].label1.set_visible(False)
        xticks[74].label1.set_visible(False)
        xticks[75].label1.set_visible(False)
        xticks[76].label1.set_visible(False)
        xticks[77].label1.set_visible(False)
        xticks[78].label1.set_visible(False)

    plt.figure(3)

    sns.set_style('whitegrid')

    w_p = sns.histplot(dane_titanic['Age'], shrink = 0.8, discrete = True, alpha = 1, binrange = [1, 80], color = '#208fb8')

    plt.xlabel('Wiek')
    plt.ylabel('Liczba pasażerów')
    w_p.set(title = "Wiek pasażerów")

    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80])
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32])

    widocznosc = True
    if (widocznosc):
        xticks = w_p.xaxis.get_major_ticks()
        xticks[66].label1.set_visible(False)
        xticks[67].label1.set_visible(False)
        xticks[68].label1.set_visible(False)
        xticks[71].label1.set_visible(False)
        xticks[72].label1.set_visible(False)
        xticks[74].label1.set_visible(False)
        xticks[75].label1.set_visible(False)
        xticks[76].label1.set_visible(False)
        xticks[77].label1.set_visible(False)
        xticks[78].label1.set_visible(False)

    plt.show()

    return ""


def status_ofiar():
    '''
    Funkcja wyświetla histogram klas biletów ofiar Titanic'a (na podstawie klas biletów ofiar, wnioskujemy status społeczny tych osób)
    '''
    plt.figure(1)

    s_o = sns.histplot(ofiary['Pclass'], shrink = .8, edgecolor = "white", discrete = True)

    plt.xlabel('Klasa biletu')
    plt.ylabel('Liczba ofiar')
    plt.xticks([1,2,3])

    s_o.patches[0].set_facecolor('#6149ff')
    s_o.patches[1].set_facecolor('#bc49ff')
    s_o.patches[2].set_facecolor('#49ceff')

    s_o.set(title = "Klasy biletów ofiar (na podstawie którego, wnioskujemy ich status społeczny)")

    plt.text(0.5,375,'Czym większa liczba klasy biletu - tym niższy status społeczny')

    for i in s_o.containers:
        s_o.bar_label(i,)

    plt.show()

    return ""


def status_pasażerów():
    '''
    Funkcja wyświetla wykres słupkowy klas biletów pasażerów Titanic'a z podziałem na ofiary i ocalałych (na podstawie klas biletów pasażerów, wnioskujemy ich status społeczny)
    '''
    plt.figure(2)

    s_p = sns.countplot(dane_titanic, x = 'Pclass', hue = 'Survived')

    plt.xlabel('Klasa biletu')
    plt.ylabel('Liczba pasażerów')
    s_p.set(title="Klasy biletów pasażerów (na podstawie którego, wnioskujemy ich status społeczny)")

    s_p.patches[0].set_facecolor('#6149ff')
    s_p.patches[1].set_facecolor('#6149ff')
    s_p.patches[2].set_facecolor('#6149ff')
    s_p.patches[3].set_facecolor('#ffb049')
    s_p.patches[4].set_facecolor('#ffb049')
    s_p.patches[5].set_facecolor('#ffb049')

    s_p.patches[-1].set_facecolor('#ffb049')
    s_p.patches[-2].set_facecolor('#6149ff')

    plt.legend(title = 'Przeżycie (0 - Nie, 1 - Tak)',
    loc = 'upper right',
    labels = [0,1])

    plt.text(-0.45,375,'Czym większa liczba klasy biletu - tym niższy status społeczny')

    for i in s_p.containers:
        s_p.bar_label(i,)

    plt.show()

    return ""


def status_all():
    '''
    Funkcja wyświetla wszystkie wykresy kategorii statusu społecznego ofiar (itd.) Titanic'a - naraz w tym samym momencie
    '''
    plt.figure(1)

    s_o = sns.histplot(ofiary['Pclass'], shrink = .8, edgecolor = "white", discrete = True)

    plt.xlabel('Klasa biletu')
    plt.ylabel('Liczba ofiar')
    plt.xticks([1,2,3])

    s_o.patches[0].set_facecolor('#6149ff')
    s_o.patches[1].set_facecolor('#bc49ff')
    s_o.patches[2].set_facecolor('#49ceff')

    s_o.set(title = "Klasy biletów ofiar (na podstawie którego, wnioskujemy ich status społeczny)")

    plt.text(0.5,375,'Czym większa liczba klasy biletu - tym niższy status społeczny')

    for i in s_o.containers:
        s_o.bar_label(i,)


    plt.figure(2)

    s_p = sns.countplot(dane_titanic, x = 'Pclass', hue = 'Survived')

    plt.xlabel('Klasa biletu')
    plt.ylabel('Liczba pasażerów')
    s_p.set(title="Klasy biletów pasażerów (na podstawie którego, wnioskujemy ich status społeczny)")

    s_p.patches[0].set_facecolor('#6149ff')
    s_p.patches[1].set_facecolor('#6149ff')
    s_p.patches[2].set_facecolor('#6149ff')
    s_p.patches[3].set_facecolor('#ffb049')
    s_p.patches[4].set_facecolor('#ffb049')
    s_p.patches[5].set_facecolor('#ffb049')
    

    s_p.patches[-1].set_facecolor('#ffb049')
    s_p.patches[-2].set_facecolor('#6149ff')


    plt.legend(title = 'Przeżycie (0 - Nie, 1 - Tak)',
    loc = 'upper right',
    labels = [0,1])

    plt.text(-0.45,375,'Czym większa liczba klasy biletu - tym niższy status społeczny')

    for i in s_p.containers:
        s_p.bar_label(i,)

    plt.show()

    return ""


def płeć_ofiar():
    '''
    Funkcja wyświetla histogram płci ofiar Titanic'a
    '''
    plt.figure(1)

    df = dane_titanic
    ofiary1 = df[df['Survived'] == 0]
    ofiary1['Sex'].replace({"female":"Kobiety","male":"Mężczyźni"},inplace=True)

    p_o = sns.histplot(ofiary1['Sex'], shrink = 0.8, color='#ff9f32', edgecolor='None', alpha = .7)
    
    plt.xlabel('Płeć')
    plt.ylabel('Liczba ofiar')
    p_o.set(title = "Płeć ofiar")
    
    p_o.patches[0].set_facecolor('#4332ff')

    for i in p_o.containers:
        p_o.bar_label(i,)

    plt.show()

    return ""


def płeć_pasażerów():
    '''
    Funkcja wyświetla wykres słupkowy płci pasażerów Titanic'a
    '''
    plt.figure(2)

    sns.set_theme(style = 'whitegrid')

    df = dane_titanic
    df['Sex'].replace({"female":"Kobiety","male":"Mężczyźni"},inplace=True)

    p_p = sns.countplot(df, x = 'Sex', hue = 'Survived', palette = 'dark')

    plt.xlabel('Płeć')
    plt.ylabel('Liczba pasażerów')
    #p_p.set_xticklabels(['Mężczyźni', 'Kobiety'])

    p_p.set(title = "Płeć pasażerów")

    plt.legend(title = 'Przeżycie (0 - Nie, 1 - Tak)',
    loc = 'upper right',
    labels = [0, 1])

    for i in p_p.containers:
        p_p.bar_label(i,)

    plt.show()

    return ""


def płeć_all():
    '''
    Funkcja wyświetla wszystkie wykresy kategorii płci ofiar (itd.) Titanic'a - naraz w tym samym momencie
    '''
    plt.figure(1)

    df = dane_titanic
    ofiary1 = df[df['Survived'] == 0]
    ofiary1['Sex'].replace({"female":"Kobiety","male":"Mężczyźni"},inplace=True)

    p_o = sns.histplot(ofiary1['Sex'], shrink = 0.8, color='#ff9f32', edgecolor='None', alpha = .7)
    
    plt.xlabel('Płeć')
    plt.ylabel('Liczba ofiar')
    p_o.set(title = "Płeć ofiar")
    
    p_o.patches[0].set_facecolor('#4332ff')


    for i in p_o.containers:
        p_o.bar_label(i,)

    plt.figure(2)

    sns.set_theme(style = 'whitegrid')

    df = dane_titanic
    df['Sex'].replace({"female":"Kobiety","male":"Mężczyźni"},inplace=True)

    p_p = sns.countplot(df, x = 'Sex', hue = 'Survived', palette = 'dark')

    plt.xlabel('Płeć')
    plt.ylabel('Liczba pasażerów')


    p_p.set(title = "Płeć pasażerów")

    plt.legend(title = 'Przeżycie (0 - Nie, 1 - Tak)',
    loc = 'upper right',
    labels = [0, 1])

    for i in p_p.containers:
        p_p.bar_label(i,)

    plt.show()

    return ""


def inter_wiek():
    '''
    Funkcja otwiera pdf z interpretacją analiz wieku ofiar Titanic'a
    '''
    os.startfile("inter-wiek.pdf")

    return ""


def inter_status():
    '''
    Funkcja otwiera pdf z interpretacją analiz statusów społecznych ofiar Titanic'a
    '''
    os.startfile("inter-status.pdf")

    return ""


def inter_płeć():
    '''
    Funkcja otwiera pdf z interpretacją analiz płci ofiar Titanic'a
    '''
    os.startfile("inter-plec.pdf")

    return ""


def main():
    '''
    Funkcja włącza program i wyświetla interfejs konsolowy pozwalający na "poruszanie" się po programie
    '''
    wyjscie = 0

    print("\n------------------------------------------------------------------------------\n" \
        "\n Witaj w analizerze danych ofiar Titanic'a (ADOT)!\n" \
        "\n------------------------------------------------------------------------------\n")

    while True:
        if (wyjscie == 1):
            break

        menu = input("\n Podaj którąś z podanych poniżej liter, żeby rozpocząć analizę danych: \n\n P - pokaż listę głównych komend \n W - wyłącz program \n\n ---> ").upper()

        while True:
            if (wyjscie == 1):
                break

            if menu == "P":
                komenda = input("\n\n----------------------------------------------------------------------------------------\n" \
                                "\n Lista komend:\n\n T - ogólna tabela pasażerów\n S - słownik danych (najbardziej przydatny do analizy danych ogólnej tabeli pasażerów)\n G - co mogło mieć"
                                " wpływ na przeżycie pasażerów? (przejście do głębszej części analizy) \n\n C - cofnij do poprzedniego punktu\n W - wyłącz program" \
                                "\n\n----------------------------------------------------------------------------------------" \
                                "\n\n Wpisz którąś z powyższych komend, jeśli chcesz przejść dalej, wrócić do poprzedniego punktu lub wyłączyć program: \n\n ---> ").upper()


                if komenda == "T":

                    tabela_titanic_max()


                elif komenda == "S":

                    slownik_danych()

                
                elif komenda == "G":

                    while True:

                        if wyjscie == 1:
                            break

                        komenda2 = input("\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"\
                                        "\n W głębszej części analizy danych ofiar Titanic'a, zwizualizowaliśmy dokładne odpowiedzi na pytanie: 'Co mogło mieć wpływ na przeżycie pasażerów?'."\
                                        "\n Niektórzy powiedzą, że ich płeć, inni że wiek, a jeszcze inni, że znaczenie miał status społeczny, ponieważ ludzie wyżsi tego-też-statusu hierarchią - zostali wcześniej poinformowani o ewakuacji z Titanic'a. Ale jak to było naprawdę?" \
                                        "\n\n Możesz dokładnie się temu przyjrzeć i samemu te dane dokładnie zinterpretować, dzięki sporządzonym przez nas wykresom! Ale jeśli nadal nie będziesz pewien(-na), to również sami odpowiedzieliśmy na te pytania i wszystko jest dla Ciebie \n dostępne!" \
                                        "\n Wybierz którąś z poniższych komend, aby wyświetlić któryś z wykresów, czy interpretację części danych (i odpowiedź na pytanie: 'Czy miało to wpływ na przeżycie pasażerów?') - lub wyłącz program: "\
                                        "\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
                                        "\n\n 1. Analiza wieku ofiar Titanic'a (z porównaniami do ocalałych i wszystkich pasażerów): " \
                                        "\n\n WOF - wiek ofiar\n WOC - wiek ocalałych\n WP - wiek wszystkich pasażerów\n W@ - wyświetl wszystkie wykresy tej kategorii na raz\n IW - interpretacja wykresów dotyczących wieku ofiar Titanic'a:" \
                                        "\n\n 2. Analiza statusu społecznego ofiar na podstawie ich klas biletów (z porównaniem do wszystkich pasażerów): " \
                                        "\n\n SO - status społeczny ofiar\n SP - status społeczny pasażerów\n S@ - wyświetl wszystkie wykresy tej kategorii na raz\n IS - interpretacja wykresów dotyczących statusu społecznego wnioskowanego na podstawie klas biletów ofiar Titanic'a:" \
                                        "\n\n\n 3. Analiza płci ofiar (z porównaniem do wszystkich pasażerów):\n\n PO - płeć ofiar\n PP - płeć pasażerów\n P@ - wyświetl wszystkie wykresy tej kategorii na raz\n IP - interpretacja wykresów płci ofiar i pasażerów" \
                                        "\n\n C - cofnij do poprzedniego punktu\n W - wyłącz program\n\n ---> ").upper()


                        if komenda2 == "WOC":

                            wiek_ocalałych()


                        elif komenda2 == "WOF":

                            wiek_ofiar()


                        elif komenda2 == "WP":

                            wiek_pasażerów()


                        elif komenda2 == "W@":

                            wiek_all()


                        elif komenda2 == "IW":

                            inter_wiek()


                        elif komenda2 == "SO":

                            status_ofiar()


                        elif komenda2 == "SP":

                            status_pasażerów()


                        elif komenda2 == "S@":

                            status_all()


                        elif komenda2 == "IS":

                            inter_status()


                        elif komenda2 == "PO":

                            płeć_ofiar()


                        elif komenda2 == "PP":

                            płeć_pasażerów()


                        elif komenda2 == "P@":

                            płeć_all()

            
                        elif komenda2 == "IP":

                            inter_płeć()


                        elif komenda2 == "C":
                            break


                        elif komenda2 == "W":
                            wyjscie = 1
                            print("\n------------------------------------------------------------------------------------------" \
                                "\n Analizer danych ofiar Titanic'a (ADOT) \n\n Wyłączanie programu..."\
                                "\n------------------------------------------------------------------------------------------\n")
                            time.sleep(3)
                            break


                        else:
                            print("\n\n-------------------------------------------------------" \
                                    "\n Wystąpił błąd: Podano złą komendę. Spróbuj ponownie: "\
                                    "\n-------------------------------------------------------")


                elif komenda == "C":
                    break


                elif komenda == "W":
                    wyjscie = 1
                    print("\n------------------------------------------------------------------------------------------" \
                        "\n Analizer danych ofiar Titanic'a (ADOT) \n\n Wyłączanie programu..."\
                        "\n------------------------------------------------------------------------------------------\n")
                    time.sleep(3)
                    break


                else:
                    print("\n\n-------------------------------------------------------" \
                            "\n Wystąpił błąd: Podano złą komendę. Spróbuj ponownie: "\
                            "\n-------------------------------------------------------")
        
            elif menu == "W":
                wyjscie = 1
                print("\n------------------------------------------------------------------------------------------" \
                    "\n Analizer danych ofiar Titanic'a (ADOT) \n\n Wyłączanie programu..."\
                    "\n------------------------------------------------------------------------------------------\n")
                time.sleep(3)
                break


            else:
                print("\n\n------------------------------------------------------" \
                        "\n Wystąpił błąd: Podano złą komendę. Spróbuj ponownie: "\
                        "\n------------------------------------------------------")
                break


if __name__ == "__main__":
    main()

