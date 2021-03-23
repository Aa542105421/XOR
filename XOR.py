import sys

class Crypt:
    def __init__(self,key):
        self.key = key
    def encrypt(self,msg):
        keyList = list(self.key)
        msgList = list(msg)
        keylen = len(keyList)
        msglen = len(msgList)
        ciperText = [''] * msglen
        
        for i in range(msglen):
            ciperText[i] = chr(ord(msgList[i]) ^ ord(keyList[i % keylen]))
        return ''.join(ciperText)

    def decrypt(self,msg):
        print("decrypt hello")
if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) > 2:
        if sys.argv[1] == '-e':
            c = Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3]))

        elif sys.argv[1] == '-d':
            c = Crypt(sys.argv[2])
            print(c.decrypt(sys.argv[3]))
