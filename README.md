# Strona internetowa pizzerii
[**Link do strony GitHub-Pages**](https://goo.gl/vmsAvZ "Pizzeria")  
Autorzy: *Monika Wiech, Kamil Michno, Paweł Paruzel, Piotr Persona, Rafał Ziobro*
  
Spis Tresci
===========
* [Opis problemu](#opis-problemu)
* [Wymagania](#wymagania)
* [Zagrożenia](#zagrożenia)
* [Docelowy użytkownik](#docelowy-użytkownik)
* [Rozwiązanie problemu](#rozwiązanie-problemu)
* [Narzędzia wykorzystane do realizacji interfejsu](#narzędzia-wykorzystane-do-realizacji-interfejsu)
  
## Opis problemu

W dzisiejszych czasach mimo łatwego dostępu do internetu klienci pizzerii nie zawsze mają możliwość złożenia zamówienia on-line oraz dokonaniu płatności przez internet. Czas składania zamówienia znacznie rośnie. Klient otrzymuje w informacji zwrotnej przewidywany czas dostawy kalkulowany przez człowieka, który może zostać błędnie oszacowany. Ponadto klient nie ma możliwości zaplanowania zamówienia na konkretną godzinę oraz monitorowania dostawy. 
Wiele aplikacji umożliwiających złożenie zamówienia posiada nie sugestywny, nieczytelny interfejs o złym zagospodarowaniu przestrzeni. 

## Wymagania

* Możliwość złożenia zamówienia przez internet
* Możliwość płatności online(karta)
* Możliwość utworzenia konta użytkownika
* Możliwość zalogowania do systemu
* Przechowywanie  danych użytkownika
* Przechowywanie danych odnośnie zamówień użytkownika
* Możliwość modyfikacji danych personalnych użytkownika
* Możliwość wybrania pizzy
* Możliwość wybrania dodatków
* Możliwość wybrania sosów i napojów
* Możliwość sprawdzenia na jakim etapie jest dostawa pizzy
* Możliwość płatności przy odbiorze

## Zagrożenia

* Wprowadzenie niepoprawnej ilości danych (rejestracja)
* Wprowadzenie niepoprawnych danych (rejestracja)
* Wprowadzenie adresu poza obszarem usługi
* Próba zalogowania się na niezarejestrowany adres
* Wprowadzenie nieprawidłowego hasła
* Wprowadzenie niepoprawnych danych podczas składania zamówienia (nr karty etc.)
* Nie wybranie produktu
* Brak informacji o zamówieniu pomimo zapłacenia
* Błąd podczas płatności
* Brak środków na koncie
* Chęć zamówienia niedostępnego produktu
* Zbyt długi czas dostawy

## Docelowy użytkownik

Przewidywanym użytkownikiem interfejsu jest osoba powyżej trzynastego roku życia. Wykształcenie oraz doświadczenie z aplikacją tego samego typu jest nie wymagane. Użytkownik musi obsługiwać podstawowe kontrolery zewnętrzne komputera: klawiaturę, mysz, ekran oraz potrafi obsługiwać przeglądarkę internetową. Przewidywanym środowiskiem użytkownika jest komputer z dostępem do internetu. Ponadto osoba korzystająca z interfejsu musi umieć czytać oraz pisać w języku polskim.  
Role w systemie: 
* Gość
* Użytkownik
* Pracownik pizzerii

## Rozwiązanie problemu

Aplikacja będzie oferować czytelny, przejrzysty oraz przyjemny dla użytkownika interfejs realizowany częściowo w stylu manipulacyjnym. Zostanie położony nacisk na prostotę w odbiorze oraz użytkowaniu interfejsu. Użytkownik będzie miał możliwość złożenia zamówienia przez internet, z wyborem sposobu płatności: on-line lub przy odbiorze.  
Interfejs oferuje powiadomienie użytkownika o statusie zamówienia oraz możliwość monitorowania zamówienia.  

## Narzędzia wykorzystane do realizacji interfejsu

Graficzny interfejs użytkownika zostanie zrealizowany za pomocą przeglądarki internetowej oraz języków służących do tworzenia i stylizowania strony internetowej: **HTML**, **CSS**.  
Symulacja serwera, odpowiedzialna za obsługę zapytań użytkowników oraz odpowiedzi zostanie zrealizowana za pomocą języka **Python 3**.  
Dane przechowywane w aplikacji będą obsługiwane przez bazę danych **MySQL**.  
