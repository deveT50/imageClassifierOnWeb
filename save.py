#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os
from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory
import inspection

#herokuにファイルを追加で保存する際のフォルダ名（tmp）
UPLOAD_FOLDER = 'tmp/'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

#flaskのおまじない
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#filenameが許可された画像の種類を示す名前かどうかを返す
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#サーバ保存用のファイル名
global g_path

#index.htmlに当たる場所にアクセスした際の処理
@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		#postリクエストがファイル部分を持っているかどうかチェック
		if 'file' not in request.files:
			flash('No file part')
			#なければリダイレクト
			return redirect(request.url)
		
		file = request.files['file']
		#ユーザがファイルを選んでいなければ
		#ブラウザは空のファイル名のないpostをする
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			#secure_filename(セキュリティ上の保護:変な階層にアクセスさせない)
			filename = secure_filename(file.filename)
			#postされたファイルを保存
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			global g_path
			#ファイルを保存した位置を保持
			g_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
			#「ファイル名のURL」に遷移させる
			return redirect(url_for('upload_file',filename=filename))
		#render_template("work.html",srcpath=g_path)
		#htmlを描画する	
	return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><br>
         <input type=submit value=Upload>
    </form>
	<a href="/classify/">classify</a>
    '''

#classifyボタン
@app.route('/classify/')
def classify():
	#画像分類結果を返す
    return inspection.inspect(g_path)

#画面上にはボタンがないが、入力すると画像を表示する
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
#main関数
if __name__ == "__main__":
	#ローカルデバッグ時に使う。
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	#リリース時はこれだけあればOK	
	app.run(host='0.0.0.0', port=port)

