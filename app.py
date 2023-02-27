import os
import cv2
from flask import Flask, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
import human_detector

app = Flask(__name__)

ALLOWED_EXTENSION = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = 'static/'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

app.config['ALLOWED_EXTENSION'] = ('.png', '.jpg', '.jpeg')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def upload_image():
    if 'image' not in request.files:
        print('Brak pliku')
        return redirect(request.url)
    image = request.files['image']
    if image.filename == None:
        print('Nie przesłano zdjęcia')
        return redirect(request.url)
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(file_path)
        print('Zdjęcie dodane prawidłowo')
        image, number_of_people_counter = human_detector.humanDetection(file_path)
        print(number_of_people_counter)
        cv2.imwrite(file_path, image)
        return render_template('upload.html', filename=filename, number=number_of_people_counter)
    else:
        print('Możesz przesłać tylko zdjęcia o formacie: .png, .jpg, .jpeg')
        return redirect(request.url)

if __name__ == '__main__':
    app.debug = True
    app.run()

