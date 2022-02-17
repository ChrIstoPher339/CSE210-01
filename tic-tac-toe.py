

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
    spot = 'X'
    while spot == 'X' or spot == 'O' or spot not in places:
        spot = input(f"{turn}'s where would you like to go? (ex. a1)\n")
        if spot == 'X' or spot == 'O' or spot not in places:
            print("I'm sorry that is not an acceptable answer. Please try again.")
    index = places.index(spot)
    places[index] = turn + " "

def check_win(places, xo, xo2):
    xo = xo + ' '
    xo2 = xo2 + ' '
    if places[0] == xo and places[1] == xo and places[2] == xo:
        return xo
    elif places[0] == xo2 and places[1] == xo2 and places[2] == xo2:
        return xo2
    elif places[3] == xo and places[4] == xo and places[5] == xo:
        return xo
    elif places[3] == xo2 and places[4] == xo2 and places[5] == xo2:
        return xo2
    elif places[6] == xo and places[7] == xo and places[8] == xo:
        return xo
    elif places[6] == xo2 and places[7] == xo2 and places[8] == xo2:
        return xo2
    elif places[0] == xo and places[4] == xo and places[8] == xo:
        return xo
    elif places[0] == xo2 and places[4] == xo2 and places[8] == xo2:
        return xo2
    elif places[2] == xo and places[4] == xo and places[6] == xo:
        return xo
    elif places[2] == xo2 and places[4] == xo2 and places[6] == xo2:
        return xo2
    elif places[0] == xo and places[3] == xo and places[6] == xo:
        return xo
    elif places[0] == xo2 and places[3] == xo2 and places[6] == xo2:
        return xo2
    elif places[1] == xo and places[4] == xo and places[7] == xo:
        return xo
    elif places[1] == xo2 and places[4] == xo2 and places[7] == xo2:
        return xo2
    elif places[2] == xo and places[5] == xo and places[8] == xo:
        return xo
    elif places[2] == xo2 and places[5] == xo2 and places[8] == xo2:
        return xo2
    else:
        return False

def cats_game(places):
    for i in places:
        if i != 'X ' and i != 'O ':
            return False
    return True

def main():
    win = False
    places = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    xo = first_player()
    print()
    xo2 = second_player(xo)
    turn = xo2
    while win == False:
        if turn == xo2:
            turn = xo
        else:
            turn = xo2
        display_game(places)
        placement(places, turn)
        print()

        win = check_win(places, xo, xo2)

        if cats_game(places) == True:
            display_game(places)
            print("It looks like it's a cat's game.")
            win = True
        elif win != False:
            display_game(places)
            congrats = list(win)[0]
            print(f"Congratulations, {congrats}'s is the winner!")
        
main()