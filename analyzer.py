import matplotlib.pyplot as plt
import logging
logger = logging.getLogger(__name__)

#pressure_psi: min 95, max 105
#temperature_c: min 19.5, max 25.5
#voltage_v: min 25.5, max 30.5
#current_a: min 4.5, max 5.5
limits = {"pressure_psi": [95, 105],
          "temperature_c" : [19.5, 25.5],
          "voltage_v" : [25.5, 30.5],
          "current_a" : [4.5, 5.5]}



#example of print => [ANOMALY] timestamp 15 | pressure_psi = 130 | exceeds max of 105
def check_limits(df):
    for i in limits:
        dataPastMax = df[df[i] > limits[i][1]]
        dataLowerMin = df[df[i] < limits[i][0]]

        for index, row in dataPastMax.iterrows():
            logger.warning(f"[ANOMALY] timestamp {row['timestamp']} | {i} = {row[i]} | exceeds max of {limits[i][1]}")
            return True
        for index, row in dataLowerMin.iterrows():
            logger.warning(f"[ANOMALY] timestamp {row['timestamp']} | {i} = {row[i]} | exceeds min of {limits[i][0]}")
            return True
    return False

def channel_plotter(df):
    fig, axs = plt.subplots(nrows=4, ncols=1)
    for index, value in enumerate(limits):
        axs[index].plot(df["timestamp"],df[value])
        axs[index].set_ylabel(value)
        axs[index].axhline(limits[value][0],color='red', linestyle=':', label = f'max threshold = {limits[value][1]}')
        axs[index].axhline(limits[value][1],color='red', linestyle=':', label = f'min threshold = {limits[value][0]}')
        axs[index].legend()
    plt.xlabel("timestamp")
    plt.tight_layout()
    plt.savefig('report/channel_plot.png')
    plt.show()


def main():
    logging.basicConfig(
    filename='analyzer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
    logger.info('Started')
    #check_limits()
    #channel_plotter()
    logger.info('Finished')

if __name__ == "__main__":
    main()