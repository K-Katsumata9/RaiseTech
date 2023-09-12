# RaiseTech AWSコース
# 第13回講義課題


## CircleCI
### 今回の課題ではローカル環境で３つのジョブが正常に実行されることを確認した後に、環境変数を利用してノンストップでジョブが実行されるように実装しました。
### .circleci/config.ymlにて、cloudformation・ansible・serverspecが実行されるように記述しております。
![lecture13](../lecture13/circleci.png)
## execute-cloudformation
![lecture13](../lecture13/execute-cf.png)
## execute-ansible
![lecture13](../lecture13/execute-ansible.png)
## execute-serverspec
![lecture13](../lecture13/execute-serverspec.png)