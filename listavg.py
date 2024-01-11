class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()

    def add(self, num):
        self.lst.append(num)

    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        # implement this method
        pass
