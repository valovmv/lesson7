from abc import abstractmethod

class Clothes:

    def __init__(self, size=0):
        self.size = size

    @abstractmethod
    def cloth_out(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        super(Coat, self).__init__(size)

    def cloth_out(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, size):
        super(Costume, self).__init__(size)

    def cloth_out(self):
        return self.size * 2 + 0.3

    @property
    def size_out(self):
        return self.size

coat = Coat(20)
print(coat.cloth_out())

costume = Costume(10)
print(costume.cloth_out())
print(costume.size_out)
