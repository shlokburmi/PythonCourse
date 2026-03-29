import os

def generateTable(n):
    # create folder if not exists
    os.makedirs("tables", exist_ok=True)

    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generateTable(i)