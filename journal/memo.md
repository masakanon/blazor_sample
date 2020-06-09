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
    * ひとまずwwwrootのindex.htmlは最低限のものにした
* リポジトリ管理はどこまでする必要があるか
    * bin,obj,Propertiesは含めない

* その他メモ
    * 20200609で使ったgit操作
        * developで修正してmasterをcheckoutして
        ```
        git merge develop
        ```
        * deleteコミットの反映
        ```
        git add . --update
        ```
        * featureブランチを別ブランチにまとめる
        ```
        git merge --squash
        ```
        * ローカルブランチ（マージ済）の削除
        ```
        git branch -d {branch}
        ```
        * ローカルブランチ（未マージ）の削除
        ```
        git branch -D {branch}
        ```
        * リモートブランチの削除
        ```
         git push --delete origin {branch}
        ```