#lambda --> 1000

nfa={}
g = open("tema2.out", "w")
with open('tema2.in') as file:
    stare_initiala = file.readline().replace('\n', '')
    stari_finale = file.readline().replace('\n', '').split()
    for linie in file:
        linie = linie.replace('\n', '').split(' ')
        sursa, litera, destinatie = linie   #ex: q0   1    q3 toate str-uri
        if sursa not in nfa: #cream dictionar pentru fiecare stare 
            nfa[sursa]={}
        if litera not in nfa[sursa]: #adaugam starea destinatie la dictionarul starii sursa cu muchia corespunzatoare 
            nfa[sursa][litera] = [destinatie]   #asignam litera respectiva unei destinatii
        else:
            nfa[sursa][litera] += [destinatie]  #adaugam destinatia la litera respectiva, deoarece deja am ajuns cu aceasta litera intr-o alta destinatie si am nevoie sa le adaug pe toate


def lambda_mutare(stari, nfa):  #functie care gaseste toate starile din care putem sa ajungem din toate starile 'stari' numai cu lambda
    stari_posibile = stari.copy()
    coada = list(stari)
    while coada:
        stare = coada.pop(0)
        for urmatoarea_stare in nfa.get(stare, {}).get('1000', []):
            if urmatoarea_stare not in stari_posibile:
                stari_posibile.append(urmatoarea_stare)
                coada.append(urmatoarea_stare)
    return sorted(stari_posibile)

# NFA --> DFA
stare_inceput = sorted(lambda_mutare(['q0'], nfa))   #gasim mai intai toate starile din care putem ajunge numai cu q0 numai cu lambda
stari_dfa = [stare_inceput]
dfa = {}
coada = [stare_inceput]
while coada: #cat timp avem stari neexplorate cu algoritmul nostru
    stare_curenta = coada.pop(0)
    for litera in ('0', '1', '2'):  #alfabetul nostru 
        urmatoarea_stare = sorted(list(set(stare for stari_nfa in stare_curenta for stare in nfa.get(stari_nfa, {}).get(litera, [])))) #toate starile in care putem sa ajungem cu 0 1 sau 2 si inclusiv cu lambda (lambda*0; lambda*1; lambda*2)
        stari_lambda2 = lambda_mutare(urmatoarea_stare, nfa) #gasim toate starile in care putem merge cu lambda dupa ce am mers deja cu 0 1 sau 2 (lambda*0lambda*; lambda*1lamnbda*; lambda*2lambda*)
        if tuple(stari_lambda2) not in [tuple(s) for s in stari_dfa]:
            stari_dfa.append(stari_lambda2) #gasim aceste stari complexe de genul q0q2q3q4q5q6
            coada.append(stari_lambda2)
        dfa.setdefault(tuple(stare_curenta), {})[litera] = tuple(stari_lambda2) 

# afisam DFA
g.write('DFA Transition Table:')
g.write('\n')
g.write('cu 0  |  cu 1  | cu 2  ')
g.write('\n')
g.write('-----------------------')
g.write('\n')
for stari in stari_dfa: #printam frumos bazandu-ne pe dfa_states care sunt acele stari complexe de genul q0q2q3q4q5q6 si dfa_transition care este exact dfa-ul nostru
    g.write('{:2s} | {:2s} | {:2s} | {:2s}'.format(','.join(stari), ','.join(dfa.get(tuple(stari), {}).get('0', [])), ','.join(dfa.get(tuple(stari), {}).get('1', [])), ','.join(dfa.get(tuple(stari), {}).get('2', []))))
    g.write('\n')
