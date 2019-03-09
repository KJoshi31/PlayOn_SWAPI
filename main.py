from controllers.controller import Swapi_Controller

s = Swapi_Controller()
print("Welcome to SWAPI Data Viewer for PlayOn!")
print("Please wait while the program loads")
s.load_data()
print("Finished Loading!")

menu_on = True
menu_options = ["1","2","3", "4"]

while menu_on:
    print("---Menu---")
    print("1. Print Planet List")
    print("2. Print People List")
    print("3. Search for Residents on Planet")
    print("4. Exit")
    print("Please type select (EX: 1):")
    num_select = input().strip()

    if num_select in menu_options:

        if num_select == "1":
            s.print_planets()
        if num_select == "2":
            s.print_people()

        #satisfies requirement 5.
        if num_select == "3":
            print("Please type the planet: ")
            planet_input = input().strip()
            planet_input = planet_input.title()
            resident_names, planet_found = s.get_planet_resident_names(planet_input)

            if planet_found:
                if len(resident_names) == 0:
                    print("No Resident Data for {}".format(planet_input))
                else:
                    print("Residents of {}:".format(planet_input))
                    
                    for name in resident_names:
                        print("\t{}".format(name))
            else:
                print("Planet does not exist, please try again")

        
        if num_select == "4":
            print("Thank You, See You Next Time")
            menu_on = False

    if num_select not in menu_options:
        print("Please enter a valid number input from 1-4")



