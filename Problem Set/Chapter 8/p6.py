def inch_to_cm(inch):
    cm=inch*2.54
    return cm
n=int(input("Enter the length in inches: "))
print(f"{n} inch is equal to {inch_to_cm(n)} cm")