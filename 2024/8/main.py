import math
with open("input.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]
  
  world_width = len(lines[0])
  world_height = len(lines)
  
  frequencies = {}
  for y in range(world_height):
    for x in range(len(lines[y])):
      if lines[y][x] != ".":
        if lines[y][x] not in frequencies:
          frequencies[lines[y][x]] = []
        frequencies[lines[y][x]].append((x, y))
  
  resonant_freq_loc = set()
  
  for frequency in frequencies:
    for i, point in enumerate(frequencies[frequency]):
      for other_point in frequencies[frequency][i + 1:]:
        distance_y = point[1] - other_point[1]
        distance_x = point[0] - other_point[0]
        
        loc1 = (point[0] - distance_x*2, point[1] - distance_y*2)
        if loc1[0] >= 0 and loc1[0] < world_width and loc1[1] >= 0 and loc1[1] < world_height:
          resonant_freq_loc.add(loc1)
          
        loc2 = (point[0] + distance_x, point[1] + distance_y)
        if loc2[0] >= 0 and loc2[0] < world_width and loc2[1] >= 0 and loc2[1] < world_height:
          resonant_freq_loc.add(loc2)
  
  print(f"Part 1: {len(resonant_freq_loc)}")

  
  resonant_freq_loc_part2 = set()
  
  for frequency in frequencies:
    for i, point in enumerate(frequencies[frequency]):
      resonant_freq_loc_part2.add(point)
      for other_point in frequencies[frequency][i + 1:]:
        distance_y = point[1] - other_point[1]
        distance_x = point[0] - other_point[0]
        
        multiplier = 0
        
        while True:
          
          changed = False
          
          loc1 = (point[0] + distance_x*multiplier, point[1] + distance_y*multiplier)
          if loc1[0] >= 0 and loc1[0] < world_width and loc1[1] >= 0 and loc1[1] < world_height:
            resonant_freq_loc_part2.add(loc1)
            changed = True
            
          loc2 = (point[0] + distance_x*-multiplier, point[1] + distance_y*-multiplier)
          if loc2[0] >= 0 and loc2[0] < world_width and loc2[1] >= 0 and loc2[1] < world_height:
            resonant_freq_loc_part2.add(loc2)
            changed = True
          
          if not changed:
            break
          
          multiplier += 1
          
  print(f"Part 2: {len(resonant_freq_loc_part2)}")
  
  

