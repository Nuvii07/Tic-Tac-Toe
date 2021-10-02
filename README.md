# Tic-Tac-Toe
Tic tac toe game vs AI

# Summary
 Przyjmujemy, że 'x' zawsze stawiamy pierwsze (użytkownik wykonuje pierwszy ruch).
 Każdy numer od 1 do 9 reprezentuje inną pozycję na planszy, zaczynając od górnego lewego rogu (1).
 Po wykonaniu ruchu przez użytkownika, następuje ruch komputera, który sam decyduje poprzez algorytm* gdzie postawić 'o'.
 Kod zawiera jedną główną pętle, która wywołuje inne funkcje.
 
#Algorytm dla AI. Krok po kroku.
1. Jeśli jest możliwy ruch wygrywający, to go wykonaj.
2. Jeśli gracz w następnej rundzie ma ruch wygrywający, to go zablokuj.
3. Wybierz pozycję jednego z rogów(losowo [1,3,7,9]).
4. Wybierz pozycję środkową.
5. Wybierz pozycję z krawędzi (losowo: [2,4,6,8])
6. Brak innego ruchu = Remis.

tutorial techwithtim.net
