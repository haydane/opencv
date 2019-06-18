from flask import Flask, render_template, redirect, url_for, request
from werkzeug import secure_filename
from datetime import datetime
import cv2
import glob
import os
import matplotlib.pyplot as plt
import numpy as np
app = Flask(__name__)

UPLOAD_FOLDER = './upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def feature_matching(img):
    path = '../images/*.jpg'
    print('============================')
    print('\n\n\n\n')
    print('you are comparing: \n', 'path: ',
          path, '\n', 'image: ', img, '\n\n')
    img = cv2.imread('./upload/' + img, 0)
    start_time = datetime.now()
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img, None)
    for file in glob.glob(path):
        file_name = cv2.imread(file, 0)

        kp2, des2 = sift.detectAndCompute(file_name, None)
        # flann
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)

        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(des1, des2, k=2)

        matchesMask = [[0, 0] for i in range(len(matches))]

        good = []

        for i, (match1, match2) in enumerate(matches):
            if match1.distance < 0.8 * match2.distance:
                good.append(match1)
        if len(good) > 80:
            print('here is the matching image: ', file)

    end_time = datetime.now()
    res_time = end_time - start_time
    print('image count in path: ', len(glob.glob(path)))
    print('time used: ', res_time.seconds, "seconds")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # path = request.form['path']
        file = request.files['img']

        filename = secure_filename(file.filename)

        file.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename))

        results = feature_matching(str(filename))
        # print('\n\n\n\n')
        print('============================')
        print('\n\n\n\n')
        return render_template('about.html')
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)