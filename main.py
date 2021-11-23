from deep_translator import GoogleTranslator


print("Ma'lumot qaysi tilda tarjima qilinsin !!!")
print("1-Rus tili")
print("2-Ingliz tili")
print("3-Nemis tili")

gap = int(input("Tanlang: "))

with open("matn.txt", "r") as f:
    file = f.read()
    if gap==1:
        gap="ru"
    elif gap==2:
        gap="en"
    else:
        gap="nl"

    result = GoogleTranslator(source='auto',target=gap).translate(file)

    with open("tarjima.txt", "w") as r:
        r.write(result)

