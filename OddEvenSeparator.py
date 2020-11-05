class OddEvenSeparator:
    def __init__(self):
        self.ch_num = []
        self.notch_num = []

    def add_number(self, number):
        if number % 2 == 0:
            self.ch_num.append(number)
        else:
            self.notch_num.append(number)

    def even(self):
        return self.ch_num

    def odd(self):
        return self.notch_num
