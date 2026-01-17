# docs/spec.md

## Problem 01: 1ユーザー残高管理（DEPOSIT / BALANCE）

### 入力

標準入力から複数行のコマンドが与えられる。各行は以下のいずれか。

* `DEPOSIT amount`

  * `amount` は 0以上の整数
* `BALANCE`

### 出力

`BALANCE` コマンドのたびに、その時点の残高を1行で出力する。

### 状態

* `balance`：残高（整数）

  * 初期値は `0`

### コマンド挙動

* `DEPOSIT amount`

  * `balance += amount`
* `BALANCE`

  * `balance` を出力する
