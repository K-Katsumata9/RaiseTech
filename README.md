# RaiseTech AWSコース
|  ファイル  |  課題内容  |
| ---- | ---- |
|  [lecture02](lecture02/lecture02.md)  |  Gitの概要とターミナルとの連携  |
|  [lecture03](lecture03/lecture03.md)  |  Cloud9上での[サンプルアプリーケーション](https://github.com/yuta-ushijima/raisetech-live8-sample-app.git)のデプロイ  |
|  [lecture04](lecture04/lecture04.md)  |  マネジメントコンソール上で{VPC[SG・サブネット]・EC2・RDS}の環境構築を行い、EC2からRDSの接続可否を実施  |
|  [lecture05](lecture05/lecture05.md)  |  Lecture04にて構築した環境上で[サンプルアプリーケーション](https://github.com/yuta-ushijima/raisetech-live8-sample-app.git)のデプロイを実施。組み込みサーバー(Puma)で起動確認後に、Webサーバー(Nginx)&APサーバー(Unicorn)に分けて起動。正常動作確認後にALBを追加して、アプリケーションの画像の保存先をS3に変更。  |
|  [lecture06](lecture06/lecture06.md)  |  CloudTrailとCloudWatchの概要について学習して、異常発生時にメールに通知が来るように設定。  |
|  [lecture07](lecture07/lecture07.md)  |  現在の構成での負荷対策や脆弱性についての考察  |
|  [lecture10](lecture10/lecture10.md)  |  CloudFormationにてLecture05と同じ環境構築を実施。  |
|  [lecture11](lecture11/lecture11.md)  |  AnsibleでEC2に対して環境構築を行い、自動テスト(ServerSpec)を実施。  |
|  [lecture12](lecture12/lecture12.md)  |  GitHubのリポジトリにCircleCIを組み込み、ジョブ(Cfn-lint)が成功することを確認。  |
|  [lecture13](lecture13/lecture13.md)  |  CircleCIで、Cloudformation → Ansible → ServerSpecをノンストップで稼働するように実装  |
### Lecture13構成図
![lecture15](/diagram.png)
