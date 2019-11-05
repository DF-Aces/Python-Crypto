import Tab
import dicoCrea

def cascii(donn,t):
    tab=list()
    t=str(t)
    d=dicoCrea.dico(t)
    
    donn=str(donn)
    for nb in donn:
        for  ct in d.keys():
            if ct == nb:
                res=d[ct]
                tab.append(res)
    tab=" ".join(tab)
    return tab


def rascii(donn,t):
    d=dicoCrea.dico(t)
    res=str()
    t=str(t)
    tab=list()
    tab2=list()
    donn=str(donn)
    if t=='0':
        ct=8
    elif t=='16':
        ct=2
    elif t=='8' or t=='10':
        ct=3
        
    for cnt in donn:
        if cnt != ' ':
            tab2.append(cnt)
            if  len(tab2)==ct:
                res="".join(tab2)
                for cle, val in d.items():
                    if val ==  res:
                        res=cle
                        tab.append(res)
                        tab2=list()
    tab="".join(tab)
    return tab
    
    

if  __name__=="__main__":
    d=str()
    while d!='-1':
        d=input("Phrase:\n")
        print(cascii(d,0))
    
    
