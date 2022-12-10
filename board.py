class Board(object):
    BUCKETS = 6

    def __init__(self, orig=None):

        if orig:
            self.board = [i for i in orig.board]
            self.numMoves = orig.numMoves
            return

        else:
            self.board = [4 for _ in range(self.BUCKETS * 2 + 2)]
            self.board[-1] = 0
            self.board[self.BUCKETS] = 0
            self.numMoves = 0
            return

    def makeMove(self, bucket):

        if bucket == self.BUCKETS or bucket > self.BUCKETS * 2 or bucket < 0:
            return -1

        if self.numMoves % 2 == 0 and bucket > self.BUCKETS or self.numMoves % 2 == 1 and bucket < self.BUCKETS:
            return -1

        stones = self.board[bucket]
        self.board[bucket] = 0

        if stones == 0:
            return -2

        offset = 0
        while (offset < stones):
            bucketIndex = (bucket + offset + 1) % (self.BUCKETS * 2 + 2)

            if ((bucket < self.BUCKETS and bucketIndex == self.BUCKETS * 2 + 1) or (
                    bucket > self.BUCKETS and bucketIndex == self.BUCKETS)):
                stones += 1

            else:
                self.board[bucketIndex] += 1
            offset += 1

        if self.board[bucketIndex] == 1 and bucketIndex != self.BUCKETS and bucketIndex != self.BUCKETS * 2 + 1:

            if bucket < self.BUCKETS and bucketIndex < self.BUCKETS:
                self.board[self.BUCKETS] += self.board[(2 * self.BUCKETS) - bucketIndex] + 1
                self.board[bucketIndex] = 0
                self.board[(2 * self.BUCKETS) - bucketIndex] = 0

            elif bucket > self.BUCKETS and bucketIndex > self.BUCKETS:
                self.board[self.BUCKETS] += self.board[(2 * self.BUCKETS) - bucketIndex] + 1
                self.board[bucketIndex] = 0
                self.board[(2 * self.BUCKETS) - bucketIndex] = 0

        self.numMoves += 1
        return bucket

    def children(self):

        children = []

        if self.numMoves % 2 == 0:
            moves = range(self.BUCKETS)
        else:
            moves = range(self.BUCKETS + 1, self.BUCKETS * 2 + 2)

        child = Board(orig=self)
        for move in moves:
            move = child.makeMove(move)

            if (move >= 0):
                children.append((move, child))
                child = Board(orig=self)

        return children

    def isOver(self):

        over = True

        for i in range(self.BUCKETS):
            if self.board[i] != 0:
                over = False
                break

        if not over:
            for i in range(self.BUCKETS + 1, self.BUCKETS * 2 + 1):
                if self.board[i] != 0:
                    return False

            return True
        else:
            return True

    def score(self):
        player1 = 0
        for i in range(self.BUCKETS + 1):
            player1 += self.board[i]

        player2 = 0
        for i in range(self.BUCKETS + 1, self.BUCKETS * 2 + 2):
            player1 += self.board[i]
            player2 += self.board[i]

        return player1 - player2

    def print(self):
        print("\t", end="")
        for bucketIndex in range(self.BUCKETS * 2, self.BUCKETS, -1):
            print(str(self.board[bucketIndex]) + "\t", end="")
        print()

        print(str(self.board[-1]) + "\t" * (self.BUCKETS + 1) + str(self.board[self.BUCKETS]))

        print(str(self.board[-1]) + "\t" * (self.BUCKETS + 1) + str(self.board[self.BUCKETS]))

        print("\t", end="")
        for bucketIndex in range(0, self.BUCKETS):
            print(str(self.board[bucketIndex]) + "\t", end="")
        print()
        print()