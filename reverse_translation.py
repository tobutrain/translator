import requests
# ここはご自分で発行されたKEYを入れてください
YOUR_API_KEY = '05220797-2fe5-6afd-2112-23a3fdaa778f:fx'


# 翻訳したい入力テキスト
input_text = '',
#翻訳前の言語(日本語:JA,英語:EN)
source_lang = "JA"
#翻訳語の言語(翻訳したい言語)
target_lang = "EN"

params = {
        "auth_key": YOUR_API_KEY,
        "text": input_text,
        "source_lang": source_lang, # 入力テキストの言語を設定(日本語:JA,英語:EN)
        "target_lang": target_lang  # 出力テキストの言語を設定
        }

def translation(params, input_text):
    # パラメータと一緒にPOSTする
    for i in range(2):
        params["text"] = input_text
        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        input_text = request.json()["translations"][0]["text"]
        params["source_lang"], params["target_lang"] = params["target_lang"], params["source_lang"]
        print("出力:{}".format(input_text))


def main(params):
    while True:
        print("-------------")
        input_text = input("入力:")
        if input_text == "end" or input_text == "えんd":
            print("終了します")
            print("-------------")
            break
        
        elif input_text == "change_lang":
            params["source_lang"], params["target_lang"] = params["target_lang"], params["source_lang"]

        else:
            translation(params, input_text)

if __name__ == "__main__":
    main(params)