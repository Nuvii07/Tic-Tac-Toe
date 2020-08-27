## Tic Tac Toe game in Python

#board = ["-", "-", "-",
#         "-", "-", "-",
#        "-", "-", "-"]
board = ['-' for x in range(10)]  # Plansza do gry

def insertLetter(letter, pos):  # Funkcja wstawia daną litere na danym miejscu
    board[pos] = letter

def spaceIsFree(pos):  # Funkcja informuje, czy dana pozycja jest wolna
    return board[pos] == '-'

def printBoard(board):  # Wyświetla tablice do gry w konsoli
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])


def isWinner(bo, le):  # Sprawdza każdą możliwą opcje wygranej
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():  # Funkcja wprowadzamy pozycje na planszy
    run = True
    while run:
        move = input('Wybierz pozycje dla \'x\' od (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:  # Sprawdza czy podaliśmy prawidlowa pozycje 1-9
                if spaceIsFree(move):  # Sprawdza czy ta pozycja jest wolna
                    run = False
                    insertLetter('x', move)
                else:
                    print('Ta pozycja jest juz zajeta!')
            else:
                print('Wybierz wlasciwa pozycje! Od 1 do 9')
        except:
            print('Wybierz pozycje!')


def compMove():  # Komputer wykonuje najlepszy ruch na podstawie algorytmu: (czyt. readme)
    possibleMoves = [x for x, letter in enumerate(board) if letter == '-' and x !=0]  # Tworzy liste możliwych ruchów
    move = 0

    #Sprawdza wygrywajacy ruch, lub go blokuje
    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    #Zajmuje pozycje na rogach
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    #Zajmuje środkową pozycje
    if 5 in possibleMoves:
        move = 5
        return move

    #Zajmuje pozostałe pozycje
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

#Funkcja losowo wybiera ruch z podanej listy
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):  # Zwraca True jesli tablica jest pelna lub False jesli nie jest
    if board.count(' ') > 1:
        return True
    else:
        return False

def main():
    print('Witaj w grze kółko i krzyzyk')
    printBoard(board)

    while not (isBoardFull(board)):     # Jeżeli tablica jest pełna to znaczy, że mamy remis
        if not(isWinner(board, 'o')):   # Sprawdza czy kolka wygraly
            playerMove()
            printBoard(board)
        else:
            print('Komputer wygral mecz!')
            break

        if not(isWinner(board, 'x')):   # Sprawdza czy krzyzyk wygral
            move = compMove()
            if move == 0:
                print('Remis!')
            else:
                insertLetter('o', move)
                print('Komputer wykonal ruch', move , ':')
                printBoard(board)
        else:
            print('Gracz X wygral mecz!')
            break

    if isBoardFull(board):
        print('Remis!')
        

main()