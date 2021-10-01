# TODO

## 問題文

> 整数閉区間を示すクラス（あるいは構造体）をつくりたい。
> 整数閉区間オブジェクトは下端点と上端点を持ち、文字列表現も返せる
> （例: 下端点 3, 上端点 8 の整数閉区間の文字列表記は "[3,8]"）。
> ただし、上端点より下端点が大きい閉区間を作ることはできない。
> 整数の閉区間は指定した整数を含むかどうかを判定できる。
> また、別の閉区間と等価かどうかや、完全に含まれるかどうかも判定できる。

## 作業をリストアップ

- [x] 整数閉区間を示すクラスをつくる
- [x] オブジェクトは下端点、上端点属性を持つ
- [x] 下端・上端の文字列表現を返すメソッドを持つ
- [ ] ~コンストラクタで区間が適切かをチェックする~
- [x] 整数を受け取り、区間内かどうかチェックするメソッドを持つ
- [x] 別の閉区間オブジェクトと等価かどうかチェックするメソッドを持つ
- [x] 別の閉区間オブジェクトに含まれるかどうかチェックするメソッドを持つ

## 作業方針

- メソッドを作成する場合は、ユニットテストを書く
  - プロパティまではテストをかかない