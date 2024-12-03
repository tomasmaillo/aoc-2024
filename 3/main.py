import re

with open("./3/input.txt", "r") as file:

    # Part 1

    
    lines = file.readlines()
    
    mults = []
    
    text = ""
    
    for line in lines:
        text += line
        mults = mults + re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
    
    total = 0
    for mult in mults:
        total += int(mult[0]) * int(mult[1])
        
    print("Total: ", total)
    
    
    # Part 2
    
    start = [(m.start(), m.group()) 
            for m in re.finditer(r'do\(\)', text)]
    
    stop = [(m.start(), m.group()) 
            for m in re.finditer(r'don\'t\(\)', text)]
    
    muls = [(m.start(), m.group()) 
            for m in re.finditer(r'mul\((\d+),(\d+)\)', text)]
    
    all = start + stop + muls
    
    all.sort(key=lambda x: x[0])

    enabled = True
    filtered_total = 0
    for i, item in enumerate(all):
        if item[1] == "do()":
            enabled = True
        elif item[1] == "don't()":
            enabled = False
        else:
            if enabled:
                m = item[1].replace("mul(", "").replace(")", "")
                m = m.split(",")
                filtered_total += int(m[0]) * int(m[1])
                
    print("Filtered total: ", filtered_total)