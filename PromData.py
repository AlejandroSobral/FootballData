import pandas as pd
import argparse
from tabulate import tabulate

equipos_copas = ['Belgrano Athletic', 'Alumni', 'Rosario Athletic', 'Quilmes Athletic Club', 
 'Club Atlético San Isidro', 'Estudiantes de Buenos Aires', 'Newells Old Boys', 
 'Racing Club', 'Rosario Central', 'River Plate', 'Independiente', 'Porteño', 'Boca Juniors', 
 'Banfield', 'Huracán', 'Tiro Federal de Rosario', 'Sportivo Barracas', 'Sportivo Balcarce', 
 'Nueva Chicago', 'Central Córdoba (R)', 'San Lorenzo de Almagro', 'San Martín de Tucumán', 
 'Estudiantes de La Plata', 'Atlanta', 'Gimnasia y Esgrima de La Plata', 'Arsenal Fútbol Club', 
 'Vélez Sarsfield', 'Lanús', 'Tigre', 'Racing', 'Club Atlético Colón']

equipos_ligas = ['Saint Andrews', 'Lomas Athletic', 'Lomas Academy', 'Belgrano Athletic', 'English High School', 'Alumni', 
                 'Quilmes', 'Porteño', 'Racing Club', 'Estudiantes de La Plata', 'Boca Juniors', 'River Plate', 'Huracán', 'Independiente', 
                 'San Lorenzo de Almagro', 'Gimnasia y Esgrima La Plata', 'Estudiantil Porteño', 'Sportivo Barracas', 'Dock Sud', 'Vélez Sarsfield', 
                 'Chacarita Juniors', 'Rosario Central', 'Newells Old Boys', 
                 'River  Plate', 'Ferro Carril Oeste', 'Argentinos Juniors', 'Lanús', 'Vélez Sarsfield', 'Bánfield', 'Arsenal F.C.']

set_copas = set(equipos_copas)
set_ligas = set(equipos_ligas)
set_equipos = set_ligas.union(set_copas)
list_equipos = list((set_equipos))


parser = argparse.ArgumentParser()
parser.add_argument("--desde_anio", required=False)
parser.add_argument("--hasta_anio", required=False)
parser.add_argument("--equipo", choices = list_equipos, required=False)
parser.add_argument("--show", required=False)
args = parser.parse_args()

equipo = args.equipo
desde_anio = args.desde_anio
hasta_anio = args.hasta_anio
show = args.show


