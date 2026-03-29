def rem(l,word):
    n=[]
    for item in l:
        if not (item==word):
            n.append(item.strip())
    return n


l=["harry","Sarry","carry","marry"]
