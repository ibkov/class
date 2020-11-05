class Balance:
    def __init__(self):
        self.weigh_right = 0
        self.weigh_left = 0

    def add_right(self, weigh_right):
        self.weigh_right += weigh_right

    def add_left(self, weigh_left):
        self.weigh_left += weigh_left

    def result(self):
        if self.weigh_left == self.weigh_right:
            return "="
        elif self.weigh_right > self.weigh_left:
            return "R"
        else:
            return "L"
