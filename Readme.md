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

setup.shを実行

IDを書き換え

自動起動を設定

## CAD
Fusion360を用いて設計した装置のケースのCADデータが入っています。  
3Dプリンターもしくはレーザー加工機で作れるような形状になっています。

## 回路
![IMG20210417144218](https://user-images.githubusercontent.com/41198895/115658147-260ec200-a373-11eb-9d8a-459aab69c589.jpg)