with open("Problem Set/Chapter 9/this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)