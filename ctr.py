"""
    This is a script to form a CTR from AES
"""

from src.main import main_encrypt, main_decrypt

import time
import math

def main_ctr(number_of_output, key, iv, counter=0):
    """
        Define IV or Nonce, of 16 hexadecimal, rest will be counter
        number of output is a var that gives the number of times we have to repeate
        Key is fixed for all the outputs
    """
    output      = []
    plain_input = ''

    for _ in xrange(number_of_output):
        inp             = iv + hex(counter)[2:].zfill(16)
        plain_input    += inp 
        counter        += 1
    cipher = main_encrypt(plain_input, key)
    output = list(map(''.join, zip(*[iter(cipher)]*32)))
    
    return output

def plain_text_xor_ctr_output(plain_text, key, iv):
    """
        XORing plain text with CTR
        Here 32 is the block size corresponding to 16 bytes
        Plain text should be in one single string
    """
    plain_blocks = [plain_text[i:i+32] for i in range(0, len(plain_text), 32)]
    plain_blocks[-1] = plain_blocks[-1] + '0'*(32 - len(plain_blocks[-1]))

    count = len(plain_blocks)

    output = main_ctr(count, key, iv)

    final_output = [hex(int(ouput[i], 16) ^ int(plain_blocks[i],16))[2:34] for i in range(count)]

    return final_output

if __name__ == "__main__":
    key = '328831e0435a3137f6309807a88da234'
    count = 10
    iv = '2b28ab097eaef7cf'

    start = time.time()
    output = main_ctr(count, key, iv)
    stop = time.time()
    print output
    print 'Done'
    print 'Time Taken -> %i sec'%(stop-start)
