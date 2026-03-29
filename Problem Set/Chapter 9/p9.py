with open("file1.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("The contents of the two files are the same")
else:
    print("The contents of the two files are different")

