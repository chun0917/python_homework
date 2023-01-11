# import module
import random as rn
from execution_logger import ExecutionLogger
from datasets_reader import DatasetReader

class HillClimbing:
    # 初始化
    def __init__(self, n, weight, profit, capacity):
        self.n = n
        self.weight = weight
        self.profit = profit
        self.capacity = capacity

    # 給 execution_logger 執行的 function
    def run(self):
        self.best_profit = 0
        self.total_weight = 0
        self.knapsack = [] # 背包 有放物品 value = 1,沒放物品 value = 0
        self.get_random_solution()

        # 預設背包未放物品
        for i in range(0, self.n):
            self.knapsack.append(0)

        # 若背包總重量未超過背包容量，則加總隨機解中的物品重量及利潤
        for item in self.solution:
            if self.total_weight + self.weight[item['index']] <= self.capacity:
                self.best_profit += self.profit[item['index']]
                self.total_weight += self.weight[item['index']]
                self.knapsack[item['index']] = 1

    # 生成隨機解
    def get_random_solution(self):
        all_items = list(range(self.n))
        self.solution = []
        for i in range(self.n):
            random_item = all_items[rn.randint(0,len(all_items)-1)]
            # 將物品的 index 及其在 dataset 中代表的利潤加入隨機解陣列中
            self.solution.append({
                "index":random_item,
                "profit":self.profit[i]
            })
            # 從所有物品中移除已加入陣列的物品
            all_items.remove(random_item)
        return self.solution

dataset = DatasetReader().read('p07')
hc = HillClimbing(len(dataset[0]), dataset[0], dataset[1], dataset[2])
ExecutionLogger().run_hc(hc)