import Tab

def dico (typ):
    try:
        typ=str(typ)
        if typ=='0':
            tab1=Tab.lettre()
            tab2=Tab.binaire() 
            i=0
            count=len(tab1)
            count2=len(tab2)
            if count == count2:
                dicot=dict()
                while count>i:
                    dicot[tab1[i]]=tab2[i]
                    i=i+1
            else:
                dicot='Les deux tableaux entrés ne sont pas égaux'
                
        elif typ=='16':
            tab1=Tab.lettre()
            tab2=Tab.hexa()
            i=0
            count=len(tab1)
            count2=len(tab2)
            if count == count2:
                dicot=dict()
                while count>i:
                    dicot[tab1[i]]=tab2[i]
                    i=i+1

        elif typ=='8':
            tab1=Tab.lettre()
            tab2=Tab.octa()
            i=0
            count=len(tab1)
            count2=len(tab2)
            if count == count2:
                dicot=dict()
                while count>i:
                    dicot[tab1[i]]=tab2[i]
                    i=i+1
                    
        elif typ=='10':
            tab1=Tab.lettre()
            tab2=Tab.decimal()
            i=0
            count=len(tab1)
            count2=len(tab2)
            if count == count2:
                dicot=dict()
                while count>i:
                    dicot[tab1[i]]=tab2[i]
                    i=i+1
            else:
                dicot='Les deux tableaux entrés ne sont pas égaux'
        else:
            dicot="-------Variable donnée impossible à traiter.Seul 0 ou 16 sont acceptés -----------"
    except NameError:
        dicot="Erreur inconnue"
    return  dicot

if  __name__=="__main__":
    print(dico(10))
