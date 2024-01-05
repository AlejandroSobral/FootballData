import json

with open('clubs_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)


def get_existing_clubs(data):    
    club_names = [club_info["club"] for club_info in data]
    return club_names


def get_title_count(club_name):
    for club_info in data:
        if club_info["club"] == club_name:
            
            title_count = {
                "Ligas nacionales":len(club_info["nac_titles"]),
                "Copas Nacionales":len(club_info["loc_titles"]),
                "Títulos Internacionales":len(club_info["int_titles"])
            }
            return title_count


def get_total_older_titles(club_name, year):
    with open('clubs_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    older_titles = 0
    
    for club_info in data:
        if club_info["club"] == club_name:
            for title_type in ["nac_titles", "int_titles", "loc_titles"]:
                for title in club_info[title_type]:
                    title_year = int(title["year"])
                    if title_year < year:
                        older_titles += 1
            break
    
    return older_titles


def get_total_newer_titles(club_name, year):
    with open('clubs_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    newer_titles = []
    
    for club_info in data:
        if club_info["club"] == club_name:
            for title_type in ["nac_titles", "int_titles", "loc_titles"]:
                for title in club_info[title_type]:
                    title_year = int(title["year"])
                    if title_year > year:
                        title_info = {
                            "name": title["name"],
                            "year": title["year"],
                            "category": title["category"],
                            "type": "Copa Nacional" if title_type == "nac_titles" else (
                                "Título Internacional" if title_type == "int_titles" else "Liga Nacional"
                            )
                        }
                        newer_titles.append(title_info)
            break
            
    sorted_titles = sorted(newer_titles, key=lambda x: int(x['year']))
    
    format_response = {
        "Titles Count": len(sorted_titles),
        "Titles": sorted_titles
    }
    
    return format_response

existing_clubs = get_existing_clubs(data)
existing_clubs.sort()

import PySimpleGUI as psg
#set the theme for the screen/window
psg.theme('SandyBeach')
#define layout

layout=[[psg.Text('Elegir equipo',size=(20, 1), font='Lucida',justification='left')],
        [psg.Combo(existing_clubs,default_value='Club Atlético San Lorenzo de Almagro',key='equipo')],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]
#Define Window
win =psg.Window('Customise your Journey',layout)
#Read  values entered by user
e,v=win.read()
#close first window
win.close()
#access the selected value in the list box and add them to a string
strx=""
for val in v:
    strx=strx+ " "+ val+","
        
#display string in a popup         
psg.popup('Equipo seleccionado :'+ v["equipo"])

#print("Información disponible para: ",list_equipos)
equipo = v["equipo"]


def print_titles(titles_data):
    print("{:<25} {:<25} {:<10} {:<15} {:<15}".format("Name", "Type", "Year", "Category", "Count"))
    print("-" * 75)
    
    titles_count = titles_data['Titles Count']
    titles_list = titles_data['Titles']
    
    for title in titles_list:
        name = title['name']
        year = title['year']
        type = title['type']
        category = title['category']
        
        print("{:<25} {:<25} {:<10} {:<15} {:<15}".format(name, type, year, category, titles_count))


def calculate_total_titles_since_year(club_info, year):
    total_titles = 0
    for title_type in ["nac_titles", "int_titles", "loc_titles"]:
        for title in club_info[title_type]:
            title_year = int(title["year"])
            if title_year >= year:
                total_titles += 1
    return total_titles

def sort_clubs_by_total_titles(data, year):
    sorted_clubs = sorted(data, key=lambda club_info: calculate_total_titles_since_year(club_info, year), reverse=True)
    return sorted_clubs

print("------------------------")
print(get_title_count(equipo))
year = input("El año ")
#print("------------------------")
# print(print_titles(get_total_newer_titles(equipo ,int(year))))
print(sort_clubs_by_total_titles(data, int(year)))






