楽天銀行のハッピープログラム対象の公営競技に自動入金/出金をするだけのプログラムです

## 動作確認環境
 - Windows10 + Python3.7(Anaconda)
 - ubuntu 16.04(server) + Python3.7(Anaconda)

## 準備
### 登録するもの
- 楽天銀行(口座開設しましょう。いくらか口座にお金入れときましょう)
- 楽天銀行のハッピープログラム対象の公営競技(楽天銀行と口座連携すること)
  - [楽天競馬](https://keiba.rakuten.co.jp/)
    - 楽天競馬のみ自動精算サービスがあるのでプログラムでの清算は実施してません。マイページ→会員情報より設定しましょう
  - [オートレース](https://pc.autoinet.jp/)
  - [ボートレース](https://ib.mbrace.or.jp/)
  - [チャリロト](https://www.chariloto.com/)
  - [e-SHINBUN BET](https://bet.e-shinbun.net/)
  - [競輪](https://keirin.jp/pc/login)
  - [オッズパーク](https://www.oddspark.com)
  - [SPAT4](https://www.spat4.jp/keiba/pc)
### インストールするもの
- python3.7
  - Anaconda入れました。インストール方法は割愛  
  ubuntuにAnacondaインストールした時のパス設定とかはうまいことやること
  - Selenium
  - 以下コマンドでインストール
    ~~~
    pip install selenium
    ~~~
- google chrome  
Windowsのインストール手順は割愛  
ubuntuは以下手順にてインストール(rootでやってます)
   ~~~bash
   curl https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
   echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
   apt update
   apt install google-chrome-stable
   ~~~
- Chrome driver  
[ここ](http://chromedriver.chromium.org/downloads)から使用しているChromeのバージョンにあったものをインストール  
pipでもインストール可能な為、作者は以下コマンドからインストールしてます
  ~~~
  pip install chromedriver-binary==76.0.3809.68.0
  ~~~
- python-dotenv  
認証情報を.pyファイルにハードコードしたくないので環境変数ファイル(.env)から読み込む用途でインストール
  ~~~
  pip install python-dotenv
  ~~~
- tesseract
  - OCRソフト。e-SHINBUN BETのみ出金時に画像認証が必要だが、本ソフトで対応可能  
  Windowsは[こちら](https://github.com/UB-Mannheim/tesseract/wiki)からインストーラをDLしてインストールする。パスも通しておくこと。  
  Ubuntuは[公式手順](https://github.com/tesseract-ocr/tesseract/wiki#installation)に従ってインストール
## 準備
- .envファイルの作成  
  - 上記公営競技の認証情報を記述したテキストファイル(`.env`というファイル名で保存する)  
    以下のような形式のファイルを用意する
     ~~~
     RAKUTEN_ID="test@test.com"
     RAKUTEN_PW="hogehoge"
     RAKUTEN_PIN="1234"

     AUTORACE_ID="12345678"
     AUTORACE_PW="absd23"
     AUTORACE_PIN="1234"

     ODDSPARK_ID="huga1234"
     ODDSPARK_PW="hogehoge"
     ODDSPARK_PIN="1234"

     KEIRIN_ID="hugahuga"
     KEIRIN_PW="hoghoge"
     KEIRIN_PIN="1234"

     CHARILOTO_ID="0000123456"
     CHARILOTO_PW="hugahuga"
     CHARILOTO_PIN="1234"

     ESHINBUN_PIN="1234"

     BOATRACE_ID="12345678"
     BOATRACE_PW="hugahuga"
     BOATRACE_VOTE_PW="aaa123"
     BOATRACE_PIN="1234"

     SPAT4_SUBSCRIBER_ID="12345678"
     SPAT4_USER_ID="12345678"
     SPAT4_PIN="1234"
     ~~~

## 実行  
~~~
python main.py
~~~
エラーなく終了すれば入金/出金完了画面のスクリーンショットをscript/resultフォルダに出力します  
エラーが発生した場合も、エラー発生時の画面のスクリーンショットをscript/resultフォルダに出力します 

## 毎日実行する
本プログラムは1回実行すると終了する為、毎日実行するには別途設定が必要になります。
早朝や夜間は入出金できない場合があるので、正午前後に実行するのがおすすめです
- Windowsの場合
  - タスクスケジューラの機能を利用します
- Ubuntuの場合
  - Cronを利用します
