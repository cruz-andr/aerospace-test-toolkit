# Aerospace Test Tool Kit

This is a Python based aerospace test automation toolkit that simulates real time telemetry streaming, anomaly detection, and test campaign orchestration via virtual serial ports.

**See `requirements.txt` for dependencies**

## Phase 1 (Telemetry Analyzer & Logger):

This is a tool that can take a csv of telemetry data with timestamp,pressure_psi,temperature_c,voltage_v,current_a readings and find fault isolation peaks and dips. Then logs the specific issues for an engineer to easily read and understand. The format of the logs are ``<date> <time> - <INFO/WARNING> - <message>`` 

This phase implements these modules:
- pandas
- matplotlib
- logging

**Run with:**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python analyzer.py
```

### Output
```
2026-04-14 18:05:47 - INFO - Started
2026-04-14 18:05:47 - WARNING - [ANOMALY] timestamp 15.0 | pressure_psi = 130.0 | exceeds max of 105
2026-04-14 18:05:47 - WARNING - [ANOMALY] timestamp 17.0 | temperature_c = 12.0 | exceeds min of 19.5
2026-04-14 18:05:47 - WARNING - [ANOMALY] timestamp 28.0 | voltage_v = 40.0 | exceeds max of 30.5
2026-04-14 18:05:47 - WARNING - [ANOMALY] timestamp 9.0 | current_a = 3.0 | exceeds min of 4.5
2026-04-14 18:05:47 - INFO - Finished
```

## Phase 2 (Test Pipeline Over Serial Ports):

This phase extends Phase 1 with a real-time test automation pipeline. The transmitter streams CSV telemetry over a virtual serial port. The receiver parses each row as it arrives and yields it to the test runner, which manages a state machine controlling the test campaign. When an anomaly is detected, the pipeline halts immediately and the receiver tears down to generate a final report.

This phase implements these modules:
- pandas
- matplotlib
- logging
- socat
- pyserial
- enum

**Run with 3 terminals:**

Terminal 1 — start virtual serial ports:
```
brew install socat  # Mac only
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```
Note the two `/dev/ttysXXX` paths are printed. Update them accordingly in `transmitter.py` and `receiver.py`.

Terminal 2 — start the test runner (this reads from telemetry):
```
python test_runner.py
```

Terminal 3 — send the telemetry stream:
```
python transmitter.py
```

The test campaign moves through five states:
- **SETUP**: verifies first 5 samples are within nominal range before starting
- **RUNNING**: main test loop, processes each row and checks for anomalies
- **HALT**: anomaly detected, logs the failure
- **TEARDOWN**: generates a final visual report from accumulated history
- **COMPLETE**: test finished successfully



### Output
```
2026-05-01 21:40:24 - INFO - Started
2026-05-01 21:40:25 - WARNING - [ANOMALY] timestamp 9.0 | current_a = 3.0 | exceeds min of 4.5
2026-05-01 21:40:25 - WARNING - [HALT]| Test was halted at timestamp: 9.0
2026-05-01 21:42:38 - INFO - Finished
```