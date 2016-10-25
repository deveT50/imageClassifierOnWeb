#多クラス分類器（Web）
深層学習を使った多クラス画像分類器をWeb上で利用できるようにする  
（flaskを使用したWebアプリケーションとしてchainerを使用した画像分類プログラムを実行する。Heroku上で。）  
  
主な環境（ローカル）：ubuntu14.04, python2.7, Chainer1.14.0,  
		（Webサーバ）：flask0.10.1, PaaS:Heroku(フリープラン)  


* templates			...flaskが使用するHTMLテンプレートファイルを格納  
	↳	work.html	...htmlテンプレート  
* tmp					...Heroku上に追加でファイルを保存する際のフォルダ  
	↳	.gitkeep	...空のフォルダを残すための.gitkeep。Herokuは空のフォルダを削除する。  
* Procfile			...herokuの設定ファイル。pythonを指定。  
* inspection.py		...chainerで画像分類を実行する  
* labels.txt			...画像分類のクラス名リスト（学習時と同じもの）  
* mean.npy			...画像分類に使用する平均画像（学習時と同じもの）  
* nin.py				...画像分類のアーキテクチャ"nin"（学習時と同じもの）  
* requirements.txt	...Heroku上に追加でインストールするモジュールを記載  
* runtime.txt			...Herokuが使用するpythonのバージョンを指定  
* save.py				...flaskを使用したルーティングのソースコード  
* sigma.npy			...画像分類に使用する学習時の画像の標準偏差（学習時と同じもの）  
* ※modelhdf5			...画像分類に使用するモデルのパラメータファイル（学習時に出力される）  
  
※重たいのでリポジトリに含めていませんが、hdf5形式の学習済みモデルのパラメータファイル"modelhdf5"が必要です。学習はMulticlassImageClassifierとして上げているコードで行いました。  
  
  
ローカルデバッグ：  
端末で、  
python save.py  
を実行するとWebサーバが立ち上がるので、http://0.0.0.0:5000/にアクセスする。  
  
Herokuデプロイ：  
HerokuToolbeltが必要  





