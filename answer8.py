#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．
def cipher(string_data):
    #引数;string data 暗号に変換する"文字列データ"
    #戻り値：変換後の"文字列データ"
    before_encrypt=len(string_data)
    print("a")



text_data="aAaAa"
Encrypted_data=cipher(text_data)
