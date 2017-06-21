'''
    Does the testing of the algos in the src
    Run this if there is a change in the fundamental level
'''

from testing.helping_functions import test_encrypt_decrypt

import time
import sys

def testing_all_algos():
    """
        Run the test_encrypt_decrypt on the list of given_functions
        list_functions consists of encrpyt, dercypt function, iv_size and weather to compile
    """
    from src.main                   import main_encrypt, main_decrypt

    #list_functions = [(main_encrypt, main_decrypt, 0, False), (sta_encrypt, sta_decrypt, 0, False), (modified_encrypt, modified_decrypt, 16, False),  (cython_encrypt, cython_decrypt, 16, False)]#(cpp_encrypt, cpp_decrypt, 0, True), (cpp_encrypt, cpp_decrypt, 0, False),

    #list_functions = [(cython_encrypt, cython_decrypt, 16, False)]
    
    
    name_functions = (main_encrypt, main_decrypt, 0, False)
    
    list_functions = [name_functions]
    start = time.time()
    print 'Testing------'
    for test_function in list_functions:
        result = test_encrypt_decrypt(*test_function)

        if not result:
            print 'Error Here ########### '
            return 0
    stop = time.time()
    print 'End testing-----\nTime Taken %i seconds'%(stop-start)

if __name__ == '__main__':
    testing_all_algos()

