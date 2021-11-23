# is_color_alert.py
特定の色の有無で正常異常を判断します。

異常時は物理スイッチの状態をもとに  
・アラート音  
・IFTTT経由でのスマートプラグOFFもしくはSwitchBot経由でスイッチ付きプラグOFF  
ができるようになっています。

## 動作確認済み環境
- Raspberry Pi 3B
- Raspbian OS

## セットアップ手順
Raspberry Piを起動しこのリポジトリをクローン
```
git clone https://github.com/Myaon/SafetyMachine.git
cd SafetyMachine
```
setup.shを実行
```
bash ./setup.sh
```
MACアドレスを書き換え
```
sudo nano is_color_alert.py
```
86行目のMACアドレスの部分を手持ちのSwitchBotの値に書き換え
```
subprocess.call(['python', '/home/pi/python-host/switchbot.py', 'SwitchBotのMacアドレス', 'Press'])
```

自動起動を設定
```
sudo nano /etc/rc.local
```
ファイルの最後にexit 0とあるので、その手前に起動時に実行したい以下のコマンドを追記。
```
pigpiod
python /home/pi/SafetyMachine/is_color_alert.py
```

## 解説資料
https://docs.google.com/presentation/d/1wn3XUVRSCCsMOj9bJDgt8lTUBzstiMSykOhqORb3o1Q/edit?usp=sharing

## CAD
Fusion360を用いて設計した装置のケースと専用カメラ治具のCADデータが入っています。  
3Dプリンターもしくはレーザー加工機で作れるような形状になっています。

## 回路及び外観
![14178](https://user-images.githubusercontent.com/41198895/116036929-5bcce700-a6a2-11eb-942a-9b1b4a453b2f.jpg)
![14179](https://user-images.githubusercontent.com/41198895/116036965-6a1b0300-a6a2-11eb-81db-51e4d3d14671.jpg)
