# make a csv file with alot of planets for Galaxy Wars.
# NOTE cannot use "," in any data fields as that is delimiter.

from csv import writer
from random import choice, randint

def main():
    """use this to make lots of planets in csv file quick."""

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
        "a bustling mining planet rich with natural resources.",
		"a bleak & sparsely inhabited world.",
		"a gas giant surrounded by strange vessels.",
		"a small space station situated near a black hole.",
		"a small brutal planet where only the strong survive.",
		"a lush forest planet brimming with wildlife.",
		"a densely populated planet where everything is scarce.",
		"a dry planet where life exists without moisture.",
		"a blue ocean planet. strange vessels glide over its surface.",
		"a frozen tundra planet. blizzards rage continuously.",
		"a peaceful planet with a highly religious population.",
		"a dark & noxious planet. deadly spores blanket its surface.",
		"an ancient planet inhabited by a powerful humanoid species.",
		"a massive trading outpost. many species do business here.",
		"a volcanic planet. much of its surface is covered by magma.",
		"an abandoned mining colony thats now home to space pirates.",
		"a tropical planet where many species seem to vacation.",
		"a ruined wartorn planet. civil war has raged for generations.",
		"a mystical planet where beings with strange powers rule.",
		"an aquatic planet. research stations lie below its waves.",
		"a prison space station home to the worst of the worst.",
		"a mysterious planet whos inhabitants have long died.",
        "a beautiful tropical planet brimming with life.",
        "a derelict alien vessel drifting through space.",
        "the ruined world of a once mighty civilization.",
        "a quaint space station known for delicious food.",
        "a peaceful world inhabited by industrious people.",
        "a space ship graveyard, inhabited by outlaws.",
        "a weapons research station shielded from prying eyes.",
        "a cloning facility that raises armies for the highest bidders.",
        "a storm ravaged world where it always rains.",
        "a merchant colony bustling with commerce.",
        "a world that fell to catastophic climate change.",
        "the seat of power to a terrible empire.",
        "the lush homeworld to a proud warrior race.",
        "a toxic planet whos people have long since fled.",
        "a technologically advanced world where energy is currency.",
        "a travelling food ship, it is famous for its Ramen bowls."
    ]
    # list of descriptions for planet generation.

    with open("PlanetNameMaker\Planets.csv", "w") as planet_file:
    # open file in write mode.

        planet_writer = writer(planet_file, lineterminator = '\n')
        # create csv writer obj.

        planet_writer.writerow(["name", "description", "population"])
        # write headings.

        for i in range(0, 100):
        # iter 100 times.

            constructed_name = f"{choice(potential_primary_names)}-{choice(potential_secondary_names)}"
            description = choice(potential_descriptions)
            population = randint(3, 9999999)
            # randomly create data for planet.

            planet_writer.writerow([constructed_name, description, population])
            # write line to file.

    exit()
    # close program.

main()