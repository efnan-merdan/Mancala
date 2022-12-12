from board import Board
import time
from player import Player

def simulateLocalGame(startBoard, p1, p2):

    board = startBoard
    isPlayer1 = True
    start_time = time.time()

    while not board.isOver():

        if isPlayer1:
            move = p1.findMove(board)
        else:
            move = p2.findMove(board)

        board.makeMove(move)
        print("----------- Move Number " + str(board.numMoves) + " -------------\n")
        board.print()

        isPlayer1 = not isPlayer1

    print("Final Score")

    print(board.score())

    print("\nTook %s Seconds" % (time.time() - start_time))

if __name__ == "__main__":

    p1 = Player(8, True)
    p2 = Player(8, False)
    board = Board()

    simulateLocalGame(board, p1, p2)