tabla_ligas = [
"1891","Liga",	                                                            "Saint Andrews"
,"1892","Liga",	                                                            "(No hubo torneo)"
,"1893","Liga",	                                                            "Lomas Athletic"
,"1894","Liga",	                                                            "Lomas Athletic"
,"1895","Liga",	                                                            "Lomas Athletic"
,"1896","Liga",	                                                            "Lomas Academy"
,"1897","Liga",	                                                            "Lomas Athletic"
,"1898","Liga",	                                                            "Lomas Athletic"
,"1899","Liga",	                                                            "Belgrano Athletic"
,"1900","Liga",	                                                            "English High School"
,"1901","Liga",	                                                            "Alumni"
,"1902","Liga",	                                                            "Alumni"
,"1903","Liga",	                                                            "Alumni"
,"1904","Liga",	                                                            "Belgrano Athletic"
,"1905","Liga",	                                                            "Alumni"
,"1906","Liga",	                                                            "Alumni"
,"1907","Liga",	                                                            "Alumni"
,"1908","Liga",	                                                            "Belgrano Athletic"
,"1909","Liga",	                                                            "Alumni"
,"1910","Liga",	                                                            "Alumni"
,"1911","Liga",	                                                            "Alumni"
,"1912", "Asociación Argentina de Football",                                "Quilmes"
,"1912", "Federación Argentina de Football",                                "Porteño"
,"1913", "Asociación Argentina de Football",                                "Racing Club"
,"1913", "Federación Argentina de Football",                                "Estudiantes de La Plata"
,"1914", "Asociación Argentina de Football",                                "Racing Club"
,"1914", "Federación Argentina de Football",                                "Porteño"
,"1915","Liga",                                                             "Racing Club"
,"1916","Liga",                                                             "Racing Club"
,"1917","Liga",                                                             "Racing Club"
,"1918","Liga",                                                             "Racing Club"
,"1919", "Asociación Argentina de Football",	                            "Boca Juniors"
,"1919", "Asociación Amateur Argentina de Football"	,                       "Racing Club"
,"1920", "Asociación Argentina de Football",                                "Boca Juniors"
,"1920", "Asociación Amateur Argentina de Football",                        "River Plate"
,"1921", "Asociación Argentina de Football",                                "Huracán"
,"1921", "Asociación Amateur Argentina de Football",                        "Racing Club"
,"1922", "Asociación Argentina de Football",                                "Huracán"
,"1922", "Asociación Amateur Argentina de Football",                        "Independiente"
,"1923", "Asociación Argentina de Football",                                "Boca Juniors"
,"1923", "Asociación Amateur Argentina de Football",                        "San Lorenzo de Almagro"
,"1924", "Asociación Argentina de Football",                                "Boca Juniors"
,"1924", "Asociación Amateur Argentina de Football",                        "San Lorenzo de Almagro"
,"1925", "Asociación Argentina de Football",                                "Huracán"
,"1925", "Asociación Amateur Argentina de Football",                        "Racing Club"
,"1926", "Asociación Argentina de Football",                                "Boca Juniors"
,"1926", "Asociación Amateur Argentina de Football",                        "Independiente"
,"1927",	"Liga",                                                         "San Lorenzo de Almagro"
,"1928",	"Liga",                                                         "Huracán"
,"1929",	"Liga",                                                         "Gimnasia y Esgrima La Plata"
,"1930",	"Liga",                                                         "Boca Juniors"
,"1931", "Asociación Argentina de Football",                                "Estudiantil Porteño"
,"1932", "Asociación Argentina de Football",                                "Sportivo Barracas"
,"1933", "Asociación Argentina de Football",                                "Dock Sud"
,"1934", "Asociación Argentina de Football",                                "Estudiantil Porteño"
,"1931" ,"Liga Argentina de Football",	                                    "Boca Juniors"
,"1932" ,"Liga Argentina de Football",	                                    "River Plate"
,"1933" ,"Liga Argentina de Football",	                                    "San Lorenzo de Almagro"
,"1934" ,"Liga Argentina de Football",	                                    "Boca Juniors"
,"1935"	,"Liga",                                                            "Boca Juniors"
,"1936" ,"Copa de Honor"	,                                               "San Lorenzo de Almagro"
,"1936" ,"Copa Campeonato"	,                                               "River Plate"
,"1936" ,"Copa de Oro"	,                                                   "River Plate"
,"1937", "Liga",	                                                        "River Plate"
,"1938", "Liga",	                                                        "Independiente"
,"1939", "Liga",	                                                        "Independiente"
,"1940", "Liga",	                                                        "Boca Juniors"
,"1941", "Liga",	                                                        "River Plate"
,"1942", "Liga",	                                                        "River Plate"
,"1943", "Liga",	                                                        "Boca Juniors"
,"1944", "Liga",	                                                        "Boca Juniors"
,"1945", "Liga",	                                                        "River Plate"
,"1946", "Liga",	                                                        "San Lorenzo de Almagro"
,"1947", "Liga",	                                                        "River Plate"
,"1948", "Liga",	                                                        "Independiente"
,"1949", "Liga",	                                                        "Racing Club"
,"1950", "Liga",	                                                        "Racing Club"
,"1951", "Liga",	                                                        "Racing Club"
,"1952", "Liga",	                                                        "River Plate"
,"1953", "Liga",	                                                        "River Plate"
,"1954", "Liga",	                                                        "Boca Juniors"
,"1955", "Liga",	                                                        "River Plate"
,"1956", "Liga",	                                                        "River Plate"
,"1957", "Liga",	                                                        "River Plate"
,"1958", "Liga",	                                                        "Racing Club"
,"1959", "Liga",	                                                        "San Lorenzo de Almagro"
,"1960", "Liga",	                                                        "Independiente"
,"1961", "Liga",	                                                        "Racing Club"
,"1962", "Liga",	                                                        "Boca Juniors"
,"1963", "Liga",	                                                        "Independiente"
,"1964", "Liga",	                                                        "Boca Juniors"
,"1965", "Liga",	                                                        "Boca Juniors"
,"1966", "Liga",	                                                        "Racing Club"
,"1967" ,"(Metropolitano)",	                                                "Estudiantes de La Plata"
,"1967" ,"(Nacional)",                                                      "Independiente"
,"1968" ,"(Metropolitano)",                                                 "San Lorenzo de Almagro"
,"1968" ,"(Nacional)",                                                      "Vélez Sarsfield"
,"1969" ,"(Metropolitano)",                                                 "Chacarita Juniors"
,"1969" ,"(Nacional)",                                                      "Boca Juniors"
,"1970" ,"(Metropolitano)",                                                 "Independiente"
,"1970" ,"(Nacional)",                                                      "Boca Juniors"
,"1971" ,"(Metropolitano)",                                                 "Independiente"
,"1971" ,"(Nacional)",                                                      "Rosario Central"
,"1972" ,"(Metropolitano)",                                                 "San Lorenzo de Almagro"
,"1972" ,"(Nacional)"	,                                                   "San Lorenzo de Almagro"
,"1973" ,"(Metropolitano)"	,                                               "Huracán"
,"1973" ,"(Nacional)"	,                                                   "Rosario Central"
,"1974" ,"(Metropolitano)"	,                                               "Newells Old Boys"
,"1974" ,"(Nacional)"	,                                                   "San Lorenzo de Almagro"
,"1975" ,"(Metropolitano)"	,                                               "River Plate"
,"1975" ,"(Nacional)"	,                                                   "River  Plate"
,"1976" ,"(Metropolitano)"	,                                               "Boca Juniors"
,"1976" ,"(Nacional)"	,                                                   "Boca Juniors"
,"1977" ,"(Metropolitano)"	,                                               "River Plate"
,"1977" ,"(Nacional)"	,                                                   "Independiente"
,"1978" ,"(Metropolitano)"	,                                               "Quilmes"
,"1978" ,"(Nacional)"	,                                                   "Independiente"
,"1979" ,"(Metropolitano)",	                                                "River Plate"
,"1979" ,"(Nacional)"	,                                                   "River Plate"
,"1980" ,"(Metropolitano)",	                                                "River Plate"
,"1980" ,"(Nacional)"	,                                                   "Rosario Central"
,"1981" ,"(Metropolitano)",	                                                "Boca Juniors"
,"1981" ,"(Nacional)"	,                                                   "River Plate"
,"1982" ,"(Metropolitano)"	,                                               "Estudiantes de La Plata"
,"1982" ,"(Nacional)"	,                                                   "Ferro Carril Oeste"
,"1983" ,"(Metropolitano)"	,                                               "Independiente"
,"1983" ,"(Nacional)"	,                                                   "Estudiantes de La Plata"
,"1984" ,"(Metropolitano)",                                                 "Argentinos Juniors"
,"1984" ,"(Nacional)"	,                                                   "Ferro Carril Oeste"
,"1985" ,"(Nacional)"	,                                                   "Argentinos Juniors"
,"1986","Liga",	                                                            "River Plate"
,"1987","Liga",	                                                            "Rosario Central"
,"1988","Liga",	                                                            "Newells Old Boys"
,"1989","Liga",	                                                            "Independiente"
,"1990","Liga",	                                                            "River Plate"
,"1991","Liga",	                                                            "Newells Old Boys"
,"1991","Apertura",                                                         "River Plate"
,"1992","Clausura",                                                         "Newells Old Boys"
,"1992","Apertura",                                                         "Boca Juniors"
,"1993","Clausura",                                                         "Vélez Sarsfield"
,"1993","Apertura",                                                         "River Plate"
,"1994","Clausura",                                                         "Independiente"
,"1994","Apertura",                                                         "River Plate"
,"1995","Clausura",                                                         "San Lorenzo de Almagro"
,"1995","Apertura",                                                         "Vélez Sarsfield"
,"1996","Clausura",                                                         "Vélez Sarsfield"
,"1996","Apertura",                                                         "River Plate"
,"1997","Clausura",                                                         "River Plate"
,"1997","Apertura",                                                         "River Plate"
,"1998","Clausura",                                                         "Vélez Sarsfield"
,"1998","Apertura",                                                         "Boca Juniors"
,"1999","Clausura",                                                         "Boca Juniors"
,"1999","Apertura",                                                         "River Plate"
,"2000","Clausura",                                                         "River Plate"
,"2000","Apertura",                                                         "Boca Juniors"
,"2001","Clausura",                                                         "San Lorenzo de Almagro"
,"2001","Apertura",                                                         "Racing Club"
,"2002","Clausura",                                                         "River Plate"
,"2002","Apertura",                                                         "Independiente"
,"2003","Clausura",                                                         "River Plate"
,"2003","Apertura",                                                         "Boca Juniors"
,"2004","Clausura",                                                         "River Plate"
,"2004","Apertura",                                                         "Newells Old Boys"
,"2005","Clausura",                                                         "Vélez Sarsfield"
,"2005","Apertura",                                                         "Boca Juniors"
,"2006","Clausura",                                                         "Boca Juniors"
,"2006","Apertura",                                                         "Estudiantes de La Plata"
,"2007","Clausura",                                                         "San Lorenzo de Almagro"
,"2007","Apertura",                                                         "Lanús"
,"2008","Clausura",                                                         "River Plate"
,"2008","Apertura",                                                         "Boca Juniors"
,"2009","Clausura",                                                         "Vélez Sarsfield"
,"2009","Apertura",                                                         "Bánfield"
,"2010","Clausura",                                                         "Argentinos Juniors"
,"2010","Apertura",                                                         "Estudiantes de La Plata"
,"2011","Clausura",                                                         "Vélez Sarsfield"
,"2011","Apertura",                                                         "Boca Juniors"
,"2012","Clausura",                                                         "Arsenal F.C."
,"2012","Torneo Inicial"	,                                               "Vélez Sarsfield"
,"2013","Torneo Final",	                                                    "Newells Old Boys"
,"2013","Campeón de Primera División 2012/13"	,                           "Vélez Sarsfield"
,"2013","Torno Inicial"	,                                                   "San Lorenzo de Almagro"
,"2014","Torneo Final",	                                                    "River Plate"
,"2014","Torneo Inicial"	,                                               "Racing Club"
,"2015","Campeonato de Primera División",	                                "Boca Juniors"
,"2016","Campeonato de Primera División",	                                "Lanús"
,"2018", "Superliga",                                                       "Boca Juniors"
,"2019", "Superliga",                                                       "Racing Club"
,"2020", "Superliga",                                                       "Boca Juniors"
,"2021", "Torneo Socios de la Liga Profesional",                            "River Plate"
,"2022", "Torneo Binance",                                                   "Boca Juniors"]

                                  
tabla_copas_nac = [
"1900", "Tie Cup Competition 1900",           	                             "Belgrano Athletic"
,"1901","Tie Cup Competition 1901",                                          "Alumni"
,"1902","Tie Cup Competition 1902",                                          "Rosario Athletic"
,"1903","Tie Cup Competition 1903",                                          "Alumni"
,"1904","Tie Cup Competition 1904",                                          "Rosario Athletic"
,"1905","Tie Cup Competition 1905",                                          "Rosario Athletic"
,"1905","Copa de Honor MCBA 1905",                                           "Alumni"
,"1906","Tie Cup Competition 1906",                                          "Alumni"
,"1906","Copa de Honor MCBA 1906",                                           "Alumni"
,"1907","Copa Competencia Jockey Club 1907",                                 "Alumni"
,"1907","Copa de Honor MCBA 1907",	                                         "Belgrano Athletic"
,"1908","Copa Competencia Jockey Club 1908",                                 "Alumni"
,"1908","Copa de Honor MCBA 1908",	                                         "Quilmes Athletic Club"
,"1909","Copa Competencia Jockey Club 1909",                                 "Alumni"
,"1909","Copa de Honor MCBA 1909",	                                         "Club Atlético San Isidro"
,"1910","Copa Competencia Jockey Club 1910",                                 "Estudiantes de Buenos Aires"
,"1911","Copa Competencia Jockey Club 1911",	                             "Club Atlético San Isidro"
,"1911","Copa de Honor MCBA 1911",	                                         "Newells Old Boys"
,"1912","Copa de Honor MCBA 1912",	                                         "Racing Club"
,"1912","Copa Competencia Jockey Club 1912",	                             "Club Atlético San Isidro"
,"1913","Copa Competencia Jockey Club 1913",	                             "Club Atlético San Isidro"
,"1913","Copa de Honor MCBA 1913",	                                         "Racing Club"
,"1913","Copa Competencia La Nación 1913",	                                 "Rosario Central"
,"1913","Copa Carlos Ibarguren 1913",	                                     "Racing Club"
,"1914","Copa Competencia Jockey Club 1914",	                             "River Plate"
,"1914","Copa Carlos Ibarguren 1914",	                                     "Racing Club"
,"1914","Copa Competencia La Nación 1914",	                                 "Independiente"
,"1915","Copa Competencia Jockey Club 1915",	                             "Porteño"
,"1915","Copa Carlos Ibarguren 1915",	                                     "Rosario Central"
,"1915","Copa de Honor MCBA 1915",	                                         "Racing Club"
,"1916","Copa de Honor MCBA 1916",	                                         "Rosario Central"
,"1916","Copa Competencia Jockey Club 1916",                                 "Rosario Central"
,"1916","Copa Carlos Ibarguren 1916",	                                     "Racing Club"
,"1917","Copa Competencia Jockey Club 1917",                                 "Independiente"
,"1917","Copa de Honor MCBA 1917",	                                         "Racing Club"
,"1917","Copa Carlos Ibarguren 1917",	                                     "Racing Club"
,"1918","Copa Competencia Jockey Club 1918",                                 "Porteño"
,"1918","Copa de Honor MCBA 1918",	                                         "Independiente"
,"1918","Copa Carlos Ibarguren 1918",	                                     "Racing Club"
,"1919","Copa Competencia Jockey Club 1919",                                 "Boca Juniors"
,"1919","Copa Carlos Ibarguren 1919",	                                     "Boca Juniors"
,"1920","Copa de Honor MCBA 1920",	                                         "Banfield"
,"1920","Copa Estímulo 1920",	                                             "Huracán"
,"1920","Copa Competencia Asociación Amateurs 1920",                         "Rosario Central"
,"1920","Copa Carlos Ibarguren 1920",	                                     "Tiro Federal de Rosario"
,"1921","Copa Carlos Ibarguren 1921",	                                     "Newells Old Boys"
,"1921","Copa Competencia Jockey Club 1921",	                             "Sportivo Barracas"
,"1922","Copa Carlos Ibarguren 1922",                                        "Huracán"
,"1923","Copa Carlos Ibarguren 1923",                                        "Boca Juniors"
,"1924","Copa Carlos Ibarguren 1924",                                        "Boca Juniors"
,"1924","Copa Competencia Asociación Amateurs 1924",	                     "Independiente"
,"1925","Copa Carlos Ibarguren 1925",	                                     "Huracán"
,"1925","Copa Competencia Jockey Club 1925",	                             "Boca Juniors"
,"1925","Copa Competencia Asociación Amateurs 1925",	                     "Independiente"
,"1926","Copa Competencia Asociación Amateurs 1926",	                     "Independiente"
,"1926","Copa Estímulo 1926",	                                             "Boca Juniors"
,"1931","Copa Competencia 1931",	                                         "Sportivo Balcarce"
,"1933","Copa Competencia Jockey Club 1933",	                             "Nueva Chicago"
,"1932","Copa Competencia Liga Argentina 1932",	                             "River Plate"
,"1932","Copa de Honor Beccar Varela 1932",	                                 "Racing Club"
,"1933","Copa Competencia 1933",	                                         "Racing Club"
,"1933","Copa de Honor Beccar Varela 1933",	                                 "Central Córdoba (R)"
,"1937","Copa Carlos Ibarguren 1937",                                        "River Plate"
,"1938","Copa Carlos Ibarguren 1938",                                        "Independiente"
,"1939","Copa Carlos Ibarguren 1939",                                        "Independiente"
,"1939","Copa Adrián Escobar 1939",                                          "Independiente"
,"1940","Copa Carlos Ibarguren 1940",                                        "Boca Juniors"
,"1941","Copa Adrián Escobar 1941",                                          "River Plate"
,"1941","Copa Carlos Ibarguren 1941",                                        "River Plate"
,"1942","Copa Carlos Ibarguren 1942",                                        "River Plate"
,"1942","Copa Adrián Escobar 1942",                                          "Huracán"
,"1943","Copa Adrián Escobar 1943",                                          "Huracán"
,"1943","Copa General de División Pedro Pablo Ramírez 1943",	             "San Lorenzo de Almagro"
,"1944","Copa Carlos Ibarguren 1944",	                                     "Boca Juniors"
,"1944","Copa General de División Pedro Pablo Ramírez 1944",	             "San Martín de Tucumán"
,"1944","Copa Competencia-Británica 1944",	                                 "Huracán"
,"1944","Copa Adrián Escobar 1944",	                                         "Estudiantes de La Plata"
,"1945","Copa General de División Pedro Pablo Ramírez 1945",	             "Estudiantes de La Plata"
,"1945","Copa Competencia-Británica 1945",	                                 "Racing Club"
,"1946","Copa Competencia George VI 1946",	                                 "Boca Juniors"
,"1949","Copa Adrián Escobar 1949",	                                         "Newells Old Boys"
,"1952","Copa Carlos Ibarguren 1952",	                                     "River Plate"
,"1958","Copa Suecia 1958",	                                                 "Atlanta"
,"1969","Copa Argentina 1969",	                                             "Boca Juniors"
,"1993","Copa Centenario de la AFA 1993",	                                 "Gimnasia y Esgrima de La Plata"
,"2012","Copa Argentina 2012",	                                             "Boca Juniors"
,"2012","Supercopa Argentina 2012",	                                         "Arsenal Fútbol Club"
,"2013","Copa Argentina 2013",	                                             "Arsenal Fútbol Club"
,"2013","Supercopa Argentina 2013",	                                         "Vélez Sarsfield"
,"2013","Copa Campeonato Primera División 2013/2014",	                     "River Plate"
,"2013","Copa Argentina 2013/2014",             	                         "Huracán"
,"2014","Supercopa Argentina 2014",	                                         "Huracán"
,"2014","Copa Argentina 2014/2015",	                                         "Boca Juniors"
,"2015","Supercopa 2015",	                                                 "San Lorenzo de Almagro"
,"2016","Copa Bicentenario 2016",	                                         "Lanús"
,"2016","Copa Argentina 2015/2016",	                                         "River Plate"
,"2016","Supercopa 2016",	                                                 "Lanús"
,"2017","Copa Argentina 2017",	                                             "River Plate"
,"2017","Supercopa Argentina 2017",	                                         "River Plate"
,"2017","Copa Argentina 2017/2018",                                          "Rosario Central"
,"2018","Supercopa Argentina 2018" ,                                         "Boca Juniors"
,"2019","Copa de la Superliga 2019",                                         "Tigre"
,"2019","Copa Argentina 2019",	                                             "River Plate"
,"2019","Trofeo de Campeones de la Superliga 2019",	                         "Racing"
,"2020","Copa Diego Armando Maradona 2020 - 2021", 	                         "Boca Juniors"
,"2019","Supercopa Argentina 2019",                                          "River Plate"
,"2021","Copa de la Liga Profesional  2021",                                 "Club Atlético Colón"
,"2020","Copa Argentina 2020",	                                             "Boca Juniors"
,"2021","Trofeo de Campeones 2021",	                                         "River Plate"
]



