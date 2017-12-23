#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
#coding:utf-8
import  os.path as path
def change_tab_to_space(filename,file_col1,file_col2):
    #入力：ファイル名
    #出力：tabをspaceに置き換えたファイル内の文字列
    if path.exists(filename):
        file=open(filename,"r",encoding="utf-8")
        col1=open(file_col1,"w",encoding="utf-8")
        col2 = open(file_col2, "w", encoding="utf-8")
        for line in file:
            string = line[:-1].split("\t")
            col1.write(string[0]+"\n")
            col2.write(string[1]+"\n")
    else:
        print("i can't found file")
        return -1


change_tab_to_space("hightemp.txt","col1.txt","col2.txt")