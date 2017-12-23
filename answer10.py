#hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
# 以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．

# さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．
#coding:utf-8
import  os.path as path

def count_number(filename):
    #入力はファイル名
    #出力は、行数のcount数
    return_count=0
    if path.exists(filename):
        for i in open(filename, "r",encoding="utf-8"):
            print(i)
            return_count=+return_count+1
    else:
        print("can't found a file")
        return_count=-1
    return return_count


print(count_number("hightemp.txt"))