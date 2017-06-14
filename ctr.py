"""
    This is a script to form a CTR from AES
"""

from src.main import main_encrypt, main_decrypt

import time

def main_ctr(number_of_output, key, nonce, counter=0):
    """
        Define IV or Nonce, of 16 hexadecimal, rest will be counter
        number of output is a var that gives the number of times we have to repeate
        Key is fixed for all the outputs
    """
    output      = []
    plain_input = ''

    for _ in xrange(number_of_output):
        inp             = nonce + hex(counter)[2:].zfill(16)
        plain_input    += inp 
        counter        += 1
    cipher = main_encrypt(plain_input, key)
    output = list(map(''.join, zip(*[iter(cipher)]*32)))
    
    return output

if __name__ == "__main__":
    key = '328831e0435a3137f6309807a88da234'
    count = 10
    nonce = '2b28ab097eaef7cf'

    start = time.time()
    output = main_ctr(count, key, nonce)
    stop = time.time()
    print output
    print 'Done'
    print 'Time Taken -> %i sec'%(stop-start)
