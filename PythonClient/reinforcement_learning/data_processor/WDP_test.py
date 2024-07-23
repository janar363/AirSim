# simplified_cpp_wrapper_usage.py
import airsim
import numpy as np
import wind_data_processor as wdp

def fetch_drone_position_and_wind():
    # Connect to the AirSim simulator
    client = airsim.MultirotorClient()
    client.confirmConnection()

    # Initialize the Wind Data Processor
    processor = wdp.Array3D("wisp_50.csv", "3darr.bin", -25, 25, -25, 25, 0, 10)
    processor.load_data()

    # Get drone state
    drone_state = client.getMultirotorState()
    
    # Get drone position
    position = drone_state.kinematics_estimated.position
    
    # Convert position to numpy array and round to integers
    position_array = np.array([position.x_val, position.y_val, position.z_val])
    rounded_position = np.round(position_array).astype(int)

    # Get wind value at the rounded position
    x, y, z = rounded_position
    wind_val = processor.get_wind_value(int(x), int(y), int(z))

    # Print results
    print("Rounded Drone Position (x, y, z):", rounded_position)
    print("Wind Values (u, v, w):", wind_val.u, wind_val.v, wind_val.w)

    x, y, z = rounded_position
    wind_val = processor.get_wind_value(int(0), int(0), int(10))

    # Print results
    print("Rounded Drone Position (x, y, z):", rounded_position)
    print("Wind Values (u, v, w):", wind_val.u, wind_val.v, wind_val.w)

if __name__ == "__main__":
    fetch_drone_position_and_wind()