import requests

class SWAPI():

    base_url = "https://swapi.co/api/"

    def __init__(self):
        self.planet_url = self.base_url + "planets/"
        self.people_url = self.base_url + "people/"
    
        planet_res = requests.get(self.planet_url)
        people_res = requests.get(self.people_url)

        planet_data = planet_res.json()
        people_data = people_res.json()

        self.num_planets = planet_data['count']
        self.num_people = people_data['count']

    def gather_planets(self):

        planets_left = self.num_planets
        page_counter = 1
        planet_objects_lst = list()

        while planets_left != 0:
            param_payload  = {'page': page_counter}
            temp_reponse = requests.get(self.planet_url, params=param_payload)

            json_data = temp_reponse.json()
            result_count = len(json_data['results'])

            for planet in json_data['results']:
                planet_objects_lst.append(planet)

            planets_left = planets_left - result_count
            page_counter = page_counter + 1

        return planet_objects_lst

    def gather_people(self):

        people_left = self.num_people
        page_counter = 1
        people_objects_lst = list()


        while people_left != 0:
            param_payload  = {'page': page_counter}
            temp_reponse = requests.get(self.people_url, params=param_payload)

            json_data = temp_reponse.json()
            result_count = len(json_data['results'])

            for person in json_data['results']:
                people_objects_lst.append(person)

            people_left = people_left - result_count
            page_counter = page_counter + 1

        return people_objects_lst