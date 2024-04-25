import random

def opti( F : str ):
    t=''
    for i in range(len(F)-1,-1,-1):
        if not '.' in t:
            t+=F[i]
    if t=='lmth.':
        T=''
        nb=0
        for i in open(F,'r').read():
            if i!='\n':
                if i==' ' or i=='>':
                    nb+=1
                else:
                    nb=0
                if 0<=nb<=1:
                    T+=i
            elif '\")'==T[-2:] or '})'==T[-2:]:
                T+=i
        open(f'indexe {random.randint(0,100)}.html','w').write(T)
    elif t=='ssc.':
        T=''
        nb=0
        for i in open(F,'r').read():
            if i!='\n':
                if i==' ':
                    nb+=1
                else:
                    nb=0
                if 0<=nb<=1 and t!='{':
                    T+=i
                    t=i
                else:
                    t=''
        open(f'style {random.randint(0,100)}.css','w').write(T)
        
opti('')