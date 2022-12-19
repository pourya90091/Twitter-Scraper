import random
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rotor_generator():
    r1 = list(alphabet)
    random.shuffle(r1)
    r1 = ''.join(r1)

    r2 = list(alphabet)
    random.shuffle(r2)
    r2 = ''.join(r2)

    r3 = list(alphabet)
    random.shuffle(r3)
    r3 = ''.join(r3)

    with open(f'{BASE_DIR}/utils/enigma/todays_rotor_state.enigma', 'wb') as file:
        pickle.dump((r1, r2, r3), file)
