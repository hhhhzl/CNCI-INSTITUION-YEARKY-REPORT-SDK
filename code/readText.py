import os
from config import (
    TEMPLATE_FOLDER,
    COVER,
    MAIN_TEXT,
    TABLES,
    ECHARTS_TXT
)
from code.replace import replace_txt


def read_front(line):
    with open(TEMPLATE_FOLDER + COVER, 'r', encoding='utf8') as template_file:
        t = template_file.read()
        html = replace_txt(t, line)
        return html


def read_text(line):
    with open(TEMPLATE_FOLDER + MAIN_TEXT, 'r', encoding='utf8') as template_file:
        t = template_file.read()
        html = replace_txt(t, line)
        return html


def read_table():
    with open(TEMPLATE_FOLDER + TABLES, 'r', encoding='utf8') as template_file:
        html = template_file.read()
        return html


def read_echarts(line):
    with open(TEMPLATE_FOLDER + ECHARTS_TXT, 'r', encoding='utf8') as template_file:
        t = template_file.read()
        html = replace_txt(t, line)
        return html
