import re

with open("./4/input.txt", "r") as file:

    # Part 1
    lines = file.read().splitlines()
    
    # lines = [
    #     "MMMSXXMASM",
    #     "MSAMXMSMSA",
    #     "AMXSXMAAMM",
    #     "MSAMASMSMX",
    #     "XMASAMXAMM",
    #     "XXAMMXXAMA",
    #     "SMSMSASXSS",
    #     "SAXAMASAAA",
    #     "MAMMMXMMMM",
    #     "MXMXAXMASX"
    # ]
    
    toFind = "XMAS"
    
    def checkDirection(x, y, direction):
        newX = x
        newY = y
        for i in range(1, len(toFind)):
            newX += direction[0]
            newY += direction[1]
            if newX < 0 or newY < 0 or newX >= len(line) or newY >= len(lines):
                return False
            if lines[newY][newX] != toFind[i]:
                return False
        return True
    
    matches = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == toFind[0]:
                checked = [checkDirection(x, y, direction) for direction in directions]
                num_matches = sum(checked)
                if num_matches > 0:
                    matches += num_matches
    print("Matches: ", matches)
    
    # Part 2
    
    count = 0
    diagonals = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    values_in_diagonals = {"M", "S"}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "A" and y >= 1 and x >= 1 and y + 1 < len(lines) and x + 1 < len(line):
                top_left = lines[y + diagonals[1][1]][x + diagonals[1][0]]
                bottom_right = lines[y + diagonals[0][1]][x + diagonals[0][0]]
                
                okay_left = top_left in values_in_diagonals and bottom_right in values_in_diagonals and top_left != bottom_right
                
                    
                bottom_left = lines[y + diagonals[2][1]][x + diagonals[2][0]]
                top_right = lines[y + diagonals[3][1]][x + diagonals[3][0]]
                
                okay_right = bottom_left in values_in_diagonals and top_right in values_in_diagonals and bottom_left != top_right
                
                if okay_left and okay_right:
                    count += 1
                
    print("Matches in X shape: ", count)
