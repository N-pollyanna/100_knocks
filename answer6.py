#06. 集合"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

origin_text_data_A="paraparaparadise"
origin_text_data_B="paragraph"
#引数:リスト

def make_N_gram(data):
    #liset型が引数
    #bi-gramに変換した形の2次配列(2次list)を返す
    answer = []
    for times,i in enumerate(range(len(data)-1)):
        sub_data=[]
        sub_data+=data[times:times+2]
        answer.append(sub_data)
    return answer


list_text_data_A=list(origin_text_data_A)
list_text_data_B=list(origin_text_data_B)
#bi-gramにする
result_A=make_N_gram(list_text_data_A)
result_B=make_N_gram(list_text_data_B)
#bi-gram(list)を集合(set)に変換する
set_A=set(map(tuple, result_A))
set_B=set(map(tuple, result_B))
#和集合
sum_set=set_A | set_B
#積集合
product_set=set_A & set_B
#差集合
difference_set = set_A - set_B
print("和集合")
print(sum_set)
print("積集合")
print(product_set)
print("差集合")
print(difference_set)