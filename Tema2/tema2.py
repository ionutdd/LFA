f = open("tema2.in", "r")
g = open("tema2.out", "w")
lines = f.readlines()
graf = [[]]
finale = []
k = 1
for linie in lines:
    graf += [linie.split()]
    k += 1
for i in range(1, len(graf)):
    if i == len(graf) - 1:
        finale = graf[i]

curent = ['q0']

def lambda_closure(graf, states):
    closure = set(states)
    for state in states:
        for j in range(1, len(graf) - 2):
            if graf[j][0] == state and graf[j][1] == '1000':
                if graf[j][2] not in closure:
                    closure.add(graf[j][2])
                    closure |= lambda_closure(graf, [graf[j][2]])
    return closure

def move(graf, states, symbol):
    new_states = set()
    for state in states:
        for j in range(1, len(graf) - 2):
            if len(graf[j]) == 3 and graf[j][0] == state and graf[j][1] == symbol:
                new_states.add(graf[j][2])
    return new_states

dfa_graf = {'q0': {}}
unmarked_states = [curent]
marked_states = []
while unmarked_states:
    curr_state_set = unmarked_states.pop()
    marked_states.append(curr_state_set)
    print(f'Current state set: {curr_state_set}')
    for symbol in set([trans[1] for state in curr_state_set for trans in graf if len(trans) == 3 and trans[0] == state and trans[1] != '1000']):
        next_state_set = lambda_closure(graf, move(graf, curr_state_set, symbol))
        print(f'  Symbol {symbol}:')
        print(f'  Next state set: {next_state_set}')
        dfa_graf.setdefault(''.join(sorted(curr_state_set)), {})[symbol] = ''.join(sorted(next_state_set))
        if next_state_set not in marked_states:
            unmarked_states.append(next_state_set)
            marked_states.append(next_state_set)
            print(f'  Appended {next_state_set} to unmarked_states')

for state_set in dfa_graf:
    if any(state in finale for state in state_set):
        dfa_graf[state_set]['accepting'] = True
    else:
        dfa_graf[state_set]['accepting'] = False

g.write('DFA Graph:\n')
for state_set in dfa_graf:
    g.write(state_set + ':\n')
    for symbol in dfa_graf[state_set]:
        if symbol != 'accepting':
            g.write('\t' + symbol + ' -> ' + dfa_graf[state_set][symbol] + '\n')
    if dfa_graf[state_set]['accepting']:
        g.write('\t' + 'accepting state\n')
    g.write('\n')

g.write('Final States:\n')
for state in finale:
    for state_set in dfa_graf:
        if state in state_set:
            g.write(state_set + '\n')

f.close()
g.close()
