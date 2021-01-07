# NumberSlangTranslate 


---
機能説明
---

ROSのトピック通信を使用する．

キーボードから入力したナンバースラングをパブリッシャのノードでメッセージとして送信する．サブスクライバのノードでメッセージを受信後，そのスラングの意味を標準出力に出力する．


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

1. ROSのワークスペースにパッケージをクローンする
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/karata-sc/NumberSlangTranslate.git
```

2. パッケージをビルドする
```
$ cd ../
$ catkin_make
$ source ~/catkin_ws/devel/setup.bash
```

3. `roscore` を実行する

```
$ roscore
```

4. 新規ターミナルを起動しパブリッシャを実行する

```
$ rosrun mypkg slang_pub.py
input slang:
```

5. 新規ターミナルを起動しサブスクライバを実行する

```
$ rosrun mypkg slang_sub.py
```

6. パブリッシャを実行したターミナルでナンバースラングを入力する

```
$ input slang: 143
```

サブスクライバを実行したターミナルに翻訳されたスラングが出力される

```
[INFO] [1609079136.484591]: 143
>> I love you
```




---
動画
---
* https://youtu.be/qL7nhUr3ohE


---
参考
---
* ロボットシステム学第10回（ROS）(https://youtu.be/PL85Pw_zQH0)最終閲覧日：2020/12/27) 
* 小倉崇(2015)．『ROSではじめるロボットプログラミング』．工学社



