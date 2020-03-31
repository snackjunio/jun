# jun
jun
## ディレクトリ構成
```
.
|--pytest
|  |--input                     ... データベースに投入するテストデータを配置
|     |--...
|  |--output                    ... テスト結果の期待データを配置
|     |--...
|  |--bcn_utils.py              ... 共通関数などをまとめたモジュール
|  |--conftest.py               ... テストデータ投入処理、テスト前後処理などをまとめたモジュール
|  |--test_sql_lib_ana.pyなど   ... pytestモジュール これを実行する
|  |--...
|  |--...
|--config.ini                   ... 設定ファイル
|--README.md                    ... このファイル
|--tox.ini                      ... flake8で無視する項番
```

## 前提
- 以下のpythonモジュールがインストールされている
  - pytest
  - pytest-cov
  - pytest-flake8


## pytest実行の流れ
1. pytestを実行
2. テスト前処理が実行され、指定したテスト対象テーブルが退避される
3. テスト関数ごとに以下を繰り返す
    1. テスト対象テーブルのデータをクリーンする
    2. テスト関数が実行される
4. テスト後処理が実行され、指定したテスト対象テーブルの退避データが復元される


## pytest実行方法
```script
# カレントディレクトリ移動
cd /opt/beacon/test
# 設定ファイル（デフォルトはconfig.ini）を適宜変更する

# デフォルトで設定ファイルはconfig.iniを参照するため
# 指定したい場合は環境変数を設定してから
# テストコードを実行する
export p_conf_name="<設定ファイル名>"

# 全テストコード実行
pytest -v -s --flake8 --cov=.
```

### pytest実行方法の例
```script
# テストモジュールを指定
pytest -v -s --cov=. test_agg_common_function.py

# テストクラスを指定
pytest -v -s --cov=. test_agg_common_function.py::Test_del_dup_rtn

# flake8を実行しない
pytest -v -s--cov=. test_agg_common_function.py

# カバレッジで網羅できなかった行を表示
pytest -v -s --cov=. test_agg_common_function.py --cov-report=term-missing
```


## pytest開発ガイド
- 1つの関数につき、1つのテストクラスを作成する
- 1つのSQL文につき、1つのテストクラスを作成する
- 1つの試験項目につき、1つのテスト関数を作成する
- 1つのテストデータにつき、1つのテストデータ投入fixture関数を作成する
- 1つのpythonモジュールにつき、1つ以上のテストモジュールを作成する
