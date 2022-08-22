import subprocess
from config import WKHTMLTOPDF_BIN_PATH


def html_to_pdf(html, to_file):
    
    '''将html文件生成pdf文件，（由于权限问题），直接在wkhtmltopdf终端渲染'''
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    """在wkhtmltopdf bin下操作指令"""
    """更多指令，请参考https://wkhtmltopdf.org/usage/wkhtmltopdf.txt"""
    
    cmd = [WKHTMLTOPDF_BIN_PATH,
           "--enable-local-file-access",
           "-s","A4",
           "--dpi","300",
           "--footer-right","[page]",
           "--image-dpi","600",
           "--disable-smart-shrinking",
           "--footer-font-size","9", 
           html,
           to_file]
    
    subprocess.run(cmd, capture_output=True, text=True)