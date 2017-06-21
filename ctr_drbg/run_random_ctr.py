"""
    Form the data files for a bunch of random input features
"""

from ctr_drbg.ctr               import call_main_ctr
from testing.helping_functions  import form_random_hex

import time
import sys
import json

def forming_data(irr_poly, number_of_files, length_data, file_location):
    """
        This forms the data files with random input features for given algo
    """
    start = time.time()
    for i in range(number_of_files):
        key, iv, nonce, plain_text = map(form_random_hex, [32,16,16,32])
        
        brk_size = 100000
        file_name = 'ctr_data_%s_%i.txt'%(irr_poly, i)
        
        call_main_ctr(length_data, key, brk_size, file_name, iv=iv, nonce=nonce, file_location=file_location)
    stop = time.time()
    print 'Done with AES'
    print 'Time Taken %i seconds'%(stop-start)


def read_input_from_json(irr_poly, json_file_name):
    """
        Read the input to forming_data function from a json file
    """
    with open(json_file_name) as json_file:
        json_data = json.load(json_file)
    
    forming_data(irr_poly, json_data['number_of_files'], json_data['count'], json_data['file_location'])

if __name__ == '__main__':
    """
    count           = 2500000
    number_of_files = 5
    file_location   = '/root/Documents/Git/Crypto/AES_modification/data/run_2/'

    #whcih_aes can be 'my_aes', 'modified_iv', 'sta'
    #which_aes       = ['modified_iv', 'my_aes', 'sta']
    which_aes       = ['cython_aes', 'sta']
    print 'AES -> ', which_aes
    #pool.map(lambda aes: forming_data(number_of_files, count, aes, file_location), which_aes)

    for aes in which_aes:
        forming_data(number_of_files, count, aes, file_location)
    """
    json_file_name = sys.argv[1]
    irr_poly = 433
    read_input_from_json(irr_poly, json_file_name)
