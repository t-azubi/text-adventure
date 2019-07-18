from googletrans import Translator



translator = Translator()




translations = translator.translate(["The quick brown fox", "jumps over", "the lazy dog"], dest="de")
for translation in translations:
    print(translation.text)