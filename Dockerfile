# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:2.7.13-jessie

COPY set_temp.py ./set_temp.py
COPY get_brewery_status.py ./get_brewery_status.py
COPY beerfridge_display.py ./beerfridge_display.py

# Intall the necessary modules
RUN pip install --no-cache-dir rpi.gpio
RUN pip install adafruit-mcp3008
RUN pip install Adafruit-LED-Backpack

CMD python /set_temp.py