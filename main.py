from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
import os
import aws_controller

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

camera_images = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = camera_images


@app.route('/')
def home():
    # selected_image_1 =

    image_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'test_image2.jpg')
    image_2 = os.path.join(app.config['UPLOAD_FOLDER'], 'test_image3.jpg')

    seat_1 = 1
    seat_2 = 5

    return render_template('home.html', image_1=image_1, image_2=image_2, seat_1=seat_1, seat_2=seat_2)


@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_items())


if __name__ == '__main__':
    app.run(debug=True)


