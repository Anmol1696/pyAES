"""
    Implementation of the AES algorithm in pyhton

    The main Class for the Aes doing all the calculations and steps
"""

from tables import *

def print_node(node):
    '''
        This function given a 4x4 table consisting of key, plain, cipher prints in the Hex form
    '''
    print '\n'
    for i in range(4):
        print [hex(node[i][j])[2:].zfill(2) for j in range(4)]
    print '\n'

class AesClass:

    def __init__(self,a):
        self.key = []
        self.do = a
        self.encrypt = ''
        self.decrypt = ''
        self.number = 0
        self.node = []

    #plain text is hexadecimal, converting to node
    def hex_text_node(self, inp):
        hex_inp = [inp[i] + inp[i+1] for i in range(0,len(inp),2)]
        noder = len(hex_inp)/16
        self.number = noder
        box = [0 for x in range(noder)]
        for u in range(noder):
            temp = [[0 for x in range(4)]for x in range(4)]
            for v in range(16):
                q = 0
                if len(hex_inp) > (u*16) + v: q = int(hex_inp[(u*16)+v], 16)
                temp[v/4][v%4] = q
            box[u] = temp
            
            #Testing
            #print 'Plain Node -> '
            #print temp
            #print_node(temp)

        self.node = box

    # Plain text to node
    def text_node(self,inp):
        noder = len(inp)/16 + 1
        self.number = noder
        box = [0 for x in range(noder)]
        for u in range(noder):
            temp = [[0 for x in range(4)]for x in range(4)]
            for v in range(16):
                q = 0
                if len(inp) > (u*16)+v: q = ord(inp[(u*16)+v])
                temp[v/4][v%4] = q
            box[u] = temp
        self.node = box

    # Cipher text hex to node
    def hex_cipher_node(self, a):
        noder = len(a)/32
        hex_a = [a[i]+a[i+1] for i in range(0, len(a), 2)]
        self.number = noder
        box = [0 for x in range(noder)]
        for u in range(noder):
            temp = [[0 for x in range(4)]for x in range(4)]
            for v in range(16):
                q = 0
                if len(hex_a) > (u*16) + v: q = int(hex_a[(u*16)+v], 16)
                temp[v/4][v%4] = q
            box[u] = temp
        self.node = box


    # Cipher text to node
    def cipher_node(self,a):
        noder = len(a)/22
        self.number = noder
        box = [0 for x in range(noder)]
        for o in range(0,len(a),22):
            Bin = []
            fin = []
            temp = [[0 for x in range(4)]for x in range(4)]
            for t in range(22):
                for i in range(5,-1,-1):
                    q = 0
                    if (((ord(a[o+t])-32)>>i)%2==1): q=1
                    Bin.append(q)
            for t in range(4): del Bin[-1]
            for e in range(0,128,8):
                w = 0
                for q in range(8):
                    w+=(pow(2,7-q)*Bin[e+q])
                fin.append(w)
            for u in range(16):
                temp[u/4][u%4] = fin[u]
            box[o/22] = temp
        self.node = box

    # key hex to node
    def hex_key_node(self, a):
        hex_a = [a[i]+a[i+1] for i in range(0,len(a),2)]
        keytemp = [0 for x in range(11)]
        keytemp[0] = [[int(hex_a[i], 16) for i in range(x,4+x)]for x in range(0,16,4)]
        self.key = keytemp

        #Testing
        #print 'Key to Node ->'
        #print_node(keytemp[0])

    # key to node
    def key_node(self,a):
        key_pad = ')!(@*#&$%^<+*/>?'
        for x in range(0,16-len(a)) :   a += key_pad[x]
        keytemp = [0 for x in range(11)]
        keytemp[0] = [[(ord(a[i])^ord(key_pad[i])) for i in range(0+x,4+x)]for x in range(0,16,4)]
        self.key = keytemp

    # making of the Round keys
    def Roundkeys(self):

        for rnd  in range(10) :
            coltemp = [self.key[rnd][x][0] for x in range(4)]
            colcur = [self.key[rnd][x][3] for x in range(4)]
            (colcur[0],colcur[1],colcur[2],colcur[3]) = (colcur[1],colcur[2],colcur[3],colcur[0])

            for x in range(4):
                r = (colcur[x]>>4) & 0x0F
                c = (colcur[x]>>0) & 0x0F
                colcur[x] = S_box[r][c]
                colcur[x] = (coltemp[x]^colcur[x]^Rcon[rnd][x])
            tempkey = [[0 for x in range(4)]for x in range(4)]

            for i in range(4): tempkey[i][0] = colcur[i]

            self.key[rnd+1] = tempkey
            for j in range(1,4):
                for i in range(4):
                    coltemp[i] = self.key[rnd][i][j]
                    colcur[i] = self.key[rnd+1][i][j-1]
                    colcur[i] = coltemp[i]^colcur[i]
                    self.key[rnd+1][i][j] = colcur[i]

        #Testing
        #print 'Key Testing -> '
        #for rnd in range(11):
        #    print 'Key Round -> ', rnd
        #    print_node(self.key[rnd])

    def _reverse_keys(self):
        (self.key[0],self.key[1],self.key[2],self.key[3],self.key[4],self.key[5],self.key[6],self.key[7],self.key[8],self.key[9],self.key[10])\
            = (self.key[10],self.key[9],self.key[8],self.key[7],self.key[6],self.key[5],self.key[4],self.key[3],self.key[2],self.key[1],self.key[0])

    def _sbox_substitution(self, repetation, inverse = False):
        for i in range(4):
            for j in range(4):
                r = (self.node[repetation][i][j]>>4)&0x0F
                c = (self.node[repetation][i][j]>>0)&0x0F
                if inverse: self.node[repetation][i][j] = inS_box[r][c]
                else: self.node[repetation][i][j] = S_box[r][c]

    def _shift_rows(self, repetation, inverse = False):
        if inverse: num = 3
        else: num = 1
        for i in range(1,4):
            for u in range(i*num):
                for j in range(3):
                    (self.node[repetation][i][j],self.node[repetation][i][j+1]) = (self.node[repetation][i][j+1],self.node[repetation][i][j])

    def _mix_columns(self, repetation, inverse = False):
        for j in range(4):
            coltemp = [self.node[repetation][i][j] for i in range(4)]
            if inverse:
                col = [table_14[coltemp[0]]^table_11[coltemp[1]]^table_13[coltemp[2]]^table_9[coltemp[3]],\
                    table_9[coltemp[0]]^table_14[coltemp[1]]^table_11[coltemp[2]]^table_13[coltemp[3]],\
                    table_13[coltemp[0]]^table_9[coltemp[1]]^table_14[coltemp[2]]^table_11[coltemp[3]],\
                    table_11[coltemp[0]]^table_13[coltemp[1]]^table_9[coltemp[2]]^table_14[coltemp[3]]]

            else:
                col = [table_2[coltemp[0]]^table_3[coltemp[1]]^coltemp[2]^coltemp[3],\
                coltemp[0]^table_2[coltemp[1]]^table_3[coltemp[2]]^coltemp[3],\
                coltemp[0]^coltemp[1]^table_2[coltemp[2]]^table_3[coltemp[3]],\
                table_3[coltemp[0]]^coltemp[1]^coltemp[2]^table_2[coltemp[3]]]

            for i in range(4):
                self.node[repetation][i][j] = col[i]

    def _add_round_keys(self, repetation, num_round):
        for j in range(4):
            for i in range(4):
                self.node[repetation][j][i] = self.node[repetation][j][i]^self.key[num_round][j][i]

    # hex is true if the the plain and cipher text are in hex
    def MainRounds(self, is_hex=True):
        # Tables
        if self.do == '0':
            for rep in range(self.number):
                for rnd in range(11):
                    if rnd > 0:
                        self._sbox_substitution(rep)

                        #Testing
                        #print 'After sbox, Round -> ', rnd
                        #print_node(self.node[rep])

                        self._shift_rows(rep)

                        #Testing
                        #print 'After shift row, Round -> ', rnd
                        #print_node(self.node[rep])

                        if rnd < 10:
                            self._mix_columns(rep)

                            #Testing
                            #print 'After Mix Col, Round -> ', rnd
                            #print_node(self.node[rep])

                    self._add_round_keys(rep, rnd)

                    #Testing
                    #print 'After Add Round Key, Round -> ', rnd
                    #print_node(self.node[rep])

        else :
            self._reverse_keys()
            for rep in range(self.number):
                for rnd in range(11):
                    if rnd > 0:
                        self._shift_rows(rep, True)

                        self._sbox_substitution(rep, True)

                    self._add_round_keys(rep, rnd)

                    if rnd<10 and rnd>0:
                        self._mix_columns(rep, True)

                    if rnd == 10:
                        for i in range(4):
                            for j in range(4):
                                if not is_hex:
                                    a = chr(self.node[rep][i][j])
                                else:
                                    a = hex(self.node[rep][i][j])[2:].zfill(2)
                                self.decrypt += a

    def hex_encrypt(self):
        for rep in range(self.number):
            for i in range(4):
                for j in range(4):
                    a = hex(self.node[rep][i][j])[2:].zfill(2)
                    self.encrypt += a

    def binary_6(self):
        for rep in range(self.number):
            Bin = []
            rare = [' ' for x in range(22)]
            for x in range(4):
                for y in range(4):
                    for i in range(7,-1,-1):
                        if ((self.node[rep][x][y]>>i)%2==1) : q=1
                        else : q=0
                        Bin.append(q)
            for x in range(4): Bin.append(0)
            for i in range(0,132,6):
                a = 0
                for q in range(6): a += (pow(2,5-q)*Bin[q+i])
                rare[i/6] = chr(a+32)
            for u in range(22): self.encrypt += rare[u]

    def Decrypted(self):
        return self.decrypt

    def Encrypted(self):
        return self.encrypt
