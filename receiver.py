import serial
import logging
logger = logging.getLogger(__name__)

def read_telemetry():
    ser = serial.Serial('/dev/ttys008', 9600)
    print(ser.readline().decode())
    ser.close()

def main():
    read_telemetry()

if __name__ == "__main__":
    main()