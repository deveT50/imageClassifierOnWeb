#多クラス画像分類器（Web）
深層学習を使った多クラス画像分類器をWeb上で利用できるようにする  
（flaskを使用したWebアプリケーションとしてchainerを使用した画像分類プログラムを実行する。Heroku上で。）  
  
主な環境（ローカル）：ubuntu14.04, python2.7, Chainer1.14.0,  
		（Webサーバ）：flask0.10.1, Chainer1.6.0, PaaS:Heroku(フリープラン)  


* templates			...flaskが使用するHTMLテンプレートファイルを格納  
	↳	work.html		...htmlテンプレート  
* tmp				...Heroku上に追加でファイルを保存する際のフォルダ  
	↳	.gitkeep		...空のフォルダを残すための.gitkeep。Herokuは空のフォルダを削除する。  
* Procfile			...herokuの設定ファイル。pythonを指定。  
* inspection.py			...chainerで画像分類を実行する  
* labels.txt			...画像分類のクラス名リスト（学習時と同じもの）※  
* mean.npy			...画像分類に使用する平均画像（学習時と同じもの）※  
* nin.py			...画像分類のアーキテクチャ"nin"（学習時と同じもの）※  
* requirements.txt		...Heroku上に追加でインストールするモジュールを記載  
* runtime.txt			...Herokuが使用するpythonのバージョンを指定  
* save.py			...flaskを使用したルーティングのソースコード  
* sigma.npy			...画像分類に使用する学習時の画像の標準偏差（学習時と同じもの）※  
* modelhdf5			...画像分類に使用するモデルのパラメータファイル（学習時に出力される）※  
  
※MulticlassImageClassifierとして別途上げているコードで学習を行っています。
  
  
##使用方法
ローカルデバッグ：  
1. 端末で、`$ python save.py`を実行するとWebサーバが立ち上がるので、<http://0.0.0.0:5000/>にアクセスする  
2. [Browse...]ボタンで画像を選択する（リサイズ処理を書いていないので256*256pxの画像を選択して下さい）  
3. [Upload]ボタンで画像をアップロードする  
4. classifyと書かれたリンクをクリックする  
5. 分類結果が表示される  
  
Herokuデプロイ：  
1. Herokuに登録してHerokuToolbeltをインストール  
2. 端末から`$ heroku login`でHerokuにログイン  
3. `$ heroku create`でHerokuにアプリを作成する  
4. `$ git init`で管理対象にする  
5. `$ heroku git:remote -a your-Heroku-AppName`でHerokuAppを紐付け  
6. `$ git add .`, `$ git commit -m "first commit"`, `$ git push heroku master`実行  
7. `$ heroku open`ブラウザでアプリケーションが表示される  
※ ソースを修正する際は6.を繰り返す  
  
##注意
* 学習が上手く行っておらず、分類精度が低い
* Herokuはフリープランでは30分アクセスがないとスリープし、スリープからの復帰時に処理待ちがあります
