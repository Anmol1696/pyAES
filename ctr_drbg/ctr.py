"""
    This is a script to form a CTR from AES
"""

from src.main import main_encrypt, main_decrypt

import time


def call_main_ctr(num, key, break_size, file_name, iv='0e905298a4114e45', nonce='2b28ab097eaef7cf', file_location='/root/Documents/Git/Crypto/AES_modification/data/'):
    """
        Divides the input if the block size is very large
    """
    if num <= break_size:
        #print 'Forming the cipher texts and numbers'
        ctr = main_ctr(num, key, 0, iv, nonce)
        #print 'Forming Text file'
        _   = form_text_file(ctr, key+' iv='+iv, True, num, file_name, file_location=file_location)
    else:
        temp = num/break_size + 1
        count = num*4 + break_size*4
        for rep in range(temp):
            #print 'Forming the cipher texts and numbers -> Round => %i'%(rep)
            ctr = main_ctr(break_size, key, rep*break_size, iv, nonce)
            #print 'Forming Text file'
            if rep == 0:
                header = True
            else: header = False
            _   = form_text_file(ctr, key+' iv='+iv, header, count, file_name, file_location=file_location)


def main_ctr(number_of_output, key, counter, iv, nonce):
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


def converting_cipher_to_32_bit_number(inp):
    '''
        Convert the 128 bit input into 4 32 bits numbers
        These 4 32 bits numbers will be considered as different result
    '''
    grp      = list(map(lambda x: int(''.join(x),16), zip(*[iter(inp)]*8)))
    
    return grp


def form_text_file(output_list, key, write_header, count, file_name, file_location):
    """
        Form the txt file for running various tests
    """
    
    if write_header:
        file_reader = open(file_location + file_name, 'w')
        seed = key 
        file_reader.write('#' + '='*66 + '\n')
        file_reader.write('#' + ' genrator AES seed = %s\n'%(seed))
        file_reader.write('#' + '='*66 + '\n' + 'type: b\ncount: %i\nnumbit: 32\n'%(count))
    else:
        file_reader = open(file_location + file_name, 'a')
    
    #print 'Output lsit -> ', output_list

    for line in output_list:
        num_32 = converting_cipher_to_32_bit_number(line)
        for num in num_32:
            file_reader.write(bin(num)[2:].zfill(32) + '\n')

    file_reader.close()

    return 0


if __name__ == "__main__":
    key = '328831e0435a3137f6309807a88da234'
    file_name = 'ctr.txt'
    count = 10
    brk_size = 100

    start = time.time()
    call_main_ctr(count, key, brk_size, file_name)
    stop = time.time()
    print 'Done'
    print 'Time Taken -> %i sec'%(stop-start)
