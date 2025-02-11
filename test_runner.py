import sys
from test_cases import run_test_cases

if __name__ == "__main__":
    hardware_port = "/dev/ttys023"  # Replace with your virtual serial port
    config_file = "config.yaml"

    results = run_test_cases(hardware_port, config_file)
    
    print("\n=== TEST RESULTS ===")
    for test_name, passed, response in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name} (Response: {response})")
