origin_text="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text_list=origin_text.split(" ")

check_list=[1, 5, 6, 7, 8, 9, 15, 16, 19]
word_dic={}
for time, word in enumerate(text_list,start=1):
    if time in check_list:
        word_dic[word[0:1:]] = time
    else:
        word_dic[word[0:2:]] = time
print(word_dic)