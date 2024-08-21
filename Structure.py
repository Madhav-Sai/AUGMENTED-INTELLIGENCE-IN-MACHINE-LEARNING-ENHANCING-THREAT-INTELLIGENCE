import os

# Define the directory structure
structure = {
    "packet_sniffer": {
        "__init__.py": "",
        "flow_classifier.py": "",
        "packet_handler.py": "",
        "risk_calculator.py": "",
        "server.py": "",
        "sniffer.py": "",
        "models": {
            "preprocess_pipeline_AE_39ft.save": "",
            "preprocess_pipeline_ConvLSTM_16ft.save": ""
        },
        "logs": {
            "input_logs.csv": "",
            "output_logs.csv": ""
        }
    }
}

# Function to create the directory structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursively create subdirectories/files
        else:
            # Create file
            with open(path, 'w') as file:
                file.write(content)

# Execute the function
create_structure('.', structure)

print("Directory structure created successfully!")
