from math import *

def cbinaire (dec):
    dec=int(dec)
    if dec>0:
        bi=list()
        bie=list()
        i=0
        while dec !=0:
            rest=dec%2
            if rest>0:
                bi.append('1')
                dec=dec/2
                dec=floor(dec)
            else:
                bi.append('0')
                dec=dec/2
                
        if len(bi)%4!=0:
                t=4-(len(bi)%4)
                while t!=0:
                    bi.append('0')
                    t=t-1
        bi.reverse()
        for ct in bi:
            bie.append(ct)
            i=i+1
            if i==4:
                if len(bi)-len(bie)>=0:
                    bie.append(' ')
                i=0
        bi=''.join(bie)
        #bi=''.join(bi)
    else:
        bi='Nombre négatif non autorisé'
    
    return bi

def rbinaire (bi):
    bi=str(bi)
    tot=0
    tot1=0
    bi=bi.split(' ')
    bi="".join(bi)
    nb=len(bi)-1
    for ct in bi:
        if ct !="  ":
            if ct == '1':
                tot=pow(2,nb)+tot1
                tot1=tot
            nb=nb-1
    tot=round(tot)

    return tot
                    
    
    
        

if __name__ =="__main__":
    while 0==0:
        d=input('Rentre:\n')
        if d == -1:
            break
        print(rbinaire(d))
