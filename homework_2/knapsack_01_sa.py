# import module
import numpy as np
import random as rn
import matplotlib.pyplot as plt
from execution_logger import ExecutionLogger
from datasets_reader import DatasetReader

class SimulatedAnnealing:
    # 初始化
    def __init__(self, n, weight, profit, capacity):
        self.n = n
        self.weight = weight
        self.profit = profit
        self.capacity = capacity
    
    # 給 execution_logger 執行的 function
    def run(self):
        self.simulated_annealing()

    # 隨機挑選背包的一個位置進行更動
    def transition(self):
        i = rn.randint(0, (self.n) - 1)
        if self.knapsack[i] == 1 :
            self.knapsack[i] = 0
        elif self.knapsack[i] == 0:
            self.knapsack[i] = 1
        return self.knapsack

    # 計算重量及利潤
    def calculate(self):
        p = 0
        w = 0
        for i in range(len(self.knapsack)):
            # 若index value為1，則加入其利潤及重量
            if self.knapsack[i] == 1:
                p += self.profit[i]
                w += self.weight[i]
        # 若重量大於背包容量，利潤為0
        if w > self.capacity:
            p = 0
        return (p,w)

    # 模擬退火演算法
    def simulated_annealing(self):
        temperature = 10000.0 # 起始溫度
        delta = 0.98 # 降溫係數
        count = 0
        best_profit = 0 # 最佳利潤
        self.knapsack = [] # 背包 有放物品 value = 1,沒放物品 value = 0
        count_array = [] # 圖表x軸的陣列(迭代次數)
        profit_array = [] # 圖表y軸的陣列(最佳解)
        rnd = np.random.RandomState(5)

        # 預設背包放滿物品
        for i in range(0, self.n):
            self.knapsack.append(1)

        # 迭代500次
        while count < 500:

            # 隨機挑選背包的一個位置進行更動
            tran_knapsack = self.transition()
            self.knapsack = tran_knapsack # 更換背包

            # 計算當前利潤
            (temp_profit,_) = self.calculate()
            
            # 若當前利潤大於先前利潤則更新背包、利潤
            if temp_profit > best_profit:
                self.knapsack = tran_knapsack
                best_profit = temp_profit
            # 若當前利潤小於先前利潤則進行退火
            else:
                accept_p = np.exp( (temp_profit - best_profit) / temperature ) # 允許機率
                r = rnd.random() # 隨機0-1浮點數

            # 隨機值小於允許機率就進行更新(跳脫區域最佳利潤)
            if r < accept_p:
                self.knapsack = tran_knapsack
                best_profit = temp_profit

            if temperature < 0.01:
                temperature = 0.01
            else:
                temperature *= delta # 降溫
                count += 1
            count_array.append(count + 1)
            profit_array.append(best_profit)

        print("Best_profit:",best_profit)
        
        # 繪製圖表
        plt.plot(count_array,profit_array)
        plt.show()

dataset = DatasetReader().read('p07')
sa = SimulatedAnnealing(len(dataset[0]), dataset[0], dataset[1], dataset[2])
ExecutionLogger().run_sa(sa)