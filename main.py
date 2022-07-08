from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
import os
import aws_controller
import forecast

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

camera_images = os.path.join('static/', 'images/')

app.config['UPLOAD_FOLDER'] = camera_images


@app.route('/', methods=["POST", "GET"])
def home():
    forecast_1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Forecast_1.png')
    forecast_2 = os.path.join(app.config['UPLOAD_FOLDER'], 'Forecast_2.png')

    seat_1 = int(aws_controller.get_latest_update_1())
    seat_2 = int(aws_controller.get_latest_update_2())

    if request.method == 'POST':
        if request.form['btnForecast'] == 'Generate':
            forecast.generate_forecast()
            print("FORM 1")

    return render_template('home.html', seat_1=seat_1, seat_2=seat_2,
                           forecast_1=forecast_1, forecast_2=forecast_2)


@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_items())


if __name__ == '__main__':
    app.run(debug=True)