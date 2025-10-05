# AtCoder用のMakefile
# 使用方法: make contest NUM=123

# デフォルトの数字（例: 123）
NUM ?= 123

# コンテスト用のディレクトリとファイルを作成
contest:
	@echo "コンテスト $(NUM) 用のディレクトリとファイルを作成します..."
	@mkdir -p $(NUM)
	@mkdir -p templates
	@if [ ! -f templates/python_template.py ]; then \
		echo "テンプレートファイルが存在しません。作成します..."; \
		echo "# AtCoder用のPythonテンプレート" > templates/python_template.py; \
		echo "# コンテスト番号: CONTEST_NUM" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# よく使う変数の初期化" >> templates/python_template.py; \
		echo "ay, an, G, tr, fa = 'Yes', 'No', {}, True, False" >> templates/python_template.py; \
		echo "flg, cnt, pos, rec = tr, 0, 0, []" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# 入力の読み込み（必要に応じてコメントアウトを外す）" >> templates/python_template.py; \
		echo "# n = int(input())" >> templates/python_template.py; \
		echo "# s = input()" >> templates/python_template.py; \
		echo "# a = list(map(int, input().split()))" >> templates/python_template.py; \
		echo "# lst = [i+1 for i in range(n)]" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# よく使う入力パターン" >> templates/python_template.py; \
		echo "# a = [int(input()) for _ in range(n)]" >> templates/python_template.py; \
		echo "# a = [list(map(int, input().split())) for _ in range(n)]" >> templates/python_template.py; \
		echo "# a = [list(map(int, list(input()))) for _ in range(n)]" >> templates/python_template.py; \
		echo "# x, y = [list(i) for i in zip(*[list(map(int, input().split())) for _ in range(n)])]" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# xy = [list(map(int, input().split())) for _ in range(n)]" >> templates/python_template.py; \
		echo "# x, y = [list(i) for i in zip(*xy)]" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# 文字列処理" >> templates/python_template.py; \
		echo "# for i in range(len(txt)):" >> templates/python_template.py; \
		echo "#     ary.append(list(txt[i]))" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# アルファベット変換" >> templates/python_template.py; \
		echo "# A-Z：65 - 90　a-z：97 - 122　ord/chr" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# デバッグ用" >> templates/python_template.py; \
		echo "# print(\"debug:\", variable_name)" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# メイン処理" >> templates/python_template.py; \
		echo "# ここにコードを書く" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# 出力" >> templates/python_template.py; \
		echo "# print(result)" >> templates/python_template.py; \
	fi
	@sed "s/CONTEST_NUM/$(NUM)/g" templates/python_template.py > $(NUM)/A.py
	@sed "s/CONTEST_NUM/$(NUM)/g" templates/python_template.py > $(NUM)/B.py
	@sed "s/CONTEST_NUM/$(NUM)/g" templates/python_template.py > $(NUM)/C.py
	@echo "✓ ディレクトリ $(NUM)/ を作成しました"
	@echo "✓ $(NUM)/A.py を作成しました（テンプレート適用済み）"
	@echo "✓ $(NUM)/B.py を作成しました（テンプレート適用済み）"
	@echo "✓ $(NUM)/C.py を作成しました（テンプレート適用済み）"
	@echo ""
	@echo "作成されたファイル:"
	@ls -la $(NUM)/

