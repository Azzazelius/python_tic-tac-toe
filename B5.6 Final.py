# Шаблон игрового поля
board = [[" ","1","2","3"],
        ["1","-","-","-"],
        ["2","-","-","-"],
        ["3","-","-","-"]]

# Задаём глобальные константы
currentMarker = "X"
nextMarker = "0"
turnsLeft = 9
gameOver = False

# Первый вывод поля
print("-------------FIGHT--------------")
for i in board:
    print(i[:])

# ======================= функция хода игрока и обновления поля
def drawGrid(incomming):
    updatedBoard = incomming.copy()
    turnComplete = False
    while turnComplete == False:
        print("--------------------------------")
        print(f"Ход игрока '{currentMarker}'!")
        row =  int(input("Укажите строку: ")) # тут надо бы сделать проверку, что игрок вводит цифры. Сейчас вылетает ошибка, как сделать чтобы игра не останавливалась я не придумал.
        column = int(input("Укажите столбец: "))
        if any([row not in range(1,len(incomming)+1), column not in range(1,len(incomming)+1)]): # Проверка, что указанны корректные координаты
            print("Вы вышли за пределы дозволенного!")
        elif incomming[row][column] != "-": # проверка, что слот свободен
            print("Там уже что-то нарисовано, попробуйте указать свободную ячейку.")
        else:
            incomming[row][column] = currentMarker
            turnComplete = True
    print("--------------------------------")
    for i in incomming:
            print(i[:])
    print("--------------------------------")
    return

# ======================= функция проверка завершения игры если в этом ходу игрок победил
def endCheck():
    lineIsX, lineIs0 = ["X", "X", "X"], ["0", "0", "0"] # последовательность при которой игра завершается.

    # ------------------------- проверка рядов ----------------------------------------
    for i in board[1:4]:
        if i[1:] == lineIsX or i[1:] == lineIs0:
            return playerWin()

    # ------------------------ проверка столбцов----------------------------------------
    column1, column2, column3 = [], [], []
    for i in board[1:]:
        column1.append(i[1])  # сгенерировать список из указанного столбца
    for i in board[1:]:
        column2.append(i[2])  # сгенерировать список из указанного столбца
    for i in board[1:]:
        column3.append(i[3])  # сгенерировать список из указанного столбца

    if any([column1 == lineIsX, column2 == lineIsX, column3 == lineIsX]):
        return playerWin()
    elif any([column1 == lineIs0, column2 == lineIs0, column3 == lineIs0]):
        return playerWin()

    # ---------------------- проверка диагоналей ----------------------------------------
    cross1, cross2 = [], []

    cross1.append(board[1][1]), cross1.append(board[2][2]), cross1.append(board[3][3])
    cross2.append(board[1][3]), cross2.append(board[2][2]), cross2.append(board[3][1])

    if any([cross1 == lineIsX, cross2 == lineIsX]):
        return playerWin()
    if any([cross1 == lineIs0, cross2 == lineIs0]):
        return playerWin()

# ================================== функция если закончились ходы
def noMoreMoves():
    global gameOver
    print("Ходы закончились! Вы оба проиграли!")
    gameOver = True
    return

# ================================= функция если игрок победил
def playerWin():
    global turnsLeft
    global gameOver
    print(f"Победил игрок '{currentMarker}'!")
    turnsLeft = 0
    gameOver = True
    return

# ======================= Цикл проверяющий не закончились ли ходы. Если остались, меняет маркер игрока и запускает новую генерацию.
while turnsLeft != 0:
    turnsLeft -=1
    drawGrid(board)
    endCheck()
    currentMarker, nextMarker = nextMarker, currentMarker # смена активного символа
if gameOver == False:
    noMoreMoves()




