"""
    Collection of helping functions
"""

import time
import random

def form_random_hex(length):
    """
        Form a random string of hex of given length
    """
    hex_rand = '%x' % random.randrange(16**length)
    hex_rand = hex_rand.zfill(length)

    return hex_rand

def test_encrypt_decrypt(encrypt_function, decrypt_function, iv_size, compile_prog):
    '''
        run tests on given fuctions for AES_EBC mode
        iv_size is the size of IV, if no IV than iv_size = 0
    '''

    print 'Starting %s and %s......'%(encrypt_function.__name__, decrypt_function.__name__)

    plain_text_1    = form_random_hex(32)
    plain_text_2    = form_random_hex(32*1024)  #For testing the block fuctions
    key             = form_random_hex(32)
    all_passed      = True

    #print "Plain_text_1 -> ", plain_text_1
    #print "Plain_text_2 -> ", plain_text_2
    #print "Key -> ", key

    if iv_size:
        iv              = form_random_hex(iv_size)
        #print "Iv -> ", iv
        input_feature   = [key, iv]
    else: input_feature = [key]

    # For testing the AES cpp
    if compile_prog:
        input_feature.append(compile_prog)

    try:
        time_1e_start = time.time()
        cipher_text_1   = encrypt_function(plain_text_1, *input_feature)
        #print "Cipher_text_1 -> ", cipher_text_1
        time_1e_stop = time.time()
        cipher_text_2   = encrypt_function(plain_text_2, *input_feature)
        #print "Cipher text 2 -> ", cipher_text_2
        time_2e_stop = time.time()
    except:
        print 'The encrypter is not working'
        return False

    try:
        time_1d_start = time.time()
        de_plain_1  = decrypt_function(cipher_text_1, *input_feature)
        #print "Final text -> ", de_plain_1
        time_1d_stop = time.time()
        de_plain_2  = decrypt_function(cipher_text_2, *input_feature)
        #print "Final text 2 ->", de_plain_2
        time_2d_stop = time.time()
    except:
        print 'The decrypt is not working'
        return False

    if plain_text_1 != de_plain_1:
       all_passed = False
       print 'Single Falied'

    if plain_text_2 != de_plain_2:
        all_passed = False
        print 'Block Not working'

    if all_passed:
        print 'All Test passed'
        print "Time taken for encrypting of size %s  is -> %s  seconds" % (str(len(plain_text_1)), str(time_1e_stop - time_1e_start))

        
        print "Time taken for encrypting of size %s  is -> %s  seconds" % (str(len(plain_text_2)), str(time_2e_stop - time_1e_stop))


        print "Time taken for decrypting of size %s  is -> %s  seconds" % (str(len(plain_text_1)), str(time_1d_stop - time_1d_start))


        print "Time taken for decrypting of size %s  is -> %s  seconds" % (str(len(plain_text_2)), str(time_2d_stop - time_1d_stop))

    return all_passed
