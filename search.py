from collections import deque

def breadth_first_search(initial_board, goal_board):

    from state import State
    initial_state = State(initial_board)

    fringe = deque([initial_state])
    visited = {initial_state.board}

    while fringe:
        current = fringe.popleft()

        if current.is_goal(goal_board):
            return current
        
        for child in current.get_successors():
            if child.board not in visited:
                visited.add(child.board)
                fringe.append(child)
    return None
