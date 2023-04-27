import re

def analysText(count = 1):
    fileText = open("text.txt", 'r', encoding='utf-8')

    ArrLenString = []

    symbols = r"[^А-я- \n]"
    arrY = []
    arrN = []
    textY = ''
    textN = ''
    outText = ''

    for n, line in enumerate(fileText):
        if len(re.findall(symbols, line)) > count:
            textY += line
            outText += line
            arrY.append(n + 1)
        else:
            textN += line
            outText += line
            arrN.append(n + 1)

    print("\n-----Строки со скрытой информацией-----")
    print(textY, '\n')
    print("\n-----Строки без скрытой информацией-----")
    print(textN)


if (__name__ == "__main__"):
    count = int(input("Введите кол-во символов пунктуации\n"))

    analysText(count)
