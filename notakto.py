from random import choice
board = {"A": [[0, 1, 2], [3, 4, 5], [6, 7, 8]], "B": [[0, 1, 2], [3, 4, 5], [6, 7, 8]], "C": [[0, 1, 2], [3, 4, 5], [6, 7, 8]]}
boardCopy = {"A": [[0, 1, 2], [3, 4, 5], [6, 7, 8]], "B": [[0, 1, 2], [3, 4, 5], [6, 7, 8]], "C": [[0, 1, 2], [3, 4, 5], [6, 7, 8]]}
rows = {"0": 0, "1": 0, "2": 0, "3": 1, "4": 1, "5": 1, "6": 2, "7": 2, "8": 2}
cols = {"0": 0, "1": 1, "2": 2, "3": 0, "4": 1, "5": 2, "6": 0, "7": 1, "8": 2}
numbers = [str(num) for num in range(0, 9)]
center = ["A4", "B4", "C4"]
mirror = {"0": "8", "1": "7", "2": "6", "3": "5", "4": "lmao", "5": "3", "6": "2", "7": "1", "8": "0"}


def print_board():
    for key in board:
        if key != list(board)[-1]:
            print(f"{key:<7}", end="")
        else:
            print(key, end="")
    print()
    for i in range(3):
        for key in board:
            print(*board[key][i], end="")
            if key != list(board)[-1]:
                print("  ", end="")
        print()


def check_condition():
    for b in board:
        diagonal1, diagonal2 = [], []
        d1, d2 = 0, 2
        for row in board[b]:
            if row.count("X") == 3:
                board.pop(b)
                if len(board) == 0:
                    return True
                else:
                    return 0
            for i in range(3):
                column = [row[i] for row in board[b]]
                if column.count("X") == 3:
                    board.pop(b)
                    if len(board) == 0:
                        return True
                    else:
                        return 0
            diagonal1.append(row[d1])
            diagonal2.append(row[d2])
            d1 += 1
            d2 -= 1
        if diagonal1.count("X") == 3 or diagonal2.count("X") == 3:
            board.pop(b)
            if len(board) == 0:
                return True
            else:
                return 0


def scan():
    complete = []
    for b in board:
        diagonal1, diagonal2 = [], []
        d1, d2 = 0, 2
        for row in board[b]:
            if row.count("X") == 2:
                for col in row:
                    if col != "X":
                        complete.append(b + str(col))
            for i in range(3):
                column = [row[i] for row in board[b]]
                if column.count("X") == 2:
                    for r in column:
                        if r != "X":
                            complete.append(b + str(r))
            diagonal1.append(row[d1])
            diagonal2.append(row[d2])
            d1 += 1
            d2 -= 1
        if diagonal1.count("X") == 2:
            for d in diagonal1:
                if d != "X":
                    complete.append(b + str(d))
        if diagonal2.count("X") == 2:
            for d in diagonal2:
                if d != "X":
                    complete.append(b + str(d))
    if len(complete) != 0:
        return complete


