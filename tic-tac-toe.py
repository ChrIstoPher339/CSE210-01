

def display_game(places):
    print(f'{places[0]}|{places[1]}|{places[2]}')
    print('--+--+--')
    print(f'{places[3]}|{places[4]}|{places[5]}')
    print('--+--+--')
    print(f'{places[6]}|{places[7]}|{places[8]}')
    print()

def first_player():
    xo = None
    while xo != 'X' and xo != 'O':
        xo = input("X's or O's? ")
        if type(xo) == str:
            xo = xo.capitalize()
        if xo != 'X' and xo != 'O':
            print("I'm sorry that isn't a valid answer. Please try again.")
    return xo

def second_player(xo):
    if xo == 'O':
        return 'X'
    else:
        return 'O'

def placement(places, turn):
    
    spot = input('Where would you like to go? (ex. a1)\n')
    index = places.index(spot)
    places[index] = turn + " "

def check_win(places, xo, x02):
    if places[0] == xo and places[1] == xo and places[2] == xo:
        return True
    elif 
        



def main():
    win = False
    places = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    xo = first_player()
    xo2 = second_player(xo)
    turn = xo2
    while win == False:
        if turn == xo2:
            turn == xo
        else:
            turn = xo2
        display_game(places)
        turn = xo
        placement(places, turn)
        win = check_win()
main()