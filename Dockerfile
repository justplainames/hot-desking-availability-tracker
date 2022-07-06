#Specifying the base image
FROM python:3.9.2

COPY Camera .

RUN apt-get update && apt-get install -y python3-opencv && pip install opencv-python && pip install paho-mqtt==1.6.1 && pip install imutils==0.5.4 && pip install numpy==1.22.3 && apt-get install -y fswebcam && apt-get install nano

CMD ["python","./run_human_detection.py"]



