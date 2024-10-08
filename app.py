from flask import Flask, render_template, Response, request, send_file, jsonify
import cv2
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import numpy as np
import pandas as pd
import glob 
import json 

from utils.query_processing import Translation
from utils.faiss import Myfaiss

# http://0.0.0.0:5001/home?index=0

# app = Flask(__name__, template_folder='templates', static_folder='static')

app = Flask(__name__, template_folder='templates')

####### CONFIG #########
with open('image_path.json') as json_file:
    json_dict = json.load(json_file)

DictImagePath = {}
for key, value in json_dict.items():
   DictImagePath[int(key)] = value 

LenDictPath = len(DictImagePath)
bin_file='faiss_normal_ViT.bin'
MyFaiss = Myfaiss(bin_file, DictImagePath, 'cpu', Translation(), "ViT-B/32")
########################

@app.route('/home')
@app.route('/')
def thumbnailimg():
    if not request.args.get('textquery') and not request.args.get('imgid'):
        # Nếu không có truy vấn tìm kiếm thì không hiển thị ảnh
        return render_template('home.html', data={'pagefile': []})
    
    print("load_iddoc")

    pagefile = []

    index_value = request.args.get('index', 0)
    try:
        index = int(index_value)
    except ValueError:
        index = 0 

    imgperindex = 100
    
    page_filelist = []
    list_idx = []

    if LenDictPath-1 > index+imgperindex:
        first_index = index * imgperindex
        last_index = index*imgperindex + imgperindex

        tmp_index = first_index
        while tmp_index < last_index:
            page_filelist.append(DictImagePath[tmp_index])
            list_idx.append(tmp_index)
            tmp_index += 1    
    else:
        first_index = index * imgperindex
        last_index = LenDictPath

        tmp_index = first_index
        while tmp_index < last_index:
            page_filelist.append(DictImagePath[tmp_index])
            list_idx.append(tmp_index)
            tmp_index += 1    

    for imgpath, id in zip(page_filelist, list_idx):
        pagefile.append({'imgpath': imgpath, 'id': id})

    data = {'num_page': int(LenDictPath/imgperindex)+1, 'pagefile': pagefile}
    
    return render_template('home.html', data=data)


@app.route('/imgsearch')
def image_search():
    print("image search")
    pagefile = []
    id_query = int(request.args.get('imgid'))
    _, list_ids, _, list_image_paths = MyFaiss.image_search(id_query, k=50)

    imgperindex = 100 

    for imgpath, id in zip(list_image_paths, list_ids):
        pagefile.append({'imgpath': imgpath, 'id': int(id)})

    data = {'num_page': int(LenDictPath/imgperindex)+1, 'pagefile': pagefile}
    
    return render_template('home.html', data=data)

def split_text(text, max_length):
    words = text.split()
    return [' '.join(words[i:i + max_length]) for i in range(0, len(words), max_length)]

@app.route('/textsearch')
def text_search():
    print("text search")

    text_query = request.args.get('textquery')

    max_length = 77  
    text_parts = split_text(text_query, max_length) 

    all_ids = []
    all_image_paths = []

    for part in text_parts:
        _, list_ids, _, list_image_paths = MyFaiss.text_search(part, k=50)
        
        all_ids.extend(list_ids)
        all_image_paths.extend(list_image_paths)

    imgperindex = 10
    pagefile = [{'imgpath': imgpath, 'id': int(id)} for imgpath, id in zip(all_image_paths[:imgperindex], all_ids[:imgperindex])]

    data = {'num_page': 1, 'pagefile': pagefile}

    return render_template('home.html', data=data)



@app.route('/get_img')
def get_img():
    fpath = request.args.get('fpath')
    if os.path.exists(fpath):
        img = cv2.imread(fpath)
    else:
        print("load 404.jpg")
        img = cv2.imread("./static/images/404.jpg")

    img = cv2.resize(img, (1280, 720))

    ret, jpeg = cv2.imencode('.jpg', img)
    return Response((b'--frame\r\n'
                     b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n'),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
