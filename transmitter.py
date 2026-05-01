import serial
import logging
import pandas as pd
logger = logging.getLogger(__name__)

data = pd.read_csv("data/telemetry.csv")

def send_telemetry():
    ser = serial.Serial('/dev/ttys000',9600)
    for index, row in data.iterrows():
        row_string = ",".join(str(value) for value in row) + "\n"
        ser.write(row_string.encode('utf-8'))
    ser.close()


def main():
    send_telemetry()

if __name__ == "__main__":
    main()