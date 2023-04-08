nfa={}
g = open("tema2.out", "w")
with open('tema2.in') as file:
    stare_initiala = file.readline().replace('\n', '')
    stari_finale = file.readline().replace('\n', '').split()
    for line in file:
        line = line.replace('\n', '').split(' ')
        sursa, litera, destinatie = line   
        if sursa not in nfa:
            nfa[sursa]={}
        if litera not in nfa[sursa]:
            nfa[sursa][litera] = [destinatie]
        else:
            nfa[sursa][litera] += [destinatie]


def lambda_closure(stari, nfa):
    l_closure = stari.copy()
    queue = list(stari)
    while queue:
        state = queue.pop(0)
        for next_state in nfa.get(state, {}).get('1000', []):
            if next_state not in l_closure:
                l_closure.append(next_state)
                queue.append(next_state)
    return sorted(l_closure)

start_state = sorted(lambda_closure(['q0'], nfa))
dfa_states = [start_state]
dfa_transition = {}
queue = [start_state]
while queue:
    current_state = queue.pop(0)
    for symbol in ('0', '1', '2'):
        next_state = sorted(list(set(state for nfa_state in current_state for state in nfa.get(nfa_state, {}).get(symbol, []))))
        epsilon_states = lambda_closure(next_state, nfa)
        if tuple(epsilon_states) not in [tuple(s) for s in dfa_states]:
            dfa_states.append(epsilon_states)
            queue.append(epsilon_states)
        dfa_transition.setdefault(tuple(current_state), {})[symbol] = tuple(epsilon_states)

g.write('DFA Transition Table:')
g.write('\n')
g.write('   |  0  |  1  |  2  ')
g.write('\n')
g.write('-----------------------')
g.write('\n')
for state in dfa_states:
    g.write('{:2s} | {:2s} | {:2s} | {:2s}'.format(','.join(state), ','.join(dfa_transition.get(tuple(state), {}).get('0', [])), ','.join(dfa_transition.get(tuple(state), {}).get('1', [])), ','.join(dfa_transition.get(tuple(state), {}).get('2', []))))
    g.write('\n')
