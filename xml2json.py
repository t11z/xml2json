import sys
import json
import xmltodict

def convert(xml_str):
    data_dict = xmltodict.parse(xml_str)
    json_data = json.dumps(data_dict)
    return json_data

if __name__ == "__main__":
    xml_input = sys.stdin.read()
    json_output = convert(xml_input)
    print(json_output)
