import subprocess
import shlex
import json
import csv

def execute_curl_command(api_name, context):
    # Construct and execute the curl command
    curl_command = f"curl -X POST 'https://abc.com/conf4/api/configuration/{context}' -H 'Authorization: Basic YOUR_ENCODED_AUTH_TOKEN' -H 'Content-Type: application/json' -d '{{\"apiName\": \"{api_name}\", \"context\": \"{context}\"}}'"
    process = subprocess.Popen(shlex.split(curl_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        return output.decode('utf-8')
    else:
        print(f"Error executing curl for {api_name}: {error.decode('utf-8')}")
        return None

def process_json_response(json_response):
    try:
        data = json.loads(json_response)
        application_properties = data.get('applicationProperties', {})
        keys_and_values = "\n".join([f"{k}: {v}" for k, v in application_properties.items()])
        return keys_and_values
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return ""

def write_to_csv(csv_file_path, fieldnames, rows):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f"Data written to {csv_file_path}")

# Placeholder for your existing data setup
existing_data = [
    # Populate with your actual data
]

# Define your CSV file path and fieldnames
csv_file_path = '/mnt/data/sampledataset-resultf.csv'
fieldnames = ["Column1.api-name", "Column1.context", "Column1.document-content-not-matching-with-conjur", "Column1.not-matching-properties", "Column1.matching-document-count", "keys_and_values_from_response"]

# Collect data to write
data_to_write = []
for data in existing_data:
    json_response = execute_curl_command(data["Column1.api-name"], data["Column1.context"])
    if json_response:
        keys_and_values = process_json_response(json_response)
        data["keys_and_values_from_response"] = keys_and_values
        data_to_write.append(data)

# Write the collected data to CSV
write_to_csv(csv_file_path, fieldnames, data_to_write)
