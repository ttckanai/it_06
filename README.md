# IT技術 第6回

AWS Lambda での Python のクラウド実行

## 作業手順

### 事前準備

```bash
mkdir package
conda create -n lambda_janome python=3.10
conda activate lambda_janome
pip install janome -t ./package
code ./package/lambda_function.py
code ./package/util.py
```

### シンプルな関数

* lambda関数の作成
  * lambda_janome_test
  * Python 3.10
  * 関数の作成
* 設定
  * 設定
  * 一般設定
  * 編集
  * メモリ：1024
  * タイムアウト：1分
* デプロイ
  * アップロード元
  * zipファイル
  * ドラッグ&ドロップ
  * 保存
* テスト
  * 「テスト」タブ
  * 「テスト」ボタン
    * 実行中の関数：成功
  * 「詳細」

### Web API

* Lambda
  * Lambda関数の作成
    * lambda_janome_api
    * python3.10
    * 関数の作成
  * 設定
    * 設定
    * 一般設定
    * 編集
    * メモリ：1024
    * タイムアウト：1分
  * トリガーを追加
    * API Gateway
    * 新規のAPIを作成
    * REST API
    * セキュリティ：APIキー
  * デプロイ
    * 「コード」タブ
    * アップロード元
    * zipファイル
    * ドラッグ&ドロップ
    * 保存
  * テスト
    * 「テスト」タブ
    * イベント名：API_query
    * テンプレート：API Gateway AWS Proxy
      * 8行目
        * "text":"明日は明日の風が吹く。"
    * 「保存」ボタン
    * 「テスト」ボタン
      * 実行中の関数：成功
    * 「詳細」
* API Gateway
  * 「設定」タブの「トリガー」
  * API Gatewayの「詳細」
  * 「APIエンドポイント」と「APIキー」をコピー

### バッチ処理

* S3
  * バケットを作成
    * バケット名：lambda-functions-ttckanai
* DynamoDB
  * テーブルの作成
    * テーブル名 : ChatHistory
    * パーティションキー : Username
    * ソートキー : Tag
  * データ登録
    * (作ったテーブルを選択)
    * 「アクション」
    * 「項目を作成」
      * UserId : kanai
      * ArticleId : 1
      * 「新しい属性の追加」 : 文字列
      * 属性名 : 「NewValue」→「Text」
      * 値 : Lambda関数を使うとPythonをクラウドで簡単に実行できます。
      * 「項目を作成」
    * あといくつか作る
* Lambda
  * 新しい関数の作成
    * 関数名 : lambda_janome_batch
    * ランタイム : Python3.10
    * デフォルトの実行ロールの変更
      * ロール名 : lambda_janome_dynamo
      * ポリシーテンプレート : シンプルなマイクロサービスのアクセス権限（DynamoDB で検索）
  * 設定
    * 設定
    * 一般設定
      * 編集
      * メモリ：1024
      * タイムアウト：1分
    * アクセス権限
      * ロール名
      * 許可を追加
      * ポリシーをアタッチ
      * 「s3」で検索 : AmazonS3FullAccess
      * 「許可を追加」
  * デプロイ
    * 「コード」タブ
    * アップロード元
    * zipファイル
    * ドラッグ&ドロップ
    * 保存
  * テスト
    * 「テスト」タブ
    * 「テスト」
    * S3を見に行く
  * トリガー
    * トリガーを追加
    * EventBridge
    * 新規のルールを作成
      * ルール名 : lambda_batch_test
      * スケジュール式
        * rate(1 minute)
  * S3を見に行く

### 使用後のリソースの削除

* Lambda
* API Gateway
* Dynamo DB
* S3
* Event Bridge
* IAM(気になれば)
