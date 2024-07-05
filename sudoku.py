class NQueensCSP:
    def __init__(self, size):
        self.size = 6
        self.variables = list(range(size))  # Variables representing the columns
        self.domains = self.initialize_domains()  # Domains representing possible values for each variable

    def initialize_domains(self):
        return [list(self.variables) for _ in range(self.size)]

    def solve_csp(self):
        return self.backtrack({}, 0)

    def backtrack(self, assignment, row):
        if row == self.size:
            # All queens are placed successfully
            return [list(assignment.values())]

        solutions = []

        for col in self.domains[row]:
            if self.is_safe(assignment, row, col):
                assignment[row] = col  # Assign the queen to the variable

                # Recursively try to place queens in the next rows
                next_row_solutions = self.backtrack(assignment.copy(), row + 1)
                solutions.extend(next_row_solutions)
                del assignment[row]  # Backtrack

        return solutions

    def is_safe(self, assignment, row, col):
        for prev_row, prev_col in assignment.items():
            # Check if the queen can be placed in the current position
            if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                return False

        return True

    def print_board(self, solution):
        for row in range(self.size):
            print(" ---" * self.size)
            for col in range(self.size):
                p = "Q" if solution and solution[row] == col else " "
                print(f"| {p} ", end="")
            print("|")
        print(" ---" * self.size)


def main():
    print(".: N-Queens Problem (CSP) :.")
    size = int(input("Please enter the size of the board: "))
    
    # Validate input
    if size <= 0:
        print("Please enter a positive integer for the size of the board.")
        return
    
    n_queens_csp = NQueensCSP(size)

    csp_solutions = n_queens_csp.solve_csp()

    print("CSP Solutions:")
    for i, solution in enumerate(csp_solutions):
        print(f"CSP Solution {i + 1}:")
        n_queens_csp.print_board(solution)

    print(f"Total CSP solutions: {len(csp_solutions)}")


if __name__ == "__main__":
    main()
