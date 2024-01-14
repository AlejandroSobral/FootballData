from clubWebScrap import clubWebScrap
import json
import yaml
import subprocess
import os
from pymongo import MongoClient
from arg_parsing import *
from misc import *

line_arguments = arguments_parsing()

os.chdir(line_arguments.working_directory)# Set Working Directory

cfg_params = read_cfg_yaml(set_yaml_file()) # YAML settable params

    

clubs_data = []
output_file = "clubs_data.json"

for i in range(cfg_params["web_scrap_min_index"], cfg_params["web_scrap_max_index"]):
    try:
        url = cfg_params["web_scrap_url"] + str(i)
        club_data = clubWebScrap(url)
        club = club_data["club"]
        print(f"Obteniendo datos de: {club}")
        clubs_data.append(club_data)
    except:
        print(f"Falló, no hay equipo para el índice {i}")


# Write the collected data into a JSON file

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(clubs_data, json_file, ensure_ascii=False, indent=4)

# Get the database using the method we defined in pymongo_test_insert file
from create_db import get_database
dbname = get_database()
collection_name = dbname["equipos"]

collection_name.insert_many([clubs_data][0])