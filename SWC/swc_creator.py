# swc/swc_creator.py
import matlab.engine

def create_new_swc(swc_name, directory):
    eng = matlab.engine.start_matlab()
    model_name = f"{directory}/{swc_name}"
    
    eng.new_system(model_name, nargout=0)
    eng.set_param(model_name, 'Solver', 'FixedStepDiscrete', nargout=0)
    eng.add_block('simulink/Sources/In1', f"{model_name}/Inport", nargout=0)
    eng.add_block('simulink/Sinks/Out1', f"{model_name}/Outport", nargout=0)
    eng.save_system(model_name, nargout=0)
    eng.quit()
