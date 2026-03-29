with open("Problem Set\Chapter 9\log.txt", "r") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if ("python " in line):
        print(f"python is present in line number {lineno}")
        break
    lineno+=1
else:
    print(f"python is not present in line number {lineno}")
