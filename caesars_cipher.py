import enchant

class CaesarsCipher:
    def __init__(self):
        self.symbols = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.')

    def decrypt(self, message):
        for n in range(len(self.symbols) + 1):
            self.__phrase = []
            for i in message:
                if i in self.symbols:
                    index = self.symbols.find(i)
                    index -= n
                    for index in self.symbols[index]:
                        self.__phrase.append(index)
            decrypt_phrases = {n: ''.join(self.__phrase)}
            for key in decrypt_phrases.values():
                a = key.split(' ')
                counter = 0
                for x in a:
                    if x != '':
                        d = enchant.Dict("en_US")
                        if d.check(x) == True:
                            counter += 1
                            if counter > 1:
                                print(f'Ключ к шифру: {n}')
                                print(f'Расшифрованная фраза: {' '.join(a)}')
                                break


    def encrypt(self, message, key):
        self.__phrase = []
        for i in message:
            if i in self.symbols:
                index = self.symbols.find(i)
                index += key
                if index > 65:
                    index = index - 66
                for index in self.symbols[index]:
                    self.__phrase .append(index)
            encrypt_phrase = ''.join(self.__phrase )
        print(f'Фраза зашифрована: {encrypt_phrase}')


if __name__ == '__main__':
    phrase = CaesarsCipher()
    phrase.encrypt('The password to my mailbox is fBIvqX5yjw', 22)
    phrase.decrypt('p41S!wAAE .zSB S9GS9w58x FS5AS2XeD?tMG6E')
