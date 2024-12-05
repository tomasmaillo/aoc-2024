

with open("./5/input.txt", "r") as file:
    lines = file.read().splitlines()
    
    split = lines.index("")
    rules = lines[:split]
    stacks = lines[split+1:]
    
    dicRules = set(rules)
    
    def isStackInOrder(stack):
      for i, item in enumerate(stack):
        for j, other in enumerate(stack[i+1:]):
          if f"{item}|{other}" not in dicRules:
            return False
      return True
    
    def isStackInOrderWithSwap(stack):
      while not isStackInOrder(stack):
        for i, item in enumerate(stack):
          for j, other in enumerate(stack[i+1:]):
            if f"{item}|{other}" not in dicRules:
              stack[i], stack[j+i+1] = stack[j+i+1], stack[i]
      return stack
    
    fine = []
    notFineButFixed = []
    for stack in stacks:
      items = stack.split(",")
      
      if isStackInOrder(items):
        fine.append(items)
      else:
        notFineButFixed.append(isStackInOrderWithSwap(items))
    
    total = 0
    for item in fine:
      middleItem = item[len(item)//2]
      total += int(middleItem)
      
    print("Total fine: ", total)
    
    
    totalFixed = 0
    for item in notFineButFixed:
      middleItem = item[len(item)//2]
      totalFixed += int(middleItem)
      
    print("Total fixed: ", totalFixed)