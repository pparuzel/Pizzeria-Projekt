# Strona internetowa pizzerii
[**Link do strony GitHub-Pages**](https://goo.gl/5HAqbw "Pizzeria")  
Autorzy: *Monika Wiech, Kamil Michno, Paweł Paruzel, Piotr Persona, Rafał Ziobro*

Spis Tresci
===========
* [Opis problemu](#opis-problemu)
* [Technologie](#technologie)
* [Instalacja](#Instalacja)
* [Rozwiązanie problemu](#rozwiązanie-problemu)
* [Narzędzia wykorzystane do realizacji interfejsu](#narzędzia-wykorzystane-do-realizacji-interfejsu)

## Opis problemu

W dzisiejszych czasach mimo łatwego dostępu do internetu klienci pizzerii nie zawsze mają możliwość złożenia zamówienia on-line oraz dokonaniu płatności przez internet. Czas składania zamówienia znacznie rośnie. Klient otrzymuje w informacji zwrotnej przewidywany czas dostawy kalkulowany przez człowieka, który może zostać błędnie oszacowany. Ponadto klient nie ma możliwości zaplanowania zamówienia na konkretną godzinę oraz monitorowania dostawy.
Wiele aplikacji umożliwiających złożenie zamówienia posiada nie sugestywny, nieczytelny interfejs o złym zagospodarowaniu przestrzeni.


## Technologie

* python: Flask, Flask_Admin, SQLAlchemy
* MySQL
* JavaScript
* HTML
* CSS

## Instalacja

Należy zainstalować interpreter języka **Python** w wersji **3.6** oraz system zarządzania bazą danych **MySQL**.

#### Mac OS X/Linux:

1. (opcjonalne) Pobranie narzędzia virtualenv: [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

2. Utworzenie wirtualnego środowiska Pythona:

        mkvirtualenv pizzera-projekt -p python3

 pizzeria-projekt to nazwa wirtualnego środowiska.

3. Następnie należy przejść do folderu Pizzeria-Projekt i wykonać komendy:

        workon pizzera-projekt

 Zmienia domyślne środowisko na wirtualne środowisko

        pip install -r requirements.txt

 Instaluje potrzebne moduły wymienione w pliku **requirements.txt.**

4. Następnie należy utworzyć bazę danych przy pomocy skryptu:

        create_database.sql

5. W pliku: Pizzeria-Projekt/python/flask/app.py należy wpisać:

        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://USERNAME:PASSWORD@localhost/Pizzeria?charset=utf8'

 W miejscu **USERNAME** - nazwę użytkownika w bazie danych

 W miejscu **PASSWORD** - hasło dostępu do bazy danych

 Domyślnie ustawiono username: **root** oraz hasło: **root**.

6. Znajdując się w katalogu Pizzeria-Projekt wykonać komendę uruchamiającą serwer na adresie ('localhost', port=5000):

        python server.py

7. Wpisać w przeglądarkę adres administratora zarządzania pizzerią:

        http://localhost:5000/admin

 Z tego panelu możliwe jest tworzenie rekordów w bazie danych oraz przeglądanie historii zamówień.

8. Panel klienta pizzerii dostępny jest pod adresem:

        http://localhost:5000/
