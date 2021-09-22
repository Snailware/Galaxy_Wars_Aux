# make a csv file with alot of objects for Galaxy Wars.
# NOTE cannot use "," in any data fields as that is delimiter.

from csv import writer
from random import choice, randint

def main():
    """use this to make lots of objects in csv file quick."""

    potential_primary_names = \
    [
        "Tuvok","Spock","Seven","Ro","Odo","Kira","Gandalf","Megatron",
        "Optimus","Starscream","Liono","Snarf","Thanos","Roger","Ebrietas",
        "Amygdala","Artorias","Sif","Ornstein","Havel","Siegward","Kalameet",
        "Manus","Gwyn","Solaire","SHODAN","Pikachu","Sonic","Miles","Knuckles",
        "Kirby","Marth","Mewtwo","Fox","Cloud","Barret","Tifa","Cid","Vincent",
        "Cait","Yuffie","Red","Sephiroth","Jenova","Squall","Leon","Mog",
        "Moogle","Rinoa","Zell","Zidane","Garnet","Eiko","Adelbert","Beatrix",
        "Vivi","Amarant","Freya","Kuja","Terra","Celes","Dusk"
    ]
    # list of primary names for obj generation.

    potential_secondary_names = \
    [
        "Laren","Nerys","the Grey","the White","Autobot","Decepticon","Thundercat",
        "Purple","Smith","Cosmos","Horror","the Abysswalker","Greatwolf",
        "the Dragonslayer","The Rock","of Catarina","the Dragon","Father of Abyss",
        "God of Sunlight","of Astora","Machine","Ketchum","the Hedgehog","Prower",
        "the Echidna","McCloud","Strife","Wallace","Lockhart","Highwind",
        "Valentine","Sith","XIII","One Winged Angel","Synthesis","Lionheart",
        "Kupo","Heartilly","Dincht","Tribal","Alexandros","Carol","Steiner",
        "Ornitier","Coral","Crescent","Branford","Chere","of Oolacile"
    ]
    # list of secondary names for obj generation.

    potential_descriptions = \
    [
        "A humanoid officer. Cold logical and highly intelligent.",
		"A leader to his people. His wisdom is known across the galaxy.",
		"A cyborg more machine than person. She is ruthless and efficient.",
		"A humanoid freedom fighter from an occupied world.",
		"A shape shifter capable of fantastic feats when transformed.",
		"A humanoid terrorist leader who rejects all authority but her own.",
		"A powerful humanoid ancient whos power knows no bounds.",
		"A mechanical zealot bent on domination at all costs.",
		"A large humanoid robot. A steadfast protecter of its kind.",
		"A cat-like humanoid. Proud and strong; They will not falter.",
		"A small furry creaure. It frequently repeats its own name.",
		"A large humanoid driven mad and bent on destruction.",
		"A small pudgy thing. it insults you mercilessly.",
		"An ancient horror. Revered by many as a God.",
		"A scorned giant with many eyes and arms. It delights in torture.",
		"A legendary humanoid warrior. Known for facing impossible odds.",
		"A massive wolf-like creature. It will die before it surrenders.",
		"The humanoid captain of his lords knights. A fierce dragon slayer.",
		"A humanoid clad in heavy stone plates. His defenses are legendary.",
		"A plump humanoid who values honor (and beer) above all else.",
		"A giant black dragon. It has devoured countless souls.",
		"A twisted monster and the father of an unstoppable abyss.",
		"The Father of Sunlight. he has sacrificed everything for power.",
		"A humble man whose quest for sunlight drives him ever onward.",
		"An omnipotent AI. It will stop at nothing to impose its will.",
        "A flufy yellow creature that produces lightning when angry.",
        "A really cool guy.",
        "A fox starship pilot known for his bravery.",
        "A powerful humanoid ex-soldier poisoned by Mako energy.",
        "A proud father and fierce protector of the planet.",
        "A humanoid martial artist known for her beauty and strength.",
        "An ace pilot with a foul mouth and a nicotine addiction.",
        "A test subject who can now transform into monstrous beasts.",
        "A completely normal gambling robot.",
        "The son of noble warrior.",
        "A powerful warrior bent on achieving Godhood.",
        "A terrible evil. Ancients called it The Calamity From the Skies.",
        "A young mercenary bearing a large scar across his face.",
        "A small fury creature with a bag of mail over its shoulder.",
        "A pretty young woman accompanied by her dog.",
        "An impulsive humanoid fighter known for his quick temper.",
        "A humanoid fighter from another dimension.",
        "A princess who fled her kingdom to seek adventure.",
        "A young girl and the last of her once powerful race.",
        "A noble knight who would give his life for his princess.",
        "A strange dark creature. it wields powerful magic.",
        "A skilled thief who will do anything for the right price.",
        "A formidable dragoon knight wielding a ceremonial lance.",
        "The last of her kind. Hunted by many.",
        "The personal knight to her king. Her strength has no equal.",
        "A princess pulled away from her own space and time."
    ]
    # list of descriptions for obj generation.

    with open("AlienMaker\Aliens.csv", "w") as obj_file:
    # open file in write mode.

        obj_writer = writer(obj_file, lineterminator = '\n')
        # create csv writer obj.

        obj_writer.writerow(["name", "description", "health", "armor", "money"])
        # write headings.

        for i in range(0, 200):
        # iter x times.

            constructed_name = f"{choice(potential_primary_names)} {choice(potential_secondary_names)}"
            description = choice(potential_descriptions)
            # name and desc.

            health = randint(10, 15)
            armor = randint(1, 3)
            money = randint(100, 500)
            # randomly create data for obj.

            obj_writer.writerow([constructed_name, description, health, armor, money])
            # write line to file.

    exit()
    # close program.

main()