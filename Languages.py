from google_trans_new import google_translator
from re import compile as regcompile
from tkinter.filedialog import askopenfilename
from os import mkdir

translator = google_translator()

file = askopenfilename()
strings = open(file, "r", encoding="utf-8")
strings_file_content = strings.read()
strings.close()

patron = regcompile("\s*\t*<string.*>.*</string>")
langs_strings = [
    "fr",
    "es",
    "de",
    "zh-cn",
    "it"
]

final = strings_file_content
for string in patron.findall(strings_file_content):
    final = final.replace(string, "\n__**STRING**__")

all_strings = []
new_strings = {}
for string in patron.findall(strings_file_content):
    tstring = string.replace("\n", "", 1).strip()
    tstring = tstring.replace("<string", "").replace("</string>", "").strip()
    attr_string = tstring.split(">")
    all_strings.append(attr_string)

for lang in langs_strings:
    new_text = final
    for tag in all_strings:
        new_text = new_text.replace("__**STRING**__", "\t<string {}>{}</string>".format(tag[0], translator.translate(text=tag[1], lang_tgt=lang)), 1)
    new_strings[lang] = new_text

root = file.replace("values/strings.xml", "")
for language in new_strings.keys():
    if language == "es":
        try:
            mkdir(root+"values-es")
            open(root+"values-es"+"/strings.xml", "w", encoding="utf-8").write(new_strings[language])
        except:
            print("{} translation alredy exists".format(language.upper()))
    elif language == "de":
        try:
            mkdir(root+"values-de")
            open(root+"values-de"+"/strings.xml", "w", encoding="utf-8").write(new_strings[language])
        except:
            print("{} translation alredy exists".format(language.upper()))
    elif language == "fr":
        try:
            mkdir(root+"values-fr")
            open(root+"values-fr"+"/strings.xml", "w", encoding="utf-8").write(new_strings[language])
        except:
            print("{} translation alredy exists".format(language.upper()))
    elif language == "zh-cn":
        try:
            mkdir(root+"values-zh")
            open(root+"values-zh"+"/strings.xml", "w", encoding="utf-8").write(new_strings[language])
        except:
            print("{} translation alredy exists".format(language.upper()))
    else:
        try:
            mkdir(root+"values-it")
            open(root+"values-it"+"/strings.xml", "w", encoding="utf-8").write(new_strings[language])
        except:
            print("{} translation alredy exists".format(language.upper()))
input("Press enter to exit: ")
