#07. x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
#coding: UTF-8
from string import Template
def text_made(x,y,z):
    #x,y,zを引数にして、「x時のyはz」という文字列を返す
    #引数：x,y,z 埋め込むパラメータ
    #戻り値：成形した文字列

    #x:時間
    #y:"気温”などのtxt
    #気温等の数位
    #s=(str(x) + "時の" + y + "は" + str(z))
    #return s
    s=Template("$hour時の$strageは$value")
    return s.substitute(hour=x, strage=y, value=z)

# テスト
x = 12
y = '気温'
z = 22.4
print(text_made(x,y,z))