import datetime


def show_time(start):
    end = datetime.datetime.now()
    print(datetime.datetime.now(), "- 总用时 -", end - start)


def html_create(name):
    print(datetime.datetime.now(), "- 成功生成 -", name + ".html")


def pdf_create(name):
    print(datetime.datetime.now(), "- 正在生成 -", name + ".pdf")


def pdf_success(name):
    print(datetime.datetime.now(), "- 成功生成 -", name + ".pdf")
