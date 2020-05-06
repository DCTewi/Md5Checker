"""
Utils
"""

#coding=utf-8

def get_sum_md5(path : str):
    import hashlib
    with open(path, 'rb') as f:
        raw = f.read()
    
    seed = hashlib.md5()
    seed.update(raw)

    return seed.hexdigest()

def convert_pic_to_python(path : str):
    import base64
    with open('icon.ico', 'rb') as icon:
        with open('logo.py', 'w+') as f:
            f.write('icon = ' + str(base64.b64encode(icon.read())))
# convert_pic_to_python('./logo.py')