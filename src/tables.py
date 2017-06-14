"""
    Reads tables from tables.json file and make them python lists
"""
import json

with open('src/tables.json') as table_file:
    json_data = json.load(table_file)

Rcon = json_data['Rcon']

S_box = json_data['S_box']
inS_box = json_data['inS_box']

table_2 = json_data['table_2']
table_3 = json_data['table_3']
table_9 = json_data['table_9']
table_11 = json_data['table_11']
table_13 = json_data['table_13']
table_14 = json_data['table_14']
