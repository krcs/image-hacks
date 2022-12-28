import random
import string

def generate_random_string(length):
    ld = string.ascii_letters+string.digits
    return ''.join([random.choice(ld) for n in range(length)])


