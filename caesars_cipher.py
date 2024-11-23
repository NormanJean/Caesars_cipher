import enchant


class CaesarsCipher:
    def __init__(self):
        self.symbols = (
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             "abcdefghijklmnopqrstuvwxyz"
             "1234567890 !?."
        )

    def decrypt(self, message):
        self.__encryption = []
        self.__crypto_key = 0
        for n in range(len(self.symbols) + 1):
            self.__phrase = []
            for i in message:
                if i in self.symbols:
                    index = self.symbols.find(i)
                    index -= n
                    for index in self.symbols[index]:
                        self.__phrase.append(index)
            decrypt_phrases = {n: "".join(self.__phrase)}
            for key in decrypt_phrases.values():
                phrase = key.split(" ")
                counter = 0
                for x in phrase:
                    if x != "":
                        d = enchant.Dict("en_US")
                        if d.check(x) is True:
                            counter += 1
                            if counter > 1:
                                self.__encryption.append(' '.join(phrase))
                                self.__crypto_key = n
                                break

        text1 = f'Фраза расшифрована: {' '.join(self.__encryption)} '
        text2 = f'Ключ к шифру: {self.__crypto_key} '
        print(text1)
        print(text2)
        path_file = input('Укажите путь к папке для записи: ')
        with (open(path_file + '/decryption.txt', 'a', encoding='utf-8')
              as file_path):
            file_path.write(text1)
            file_path.write(text2)

    def encrypt(self, message, key):
        self.__phrase = []
        for i in message:
            if i in self.symbols:
                index = self.symbols.find(i)
                index += key
                if index > 65:
                    index = index - 66
                for index in self.symbols[index]:
                    self.__phrase.append(index)
            encrypt_phrase = "".join(self.__phrase)
        text = f'Фраза зашифрована: {encrypt_phrase} '
        print(text)
        path_file = input('Укажите путь к папке для записи: ')
        with (open(path_file + '/encryption.txt', 'a', encoding='utf-8')
              as file_path):
            file_path.write(text)


if __name__ == "__main__":
    phrase = CaesarsCipher()
    phrase.encrypt("The password to my mailbox is fBIvqX5yjw", 21)
    phrase.decrypt("o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D")
