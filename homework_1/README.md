# homework_1
## 程式流程及作法
1.import module。除了訓練模型基本的tensorflow、keras等，因為需要辨識花卉種類，所以我import了cv2用來對影像進行讀取及縮放，以及sklearn來切割資料集還有encode label等操作。

2.設定資料夾的相對路徑(github內並沒有dataset的資料夾，請至[Kaggle](https://www.kaggle.com/alxmamaev/flowers-recognition)下載並放入此資料夾內。

3.撰寫分類標籤及取得訓練集的function

4.資料前處理，將影像標準化及標籤做One-hot Encoding

5.將資料集分割成訓練集和驗證集(7:3)

6.建立網路模型，我使用到以下幾種網路層：
```
keras.Input：輸入層(輸入影像大小為150x150x3)
layers.Conv2D：卷積層(使用ReLU激活函數，以及3x3大小的kernel)
layers.MaxPool2D：池化層(對特徵圖下採樣)
layers.Flatten：扁平層(特徵圖轉成一維Tensor)
layers.Dropout：Dropout層(每次訓練隨機丟棄50%網路)
layers.Dense：全連接層(隱藏層使用ReLU激活函數，輸出層使用Softmax激活函數)
```

7.訓練網路模型

8.透過matplotlib繪製圖表來評估模型

9.隨機取樣來檢視預測與正解是否符合

10.將隨機取樣的預測及正解可視化

## 心得
剛接觸Python沒多久，這是我第一次訓練模型，途中遇到了很多的問題，從如何讀取圖片、如何切割資料集、架設網路模型及模型優化、將loss、accuracy繪製成圖表，甚至是從測試集中隨機取樣都花了我好大一番心力，在途中我慢上網尋找如何解決遇到的問題，雖然很多資訊並沒有辦法太詳盡的吸收，也不是很清楚網路層的參數為什麼要這樣設，但這個模型是我是到目前為止訓練時間最短且正確率最高的一個(0.7左右)，但是到後面val_loss會升高，可能是我over-fitting那部分沒有處理得很完善。接下來會慢慢參閱書籍或是網路上的資訊，來深入研究有關於模型訓練方面的學問。
