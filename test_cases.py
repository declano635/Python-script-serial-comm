import yaml
from serial_comm import send_command

def run_test_cases(port, config_file):
    """Loads test cases from a YAML file and runs them."""
    with open(config_file, "r") as file:
        test_cases = yaml.safe_load(file)["tests"]

    results = []
    for test in test_cases:
        response = send_command(port, test["command"])
        passed = response == test["expected_response"]
        results.append((test["name"], passed, response))
    
    return results
