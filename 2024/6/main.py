
def hasSolution(lines):
    
    guard_pos = (0, 0)
    
    for line in lines:
        if "^" in line:
            guard_pos = (line.index("^"), lines.index(line))
            break
    
    # up right down left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    facing = directions[0] # start facing up
    guard_trail = []
    guard_trail_with_facing = set()
    
    while True:
      guard_trail.append(guard_pos)
      if f"{guard_pos[0]},{guard_pos[1]},{facing}" in guard_trail_with_facing:
        return -1
      guard_trail_with_facing.add(f"{guard_pos[0]},{guard_pos[1]},{facing}")
      
      if facing == directions[0] and guard_pos[1] == 0:
        break
      elif facing == directions[1] and guard_pos[0] == len(lines[0]) - 1:
        break
      elif facing == directions[2] and guard_pos[1] == len(lines) - 1:
        break
      elif facing == directions[3] and guard_pos[0] == 0:
        break
      
      for i, direction in enumerate(directions):
        if facing != direction:
          continue
        
        if lines[guard_pos[1] + direction[1]][guard_pos[0] + direction[0]] == "#":
          facing = directions[(i + 1) % 4]
          break
        else:
          guard_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])
      
    # Print the map with guard trail
    # map_lines = [list(line.strip()) for line in lines]
    # for pos in guard_trail:
    #     map_lines[pos[1]][pos[0]] = "X"
    
    # for line in map_lines:
    #     print("".join(line))

    return len(set(guard_trail))


with open("./6/input.txt", "r") as f:
    lines = f.readlines()
    
    lines = [line.strip() for line in lines]
    
    # Part 1
    print("Part 1:", hasSolution(lines))
    
    # Part 2
    loops_found = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            original_char = lines[y][x]
            if original_char == "#" or original_char == "^":
                continue
            
            lines[y] = lines[y][:x] + "#" + lines[y][x+1:]
            if hasSolution(lines) == -1:
                loops_found += 1
                
            lines[y] = lines[y][:x] + original_char + lines[y][x+1:]
        print(f"loops found: {loops_found}    \t rows left: {len(lines) - y - 1}  \t{((y / len(lines)) * 100):.2f}%")
    
    print("Part 2:", loops_found)

