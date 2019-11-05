n import  ascii2
import binaire


def rootN( x,y):
    str(x)
    if x>'0':
        x=int(x)
        y=int(y)
        r=round(pow(x,(1/y)))
    else:
        r=0
    return r
        

def  crypt(d):
    i=0
    word=str(d)
    key1=0
    key2=0
    tab=list()
    
    #GENERATION DES CLEFS
    d=ascii2.cascii(d,16)
    d=ascii2.cascii(d,8)
    d=ascii2.cascii(d,0)
    for ct in d:
        if ct =='1':
            key1=key1+1
        elif ct == '0':
            key2=key2+1

    #CREATION DE LA CLEF PRIMAIRE
    if key2>key1:
        keyP=key2%key1       
    else:
        if key1>0:
            keyP=key1%key2
            key2=key1
        else:
            keyP=0
        

    return word,keyP,key2,key1



if  __name__==  "__main__":
     d=input("Phrase:\n")
     print(crypt(d))
    