# 特定の数字のコンテスト用ファイルを作成（例: make 123）
%:
	@echo "コンテスト $@ 用のディレクトリとファイルを作成します..."
	@mkdir -p $@
	@mkdir -p templates
	@if [ ! -f templates/python_template.py ]; then \
		echo "テンプレートファイルが存在しません。作成します..."; \
		echo "# AtCoder用のPythonテンプレート" > templates/python_template.py; \
		echo "# コンテスト番号: CONTEST_NUM" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# よく使う変数の初期化" >> templates/python_template.py; \
		echo "ay, an, G, tr, fa = 'Yes', 'No', {}, True, False" >> templates/python_template.py; \
		echo "flg, cnt, pos, rec = tr, 0, 0, []" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# 入力の読み込み（必要に応じてコメントアウトを外す）" >> templates/python_template.py; \
		echo "# n = int(input())" >> templates/python_template.py; \
		echo "# s = input()" >> templates/python_template.py; \
		echo "# a = list(map(int, input().split()))" >> templates/python_template.py; \
		echo "# lst = [i+1 for i in range(n)]" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# よく使う入力パターン" >> templates/python_template.py; \
		echo "# a = [int(input()) for _ in range(n)]" >> templates/python_template.py; \
		echo "# a = [list(map(int, input().split())) for _ in range(n)]" >> templates/python_template.py; \
		echo "# a = [list(map(int, list(input()))) for _ in range(n)]" >> templates/python_template.py; \
		echo "# x, y = [list(i) for i in zip(*[list(map(int, input().split())) for _ in range(n)])]" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# xy = [list(map(int, input().split())) for _ in range(n)]" >> templates/python_template.py; \
		echo "# x, y = [list(i) for i in zip(*xy)]" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# 文字列処理" >> templates/python_template.py; \
		echo "# for i in range(len(txt)):" >> templates/python_template.py; \
		echo "#     ary.append(list(txt[i]))" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# アルファベット変換" >> templates/python_template.py; \
		echo "# A-Z：65 - 90　a-z：97 - 122　ord/chr" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# デバッグ用" >> templates/python_template.py; \
		echo "# print(\"debug:\", variable_name)" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# メイン処理" >> templates/python_template.py; \
		echo "# ここにコードを書く" >> templates/python_template.py; \
		echo "" >> templates/python_template.py; \
		echo "# 出力" >> templates/python_template.py; \
		echo "# print(result)" >> templates/python_template.py; \
	fi
	@sed "s/CONTEST_NUM/$@/g" templates/python_template.py > $@/A.py
	@sed "s/CONTEST_NUM/$@/g" templates/python_template.py > $@/B.py
	@sed "s/CONTEST_NUM/$@/g" templates/python_template.py > $@/C.py
	@echo "✓ ディレクトリ $@/ を作成しました"
	@echo "✓ $@/A.py を作成しました（テンプレート適用済み）"
	@echo "✓ $@/B.py を作成しました（テンプレート適用済み）"
	@echo "✓ $@/C.py を作成しました（テンプレート適用済み）"
	@echo ""
	@echo "作成されたファイル:"
	@ls -la $@/

# 記事を自動生成
article-%:
	@echo "コンテスト $* 用の記事を生成します..."
	@mkdir -p $*
	@echo "# [ABC$*] ABC $*(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)" > $*/article.md
	@echo "" >> $*/article.md
	@echo "#### 合計回答時間：分" >> $*/article.md
	@echo "# A問題" >> $*/article.md
	@echo "### 自分の回答" >> $*/article.md
	@echo "かかった時間：分" >> $*/article.md
	@echo '```python' >> $*/article.md
	@if [ -f $*/A.py ]; then cat $*/A.py >> $*/article.md; else echo "# A.py のコードをここに貼り付けてください" >> $*/article.md; fi
	@echo '```' >> $*/article.md
	@echo "" >> $*/article.md
	@echo "### 終了後考えた最適な回答" >> $*/article.md
	@echo '```python' >> $*/article.md
	@echo "" >> $*/article.md
	@echo '```' >> $*/article.md
	@echo "" >> $*/article.md
	@echo "# B問題" >> $*/article.md
	@echo "### 自分の回答" >> $*/article.md
	@echo "かかった時間：分" >> $*/article.md
	@echo '```python' >> $*/article.md
	@if [ -f $*/B.py ]; then cat $*/B.py >> $*/article.md; else echo "# B.py のコードをここに貼り付けてください" >> $*/article.md; fi
	@echo '```' >> $*/article.md
	@echo "" >> $*/article.md
	@echo "### 終了後考えた最適な回答" >> $*/article.md
	@echo '```python' >> $*/article.md
	@echo "" >> $*/article.md
	@echo '```' >> $*/article.md
	@echo "" >> $*/article.md
	@echo "# C問題" >> $*/article.md
	@echo "### 自分の回答" >> $*/article.md
	@echo "かかった時間：分" >> $*/article.md
	@echo '```python' >> $*/article.md
	@if [ -f $*/C.py ]; then cat $*/C.py >> $*/article.md; else echo "# C.py のコードをここに貼り付けてください" >> $*/article.md; fi
	@echo '```' >> $*/article.md
	@echo "" >> $*/article.md
	@echo "### 終了後考えた最適な回答" >> $*/article.md
	@echo '```python' >> $*/article.md
	@echo "" >> $*/article.md
	@echo '```' >> $*/article.md
	@echo "" >> $*/article.md
	@echo "# 次に向けてやること" >> $*/article.md
	@echo "" >> $*/article.md
	@echo "# 感想" >> $*/article.md
	@echo "" >> $*/article.md
	@echo "# 補足" >> $*/article.md
	@echo "### 関係するリンク(参考文献など)" >> $*/article.md
	@echo "・[今回のコンテスト](https://atcoder.jp/contests/abc$*)" >> $*/article.md
	@echo "" >> $*/article.md
	@echo "#### 回答の正当性は保証できません。ベストエフォート方式です。" >> $*/article.md
	@echo "✓ 記事 $*/article.md を生成しました"
	@echo "✓ コンテスト番号 $* で統一されました"
	@echo "✓ 既存のPythonファイルの内容を自動で貼り付けました"

