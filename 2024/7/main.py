

def isValid(result: int, values: list[int]):
    
    if len(values) == 1:
      return values[0] == result
       
    running_value = values[0]
    
    if running_value > result:
      return False
  
    mult = running_value * values[1]
    add = running_value + values[1]
    
    return isValid(result, [mult] + values[2:]) or isValid(result, [add] + values[2:])


def isValidPart2(result: int, values: list[int]):
    
    if len(values) == 1:
      return values[0] == result
    
    
    running_value = values[0]
    
    if running_value > result:
      return False
  
    mult = running_value * values[1]
    add = running_value + values[1]
    concat = int(str(running_value) + str(values[1]))
    
    return isValidPart2(result, [mult] + values[2:]) or isValidPart2(result, [add] + values[2:]) or isValidPart2(result, [concat] + values[2:])
  


with open("input.txt", "r") as file:
    lines = file.readlines()
    
    equations = []
    for line in lines:
        halves = line.strip().split(": ")
        equations.append((halves[0], halves[1].split(" ")))
        
    total_totals  = 0
    for equation in equations:
      if isValid(int(equation[0]), [int(x) for x in equation[1]]):
        total_totals += int(equation[0])
    
    print(f"Part 1: {total_totals}")
      
      
    total_totals_part2  = 0
    for equation in equations:
      if isValidPart2(int(equation[0]), [int(x) for x in equation[1]]):
        total_totals_part2 += int(equation[0])
    print(f"Part 2: {total_totals_part2}")
    