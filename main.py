from search import a_star_search

def print_board(board):
    """Helper to print the 3x3 grid nicely."""
    for row in board:
        # Display 0 as a blank space for better UX
        print(f"| {' '.join(str(x) if x != 0 else ' ' for x in row)} |")
    print("-" * 13)

def run_task(task_num, initial, goal, h_type):
    print(f"\n{'='*10} Running Task {task_num} (Using {h_type}) {'='*10}")
    result = a_star_search(initial, goal, h_type)
    
    if result:
        # Backtrack using the 'parent' pointer to get the path
        path = []
        curr = result
        while curr:
            path.append(curr)
            curr = curr.parent
        path.reverse() # Start from the initial state

        # Print each step
        for i, step in enumerate(path):
            print(f"Step {i}: Move {step.move}")
            print_board(step.board)
        
        print(f" Goal reached in {result.depth} moves!")
    else:
        print(" No solution found.")

if __name__ == "__main__":
    # TASK 1: Misplaced Tiles (h1)
    t1_initial = ((2, 8, 3), (1, 6, 4), (7, 0, 5))
    t1_goal = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
    run_task(1, t1_initial, t1_goal, 'h1')

    # TASK 2: Manhattan Distance (h2)
    t2_initial = ((0, 1, 3), (4, 2, 5), (7, 8, 6))
    t2_goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    run_task(2, t2_initial, t2_goal, 'h2')