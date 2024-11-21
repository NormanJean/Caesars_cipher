class CaesarsCipher:
    def __init__(self):
        self.code_symbols = ('''ABCDEFGHIJKLMNOPQRSTUVWXYZ
                             abcdefghijklmnopqrstuvwxyz1234567890 !?.''')

    def decrypt(self, message_decrypt):
        pass

    def encrypt(self, message_encrypt):
        print(self, message_encrypt)


if __name__ == '__main__':
    phrase = CaesarsCipher
    phrase.encrypt(5,'Hello, world!')