def knight(player2):
    if player2[1] == "0":
        if board[player2[0]][1][2] != "X" and (player2[0] + str(board[player2[0]][1][2])) not in scan():
            p1 = player2[0] + "5"
        else:
            p1 = player2[0] + "7"
    elif player2[1] == "1":
        if board[player2[0]][2][0] != "X" and (player2[0] + str(board[player2[0]][2][0])) not in scan():
            p1 = player2[0] + "6"
        else:
            p1 = player2[0] + "8"
    elif player2[1] == "2":
        if board[player2[0]][1][0] != "X" and (player2[0] + str(board[player2[0]][1][0])) not in scan():
            p1 = player2[0] + "3"
        else:
            p1 = player2[0] + "7"
    elif player2[1] == "3":
        if board[player2[0]][0][2] != "X" and (player2[0] + str(board[player2[0]][0][2])) not in scan():
            p1 = player2[0] + "2"
        else:
            p1 = player2[0] + "8"
    elif player2[1] == "5":
        if board[player2[0]][0][0] != "X" and (player2[0] + str(board[player2[0]][0][0])) not in scan():
            p1 = player2[0] + "0"
        else:
            p1 = player2[0] + "6"
    elif player2[1] == "6":
        if board[player2[0]][0][1] != "X" and (player2[0] + str(board[player2[0]][0][1])) not in scan():
            p1 = player2[0] + "1"
        else:
            p1 = player2[0] + "5"
    elif player2[1] == "7":
        if board[player2[0]][0][0] != "X" and (player2[0] + str(board[player2[0]][0][0])) not in scan():
            p1 = player2[0] + "0"
        else:
            p1 = player2[0] + "2"
    elif player2[1] == "8":
        if board[player2[0]][0][1] != "X" and (player2[0] + str(board[player2[0]][0][1])) not in scan():
            p1 = player2[0] + "1"
        else:
            p1 = player2[0] + "3"
    return p1


def is_trap():
    for b in board:
        totalX = []
        for r in board[b]:
            for c in r:
                if c == "X":
                    totalX.append(c)
        if (((board[b][0][0] == "X" and board[b][1][2] == "X" and board[b][2][1] == "X") or
                (board[b][0][2] == "X" and board[b][1][0] == "X" and board[b][2][1] == "X") or
                (board[b][2][2] == "X" and board[b][1][0] == "X" and board[b][0][1] == "X") or
                (board[b][2][0] == "X" and board[b][1][2] == "X" and board[b][0][1] == "X")) and
                (len(totalX) == 3)):
            return True


def two_X_trap(player2):
    if ((board[player2[0]][0][0] == "X" and board[player2[0]][1][2] == "X") or
            (board[player2[0]][0][2] == "X" and board[player2[0]][1][0] == "X")):
        n = "7"
    elif ((board[player2[0]][1][0] == "X" and board[player2[0]][2][2] == "X") or
            (board[player2[0]][1][2] == "X" and board[player2[0]][2][0] == "X")):
        n = "1"
    elif board[player2[0]][0][1] == "X" and board[player2[0]][1][0] == "X":
        n = "8"
    elif board[player2[0]][0][1] == "X" and board[player2[0]][1][2] == "X":
        n = "6"
    elif board[player2[0]][1][0] == "X" and board[player2[0]][2][1] == "X":
        n = "2"
    elif board[player2[0]][1][2] == "X" and board[player2[0]][2][1] == "X":
        n = "0"
    elif ((board[player2[0]][0][2] == "X" and board[player2[0]][2][1] == "X") or
            (board[player2[0]][0][1] == "X" and board[player2[0]][2][2] == "X")):
        n = "3"
    elif ((board[player2[0]][0][1] == "X" and board[player2[0]][2][0] == "X") or
            (board[player2[0]][0][0] == "X" and board[player2[0]][2][1] == "X")):
        n = "5"
    return player2[0] + n


def mirror_move(player2):
    for b in board:
        totalX = []
        for r in board[b]:
            for c in r:
                if c == "X":
                    totalX.append(c)
    if len(totalX) == 1:
        for b in board:
            for r in range(3):
                for c in range(3):
                    if board[b][r][c] == "X":
                        return mirror[str(boardCopy[b][r][c])]
    else:
        return mirror[player2[1]]


def get_board_center():
    for b in board:
        if board[b][1][1] == "X":
            return b


def get_other_board():
    for b in board:
        if board[b][1][1] != "X":
            return b


def five():
    for b in board:
        totalX = []
        for r in board[b]:
            for c in r:
                if c == "X":
                    totalX.append(c)
        if len(totalX) == 5:
            return b


