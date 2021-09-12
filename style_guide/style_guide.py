# 変数定義

# correct
x = 1
y = 1
# wrong
xxxx      = 1
y         = 1

# 関数の引数の=にはスペース不要
def complex(real, imag=0.0)
    return magic(r=real, i=imag)

# operatorの周りにスペース一個, operatorにpriorityがある場合はスペースをなくす
x = x + 1
x += 1
x = x*2 - 1
a = x*x + y*y
c = (a+1) * (a-1)

# カンマの後にはスペースをいれる
range(1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)

# カンマの後にかっこがくる場合はスペースは不要
# correct
foo = (0,)

#coorect
FILES = [
    'setup.cfg',
    'toc.ini',
]

# wrong
FILES = ['setup.cfg', 'toc.ini',]

# 行の折り返し
#correct
foo = long_function(var_one, ver_two,
                    var_three, var_func)

foo = long_function(
    var_one, ver_two,
    var_three, var_func)

# wrong
foo = long_function(var_one, ver_two,
    var_three, var_func)

# correct
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# wrong
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

# '\'で区切って改行する

# correct
a = 1000000000000 \
    + 1000000 \
    + 10000 \
    + 100 \

# wrong
a = 1000000000000+ \
    1000000+ \
    10000+ \
    100+ \

# 関数間は二行空ける
def func():
    pass


def func2():
    pass

# 同じクラスのメソッドは二行空ける
class MyClass:
    def __init__(self):
        pass

    def method(self):
        pass

# importの書き方

import os
import sys

from subprocess import Popen, PIPE

# 順番
# 1. Standard library (time, sys)
# 2. Third party (numpy, pandas)
# 3. Our library
# 4. Local library
# それぞれ一行空ける(abc順)

# 基本的にはabsolute import
import mypkg.sibling
from myplg import sibling
from myplg.sibling import example

# コメント
# ・コメントは常に最新にする．コメントとコードの中身が異なるなら，コメントは無い方がまし
# ・なるべく英語で書く．絶対に日本語がわからない人が読むことがないなら英語で書く必要はない
# ・書くときは文章で書くのが望ましい
# ・# のあとに半角スペースを入れる
# ・Docstringは基本的に全てのmodule, function, class, methodにつける(non publicな外からアクセスしない関数には不要)
# ・そのコードが「なにをしているか」より「なぜそう書いたか」の方が有益


# 命名規則(naming convention)
# 変数名や関数(メソッド)名: snake_case 例) balance, image_height
# クラス名: CamelCase 例) Person, MyClass
# モジュールやパッケージ名: なるべく短いlower caseで，必要であればsnake_case 例) time, numpy

# アンダースコア
# - _xxx internal use only(non public)の意味
# - xxx_ Pythonで既に使われている単語を使いたいとき．(例:type_
# - __xxx クラスの属性として使うことで名前修飾される
# - __xxx__ magic methodと呼ばれるもので，Pythonが特別に設定しているもの．開発者定義することはない．(overrideすることはある)
# - _: 最近実行した戻り値や，iteration時に使わない変数

# l, I, Oという一文字の変数名は1や0に見間違えるので使わないこと
# Correct:
length = len(letter)
# Wrong:
l = len(letter)

# Constants(宣言後変更しない変数)は大文字のsnakecaseを使う
PI = 3.14
# 変更は可能なので注意(Pythonでは強制できない)
PI = 3

# Return
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

# オブジェクトタイプの確認はisinstance()を使う
# correct
if isinstance(obj, int)
# wrong
if type(obj) is type(1)

# Booleanに比較演算子を使えない
bool_var = True

# correct
if bool_var:
# wrong
if bool_var == True:

# type hint (type annotation)
def greeting(name: str) -> str:
# のように型のヒントを与えることができる．
# ・一つでもhitをつけたら全てにつける．
# ・typeのチェックをするわけではない
# ・Pythonは動的型付言語であることを意識すること
# ・このtype hintを強制したり，命名規約に入れるべきではない
