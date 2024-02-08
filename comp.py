import csv


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
