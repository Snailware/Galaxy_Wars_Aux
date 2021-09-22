# make a csv file with alot of objects for Galaxy Wars.
# NOTE cannot use "," in any data fields as that is delimiter.

from csv import writer
from random import choice, randint

def main():
    """use this to make lots of objects in csv file quick."""

    potential_primary_names = \
    [
        "Glaxon", "Bleezor", "Romulus", "Gallifrey", "Cybertron", "Krypton", 
        "Mora", "Kepler", "Arda", "Iotov", "Silon", "Nivion", "Doth", "Elea",
        "Halcyon", "Nuna", "Erus", "Talara", "Erd", "Cryon", "Terra", "Bruma",
        "Talaxia", "Eleum", "Alexandria", "Midgar", "Yharnam", "Lordran",
        "Izalith", "Oolacile", "Shulva", "Balamb", "Cainhurst", "Drangleic",
        "Junon", "Corel", "Gongaga", "Mideel", "Wutai", "Cardassia", "Besaid",
        "Kilika", "Luca", "Djose", "Macalania", "Guadosalam", "Bevelle",
        "Zanarkand", "Dali", "Burmecia", "Cleyra", "Treno", "Gulug"
    ]
    # list of primary names for planet generation.

    potential_secondary_names = \
    [
        "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", 
        "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho",
        "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega", "1", "2", 
        "3", "4", "5", "6", "7", "8", "9"
    ]
    # list of secondary names for planet generation.

    potential_descriptions = \
    [
        "A bustling mining planet rich with natural resources.",
        "A bleak & sparsely inhabited world.",
        "A gas giant surrounded by strange vessels.",
        "A small space station situated near a black hole.",
        "A small brutal planet where only the strong survive.",
        "A lush forest planet brimming with wildlife.",
        "A densely populated planet where everything is scarce.",
        "A dry planet where life exists without moisture.",
        "A blue ocean planet. strange vessels glide over its surface.",
        "A frozen tundra planet. blizzards rage continuously.",
        "A peaceful planet with a highly religious population.",
        "A dark & noxious planet. deadly spores blanket its surface.",
        "An ancient planet inhabited by a powerful humanoid species.",
        "A massive trading outpost. many species do business here.",
        "A volcanic planet. much of its surface is covered by magma.",
        "An abandoned mining colony thats now home to space pirates.",
        "A tropical planet where many species seem to vacation.",
        "A ruined wartorn planet. civil war has raged for generations.",
        "A mystical planet where beings with strange powers rule.",
        "An aquatic planet. research stations lie below its waves.",
        "A prison space station home to the worst of the worst.",
        "A mysterious planet whos inhabitants have long died.",
        "A beautiful tropical planet brimming with life.",
        "A derelict alien vessel drifting through space.",
        "The ruined world of a once mighty civilization.",
        "A quaint space station known for delicious food.",
        "A peaceful world inhabited by industrious people.",
        "A space ship graveyard inhabited by outlaws.",
        "A weapons research station shielded from prying eyes.",
        "A cloning facility that raises armies for the highest bidders.",
        "A storm ravaged world where it always rains.",
        "A merchant colony bustling with commerce.",
        "A world that fell to catastophic climate change.",
        "The seat of power to a terrible empire.",
        "The lush homeworld to a proud warrior race.",
        "A toxic planet whos people have long since fled.",
        "A technologically advanced world where energy is currency.",
        "A travelling food ship that is famous for its Ramen bowls."
    ]
    # list of descriptions for planet generation.

    with open("PlanetMaker\Planets.csv", "w") as obj_file:
    # open file in write mode.

        obj_writer = writer(obj_file, lineterminator = '\n')
        # create csv writer obj.

        obj_writer.writerow(["name", "description", "population"])
        # write headings.

        for i in range(0, 200):
        # iter x times.

            constructed_name = f"{choice(potential_primary_names)}-{choice(potential_secondary_names)}"
            description = choice(potential_descriptions)
            population = randint(3, 9999999)
            # randomly create data for obj.

            obj_writer.writerow([constructed_name, description, population])
            # write line to file.

    exit()
    # close program.

main()