import hashlib
import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class Crypto(object):
    def __init__(self, key):
        self.BLOCK_SIZE = AES.block_size
        self.KEY = hashlib.sha256(key.encode()).digest()
    
    def encrypt(self, input_data):

        input_data = self._pad(input_data)

        #random generator 로 initializing vector 생성
        iv = Random.new().read(AES.block_size)

        #보안성이 강화된 CBC 모드와 iv값, 입력받은 key값으로 cipher 객체 생성
        cipher = AES.new(self.KEY, AES.MODE_CBC, iv)

        #base64로 encoding 진행
        return base64.b64encode(iv + cipher.encrypt(input_data.encode()))
    
    def decrypt(self, enc):
        enc = base64.b64decode(enc)

        #뒤에서부터 block_size만큼 자르면 iv
        iv = enc[:AES.block_size]
        cipher = AES.new(self.KEY, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    #encoding시 block_size 배수만큼의 byte 길이로 변환하기 위하여 padding 진행
    def _pad(self, s):
        return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)

    
    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

def hash_type(message):
    print('\r\r')
    print('hash type(SHA256): ')
    
    x = bytearray(message, encoding="utf-8")
    # print(x)
    m = hashlib.sha256()
    m.update(x)
    e=m.digest()
    print(e)

def aes(message):
    print("\r\r")
    print('cipher type(AES)')
    key = ""

    while(len(key) != 16 and len(key) != 24 and len(key) != 32):
        key = input('key(16/24/32): ')

    cipher = Crypto(key)
    en = cipher.encrypt(message)
    print("\r\r")
    print ('encrypted: ', en)
    de = cipher.decrypt(en)
    print("\r\r")
    print('decrypted: ', de)
    
def rsa(message):
    key_len = int(input("key length(x256, >=1024): "))

    #public, private key 생성
    private_key = RSA.generate(key_len, Random.new().read)
    public_key = private_key.publickey()

    encryptor = PKCS1_OAEP.new(public_key)
    en = encryptor.encrypt(bytearray(message, encoding='utf-8', errors='ignore'))

    print('\r\r')
    print('encrypted: ', en)
    
    decryptor = PKCS1_OAEP.new(private_key)
    de =  decryptor.decrypt(en)
    print('decrypted:', de.decode())


message = input('Original data: ')
hash_type(message)
aes(message)
rsa(message)
