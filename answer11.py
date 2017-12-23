#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ
#coding:utf-8
import  os.path as path
def change_tab_to_space(filename):
    #入力：ファイル名
    #出力：tabをspaceに置き換えたファイル内の文字列
    if path.exists(filename):
        file=open(filename,encoding="utf-8")
        string = file.read()
        change_string=string.replace("\t", " ")
        return (change_string)
    else:
        print("i can't found file")
        return -1

print(change_tab_to_space("hightemp.txt"))
