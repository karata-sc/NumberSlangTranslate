# NumberSlangTranslate 


---
機能説明
---

英語圏では数列で意味を伝えるナンバースラングという文化がある．

（例）I love you : 137

ROSのトピック通信を使用し，PCのキーボードから入力した文章をナンバースラングに翻訳してLEDアレイの点灯で表現するプログラムを作成した．

![](https://i.gyazo.com/e61286e0fb8b94349731b5f11c38a298.gif)

PCのキーボードから入力した文章はパブリッシャのノードでメッセージとして発信され，Raspberry Piのサブスクライバのノードで受信される．

その後ナンバースラングに翻訳され，Raspberry Piに接続された8個のLEDがナンバースラングの１の位から１桁ごとに桁の数字の分だけ点灯する．

（例）I love you : 143 → LED１個点灯，LED４個点灯，LED３個点灯



---
実行環境
---
* ORACLE VM VirtualBox 6.1 (Ubuntu 18.04 LTS Desktop)
* Raspberry Pi 3 model B+  (Ubuntu MATE 18.04 LTS)
* ROS Melodic

以下の図のように，Raspberry PiとLEDを接続する．

![](https://i.gyazo.com/0ef4ae9163ba8614c9089770a8faaee9.png)

![](https://i.gyazo.com/c209de0f59cd3cb7d55deac9a3d7c219.jpg)
---
使用方法
---
※ワークスペースを含むROSの実行環境は準備出来ているものとする．

まず，PC，Raspberry PiともにROSのワークスペースにパッケージをクローンする．
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/karata-sc/NumberSlangTranslate.git
```

PCをROSのMASTERとするため，PCで環境変数を設定しパブリッシャを起動する．
```
$ export ROS_MASTER_URI=http://{PCのマシン名}.local:11311
$ export ROS_HOSTNAME={PCのマシン名}.local
$ roscore &
$ rosrun NumberSlangTranslate.git slang_pub.py
input slang:
```
Raspberry Piでも同様に環境変数を設定し，サブスクライバを起動する．
```
$ export ROS_MASTER_URI=http://{PCのマシン名}.local:11311
$ export ROS_HOSTNAME={Raspberry Piのマシン名}.local
$ rosrun NumberSlangTranslate.git slang_sub.py
```

パブリッシャを起動した端末で指定の文章を入力するとナンバースラングに翻訳され，Raspberry Piに接続された8個のLEDがナンバースラングの１の位から１桁ごとに桁の数字の分だけ点灯する．

プログラム内でナンバースラングが定義されていない文章が入力された場合，エラーとなり以下のようにLEDアレイの光がLED1からLED8まで流れる．

![](https://i.gyazo.com/119df12d78d4beacb690f882f17a56e8.gif)

---
動画
---
* https://youtu.be/lb9jdzhQ4gM

---
参考文献
---
* ロボットシステム学第10回（ROS）(https://youtu.be/PL85Pw_zQH0)最終閲覧日：2020/1/9
* 第26回 Raspberry PiのGPIOを制御する (Python編)│ツール・ラボ（ https://tool-lab.com/raspberrypi-startup-26/ ）最終閲覧日：2020/1/9
* 【ナンバースラング】数字で表す英語のスラング&略語をまとめてみた！ | E-NEWS （ https://e-news67.com/number-slang ） 最終閲覧日：2020/1/9
* 小倉崇(2015)．『ROSではじめるロボットプログラミング』．工学社



