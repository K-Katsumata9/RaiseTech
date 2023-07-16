# RaiseTech AWSコース
## 第5回講義課題

### Pumaでの起動
![lecture05](../lecture05/puma.png)


### NginxとUnicornでの起動
![lecture05](../lecture05/Nginx＆Unicorn.png)


### ELB経由での起動
![lecture05](../lecture05/Banana.png)


### AWS構成図
![lecture05](../lecture05/diagram.png)


### S3利用
 今回は下記の設定を行い、サンプルアプリケーションの画像の保存先をEC2ではなくS3へとしました。

 config/environments/production.rbをconfig.active_storage.service = :amazonへと変更

 strage.ymlに以下を追加

 	amazon:

	service: S3

	region: ap-northeast-1

	bucket: 作成した自身の「バケット名」を入力

	access_key_id: <%= ENV['AWS_ACCESS_KEY_ID'] %>

	secret_access_key:  <%= ENV['AWS_SECRET_ACCESS_KEY'] %>
	
