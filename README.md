# Aerospace Test Tool Kit

This is a tool kit for testing and integrations for me to learn these libraries:
- pandas
- matplotlib

## Phase 1 (Telemetry Analyzer & Logger):

This is a tool that can take a csv of telemetry data with timestamp,pressure_psi,temperature_c,voltage_v,current_a readings and find fault isolation peaks and dips. Then logs the specific issues for an engineer to easily read and understand. The format of the logs are ``<date> <time> - <INFO/WARNING> - <message>`` 

**Run with:**
```
python3 -m venv venv
source venv/bin/activate
python analyzer.py
```

### Steps taken
1. Begin to understand first principles of fluctuations and data as well as the importance of fault isolation
2. Created a csv with peaks and dips
3. Understood how pandas extracts data from a csv
4. Print a filtered DataFrame 