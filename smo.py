###smo.py - логическая основа программы

import random

def change_state(A, state, states_counter, states):
    
    state = random.choices(list(states.keys()), weights=A[states[state]])[0]
    states_counter[state] = states_counter[state] + 1

    return state, states_counter

    
def make_cacl(tick, Acounter, Lccounter, Wccounter, Tickscounter, P1, P2, states_counter):

    P000 = states_counter['000']
    P100 = states_counter['100']
    P001 = states_counter['001']
    P101 = states_counter['101']
    P111 = states_counter['111']
    P011 = states_counter['011']

    P000 = P000  / tick if P000 else 0
    P100 = P100  / tick if P100 else 0
    P001 = P001  / tick if P001 else 0
    P101 = P101  / tick if P101 else 0
    P111 = P111  / tick if P111 else 0
    P011 = P011  / tick if P011 else 0

    Ac = (1 - P2) * (1 - P000 - P100)
    Lc = sum([k.count('1') * v  for k,v in states_counter.items()]) / tick
    Wc = (1 / (1 - P1)) + (P001 + P101 + 2*(P111 + P011)) / Ac

    Acounter.setText(str(round(Ac, 3)))
    Lccounter.setText(str(round(Lc, 3)))
    Wccounter.setText(str(round(Wc, 3)))
    Tickscounter.setText(str(round(tick, 3)))


def main_event(Ro, P1, P2, Ticks, labels_counter, Acounter, Lccounter, Wccounter, Tickscounter):

    A = [
    [Ro, 0,  1-Ro,  0, 0, 0],
    [Ro*(1 - P2), Ro*P2,  (1 - Ro) * ( 1- P2), (1 - Ro)*P2,  0, 0],
    [0, Ro*(1 - P1),  P1,  (1 - Ro)*(1 - P1), 0, 0],
    [0, Ro* (1-P1)*(1-P2),  P1*(1-P2), P1*P2 + (1 - Ro)*(1 - P1)*(1 - P2),  Ro *(1-P1)*P2, (1 - Ro) * (1 - P1)],
    [0, Ro*(1-P2),  0,  (1-Ro)*(1-P2), Ro*P2, (1-Ro)*P2],
    [0, 0, 0, P1*(1-P2), Ro * (1-P1), P1*P2 + (1 - Ro) * (1 - P1)]
    ]

    state = '000'    
    states = {'000': 0, '001': 1, '100': 2, '101': 3, '011': 4, '111': 5}
    states_counter = {'000': 0, '001': 0, '100': 0, '101': 0, '011': 0, '111': 0}
    
    for tick in range(1, Ticks + 1):

        if not P2:
            for i in A:
                i[states['011']] = 0
                i[states['111']] = 0

        state, states_counter = change_state(A, state, states_counter, states)

    for label_counter, state_counter in zip(labels_counter, list(states_counter.values())):
        label_counter.setText(str(state_counter))
        
    make_cacl(Ticks, Acounter, Lccounter, Wccounter, Tickscounter, P1, P2, states_counter)