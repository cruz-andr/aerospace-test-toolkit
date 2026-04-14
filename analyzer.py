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



def check_limits():
    for i in limits:
        dataPastMax = data[data[i] > limits[i][1]]
        dataLowerMin = data[data[i] < limits[i][0]]
        if not dataPastMax.empty:
            print(dataPastMax)
        if not dataLowerMin.empty:
            print(dataLowerMin)

def main():
    check_limits()

if __name__ == "__main__":
    main()