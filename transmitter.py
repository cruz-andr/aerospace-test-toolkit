import serial
import logging
logger = logging.getLogger(__name__)

def send_telemetry():
    ser = serial.Serial('/dev/ttys003',9600)
    ser.write(b'pressure_psi=100\n')
    ser.close()


def main():
    send_telemetry()

if __name__ == "__main__":
    main()