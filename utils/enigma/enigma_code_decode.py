import pickle
from pathlib import Path
from utils.enigma.todays_rotor_generator import rotor_generator


alphabet = 'abcdefghijklmnopqrstuvwxyz'

BASE_DIR = Path(__file__).resolve().parent.parent.parent

rotor_generator()

with open(f'{BASE_DIR}/utils/enigma/todays_rotor_state.enigma', 'rb') as file:
    r1, r2, r3 = pickle.load(file)

rotors = (r1, r2, r3)
rotors_config = (alphabet.index(rotors[0][0]) + 1, alphabet.index(rotors[1][0]) + 1, alphabet.index(rotors[2][0]) + 1)

state = 0

def reflector(c):
    return alphabet[len(alphabet)-alphabet.find(c)-1]


def enigma_one_char(c):
    c1 = r1[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    reflected = reflector(c3)
    c3 = alphabet[r3.find(reflected)]
    c2 = alphabet[r2.find(c3)]
    c1 = alphabet[r1.find(c2)]

    return c1


def rotate_rotors():
    global r1, r2, r3
    global state

    r1 = r1[1:] + r1[0]
    if state % 26:
        r2 = r2[1:] + r2[0]
    if state % (26*26):
        r3 = r3[1:] + r3[0]


def code(plain, config):
    global r1, r2, r3
    global state

    for _ in range(config[0]):
        r1 = r1[1:] + r1[0]
    for _ in range(config[1]):
        r2 = r2[1:] + r2[0]
    for _ in range(config[2]):
        r3 = r3[1:] + r3[0]

    cipher = ''

    for c in plain:
        state += 1
        cipher += enigma_one_char(c)
        rotate_rotors()

    r1 = rotors[0]
    r2 = rotors[1]
    r3 = rotors[2]
    state = 0

    return cipher
