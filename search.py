from collections import deque
import heapq


def a_star_search(initial_board, goal_board, heuristic='h2'):
    from state import State
    start_node = State(initial_board, goal_board)

    # f(n) = g(n) + h(n)
    h_val = start_node.h1 if heuristic == 'h1' else start_node.h2
    fringe = [(h_val, start_node)]
    visited = {start_node.board: 0}  # Board state to g(n) cost

    while fringe:
        f_score, current = heapq.heappop(fringe)

        if current.is_goal(goal_board):
            return current
        
        for child in current.get_successors():
            h_val = child.h1 if heuristic == 'h1' else child.h2
            child_f = child.depth + h_val  # g(n) is depth

            if child.board not in visited or child.depth < visited[child.board]:
                visited[child.board] = child.depth
                heapq.heappush(fringe, (child_f, child))
    return None



# BFS is from the last task, so Ignore it
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
