# RaiseTech AWSコース
## 第3回講義内容


### サンプルアプリケーションをブラウザ内で起動する
../lecture03.png

### AP サーバーについて調べてみましょう。
 Puma
### AP サーバーの名前とバージョンを確認してみましょう。
 version 5.6.5
### AP サーバーを終了させた場合、引き続きアクセスできますか?結果を確認して、また AP サーバーを起動してください。
 アクセス不可　再起動でアクセス可

### DB サーバーについて調べてみましょう。
 Mysql
### サンプルアプリケーションで使った DB サーバー(DB エンジン)の名前と、今 Cloud9 で動作しているバージョンはいくつか確認してみましょう。
 Mysql  Ver 8.0.32 for Linux on x86_64
### DB サーバーを終了させた場合、引き続きアクセスできますか?
 アクセス不可

### Rails の構成管理ツールの名前は何でしたか?確認してみてください。
 Bundler

### 今回の課題から学んだこと
#### 今回の作業の流れ
 yumのアップデート(sudo yum -y update)  
 mysqlのインストール(sudo yum remove -y mysql-server)  
 mysqlと互換性のあるmariadbを削除(sudo yum remove -y mariadb*)  
 mysqlのローカルインストール(sudo yum localinstall -y $MYSQL_PACKAGE_URL)  
 (sudo yum install -y mysql-community-devel)  
 (sudo yum install -y mysql-community-server)  
 Mysqlサーバーの起動と状態確認　activeならOK (sudo service mysqld start && sudo service mysqld status)  
 mysqlの初期PWを確認(sudo cat /var/log/mysqld.log | grep "temporary password" | awk '{print $13}')  
 mysqlにログイン可能かを確認(mysql -u root -p)    
 念のためmysqlにログイン後にPW変更(ALTER USER 'root'@'localhost' IDENTIFIED BY '*********';)  
 database.yml→password欄に変更したPWを入力    
 データーベースの構築(bundle exec rails db:create)  
 データベースのマイグレーションを行う(bundle exec rails db:migrate)  
 アプリケーションサーバーの起動(bundle exec rails s)  
 「config.hosts << "4d46919b6fce460996df384c5e37b0c0.vfs.cloud9.us-east-2.amazonaws.com」を「development.rb」へ追加  
 ActionView::Template::Error (The asset “application.css” is not present in the asset pipelineというエラーが表示される  
 プリコンパイルの実行（rails tmp:cache:clearとrails assets:precompile）←Qiitaから引用  
 confit配下のproduction.rbのconfig.assets.compile = false を config.assets.compile = trueへ変更  
 再起動を実施(rails s -e production)  