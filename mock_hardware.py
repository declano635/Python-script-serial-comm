import serial

RESPONSES = {"GET_VERSION": "v1.2.3",
             "TOGGLE_LED": "OK",
             "READ_TEMP": "25.4C"}

def simulate_hardware(port):
    """Simulates a serial command responsive hardware device"""
    with serial.Serial(port, baudrate=115200, timeout=1) as ser:
       print(f"Mock hardware is running on {port}...")
       while True:
           if ser.in_waiting:
              command=ser.readline().decode().strip()
              response=RESPONSES.get(command,"ERROR")
              ser.write(f"{response}\n".encode())   

if __name__ == "__main__":
    virtual_port= "/dev/ttys022"  
    simulate_hardware(virtual_port)           