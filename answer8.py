#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．
def cipher(string_data):
    #引数;string data 暗号に変換する"文字列データ"
    #戻り値：変換後の"文字列データ"
    #before_encrypt=list(string_data)
    #英小文字かどうかの判別、英小文字であれば(219 - 文字コード)に変換
    after_encrypt=""
    for target in string_data:
        if(target.islower()):
            after_encrypt += chr(219-ord(target))
        else:
            after_encrypt += target
    return after_encrypt



text_data=input("英文字入力：")
Encrypted_data=cipher(text_data)
print("暗号化："+Encrypted_data)

Decrypted_data=cipher(Encrypted_data)
print("復号化："+Decrypted_data)