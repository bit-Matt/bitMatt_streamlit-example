provinces_dict = {
    "ILOCOS NORTE": "Ilocos Norte",
    "ILOCOS SUR": "Ilocos Sur",
    "LA UNION": "La Union",
    "PANGASINAN": "Pangasinan",

    "BATANES": "Batanes",
    "CAGAYAN": "Cagayan",
    "ISABELA": "Isabela",
    "NUEVA VIZCAYA": "Nueva Vizcaya",
    "QUIRINO": "Quirino",

    "AURORA": "Aurora",
    "BATAAN": "Bataan",
    "BULACAN": "Bulacan",
    "NUEVA ECIJA": "Nueva Ecija",
    "PAMPANGA": "Pampanga",
    "TARLAC": "Tarlac",
    "ZAMBALES": "Zambales",

    "ALBAY": "Albay",
    "CAMARINES NORTE": "Camarines Norte",
    "CAMARINES SUR": "Camarines Sur",
    "CATANDUANES": "Catanduanes",
    "MASBATE": "Masbate",
    "SORSOGON": "Sorsogon",

    "AKLAN": "Aklan",
    "ANTIQUE": "Antique",
    "CAPIZ": "Capiz",
    "ILOILO": "Iloilo",
    "GUIMARAS": "Guimaras",

    "BOHOL": "Bohol",
    "CEBU": "Cebu",
    "SIQUIJOR": "Siquijor",

    "BILIRAN": "Biliran",
    "EASTERN SAMAR": "Eastern Samar",
    "LEYTE": "Leyte",
    "NORTHERN SAMAR": "Northern Samar",
    "SOUTHERN LEYTE": "Southern Leyte",
    "SAMAR (WESTERN SAMAR)": "Samar",

    "CITY OF ISABELA": "City of Isabela",
    "ZAMBOANGA DEL NORTE": "Zamboanga del Norte",
    "ZAMBOANGA DEL SUR": "Zamboanga del Sur",
    "ZAMBOANGA SIBUGAY": "Zamboanga Sibugay",

    "BUKIDNON": "Bukidnon",
    "CAMIGUIN": "Camiguin",
    "LANAO DEL NORTE": "Lanao del Norte",
    "MISAMIS OCCIDENTAL": "Misamis Occidental",
    "MISAMIS ORIENTAL": "Misamis Oriental",

    "COMPOSTELA VALLEY": "Compostela Valley",
    "DAVAO DEL NORTE": "Davao del Norte",
    "DAVAO DEL SUR": "Davao del Sur",
    "DAVAO ORIENTAL": "Davao Oriental",
    "DAVAO OCCIDENTAL": "Davao Occidental",

    "COTABATO (NORTH COTABATO)": "Cotabato",
    "COTABATO CITY (NOT A PROVINCE)": "Cotabato City",
    "SOUTH COTABATO": "South Cotabato",
    "SARANGANI": "Sarangani",
    "SULTAN KUDARAT": "Sultan Kudarat",

    "AGUSAN DEL NORTE": "Agusan del Norte",
    "AGUSAN DEL SUR": "Agusan del Sur",
    "DINAAGAT ISLANDS": "Dinagat Islands",
    "SURIGAO DEL NORTE": "Surigao del Norte",
    "SURIGAO DEL SUR": "Surigao del Sur",

    "ABRA": "Abra",
    "APAYAO": "Apayao",
    "BENGUET": "Benguet",
    "IFUGAO": "Ifugao",
    "KALINGA": "Kalinga",
    "MOUNTAIN PROVINCE": "Mountain Province",

    "MARINDUQUE": "Marinduque",
    "OCCIDENTAL MINDORO": "Occidental Mindoro",
    "ORIENTAL MINDORO": "Oriental Mindoro",
    "PALAWAN": "Palawan",
    "ROMBLON": "Romblon",

    "NEGROS OCCIDENTAL": "Negros Occidental",
    "NEGROS ORIENTAL": "Negros Oriental"
}

provinces_list = list(provinces_dict.keys())

def get_key_province(val):
    for key, value in provinces_dict.items():
        if val == value:
            return key
