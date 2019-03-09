from api.SWAPI_Connection import SWAPI
from models.Person import Person
from models.Planet import Planet

class Swapi_Controller():

    def __init__(self):
        #lists for requirement 2.
        self.planet_obj_list = list()
        self.people_obj_list = list()

        # data structure for requirement 4.
        self.joined_structure = dict() 

    # satisifies requirement 2.
    def load_data(self):
        swapi_conn = SWAPI()

        list_planet_dicts = swapi_conn.gather_planets()
        list_people_dicts = swapi_conn.gather_people()

        # satisfies requirement 1.
        [self.planet_obj_list.append(Planet(p['url'], p['name'], p['residents'])) for p in list_planet_dicts]
        [self.people_obj_list.append(Person(p['url'], p['name'], p['homeworld'])) for p in list_people_dicts]

        for planet_obj in self.planet_obj_list:
            temp_people_obj_list = list()

            for people_obj in self.people_obj_list:

                if people_obj.url_id in planet_obj.residents_list:

                    temp_people_obj_list.append(people_obj)


            self.joined_structure[planet_obj] = temp_people_obj_list

    # helps satisfy requirement 5.
    def get_planet_resident_names(self, planet_name):
        
        names_list = list()

        planet_name = planet_name.title()

        planet_found = False
        for Planet, people_list in self.joined_structure.items():
            
            if planet_name == Planet.name:
                planet_found = True
                [names_list.append(p.name) for p in people_list]
        
        return names_list, planet_found
                
    # method that satisfies requirement 3.
    def print_planets(self):
        print("List of Planets:")
        [print("\t{}".format(p)) for p in self.planet_obj_list]

    # method that satisfies requirement 3.
    def print_people(self):
        print("List of People:")
        [print("\t{}".format(p)) for p in self.people_obj_list]