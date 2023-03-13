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
for litera in cuvant:
    ok=0
    for j in range(1,len(graf)):
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
f.close()
g.close()