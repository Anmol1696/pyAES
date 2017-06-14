from aes import *

def main_encrypt(inp,key):
    ob = AesClass('0')
    #ob.text_node(inp)
    ob.hex_text_node(inp)
    #ob.key_node(key)
    ob.hex_key_node(key)
    ob.Roundkeys()
    ob.MainRounds()
    #ob.binary_6()
    ob.hex_encrypt()
    return ob.Encrypted()
	
def main_decrypt(inp,key):
    ob = AesClass('1')
    #ob.cipher_node(inp)
    ob.hex_cipher_node(inp)
    #ob.key_node(key)
    ob.hex_key_node(key)
    ob.Roundkeys()
    ob.MainRounds()
    return ob.Decrypted()

def inverting_inp(text):
    temp = [text[i] + text[i+1] for i in range(0,len(text),2)]
    text = [temp[i] + temp[i+4] + temp[i+8] + temp[i+12] for i in range(4)]
    text = ''.join(text)

    return text

if __name__ == "__main__":
    '''
    w = raw_input('0. for encryption & 1. for decryption : ')
    intput = raw_input('Enter the Text : ')
    key = raw_input('Enter the key : ')
    if w == '0':
        print Main_Encrypt(intput,key)
    else : print Main_Decrypt(intput,key)
    '''

    #Testing
    key = '2b28ab097eaef7cf15d2154f16a6883c'
    inp = '328831e0435a31372b28ab097eaef7cf15d2154f16a6883cf6309807a88da234'
    cip = '951925b549f604129558035b3d2aa478fecce0251bdaa1aeb8c426a9aecb59e3'

    print main_encrypt(inp, key)
    print main_decrypt(cip, key)
