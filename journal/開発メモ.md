# 20200609メモ
* MSLearnのClCalcの演習は一通り履修した状態でスタート
* 最小構成で進めたくなったので以下のコマンドで最小のテンプレートをとってきた
```
dotnet new --install Toolbelt.AspNetCore.Blazor.Minimum.Templates::3.2.0
```
* Webサーバー実装を持たないプロジェクトを新規作成（リポジトリ直下なので-oオプションはつけていない）
```
dotnet new blazorwasmmin
```
* リストアできたので試しに実行
```
dotnet run
```
* Welcome to Blazor!のページが表示される
* リポジトリ管理はどこまでする必要があるか
