#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random
def get_random_word_position(text_data):
    #入力値：文字列
    #戻り値：処理跡の文字列
    #戻り値用のlist
    return_list=[]
    for data in text_data.split():
        #文字数が4文字移住ならそんまま
        if(len(data) <=4):
            return_list.append(data)
        else:
            intermediate_data=list(data[1:-1])
            random.shuffle(intermediate_data)
            return_list.append(data[0] + "".join(intermediate_data) + data[-1])
    return " ".join(return_list)




input_data="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result=get_random_word_position(input_data)
print(result)