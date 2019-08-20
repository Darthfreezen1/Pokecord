import random
import pymysql.cursors

def gen_type(selected):
    water = ['Squirtle', 'Wartortle', 'Blastoise', 'Psyduck', 'Golduck', 'Poliwag', 'Poliwhirl', 'Seel', 'Shellder', 'Krabby', 'Kingler', 'Horsea', 'Seedra', 'Goldeen', 'Seaking', 'Staryu', 'Magikarp', 'Vaporeon', 'Articuno',
             'Tentacool', 'Tentacruel', 'Slowpoke', 'Dewgong', 'Cloyster', 'Starmie', 'Gyrados', 'Lapras', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Slowbro']
    grass = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Oddish', 'Gloom', 'Vileplume', 'Bellsprout', 'Weepinbell', 'Victreebell', 'Exeggcute', 'Exeggutor', 'Tangela']
    fire  = ['Charmander', 'Charmeleon', 'Charizard', 'Vulpix', 'Ninetails', 'Growlithe', 'Arcanine', 'Ponyta', 'Rapidash', 'Magmar','Flareon', 'Moltres']
    fight = ['Mankey', 'Primeape', 'Machop', 'Machoke', 'Machamp', 'Hitmonlee', 'Hitmonchan']
    normal= ['Rattata', 'Raticate', 'Jigglypuff', 'Wigglytuff', 'Meowth', 'Persian', 'Lickitung', 'Chansey', 'Kangaskhan', 'Tauros', 'Ditto', 'Eevee', 'Snorlax']
    bug   = ['Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Scyther']
    poison= ['Ekans', 'Arbok', 'Nidoran(g)', 'Nidorina', 'Nidoqueen', 'Nidoran(b)', 'Nidorino', 'Nidoking', 'Zubat', 'Golbat', 'Gimer', 'Muk', 'Koffing', 'Weezing']
    flying= ['Pidgey', 'Pidgeotto', 'Pidgeot', 'Spearow', 'Fearow', 'Fartetch-d', 'Doduo', 'Dodrio']
    elect = ['Pikachu', 'Raichu', 'Magnemite','Magneton', 'Voltorb', 'Electrode', 'Electabuzz', 'Jolteon', 'Zapdos']
    psychic=['Abra', 'Kadabra', 'Alakazam','Drowzee', 'Hypno', 'MrMime', 'Mewtwo', 'Mew']
    rock  = ['Geodude', 'Graveler', 'Golem', 'Onix']
    ground =['Sandshrew', 'Sandslash', 'Diglett', 'Dugtrio', 'Cubone', 'Marowak', 'Rhyhorn', 'Rhydon']
    dragon =['Dratini', 'Dragonair', 'Dragonite']
    ghost = ['Ghastly', 'Haunter', 'Gengar']

    if selected in water:
        return 'Water'
    elif selected in grass:
        return 'Grass'
    elif selected in fire:
        return 'Fire'
    elif selected in fight:
        return 'Fighting'
    elif selected in normal:
        return 'Normal'
    elif selected in bug:
        return 'Bug'
    elif selected in poison:
        return 'Poison'
    elif selected in flying:
        return 'Flying'
    elif selected in elect:
        return 'Electric'
    elif selected in psychic:
        return 'Psychic'
    elif selected in rock:
        return 'Rock'
    elif selected in ground:
        return 'Ground'
    elif selected in dragon:
        return 'Dragon'
    elif selected in ghost:
        return 'Ghost'
    else:
        print("Mon %s does no have a type... Did you forget to add it?" % selected)

def get_pokelist():
    names = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot',
             'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran(g)', 'Nidorina','Nidoqueen', 'Nidoran(b)','Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetails',
             'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape','Growlithe',
             'Arcanine','Poliwag', 'Poliwhirl', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebell', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta',
             'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Farfetch-d', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno',
             'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan',
             'Horsea', 'Seedra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'MrMime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyrados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 
             'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dagonair', 'Dragonite', 'Mewtwo', 'Mew']
    return names


def grab_mon(db):
    if db:
        print("connected")
    else:
        print("no connection")

    thing = ""
    try:
        with db.cursor() as cursor:
            sql = "SELECT * FROM base_stats WHERE id = %s"
            cursor.execute(sql, (random.randint(1,143)))
            result = cursor.fetchone()
            if not result:
                print("Could not pull a pokemon")
            else:
                thing = result
    except Exception as e:
        print("An error occurred while pulling a pokemon\n%s" % e)

    n = gen_stats(thing)
    return n


def gen_stats(mon):
    ivs = [random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31),random.randint(0,31)]
    for m in mon:
        print(f"before mods: {m}")
    
    for iv in ivs:
        print(iv)
    
    nmon = list(mon)
    
    nmon[2] = round((((2*mon[2]+ivs[0])*5)/100)+1+10)

    nmon[3] = round(((((2*mon[3]+ivs[1])*5)/100)+5)*1)

    nmon[4] = round(((((2*mon[4]+ivs[2])*5)/100)+5)*1)
    
    nmon[5] = round(((((2*mon[5]+ivs[3])*5)/100)+5)*1)

    nmon[6] = round(((((2*mon[6]+ivs[4])*5)/100)+5)*1)

    nmon[7] = round(((((2*mon[7]+ivs[5])*5)/100)+5)*1)

    for i in nmon:
        print(f"after mods: {i}")

    return nmon