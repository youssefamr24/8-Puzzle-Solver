import tkinter as tk
from tkinter import messagebox
import time
from search import breadth_first_search

class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FCAI-CU: 8-Puzzle Solver")
        
        # Initial and Goal states 
        self.initial_board = (('b', 'd', 'c'), ('a', 0, 'e'), ('g', 'h', 'f'))
        self.goal_board = (('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 0))
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.setup_ui()

    def setup_ui(self):
        # Create a container for the grid
        grid_frame = tk.Frame(self.root, bg="black", bd=2)
        grid_frame.pack(pady=20, padx=20)

        for r in range(3):
            for c in range(3):
                btn = tk.Label(grid_frame, text="", width=6, height=3, 
                               font=('Helvetica', 24, 'bold'), relief="raised")
                btn.grid(row=r, column=c, padx=2, pady=2)
                self.buttons[r][c] = btn
        
        # Control Button
        self.solve_btn = tk.Button(self.root, text="Start BFS Animation", 
                                   command=self.run_solve, font=('Arial', 12))
        self.solve_btn.pack(pady=10)
        
        self.update_grid(self.initial_board)

    def update_grid(self, board):
        """Maps the logic board to the UI labels."""
        for r in range(3):
            for c in range(3):
                val = board[r][c]
                if val == 0:
                    self.buttons[r][c].config(text="", bg="#ecf0f1") # Blank color
                else:
                    self.buttons[r][c].config(text=str(val).upper(), bg="#3498db", fg="white")
        self.root.update()

    def run_solve(self):
        self.solve_btn.config(state="disabled")
        
        # 1. Call your existing BFS Logic
        solution_node = breadth_first_search(self.initial_board, self.goal_board)
        
        if not solution_node:
            messagebox.showerror("Error", "No solution found!")
            self.solve_btn.config(state="normal")
            return

        # 2. Reconstruct path
        path = []
        curr = solution_node
        while curr:
            path.append(curr)
            curr = curr.parent
        path.reverse()

        # 3. Animate the path
        for i, step in enumerate(path):
            self.update_grid(step.board)
            # Short delay to see the "slide"
            time.sleep(0.6) 
            
        messagebox.showinfo("Success", f"Goal reached in {len(path)-1} moves!")
        self.solve_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()