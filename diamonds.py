num_diamonds = 9
size = 8
num_rows = 20

width = size//2

for r in range(num_rows):
    sides = abs((r-width) % size - width) 

    row = "X" * sides + " " + "X" * (size - 2*sides - 1)

    if (sides != 0 and sides != width):
        row += " "

    if sides > 0:
        row += "X" * (sides-1)

    print(row * num_diamonds)