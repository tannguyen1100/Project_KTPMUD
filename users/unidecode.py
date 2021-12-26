import re


def no_accent_vietnamese(s):
    s = str(s)
    s = s.lower()
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('đ', 'd', s)
    return s

def name_2_email(ten, ho=None, dem=None, code=None):
    ten_khong_dau = no_accent_vietnamese(ten)
    ho_khong_dau = no_accent_vietnamese(ho)
    if code:
        code = code[2:]
    else:
        code = ""
    if dem:
        dem_khong_dau = no_accent_vietnamese(dem)
        dem_khong_dau = dem_khong_dau.replace(" ", "")
        return ten_khong_dau+"."+ho_khong_dau[0]+dem_khong_dau[0]+str(code)+"@edu.com.vn"
    return ten_khong_dau+"."+ho_khong_dau[0]+str(code)+"@edu.com.vn"

