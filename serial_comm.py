import serial
import time

def send_command(port, command, timeout=2):
    """Sends a command to the mock hardware and returns the response."""
    with serial.Serial(port, baudrate=115200, timeout=timeout) as ser:
        ser.write(f"{command}\n".encode())
        time.sleep(0.5)  # Simulating processing delay
        response = ser.readline().decode().strip()
        return response







