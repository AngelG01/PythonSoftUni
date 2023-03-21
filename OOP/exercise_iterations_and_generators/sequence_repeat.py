class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.end == self.number:
            raise StopIteration

        if self.index == len(self.sequence):
            self.index = 0
        self.end += 1
        return self.sequence[self.index]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