year_list = []
data_list = []
team_list = []
i = 0
for element in tabla_ligas:
    if (i == 0):
        year_list.append(element)
        i = i + 1
        continue
    if(i == 1):
        data_list.append(element)
        i = i + 1
        continue
    if(i == 2):
        team_list.append(element)
        i = 0
        
int_list = []
for year in year_list:
    int_list.append(int(year))
df_ligas = pd.DataFrame({"Anio": int_list,
                   "Competicion": data_list,
                  "Campeón": team_list
                    })


year_list = []
data_list = []
team_list = []
i = 0
for element in tabla_copas_nac:
    if (i == 0):
        year_list.append(element)
        i = i + 1
        continue
    if(i == 1):
        data_list.append(element)
        i = i + 1
        continue
    if(i == 2):
        team_list.append(element)
        i = 0

int_list = []
for year in year_list:
    int_list.append(int(year))
df_cop_nac = pd.DataFrame({"Anio": int_list,
                   "Competicion": data_list,
                  "Campeón": team_list
                    })


if(desde_anio):
    anio = desde_anio
    rslt_df = df_cop_nac[df_cop_nac["Anio"] > anio]
    print(rslt_df)
    camps_list = rslt_df["Campeón"].unique()
    for camp in camps_list:
        rslt_df_2 = rslt_df[rslt_df["Campeón"] == camp]
        if (len(rslt_df_2)>0):
            print("El equipo", camp, "ganó",len(rslt_df_2), "Copas Nacionales desde", anio )
        if(show):
            print(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))

if(equipo):
    rslt_df = df_cop_nac[df_cop_nac["Campeón"] == equipo]
    #print("Copas Nacionales\n", rslt_df)
    camps_list = rslt_df["Campeón"].unique()
    for camp in camps_list:
        rslt_df_2 = rslt_df[rslt_df["Campeón"] == camp]
        if (len(rslt_df_2)>0):
            print("----------------")
            print("El equipo", camp, "ganó",len(rslt_df_2), "Copas Nacionales")
            if(show):
                print("----------------")
                print(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))
    rslt_df = df_ligas[df_ligas["Campeón"] == equipo]
    #print("Ligas Locales\n", rslt_df)
    camps_list = rslt_df["Campeón"].unique()
    for camp in camps_list:
        rslt_df_2 = rslt_df[rslt_df["Campeón"] == camp]
        if (len(rslt_df_2)>0):
            print("El equipo", camp, "ganó",len(rslt_df_2), "Ligas Locales")
            if(show):
                print("----------------")
                print(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))
                