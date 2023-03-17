class vowels:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.vowels = 'aeiouyAEIOUY'

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < len(self.text):
            if self.text[self.index] in self.vowels:
                vowel = self.text[self.index]
                self.index += 1
                return vowel
            else:
                self.index += 1
                return self.__next__()
        else:
            raise StopIteration
