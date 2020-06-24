###smo.py - логическая основа программы

import random

def change_state(trans_matrix, state, states_counter, trans_states):
    
    state = random.choices(list(trans_states.keys()), weights= trans_matrix[trans_states[state]])[0]
    states_counter[state] = states_counter[state] + 1

    return state, states_counter

    
def make_cacl(tick, ac_counter, lc_counter, wc_counter, ticks_counter, p1, p2, states_counter):

    p000 = states_counter['000']
    p100 = states_counter['100']
    p001 = states_counter['001']
    p101 = states_counter['101']
    p111 = states_counter['111']
    p011 = states_counter['011']

    p000 = p000  / tick if p000 else 0
    p100 = p100  / tick if p100 else 0
    p001 = p001  / tick if p001 else 0
    p101 = p101  / tick if p101 else 0
    p111 = p111  / tick if p111 else 0
    p011 = p011  / tick if p011 else 0

    ac = (1 - p2) * (1 - p000 - p100)
    lc = sum([k.count('1') * v  for k,v in states_counter.items()]) / tick
    wc = (1 / (1 - p1)) + (p001 + p101 + 2*(p111 + p011)) / ac

    ac_counter.setText(str(round(ac, 3)))
    lc_counter.setText(str(round(lc, 3)))
    wc_counter.setText(str(round(wc, 3)))
    ticks_counter.setText(str(round(tick, 3)))


def main_event(ro, p1, p2, ticks, labels_counter, Acounter, Lccounter, Wccounter, Tickscounter):

    trans_matrix = [
    [ro, 0,  1-ro,  0, 0, 0],
    [ro*(1 - p2), ro*p2,  (1 - ro) * ( 1- p2), (1 - ro)*p2,  0, 0],
    [0, ro*(1 - p1),  p1,  (1 - ro)*(1 - p1), 0, 0],
    [0, ro* (1-p1)*(1-p2),  p1*(1-p2), p1*p2 + (1 - ro)*(1 - p1)*(1 - p2),  ro *(1-p1)*p2, (1 - ro) * (1 - p1)],
    [0, ro*(1-p2),  0,  (1-ro)*(1-p2), ro*p2, (1-ro)*p2],
    [0, 0, 0, p1*(1-p2), ro * (1-p1), p1*p2 + (1 - ro) * (1 - p1)]
    ]

    state = '000'    
    trans_states = {'000': 0, '001': 1, '100': 2, '101': 3, '011': 4, '111': 5}
    states_counter = {'000': 0, '001': 0, '100': 0, '101': 0, '011': 0, '111': 0}
    
    for tick in range(1, ticks + 1):

        if not p2:
            for chance in trans_matrix:
                chance[trans_states['011']] = 0
                chance[trans_states['111']] = 0

        state, states_counter = change_state(trans_matrix, state, states_counter, trans_states)

    for label_counter, state_counter in zip(labels_counter, list(states_counter.values())):
        label_counter.setText(str(state_counter))
        
    make_cacl(ticks, ac_counter, lc_counter, wc_counter, ticks_counter, p1, p2, states_counter)
