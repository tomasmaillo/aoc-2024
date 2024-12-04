with open("./2/input.txt", "r") as file:

    # Part 1
    
    left_column = []
    right_column = []
    
    lines = file.readlines()
    
    reports = []
    for line in lines:
        reports.append(list(map(int, line.strip().split(" "))))
      
    
    def isSafe(report):
      trend = report[0] < report[1]
      for i in range(len(report) - 1):
        difference = abs(report[i+1] - report[i])
        increasing = report[i+1] > report[i]
        if trend == increasing and 1 <= difference and difference<= 3:
          pass
        else:
          return False
      return True
    
    
    safe_reports = 0
    for report in reports:
      if isSafe(report):
        safe_reports += 1
        
    print("Safe reports: ", safe_reports)
    
    safe_reports_dampener = 0
    for report in reports:
      if isSafe(report):
        safe_reports_dampener += 1
      else:
        for i in range(len(report)):
          if isSafe(report[:i]+report[i+1:]):
            safe_reports_dampener += 1
            break

    print("Safe reports with dampener: ", safe_reports_dampener)
   
