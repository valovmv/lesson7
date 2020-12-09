class Org_cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Org_cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells <= other.cells:
            raise ValueError("Отрицательный результат")
        return Org_cell(self.cells - other.cells)

    def __mul__(self, other):
        return Org_cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Org_cell(round(self.cells / other.cells))

    def make_order(self, row):
        ordered = ['*' * row for _ in range(self.cells // row)]
        ordered.append('*' * (self.cells % row))
        return f'\n'.join(ordered)

org1 = Org_cell(7)
org2 = Org_cell(11)
org3 = org1 + org2
org4 = org3 - Org_cell(9)
org5 = org3 * org4
org6 = org5 / org2
print(f'org1: cells({org1.cells})\n{org1.make_order(5)}')
print(f'org2: cells({org2.cells})\n{org2.make_order(5)}')
print(f'org3: cells({org3.cells})\n{org3.make_order(5)}')
print(f'org4: cells({org4.cells})\n{org4.make_order(5)}')
print(f'org5: cells({org5.cells})\n{org5.make_order(5)}')
print(f'org6: cells({org6.cells})\n{org6.make_order(5)}')