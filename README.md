# NumberSlangTranslate 


---
機能説明
---

英語圏では数列で意味を伝えるナンバースラングという文化がある．

今回はROSのトピック通信にその翻訳機能を付与したプログラムを作成した．

以下に実行時の画像を示す．

キーボードから入力したナンバースラングをパブリッシャのノードでメッセージとして送信し，サブスクライバのノードでメッセージを受信後，そのスラングの意味を標準出力に出力する．


![](https://i.gyazo.com/b954dcc9be110eeda8c1ad084bfef7c0.png)


ナンバースラングについては以下のサイトを参考にした．
* https://e-news67.com/number-slang


---
実行環境
---
* Ubuntu 18.04 LTS 
* ROS Melodic


---
使用方法
---
※ワークスペースを含むROSの実行環境は準備出来ているものとする．

1. ROSのワークスペースにパッケージをクローン
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/karata-sc/NumberSlangTranslate.git
```

2. `roscore` を実行

```
$ roscore
```

3. 新規ターミナルを起動しパブリッシャを起動

```
$ rosrun NumberSlangTranslate.git slang_pub.py
input slang:
```

4. 新規ターミナルを起動しサブスクライバを起動

```
$ rosrun NumberSlangTranslate.git slang_sub.py
```

5. パブリッシャを実行したターミナルで任意のナンバースラングを入力

```
$ input slang: 143
```

サブスクライバを実行したターミナルに翻訳されたスラングが出力される．

```
[INFO] [1609079136.484591]: 143
>> I love you
```
定義されていない数列の場合は以下のように出力される．
```
[INFO] [1610028699.154744]: 2
[UNDEFINED]
```



---
動画
---
* https://youtu.be/qL7nhUr3ohE


---
参考文献
---
* ロボットシステム学第10回（ROS）(https://youtu.be/PL85Pw_zQH0)最終閲覧日：2020/12/27) 
* 小倉崇(2015)．『ROSではじめるロボットプログラミング』．工学社



