# Aerospace Test Tool Kit

This is a tool kit for testing and integrations:
- pandas
- matplotlib

## Phase 1 (Telemetry Analyzer & Logger):

This is a tool that can take a csv of telemetry data with timestamp,pressure_psi,temperature_c,voltage_v,current_a readings and find fault isolation peaks and dips. Then logs the specific issues for an engineer to easily read and understand. The format of the logs are ``<date> <time> - <INFO/WARNING> - <message>`` 

**Run with:**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python analyzer.py
```

## Output
```
2026-04-14 18:05:47 - INFO - Started
2026-04-14 18:05:47 - WARNING - [ANOMALY] timestamp 15.0 | pressure_psi = 130.0 | exceeds max of 105
2026-04-14 18:05:47 - WARNING - [ANOMALY] timestamp 17.0 | temperature_c = 12.0 | exceeds min of 19.5
2026-04-14 18:05:47 - WARNING - [ANOMALY] timestamp 28.0 | voltage_v = 40.0 | exceeds max of 30.5
2026-04-14 18:05:47 - WARNING - [ANOMALY] timestamp 9.0 | current_a = 3.0 | exceeds min of 4.5
2026-04-14 18:05:47 - INFO - Finished
```