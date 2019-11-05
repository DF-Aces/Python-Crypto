import math as mth

def rootN( x,y):
    str(x)
    if x>'0':
        x=int(x)
        y=int(y)
        r=round(pow(x,(1/y)))
    else:
        r=0
    return r


if  __name__==  "__main__":
     d=input("Phrase:\n")
     print(rootN(d,220))
