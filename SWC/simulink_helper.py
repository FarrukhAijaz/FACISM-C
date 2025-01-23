# swc/simulink_helper.py
import matlab.engine

def start_matlab_engine():
    """Starts the MATLAB Engine and returns the instance."""
    return matlab.engine.start_matlab()

def stop_matlab_engine(engine):
    """Stops the MATLAB Engine."""
    engine.quit()
