# CHANGELOG.md

## v0.1.0

* Add: DEPOSIT amount
* Add: BALANCE

## v0.2.0

* Add: 複数ユーザー残高管理（dictによる管理）
* Change: 未登録ユーザーの残高は 0 とみなす仕様に対応
* Add: `DEPOSIT user amount` コマンド
* Add: `BALANCE user` コマンド
* Fix: 未登録ユーザー参照時の KeyError を防止

## v0.3.0

* Add: `WITHDRAW user amount` コマンドを追加
* Add: 残高不足時に `INSUFFICIENT` を出力する仕様
* Change: 出金は「残高が amount 以上のときのみ実行」するよう制御
* Fix: 出金失敗時に状態（残高）が変化しないように修正
* Test: 出金成功・失敗・未登録ユーザーを含む examples/03_withdraw を追加

## v0.4.0

* Add: `TRANSFER from_user to_user amount` コマンドを追加
* Add: 送金成功時に送信元・送信先の残高を同時に更新
* Change: 送金は「送信元残高が amount 以上のときのみ実行」する仕様
* Fix: 残高不足・未登録ユーザー時に状態が変化しないよう制御
* Test: 送金成功・失敗・未登録ユーザーを含む examples/04_transfer を追加

## v0.5.0

* Add: 取引履歴管理（history リスト）を追加
* Add: `HISTORY n` コマンドを追加（直近 n 件を新しい順で表示）
* Add: 成功した `DEPOSIT / WITHDRAW / TRANSFER` を履歴に記録
* Change: 失敗した `WITHDRAW / TRANSFER` は履歴に記録しない仕様
* Change: `BALANCE` および `HISTORY` コマンド自体は履歴に残さない
* Test: 履歴表示・失敗操作除外・順序確認を含む examples/05_history を追加
