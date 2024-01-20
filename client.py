import argparse
import requests

def format_return(item_list: list[dict]) -> str:
    """
    Formats a tabular response based on the input dictionary.
    :param item_dict: dict, The dictionary of items to format.
    :return: str, Table format
    """
    table_header_separator = "-"
    table_header_column_break = "+"
    table_column_separator = "|"
    table_headers = ["name", "quantity"]
    padding = 5 # Pad five extra spaces after max length item
    table_output = ""

    max_width_dict = {header: len(header) for header in table_headers}
    for item in item_list:
        for elem in item.items():
            if len(str(elem[1])) > max_width_dict[elem[0]]:
                max_width_dict[elem[0]] = len(str(elem[1]))
    
    # Now, we can construct the table
    table_header = ""
    for header in table_headers:
        extra_space = " " * (max_width_dict[header] - len(header) + padding)
        table_header += f"{header}{extra_space}| "
    table_header = table_header[:-2] # Remove extra column sep and space on last element
    
    # Table header line
    table_header_line = ""
    for header in table_headers:
        sep = "-" * (max_width_dict[header] + padding) + "+"
        table_header_line += sep
    table_header_line = table_header_line[:-2]

    # Table body
    table_body = ""
    for item in item_list:
        elem_row = ""
        for elem in item.items():
            elem_padding = " " * (max_width_dict[elem[0]] - len(str(elem[1])) + padding)
            elem_row += f"{elem[1]}{elem_padding}| "
        elem_row = elem_row[:-2]
        table_body += elem_row + "\n"

    table_output = "\n".join([table_header, table_header_line, table_body])
    print(table_output)

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("action", choices=["list", "add"])

args = parser.parse_args()
action = args.action

# Define URL
base_url = "http://localhost:5000"

# Parse action
if action == "list":
    endpoint = f"{base_url}/items/"
    try:
        response = requests.get(endpoint)
        if response.status_code > 200:
            print("Error: An error occured getting the inventory.")
    except Exception as e:
        print(f"Error: An error occured making the request. Please contact a system administrator.")
    else:
        format_return(response.json())