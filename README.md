# Python-script-serial-comm
Python script to simulate serial communication

## 📌 Overview
This project simulates a **hardware device communicating over a UART (serial) connection**, verifies received data, and checks for expected responses. It is designed for verification engineers who want to **test serial communication logic** without requiring real hardware.

## Step 1: Install Required Python Libraries

Before you begin, install the required Python libraries to simulate serial communication and manage configuration files easily.

Run the following command in your terminal:

pip install pyserial pyyaml

Libraries Used:

pyserial: A Python library to simulate serial communication.

pyyaml: A library to handle test configurations in a YAML format, making it easier to edit and manage.

## Step 2: Set Up a Virtual Serial Port on macOS

Since we are simulating hardware, we will create a pair of virtual serial ports using socat. This will allow two Python scripts to communicate as if they were connected to actual hardware.

1️⃣ Install socat

Install socat on macOS using Homebrew:

brew install socat

2️⃣ Create Virtual Serial Ports

After installing socat, run the following command in your terminal to create two virtual serial ports:

socat -d -d pty,raw,echo=0 pty,raw,echo=0

This command will generate two virtual serial ports. The output will look similar to this:

2024/02/10 12:34:56 socat[12345] N PTY is /dev/ttys004
2024/02/10 12:34:56 socat[12345] N PTY is /dev/ttys005

3️⃣ Take Note of the Virtual Ports

Take note of the two virtual serial devices created by socat (e.g., /dev/ttys004 and /dev/ttys005).

One port will be used by the mock hardware script.
The other port will be used by the test script to simulate communication.

## 🚀 Running the Project

1️⃣ Start the Mock Hardware

python mock_hardware.py

(Simulates a device sending data every 2 seconds.)

2️⃣ Start the Test Runner

python test_runner.py

(Listens for data and verifies expected responses.)

## Expected Output
✅ PASS - Check Device Version (Response: v1.2.3)

✅ PASS - Test LED Toggle (Response: OK)

✅ PASS - Read Temperature Sensor (Response: 25.4C)

✅ PASS - Invalid Command (Response: ERROR)

=== TEST RESULTS ===
4 tests run, 4 passed, 0 failed.






