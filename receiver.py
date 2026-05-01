import serial
import logging
import pandas as pd
import analyzer
logger = logging.getLogger(__name__)

column_names = ["timestamp","pressure_psi","temperature_c","voltage_v","current_a"]

def read_telemetry():
    ser = serial.Serial('/dev/ttys005', 9600, timeout=5)
    try:
        while True:
            line = ser.readline()
            if line:
                decoded = line.decode()
                values = decoded.strip().split(",")
                values = [float(v) for v in values]
                row_dict = dict(zip(column_names, values))
                df = pd.DataFrame([row_dict])
                yield df
                #analyzer.check_limits(df)
            else:
                break
    finally:
        ser.close()

def main():
    logging.basicConfig(
    filename='analyzer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
    logger.info('Started')
    read_telemetry()
    logger.info('Finished')

if __name__ == "__main__":
    main()