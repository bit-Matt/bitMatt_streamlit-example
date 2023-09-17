regions_dict = {
    'Region I': {
        'value': "REGION I (ILOCOS REGION)",
        "path": "data/jsons/region-1.geojson"
    },
    'Region II': {
        'value': "REGION II (CAGAYAN VALLEY)",
        "path": "data/jsons/region-2.geojson"
    },
    'Region III': {
        'value': "REGION III (CENTRAL LUZON)",
        "path": "data/jsons/region-3.geojson"
    },
    'Region IV-B': {
        'value': "MIMAROPA REGION",
        "path": "data/jsons/region-17.geojson"
    },
    'Region V': {
        'value': "REGION V (BICOL REGION)",
        "path": "data/jsons/region-5.geojson"
    },
    'Region VI': {
        'value': "REGION VI (WESTERN VISAYAS)",
        "path": "data/jsons/region-6.geojson"
    },
    'Region VII': {
        'value': "REGION VII (CENTRAL VISAYAS)",
        "path": "data/jsons/region-7.geojson"
    },
    'Region VIII': {
        'value': "REGION VIII (EASTERN VISAYAS)",
        "path": "data/jsons/region-8.geojson"
    },
    'Region IX': {
        'value': "REGION IX (ZAMBOANGA PENINSULA)",
        "path": "data/jsons/region-9.geojson"
    },
    'Region X': {
        'value': "REGION X (NORTHERN MINDANAO)",
        "path": "data/jsons/region-10.geojson"
    },
    'Region XI': {
        'value': "REGION XI (DAVAO REGION)",
        "path": "data/jsons/region-11.geojson"
    },
    'Region XII': {
        'value': "REGION XII (SOCCSKSARGEN)",
        "path": "data/jsons/region-12.geojson"
    },
    'Region XIII': {
        'value': "REGION XIII (CARAGA)",
        "path": "data/jsons/region-13.geojson"
    },
    'Cordillera Administrative Region': {
        'value': "CORDILLERA ADMINISTRATIVE REGION (CAR)",
        "path": "data/jsons/region-14.geojson"
    },
}


regions_list = ['All Regions'] + list(regions_dict.keys())


def get_key(val):
    for key, value in regions_dict.items():
        if val == value["value"]:
            return key



