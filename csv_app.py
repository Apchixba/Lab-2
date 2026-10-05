from csv import reader
import random
import xml.dom.minidom as minidom


def nom1():
    s = list(reader(open("books.csv", "r"), delimiter=";"))

    c = 0
    id_n = s[0].index("Название")
    for i in s[1:]:
        if len(i[id_n]) > 30:
            c += 1
        
    print(c)

def nom2(author):
    s = list(reader(open("books.csv", "r"), delimiter=";"))

    id_n, id_a, id_af, id_d = s[0].index("Название"), s[0].index("Автор"), s[0].index("Автор (ФИО)"), s[0].index("Дата поступления")
    for i in s[1:]:
        if author in [i[id_a], i[id_af]] and int(i[id_d].split(".")[2][:4]) >= 2018:
            print(i[id_n])


def nom3():
    res = open("result.txt", "w", encoding="utf-8")
    txt = list(reader(open("books.csv", "r"), delimiter=";"))

    title = txt[0]
    lines = txt[1:]
    random.shuffle(lines)
    c = 1
    id_n, id_a, id_d = title.index("Название"), title.index("Автор"), title.index("Дата поступления")
    for i in sorted(lines[:20], key=lambda x: [x[id_a], int(x[id_d].split(".")[2][:4])]):
        res.write(f"{c}){i[id_a]}. {id_n} - {int(i[id_d].split('.')[2][:4])}\n")
        c += 1
    
    res.close()
        
    # print(c)


def nom4():
    dom = minidom.parse('currency.xml')
    dom.normalize()

    elements = dom.getElementsByTagName('Valute')
    books_dict = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Name':
                    if child.firstChild:
                        name = child.firstChild.data
                if child.tagName == 'CharCode':
                    if child.firstChild:
                        CharCode = child.firstChild.data
        books_dict[name] = CharCode

    print(books_dict)

# nom1()
# nom2(input("Введите автора"))
# nom3()
# nom4()