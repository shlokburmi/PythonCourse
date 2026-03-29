def f_to_c(f):
    c=(f-32)*5/9
    return c
f=int(input("Enter the temperature in fahrenheit: "))
c=f_to_c(f)
print(f"{round(c,2)} degree fahrenheit is equal to {round(f_to_c(f),2)} degree celsius")
