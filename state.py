class State:
    def __init__(self, board, parent=None, move="Initial"):
        self.board = board
        self.parent = parent
        self.move = move
    
    def find_blank(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0: # Represent the empty space
                    return r, c
    
    def is_goal(self, goal_board):
        return self.board == goal_board
    
    def get_successors(self):
        successors = []
        r, c = self.find_blank()

        # Directions: Row change, Column change, Move name
        directions = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]


        for dr, dc, move_name in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                # Create a new board by wapping the blank with the tile
                new_board = [list(row) for row in self.board] # Deep copy of the board
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]

                # convert back to tuple of tuples for hashing
                tuple_board = tuple(tuple(row) for row in new_board)
                successors.append(State(tuple_board, parent=self, move=move_name))
        return successors
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __hash__(self):
        return hash(self.board)
