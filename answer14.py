#hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

# さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

#coding:utf-8
import  os.path as path

def until_input_print(filename,for_count):
    #入力はファイル名
    #出力は指定された行数までの入力
    count=0
    if path.exists(filename):
        for i in open(filename, "r",encoding="utf-8"):
            print(i)
            count=count+1
            if count==for_count:
                break
    else:
        print("can't found a file")
        return_count=-1

def until_input_print2(filename,for_count):
    #入力はファイル名
    #出力は指定された行数までの入力
    count=0
    if path.exists(filename):
        with open(filename, "r",encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines[:for_count]:
                print(i)
    else:
        print("can't found a file")
        return_count=-1

input_number=input("please enter number:")
input_number=int(input_number)
until_input_print("hightemp.txt",input_number)
until_input_print2("hightemp.txt",input_number)
