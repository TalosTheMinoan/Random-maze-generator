import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set the dimensions of the maze
width, height = 400, 400

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-width // 2, height // 2)
t.pendown()
t.hideturtle()

# Set the size of maze cells
cell_size = 20

# Calculate the number of cells in each direction
num_cells_x = width // cell_size
num_cells_y = height // cell_size

# Create a grid to represent the maze
grid = [[0 for _ in range(num_cells_x)] for _ in range(num_cells_y)]

# Define directions (up, down, left, right)
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Function to check if a cell is in bounds
def is_in_bounds(x, y):
    return 0 <= x < num_cells_x and 0 <= y < num_cells_y

# Function to perform DFS maze generation
def generate_maze(x, y):
    grid[y][x] = 1  # Mark the current cell as visited

    random.shuffle(directions)  # Shuffle the directions

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        if is_in_bounds(new_x, new_y) and grid[new_y][new_x] == 0:
            t.penup()
            t.goto(x * cell_size - width // 2, height // 2 - y * cell_size)
            t.pendown()
            t.goto(new_x * cell_size - width // 2, height // 2 - new_y * cell_size)
            generate_maze(new_x, new_y)

# Start generating the maze from the top-left corner
generate_maze(0, 0)

# Close the window on click
screen.exitonclick()
