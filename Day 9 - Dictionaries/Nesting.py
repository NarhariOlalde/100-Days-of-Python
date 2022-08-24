#Nesting Example

capitals = {
    "France": "Paris",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Germany": "Berlin",
}


travel_log = {
    "France": ["Paris", "Lyon", "Marseille"],
    "Spain": ["Madrid", "Barcelona", "Valencia"],
    "Italy": ["Rome", "Milan", "Naples"],
}

#Nesting Dictionary on Dictionary
cities_visited = {
    "France": {"Parades": ["Paris", "Lyon", "Marseille"], "Culture": "French", "total_days": 3},
    "Spain": {"Parades": ["Madrid", "Barcelona", "Valencia"], "Culture": "Spanish", "total_days": 3},
    "Italy": {"Parades": ["Rome", "Milan", "Naples"], "Culture": "Italian", "total_days": 3},
}

#Nesting Dictionary on Lists
travel_log = [
    {
        "Countries": "France",
        "Parades": ["Paris", "Lyon", "Marseille"],
        "Culture": "French",
        "total_days": 3
        },
    {
        "Countries": "Spain",
        "Parades": ["Madrid", "Barcelona", "Valencia"],
        "Culture": "Spanish",
        "total_days": 3
    },
    {
        "Countries": "Italy",
        "Parades": ["Rome", "Milan", "Naples"],
        "Culture": "Italian",
        "total_days": 3
        },
]

travel_log.append({"Countries": "Germany", "Parades": ["Berlin", "Munich", "Frankfurt"], "Culture": "German", "total_days": 3})

def add_new_country(country_name, country_parades, country_culture, country_days):
    new_country = {}
    new_country["Country"] = country_name
    new_country["Parades"] = country_parades
    new_country["Culture"] = country_culture
    new_country["total_days"] = country_days
    travel_log.append(new_country)

add_new_country("Germany", ["Berlin", "Munich", "Frankfurt"], "German", 3)
print(travel_log)