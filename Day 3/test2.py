from wordcloud import WordCloud

text = ''
with open("KakaoTalk_Chat_20201003.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if '",' in line:
            text += line.split('",')[1].replace('ㅋ', '').replace('ㅠ', '').replace('이모티콘', '').replace('사진\n', '').replace('삭제된', '').replace('사진', '').replace('https', '')

# print(text)

wc = WordCloud(font_path='/System/Library/Fonts/AppleSDGothicNeo.ttc', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")
