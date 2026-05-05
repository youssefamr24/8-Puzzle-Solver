class State:
    def __init__(self, board,goal_board, parent=None, move="Initial", depth=0):
        self.board = board
        self.goal_board = goal_board
        self.parent = parent
        self.move = move
        self.depth = depth
        # Recalculate heuristics for the new state
        self.h1 = self.calculate_h1()
        self.h2 = self.calculate_h2()

    # H1: Number of misplaced tiles
    def calculate_h1(self):
        """Task 1: Count misplaced tiles (excluding blank)."""
        count = 0
        for r in range(3):
            for c in range(3):
                val = self.board[r][c]
                if val != 0 and val != self.goal_board[r][c]:
                    count += 1 
        return count
    

    # H2: Manhattan distance
    def calculate_h2(self):
        """Task 2: Manhattan Distance."""
        total_dist = 0
        # Map goal positions for fast lookup
        goal_pos = {}

        for r in range(3):
            for c in range(3):
                goal_pos[self.goal_board[r][c]] = (r, c)
        
        for r in range(3):
            for c in range(3):
                val = self.board[r][c]
                if val != 0: # Skip blank
                    gr, gc = goal_pos[val]
                    total_dist += abs(r - gr) + abs(c - gc)
        return total_dist


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
                successors.append(State(
                    board=tuple_board, 
                    goal_board=self.goal_board, # Added this argument
                    parent=self, 
                    move=move_name, 
                    depth=self.depth + 1
                ))
        return successors
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __hash__(self):
        return hash(self.board)
    
    def __lt__(self, other):
        # Needed for the Priority Queue to handle ties
        return False