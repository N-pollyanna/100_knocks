target="I am an NLPer"
#引数:リスト
def make_N_gram(data):
    answer = []
    for times,i in enumerate(range(len(data)-1)):
        sub_data=[]
        sub_data+=data[times:times+2]
        answer.append(sub_data)
    return answer



#単語N-gram
data_list_word=list(target)
result=make_N_gram(data_list_word)
print(result)

#文章N-garm
data_list_text=target.split(" ")
result=make_N_gram(data_list_text)
print(result)