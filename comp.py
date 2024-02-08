import csv


def process_api_response(api_response, csv_writer, existing_row_data):
    """
    Process the API response, extracting applicationProperties, and write to CSV.

    :param api_response: JSON response from the API as a string.
    :param csv_writer: CSV writer object to write data to the CSV file.
    :param existing_row_data: Dictionary containing the existing row data.
    """
    # Parse the JSON response
    response_data = json.loads(api_response)

    # Extract applicationProperties
    application_properties = response_data.get('applicationProperties', {})

    # Prepare keys and values from the applicationProperties as a single string
    keys_and_values = "\n".join([f"{key} : {value}" for key, value in application_properties.items()])

    # Update the existing row data with keys and values from the response
    existing_row_data["keys_and_values_from_response"] = keys_and_values

    # Write the updated row to the CSV
    csv_writer.writerow(existing_row_data)

# Define the path to your new CSV file
new_csv_file_path = 'updated_data.csv'

# Define your fieldnames (column headers)
fieldnames = [
    "Column1.document-not-in-conjur",
    "Column1.context",
    "Column1.api-name",
    "Column1.document-content-not-matching-with-conjur",
    "Column1.not-matching-properties",
    "Column1.matching-document-count",
    "keys_and_values_from_response"
]



def send_post_request(api_name, context):
    url = f"https://abc.com/conf4/api/configuration/{context}"
    credentials = base64.b64encode(b'username:password').decode('utf-8')
    headers = f"Authorization: Basic {credentials}"
    content_type = "Content-Type: application/json"
    
    # Example JSON body. Modify this as per your requirement.
    json_body = json.dumps({
        "apiName": api_name,
        "context": context
    })
    
    curl_command = f'curl -X POST "{url}" -H "{headers}" -H "{content_type}" -d \'{json_body}\''
    
    try:
        # Use shlex.split to handle the curl command properly
        process = subprocess.Popen(shlex.split(curl_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        if process.returncode == 0:
            return "Success", output.decode('utf-8')
        else:
            return "Error", error.decode('utf-8')
    except Exception as e:
        return "Exception", str(e)
        
def print_column_values(csv_file_path):
    # Open the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Iterate through each row in the CSV
        for index, row in enumerate(csv_reader):
            # Extract values from specified columns
            context = row.get('Column1.context', 'N/A')
            api_name = row.get('Column1.api-name', 'N/A')
            document_content_not_matching_with_conjur = row.get('Column1.document-content-not-matching-with-conjur',
                                                                'N/A')
            not_matching_properties = row.get('Column1.not-matching-properties', 'N/A')

            # Split the 'not-matching-properties' by commas for separate lines
            not_matching_properties_list = not_matching_properties.split(',')

            # Print the extracted values
            print(f"Row {index + 1}:")
            print(f"Context: {context}")
            print(f"API Name: {api_name}")
            print(f"Document Content Not Matching With Conjur: {document_content_not_matching_with_conjur}")
            print("Not Matching Properties:")
            for prop in not_matching_properties_list:
                print(f" - {prop.strip()}")
            print("-" * 50)


# Replace 'your_file_path.csv' with the path to your CSV file
csv_file_path = 'sampledataset-table.csv'
print_column_values(csv_file_path)
