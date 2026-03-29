
word="Donkey"
with open("S:/Programming/Python/python/Chapter 9 - File io/file.txt") as f:
    content=f.read()
contentNew=content.replace(word,"######")
with open("S:/Programming/Python/python/Chapter 9 - File io/file.txt","w") as f:
    f.write(contentNew)

