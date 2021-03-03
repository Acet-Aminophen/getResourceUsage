def getResourceUsage(filename:str, type:str):
    #top -d [duration second] -b | grep "load average" -A [how many line you want] --line-buffered | tee [name].log
    #the type can be send "cpu" or "mem"
    
    depth1 = []
    file = open(filename, 'r')
    strTmp:str = ""
    while True:
        nowLine = file.readline()
        if not nowLine:
            break
        if "--" in strTmp:
            depth1.append(strTmp)
            strTmp = ""
        strTmp += nowLine
    file.close()

    depth2 = []
    for org in depth1:
        orgSplit = org.split("\n")
        for i in range(len(orgSplit)):
            if "java" in orgSplit[i]:
                depth2.append(orgSplit[i])
                break

    depth3 = []
    cpu = []
    mem = []
    for i in depth2:
        depth3 .append(i[46:58].strip().split("  ")[0])
        depth3 .append(i[46:58].strip().split("  ")[1])

    for i in range(len(depth3)):
        if i % 2 == 0:
            cpu.append(depth3[i])
        else:
            mem.append(depth3[i])

    cpu_f = list(map(float,cpu))
    mem_f = list(map(float,mem))
    if type == "cpu": return cpu_f
    else: return mem_f
