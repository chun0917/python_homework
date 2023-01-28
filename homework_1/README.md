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

## 優化
在先前的模型中，有over-fitting的跡象，因此我使用了ImageDataGenerator來進行影像的前處理，將影像隨機旋轉、縮放、水平翻轉、水平平移、垂直平移，套用在x_train上。並將第一個卷積層的kernel大小設成5x5
### 改善前
![messageImage_1674893792471](https://user-images.githubusercontent.com/65705058/215256524-8aa678fb-af86-41f3-a38c-12853beb2981.jpg)
![image](https://user-images.githubusercontent.com/65705058/215256543-cde32ab7-088f-45a0-a5a4-b213664c6c10.png)
### 改善後
![image](https://user-images.githubusercontent.com/65705058/215256577-994bdc14-cf79-4949-8995-9028d5d9409e.png)
![image](https://user-images.githubusercontent.com/65705058/215256584-afa87aa7-0e2a-4316-943b-9342d6d77611.png)

可以從圖表中看到over-fitting的現象已大幅改善，且train與test的收斂值接近了許多，test的accuracy也提高了。

我還透過混淆矩陣求得tp、tn、fp、fn。
![image](https://user-images.githubusercontent.com/65705058/215258123-ea54f115-493b-482a-8c89-70145a17c809.png)

從上圖可以得知，第i類別的TruePositive為矩陣中(i,i)之值(即對角線元素)，因此利用np.diag即可求出；其FalseNegative之值為橫排總和(sum(axis=1))-TruePositive之值，其FalsePositive之值為縱排總和(sum(axis=0))-TruePositive之值，剩餘部分皆為TrueNegative。
求出tp、tn、fp、fn後，就能帶入公式算出accuracy、precision、recall及f1-score來評估模型，計算出的結果與classification_report的計算結果一致。

## 心得
剛接觸Python沒多久，這是我第一次訓練模型，途中遇到了很多的問題，從如何讀取圖片、如何切割資料集、架設網路模型及模型優化、將loss、accuracy繪製成圖表，甚至是從測試集中隨機取樣都花了我好大一番心力，在途中我慢上網尋找如何解決遇到的問題，雖然很多資訊並沒有辦法太詳盡的吸收，也不是很清楚網路層的參數為什麼要這樣設，但這個模型是我是到目前為止訓練時間最短且正確率最高的一個(0.7左右)，但是到後面val_loss會升高，可能是我over-fitting那部分沒有處理得很完善。接下來會慢慢參閱書籍或是網路上的資訊，來深入研究有關於模型訓練方面的學問(後來才想到google colab有提供免費的GPU，電腦CPU不夠好還一直傻傻的用jupyter notebook執行浪費了好多時間)。
