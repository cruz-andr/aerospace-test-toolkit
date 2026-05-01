import receiver
import analyzer
import logging
import pandas as pd
from enum import Enum
logger = logging.getLogger(__name__)

class TestState(Enum):
    SETUP = 1
    RUNNING = 2
    HALT = 3
    TEARDOWN = 4
    COMPLETE = 5

def run_test():
    state = TestState.SETUP
    setup_count = 0
    history = []
    for row in receiver.read_telemetry():
        history.append(row)
        if state == TestState.SETUP:
            if setup_count >= 5:
                state = TestState.RUNNING
            elif analyzer.check_limits(row):
                state = TestState.HALT
            else:
                setup_count += 1
        elif state == TestState.RUNNING:
            if analyzer.check_limits(row):
                state = TestState.HALT
        elif state == TestState.HALT:
           logger.warning(f"[HALT]| Test was halted at timestamp: {row['timestamp']}")
           state = TestState.TEARDOWN    
        elif state == TestState.TEARDOWN:
            full_df = pd.concat(history, ignore_index=True)
            analyzer.channel_plotter(full_df)
            state = TestState.COMPLETE
            break
        elif state == TestState.COMPLETE:
            pass

def main():
    logging.basicConfig(
    filename='analyzer_runner.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
    logger.info('Started')
    run_test()
    logger.info('Finished')

if __name__ == "__main__":
    main()