# RaiseTech AWSコース
## 第2回講義内容

### Gitの役割
ローカルリポジトリとリモートリポジトリに分ける
プログラムを変更するということは不具合が起きる可能性が起きるため、
ローカル環境で元データに編集を行ったファイルを作成する。
それを、リモートにアップロードを行い二重確認を行い（自分が行う場合もある）、
問題がなければ、元データに反映させる。

### 今回の作業の流れ
#### GitHubとcoud9の連携
1.git config --global user.name "ユーザーネーム"　GitHub情報の登録
2.git config --global user.email "メールアドレス"　GitHub情報の登録
3.cd ~/.sshでSSHディレクトリへ移動
4.ssh-keygenとcat ~/.ssh/id_rsa.pubを実行して、表示されたSSHキーをGitHubのサイトで設定
#### ファイルのpush
1.githubでリポジトリを作成して、ローカル環境に反映させる(git clone URL)
2.反映されたディレクトリへcdコマンドを使い移動する
3.新しいブランチを作成して移動する(git checkout -b ブランチ名)
4.touchコマンドで、新しいファイルを作成して編集をする
5.git add ファイル名をタインプインして、作成したファイルをコミット対象にする
6.git commit -m "任意の説明"でコミットを行う
7.git push origin ブランチ名でpushを行う
8.githubに移動して、プルリクエスト発行を行う

#### Git-Flowの開発の流れ
#### GitHub-Floeの開発の流れ