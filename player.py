import math


class Player:

    def __init__(self, depthLimit, isPlayer1):
        self.depthLimit = depthLimit
        self.isPlayer1 = isPlayer1

    def findMove(self, board):

        def findMoveHelper(currentBoard, depth, alpha, beta, isMax):

            if currentBoard.isOver():
                return (board.score(), -1)

            elif depth == 0:
                return (self.heuristic(board), -1)

            children = currentBoard.children()

            if isMax:
                bestScore = -math.inf
                shouldReplace = lambda x: x > bestScore

            else:
                bestScore = math.inf
                shouldReplace = lambda x: x < bestScore



            moveForBestScore = -1

            for child in children:
                childMove, childBoard = child

                tempVal = findMoveHelper(childBoard, depth - 1, alpha, beta, not isMax)[0]

                if shouldReplace(tempVal):
                    bestScore = tempVal
                    moveForBestScore = childMove

                if isMax:
                    alpha = max(alpha, tempVal)
                else:
                    beta = min(beta, tempVal)

                if alpha > beta:
                    break

            return (bestScore, moveForBestScore)

        score, move = findMoveHelper(board, self.depthLimit, -math.inf, math.inf, self.isPlayer1)
        return move

    def heuristic(self, board):

        player1Stones = 0
        for i in range(board.BUCKETS):
            player1Stones += board.board[i]
        player1Stones += board.board[board.BUCKETS] * 1.5

        player2Stones = 0
        for i in range(board.BUCKETS + 1, board.BUCKETS * 2 + 1):
            player2Stones += board.board[i]
        player2Stones += board.board[board.BUCKETS * 2 + 1] * 1.5

        return player1Stones - player2Stones
