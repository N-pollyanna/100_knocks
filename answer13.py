#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
#coding:utf-8
import  os.path as path

def count_number(filename_write,filename_col1, filename_col2):
    #入力はファイル名:col1,col2
    #出力は、合成されたファイル
    file = open(filename_write, "w", encoding="utf-8")
    col1 = open(filename_col1, "r", encoding="utf-8")
    col2 = open(filename_col2, "r", encoding="utf-8")

    return_count=0
    if path.exists(filename_col1)&path.exists(filename_col2):
        for i,j in zip(col1,col2):
            file.write((i.rstrip()+"\t"+j.rstrip())+"\n")
    else:
        print("can't found a file")
        return_count=-1
    return return_count


print(count_number("Combining_col1_col2.txt","col1.txt","col2.txt"))