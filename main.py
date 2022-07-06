from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
import os
import aws_controller

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

camera_images = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = camera_images


@app.route('/', methods=["POST", "GET"])
def home():
    image_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'test_image2.jpg')
    image_2 = os.path.join(app.config['UPLOAD_FOLDER'], 'test_image3.jpg')

    forecast_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.png')
    forecast_2 = os.path.join(app.config['UPLOAD_FOLDER'], 'test2.png')

    seat_1 = int(aws_controller.get_latest_update())
    seat_2 = 5

    if request.method == 'POST':
        if request.form['btnForecast1'] == 'Generate 1':
            print("FORM 1")

    return render_template('home.html', image_1=image_1, image_2=image_2, seat_1=seat_1, seat_2=seat_2,
                           forecast_1=forecast_1, forecast_2=forecast_2)


@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_items())


if __name__ == '__main__':
    app.run(debug=True)