from config import ECHART_JS_PATH, PICTURE_PATH

def replace_txt(t, ins):
    '''
    Replace the identifiers with actural data.

    Input:
    --t: The .txt file to replace.
    --ins: An institute instance.

    Returns:
    -- t: The replaced .txt file.
    '''
    picture = '(' + "PICTURE_PATH" + ')'
    echart_path = '(' + "ECHART_JS_PATH" + ')'
    for  identifier, value in ins.items():
        identifier = '(' + identifier + ')'
        t = t.replace(identifier, str(value[0])).replace(picture, PICTURE_PATH).replace(echart_path, ECHART_JS_PATH)
    return t
