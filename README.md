# RaiseTech AWSコース課題

## Lecture02
### Gitの概要について学習して、ターミナルとの連携を実施
## Lecture03
### Cloud9上でサンプルアプリーケーション(https://github.com/yuta-ushijima/raisetech-live8-sample-app.git)のデプロイ
## Lecture04
### マネジメントコンソール上で{VPC[SG・サブネット]・EC2・RDS}の環境構築を行い、EC2からRDSの接続可否を実施
## Lecture05
### Lecture04にて構築した環境上でサンプルアプリケーションのデプロイを実施。組み込みサーバー(Puma)で起動確認後に、Webサーバー(Nginx)&APサーバー(Unicorn)に分けて起動。正常動作確認後にALBを追加して、アプリケーションの画像の保存先をS3に変更。
## Lecture06
### CloudTrailとCloudWatchの概要について学習して、異常発生時にメールに通知が来るように設定。
### 自身のAWS料金の確認を行い、AWSPricingCalculatorにてLecture05の環境の見積もりを作成。
## Lecture10
### CloudFormationにてLecture05と同じ環境構築を実施。
## Lecture11
### AnsibleでEC2に対して環境構築を行い、自動テスト(ServerSpec)を実施。
## Lecture12
### GitHubのリポジトリにCircleCIを組み込み、ジョブ(Cfn-lint)が成功することを確認。
## Lecture13
### CircleCIにてCloudformation・Ansible・ServerSpecのそれぞれのジョブが成功することを確認。
### 現在、上記の3ジョブをノンストップで稼働するよう編集中。