class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.total_sum = 0
        for num in lst:
            self.total_sum += num

    def add(self, num):
        self.lst.append(num)
        self.total_sum += num

    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        scaled_average = round(self.total_sum * 10 / len(self.lst))
        return scaled_average / 10
