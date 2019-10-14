class employees():
    _list = []
    _edit = []
    def __init__(self, _count):
        for i in range(_count):
            self.insert()
    def insert(self):
        self._list.append([
            input("Введите ФИО: "),
            input("Введите табельный номер: "),
            float(input("Введите размер оклада: ")),
            int(input("Введите категорию: "))
        ])
    def calculate(self):
        for value in self._list:
            self._edit.append([
                value[0],
                value[1],
                value[2] + 3000 if value[3] == 1 else value[2],
                value[3]
            ])
    def showOrigin(self):
        return self._list
    def showCalculated(self):
        if (len(self._edit) != 0):
            return self._edit
        else:
            self.calculate()
            return self._edit

_empls = employees(int(input("Введите количество работников: ")))
print(_empls.showOrigin())
print(_empls.showCalculated())