def big_brain_ai(player2):
    no_center = True
    for b in board:
        if board[b][1][1] == "X":
            no_center = False
    if len(board) == 3:
        if scan() is not None:
            p1 = choice(scan())
        elif scan() is None:
            if len(center) != 0:
                for c in center:
                    if c[0] == player2[0]:
                        center.remove(c)
                        p1 = center.pop(0)
            else:  # fix this shit
                p1 = two_X_trap(player2)

    if len(board) == 2:
        in_s = False
        if scan() is not None and len(center) == 0:
            if not is_trap() and player2[0] == get_other_board():
                for s in scan():
                    if player2[0] in s:
                        p1 = s
                        in_s = True
                        break
                if not in_s:
                    p1 = two_X_trap(player2)
            elif get_board_center() == player2[0] and get_board_center() == choice(scan())[0]:
                if not no_center and not is_trap() and board[list(board)[0]][1][1] == "X" and board[list(board)[1]][1][1] == "X":
                    if five() is not None:
                        for s in scan():
                            if five() not in s:
                                p1 = s
                                in_s = True
                                break
                        if not in_s:
                            p1 = choice(scan())
                    else:
                        p1 = choice(scan())
                elif not no_center and not is_trap():
                    p1 = knight(player2)
                elif not no_center and is_trap():
                    p1 = knight(player2)
                else:
                    p1 = knight(player2)
            else:
                if five() is not None:
                    for s in scan():
                        if five() not in s:
                            p1 = s
                            in_s = True
                            break
                    if not in_s:
                        p1 = choice(scan())
                else:
                    p1 = choice(scan())

        elif scan() is None:
            if len(center) != 0:
                for c in center:
                    if c[0] == player2[0]:
                        center.remove(c)
                        p1 = center.pop(0)
            else:  # setting up 2x trap
                p1 = two_X_trap(p2)

    if len(board) == 1:
        edges = [board[list(board)[0]][0][1], board[list(board)[0]][1][0], board[list(board)[0]][1][2], board[list(board)[0]][2][1]]
        if not is_trap() and no_center and edges.count("X") != 3:
            p1 = list(board)[0] + mirror_move(p2)
        elif is_trap():
            if board[list(board)[0]][0][1] == "X":
                if board[list(board)[0]][1][0] == "X":
                    p1 = list(board)[0] + "0"
                elif board[list(board)[0]][1][2] == "X":
                    p1 = list(board)[0] + "2"
            elif board[list(board)[0]][2][1] == "X":
                if board[list(board)[0]][1][0] == "X":
                    p1 = list(board)[0] + "6"
                elif board[list(board)[0]][1][2] == "X":
                    p1 = list(board)[0] + "8"
        elif edges.count("X") == 3:
            for e in edges:
                if str(e) != "X":
                    p1 = list(board)[0] + str(e)
        else:
            p1 = knight(p2)

    print(f"Player 1: {p1}")
    if len(p1) == 2 and p1[0] in board and p1[1] in numbers and board[p1[0]][rows[p1[1]]][cols[p1[1]]] != "X":
        board[p1[0]][rows[p1[1]]][cols[p1[1]]] = "X"
    else:
        print("Whoops something went wrong (invalid move)")


p1 = choice(center)
print(f"Player 1: {p1}")
if len(p1) == 2 and p1[0] in board and p1[1] in numbers and board[p1[0]][rows[p1[1]]][cols[p1[1]]] != "X":
    board[p1[0]][rows[p1[1]]][cols[p1[1]]] = "X"
center.remove(p1)

while True:
    print_board()
    while True:
        p2 = input("Player 2: ")
        if len(p2) == 2 and p2[0] in board and p2[1] in numbers and board[p2[0]][rows[p2[1]]][cols[p2[1]]] != "X":
            board[p2[0]][rows[p2[1]]][cols[p2[1]]] = "X"
            break
        else:
            print("Invalid move, please input again")
            continue
    if check_condition():
        print("Player 1 wins game")
        break
    print_board()

    big_brain_ai(p2)
    if check_condition():
        print("Lost... lmao..")
        break
