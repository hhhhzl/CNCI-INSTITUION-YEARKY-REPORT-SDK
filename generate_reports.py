from code.readText import read_text, read_front, read_table, read_echarts
from code.转pdf import html_to_pdf
from code.replace import replace_txt
from config import (
    PDF_FOLDER,
    PDF_CODE_FOLDER,
    TEMPLATE_FOLDER,
    HTML_FOLDER,
    DATA_FOLDER,
    INSTITUTION_DATA,
    INSTITUTION_NAME,
    ECHARTS_DATA,
    ALL_DATA,
    YEAR
)
import pandas as pd
import datetime
from logger import show_time, html_create, pdf_create, pdf_success
import os


def generator_files():
    start = datetime.datetime.now()
    try:
        # 数据预处理，导入表格
        data_individual = pd.read_excel(DATA_FOLDER + INSTITUTION_DATA)
        data_name = pd.read_excel(DATA_FOLDER + INSTITUTION_NAME)
        data_scores = pd.read_excel(DATA_FOLDER + ALL_DATA)
        data_echarts = pd.read_excel(DATA_FOLDER + ECHARTS_DATA)
        institutes_names = data_name['研究所'].values.tolist()
    except IOError:
        print("Error: 没有找到文件或读取文件失败")

    else:
        for i in range(104):
            # 在几个excel表格中找到所在单位的4个板块数据
            individual1 = data_name[(data_name['研究所'] == institutes_names[i])]
            individual2 = data_individual[(data_individual['研究所'] == institutes_names[i])]
            scores = data_scores[(data_scores['研究所'] == institutes_names[i])]
            echarts = data_echarts[(data_echarts['研究所'] == institutes_names[i])]

            # 放入模板，生成html
            html = read_front(individual1.to_dict('list')) + replace_txt(read_text(individual2.to_dict('list')),
                                                                         scores.to_dict(
                                                                             'list')) + read_table() + read_echarts(
                echarts.to_dict('list'))

            # 确认html保存路径
            html_file_path = HTML_FOLDER + individual1['研究所'].values.tolist()[0] + '_' + YEAR + '.html'
            # 打出html
            f = open(html_file_path, 'w', encoding='utf-8')
            f.write(html)
            f.close()
            html_create(individual1['研究所'].values.tolist()[0])

            # 确认生成pdf路径
            pdf_file_path = PDF_FOLDER + individual1['研究所'].values.tolist()[0] + '_' + YEAR + '.pdf'
            # 生成最终机构代码pdf，上传服务器
            pdf_file_path_indi = PDF_CODE_FOLDER + YEAR + "/" + individual1['研究所代码'].values.tolist()[
                0] + '_' + YEAR + '.pdf'
            # 转为pdf并渲染

            pdf_create(individual1['研究所'].values.tolist()[0] + '_' + YEAR)
            html_to_pdf(html_file_path, pdf_file_path)
            pdf_success(individual1['研究所'].values.tolist()[0] + '_' + YEAR)
            show_time(start)

            pdf_create(individual1['研究所代码'].values.tolist()[0] + '_' + YEAR)
            html_to_pdf(html_file_path, pdf_file_path_indi)
            pdf_success(individual1['研究所代码'].values.tolist()[0] + '_' + YEAR)
            show_time(start)
            print()


if __name__ == "__main__":
    if not os.path.exists(os.path.join(os.path.dirname(__file__), PDF_CODE_FOLDER + YEAR)):
        os.mkdir(os.path.join(os.path.dirname(__file__), PDF_CODE_FOLDER + YEAR))
    generator_files()
    print('恭喜导出所有pdf！')  # 导出结束
