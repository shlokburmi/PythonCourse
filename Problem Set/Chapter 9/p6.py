with open("Problem Set\Chapter 9\log.txt", "r") as f:
    content = f.read()


if "python" in content.lower():
    print("python is present in the log")
else:
    print("python is not present in the log")