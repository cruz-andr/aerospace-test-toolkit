import pandas as pd

data = pd.read_csv("data/telemetry.csv")
#print(data)

#pressure_psi: min 95, max 105
#temperature_c: min 19.5, max 25.5
#voltage_v: min 25.5, max 30.5
#current_a: min 4.5, max 5.5
limits = {"pressure_psi": [95, 105],
          "temperature_c" : [19.5, 25.5],
          "voltage_v" : [25.5, 30.5],
          "current_a" : [4.5, 5.5]}


#example of print => [ANOMALY] timestamp 15 | pressure_psi = 130 | exceeds max of 105
def check_limits():
    for i in limits:
        dataPastMax = data[data[i] > limits[i][1]]
        dataLowerMin = data[data[i] < limits[i][0]]

        for index, row in dataPastMax.iterrows():
            print(f"[ANOMALY] timestamp {row['timestamp']} | {i} = {row[i]} | exceeds max of {limits[i][1]}")
        for index, row in dataLowerMin.iterrows():
            print(f"[ANOMALY] timestamp {row['timestamp']} | {i} = {row[i]} | exceeds min of {limits[i][0]}")
        


def main():
    check_limits()

if __name__ == "__main__":
    main()