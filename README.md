Aplikacja wyświetla zaszyfrowaną wskazówkę, która może naprowadzić użytkownika na ukryty 5-cyfrowy PIN. Kod jest oparty na słowie „magic”, a każda litera występuje w nim wielokrotnie – liczba jej powtórzeń to jedna cyfra PIN-u. Jednak użytkownik nie otrzymuje tej instrukcji wprost – musi sam wydedukować mechanizm działania aplikacji na podstawie tekstu i nazwy.

Czyli to coś więcej niż tylko zabawa z Tkinterem. To:
logiczna łamigłówka,

gra w dedukcję,

test kreatywności,

zadanie inżynierii wstecznej.

Możliwości rozwoju (opcjonalnie, jeśli chcesz iść dalej):
Zamiana kodu na hash PIN-u:

Użytkownik musi zgadnąć, a Ty sprawdzasz np. hashlib.sha256(pin.encode()).hexdigest().

Dodanie systemu punktów / czasu – np. ile prób zajęło odgadnięcie.

Tryb tekstowy (CLI) – dla nauki obsługi inputu i warunków.

Zamiana liter kodu (magic) na inny zestaw – np. losowy alfabet, emoji, albo system heksadecymalny.

Wersja CTF (dla innych):

Wersja .exe bez magic.py.

Zadanie: Odzyskaj PIN z samego code.
