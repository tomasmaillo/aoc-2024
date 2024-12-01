
with open("./1/input.txt", "r") as file:

    # Part 1
    
    left_column = []
    right_column = []
    
    for line in file:
        sides = line.strip().split("   ")
        left_column.append(sides[0])
        right_column.append(sides[1])
        
    left_column.sort()
    right_column.sort()
    
    total_distance = 0
    for i in range(len(left_column)):
        total_distance += abs(int(left_column[i]) - int(right_column[i]))

    print("Total distance: ", total_distance)
    
    # Part 2
    
    occurrences_right_column = {}
    
    for side in right_column:
        if side in occurrences_right_column:
            occurrences_right_column[side] += 1
        else:
            occurrences_right_column[side] = 1
    
    similarity_score = 0
    for number in left_column:
        if number in occurrences_right_column:
            similarity_score =  similarity_score + int(number) * occurrences_right_column[number]
    
    print("Similarity score: ", similarity_score)
