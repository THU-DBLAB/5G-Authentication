#xor
def xor(x, y): #x = 0 or 1(str), y = 0 or 1(str)
    _xormap = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}
    return ''.join([_xormap[a, b] for a, b in zip(x, y)])
#print(xor("11","00"))

#str to bit
def str_to_bit(m): #m = str
    string = m
    binary_converted = ''.join(format(ord(c), 'b').zfill(8) for c in string)
    return binary_converted
#print(str_to_bit("1000000000000001")) #result

#bit to str
def bit_to_str(n): #n = bit(str)
    n = n.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    return ''.join(chr(int(n[i * 8:i * 8 + 8], 2)) for i in range(len(n) // 8))
#print(bit_to_str("01100001")) #result

#bit to hex
def binary_to_hex(binary_str): #binary_str = str
    decimal_number = int(binary_str, 2)
    hex_number = hex(decimal_number)
    return hex_number[2:]

#hash - sha-256
def sha256(t): #t = str
    import hashlib
    hash = hashlib.sha256()
    hash.update(t.encode('utf-8'))
    return (hash.hexdigest())
#print(sha256("n9daily"))

#KDF - hmac-sha-256
def KDF(key, data):
    from hashlib import sha256
    import hmac
    data = data.encode('utf-8')
    #return (hmac.new(key.encode('utf-8'), data, digestmod=sha256).hexdigest().upper()) #大寫
    return (hmac.new(key.encode('utf-8'), data, digestmod=sha256).hexdigest()) #小寫
#print(KDF("0123456789", "n9daily"))

#Algorithm f1
def f1(Key, RAND, AMF, SQN):
    u = "%s%s" %(AMF, SQN) #80bits
    u = str(int(Key)^(int(RAND)^int(u))).zfill(16)
    MAC = str(int(u[0:8])^int(u[8:])).zfill(8)
    return MAC
#print(f1("1000000000000001", "0123456701234567", "10", "010102"))

#Algorithm f1*

#Algorithm f2
def f2(Key, RAND):
    OUT2 = int(Key)^int(RAND)
    OUT2 = str(OUT2).zfill(16)
    RES = OUT2[8:]
    return RES
#print(f2("1000000000000001", "0123456701234567"))

#Algorithm f3
def f3(Key, RAND):
    OUT3 = int(Key)^int(RAND)
    CK = str(OUT3 >> 4).zfill(16)
    return CK
#print(f3("1000000000000001", "0123456701234567"))

#Algorithm f4
def f4(Key, RAND):
    OUT4 = int(Key)^int(RAND)
    IK = str(OUT4 >> 8).zfill(16)
    return IK
#print(f4("1000000000000001", "0123456701234567"))

#Algorithm f5
def f5(Key, RAND):
    OUT2 = int(Key)^int(RAND)
    OUT2 = str(OUT2).zfill(16)
    AK = OUT2[:6]
    return AK
#print(f5("1000000000000001", "0123456701234567"))

#Algorithm f5*