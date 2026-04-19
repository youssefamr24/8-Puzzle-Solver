from search import breadth_first_search

def print_board(board):
    for row in board:
        # 0 is displayed as an empty space to match the lab diagram
        print(f"| {' '.join(str(x) if x != 0 else ' ' for x in row)} |")
    print("-" * 13)

if __name__ == "__main__":

    initial = (('b', 'd', 'c'), 
               ('a',  0,  'e'), 
               ('g', 'h', 'f'))
               
    goal = (('a', 'b', 'c'), 
            ('d', 'e', 'f'), 
            ('g', 'h',  0))

    print("Solving Lab 6 8-Puzzle using BFS...")
    solution = breadth_first_search(initial, goal)

    if solution:
        path = []
        curr = solution
        while curr:
            path.append(curr)
            curr = curr.parent
        
        for i, step in enumerate(reversed(path)):
            print(f"Step {i}: Move {step.move}")
            print_board(step.board)
    else:
        print("No solution found. Check if the initial state is solvable.")