# テンプレートを更新
update-template:
	@echo "テンプレートファイルを更新します..."
	@mkdir -p templates
	@echo "# AtCoder用のPythonテンプレート" > templates/python_template.py
	@echo "# コンテスト番号: CONTEST_NUM" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# よく使う変数の初期化" >> templates/python_template.py
	@echo "ay, an, G, tr, fa = 'Yes', 'No', {}, True, False" >> templates/python_template.py
	@echo "flg, cnt, pos, rec = tr, 0, 0, []" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# 入力の読み込み（必要に応じてコメントアウトを外す）" >> templates/python_template.py
	@echo "# n = int(input())" >> templates/python_template.py
	@echo "# s = input()" >> templates/python_template.py
	@echo "# a = list(map(int, input().split()))" >> templates/python_template.py
	@echo "# lst = [i+1 for i in range(n)]" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# よく使う入力パターン" >> templates/python_template.py
	@echo "# a = [int(input()) for _ in range(n)]" >> templates/python_template.py
	@echo "# a = [list(map(int, input().split())) for _ in range(n)]" >> templates/python_template.py
	@echo "# a = [list(map(int, list(input()))) for _ in range(n)]" >> templates/python_template.py
	@echo "# x, y = [list(i) for i in zip(*[list(map(int, input().split())) for _ in range(n)])]" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# xy = [list(map(int, input().split())) for _ in range(n)]" >> templates/python_template.py
	@echo "# x, y = [list(i) for i in zip(*xy)]" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# 文字列処理" >> templates/python_template.py
	@echo "# for i in range(len(txt)):" >> templates/python_template.py
	@echo "#     ary.append(list(txt[i]))" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# アルファベット変換" >> templates/python_template.py
	@echo "# A-Z：65 - 90　a-z：97 - 122　ord/chr" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# デバッグ用" >> templates/python_template.py
	@echo "# print(\"debug:\", variable_name)" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# メイン処理" >> templates/python_template.py
	@echo "# ここにコードを書く" >> templates/python_template.py
	@echo "" >> templates/python_template.py
	@echo "# 出力" >> templates/python_template.py
	@echo "# print(result)" >> templates/python_template.py
	@echo "✓ テンプレートファイルを更新しました"

# ヘルプを表示
help:
	@echo "AtCoder用のMakefile"
	@echo ""
	@echo "使用方法:"
	@echo "  make contest NUM=123    # コンテスト123用のファイルを作成"
	@echo "  make 123               # コンテスト123用のファイルを作成（短縮形）"
	@echo "  make article-123       # コンテスト123用の記事を自動生成"
	@echo "  make update-template   # テンプレートファイルを更新"
	@echo "  make help              # このヘルプを表示"
	@echo ""
	@echo "例:"
	@echo "  make 456               # コンテスト456用のファイルを作成"
	@echo "  make contest NUM=789   # コンテスト789用のファイルを作成"
	@echo "  make article-422       # コンテスト422用の記事を自動生成"
	@echo "  make update-template   # テンプレートを最新版に更新"

# デフォルトターゲット
.DEFAULT_GOAL := help
