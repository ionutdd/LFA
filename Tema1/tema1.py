f=open("tema1.in" , "r")
g=open("tema1.out" , "w")
lines=f.readlines()
graf = [[]]
finale = []
cuvant=[]
k=1
for linie in lines:
    graf+=[linie.split()]
    k+=1
for i in range(1,len(graf)):
    if i==len(graf)-1:
        cuvant=graf[i]
    if i==len(graf)-2:
        finale = graf[i]

curent = 'q0'
cuvant = list(cuvant[0])
drum = ['q0']
nu_printa = False
nfa=False

for i in range(2,len(graf)-1):
    if graf[i][0] == graf[i-1][0] and graf[i][1] == graf[i-1][1] and graf[i][2] != graf[i-1][2]:
        g.write("NFA")
        g.write("\n")
        nfa=True
        break


def DEI(graf, cuvant, finale, curent):
    global ok
    for i in range(len(cuvant)):
        for j in range(1,len(graf)-2):
            if graf[j][0] == curent and graf[j][1] == cuvant[i]:
                if i+1 != len(cuvant):
                    DEI(graf, cuvant[(i+1):], finale, graf[j][2])
                else:
                    if graf[j][2] in finale and ok == 0:
                        ok = 1

if nfa==False:
    g.write("DFA")
    g.write("\n")
    for litera in cuvant:
        ok=0
        for j in range(1,len(graf)-1):
            if graf[j][0]==curent and graf[j][1]==litera:
                curent = graf[j][2] 
                drum += [curent]
                ok=1
                break
        if ok==0:
            g.write("Neacceptat")
            nu_printa = True
            break
    if nu_printa is not True:
        if curent in finale:
            g.write("Acceptat")
            g.write("\n")
            for elem in drum:
                g.write(elem)
                g.write(" ")
        else:
            g.write("Neacceptat")   
else:
    ok = 0
    DEI(graf, cuvant, finale, curent)
    if ok == 1:
        g.write("acceptat")
    else:
        g.write("neacceptat")

    
f.close()
g.close()
