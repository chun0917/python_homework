import matplotlib.pyplot as plt

class ExecutionLogger:
    def __init__(self):
        self

    def run_hc(self, solver):
        init_profit = 1440 #預設初始利潤為 1440
        count_array = [] # 圖表x軸的陣列(迭代次數)
        profit_array = [] # 圖表y軸的陣列(最佳解)
        # 迭代 500 次
        for i in range(500):
            solver.run()
            count_array.append(i + 1)
            profit_array.append(init_profit)
            # 若最佳解大於當前最佳解則取代
            if init_profit < solver.best_profit:
                init_profit = solver.best_profit
                print("Solution: %s" % solver.knapsack)
                print("Total weight: %s" % solver.total_weight)
                print("Best profit: %s" % init_profit)
        # 繪製圖表
        plt.plot(count_array,profit_array)
        plt.show()

    def run_sa(self,solver):
        solver.run()