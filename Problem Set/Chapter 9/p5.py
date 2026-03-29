
words=["Donkey","bad","ugly"]
with open("S:/Programming/Python/python/Chapter 9 - File io/file.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"#"*len(word))
with open("S:/Programming/Python/python/Chapter 9 - File io/file.txt","w") as f:
    f.write(content)

