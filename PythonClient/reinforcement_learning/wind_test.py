import airsim
import time
import numpy as np
import matplotlib.pyplot as plt

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Takeoff
client.takeoffAsync().join()


target = airsim.Vector3r(50, 50, -10)  # enter target coordinates (x, y, z)
client.moveToPositionAsync(target.x_val, target.y_val, target.z_val, 5).join() 

def calculate_wind_disturbance(sensor_data):
    wind_disturbance = np.sqrt(sensor_data.linear_acceleration.x_val**2 + 
                               sensor_data.linear_acceleration.y_val**2 + 
                               sensor_data.linear_acceleration.z_val**2)
    return wind_disturbance

# Collect data for a certain period
duration = 60  # in seconds
start_time = time.time()

# Lists to store data for plotting
actual_positions = []
optimal_positions = []
wind_disturbances = []

while time.time() - start_time < duration:
    # Get sensor data
    imu_data = client.getImuData()
    gps_data = client.getGpsData()
    barometer_data = client.getBarometerData()

    # Calculate wind disturbance
    wind_disturbance = calculate_wind_disturbance(imu_data)

    # Log data for plotting
    actual_positions.append((gps_data.gnss.geo_point.latitude, gps_data.gnss.geo_point.longitude, gps_data.gnss.geo_point.altitude))
    optimal_positions.append((target.x_val, target.y_val, target.z_val))
    wind_disturbances.append(wind_disturbance)

    # Print the wind disturbance value
    print(f"Time: {time.time() - start_time:.2f} s, Wind Disturbance: {wind_disturbance:.4f}")

    # Delay to avoid overwhelming the simulator
    time.sleep(0.1)

# Land the drone
client.landAsync().join()
client.armDisarm(False)
client.enableApiControl(False)

# Extract data for plotting
actual_positions = np.array(actual_positions)
optimal_positions = np.array(optimal_positions)
wind_disturbances = np.array(wind_disturbances)

# Plot actual vs optimal path
plt.figure(figsize=(10, 5))

# Subplot 1: Paths
plt.subplot(1, 2, 1)
plt.plot(actual_positions[:, 0], actual_positions[:, 1], label='Actual Path')
plt.plot(optimal_positions[:, 0], optimal_positions[:, 1], 'r--', label='Optimal Path')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Drone Path')
plt.legend()

# Subplot 2: Wind Disturbance
plt.subplot(1, 2, 2)
plt.plot(wind_disturbances)
plt.xlabel('Time (s)')
plt.ylabel('Wind Disturbance')
plt.title('Wind Disturbance Over Time')

plt.tight_layout()
plt.show()
