import pymysql.cursors
import discord
from settings import BOT_TOKEN, DB_HOST, DB_USER, DB_PASS, DB_NAME
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import os
import json
import gen_mon
import gamecorner

BOT_PREFIX = ("?", "!", "$", ".")


#Connects to the MySQL database
#Return: The connection context
def db_connect():
    conn = pymysql.connect(host='', port=, user='', passwd='', db='', autocommit=True)
    if conn:
        print("[*] Connected to db")
        return conn
    else:
        print("Cannot connect to db")


#This class contains the chatbot
class RpgBot:
    
    #Initializes the bot
    def __init__(self, token):
        self.db = db_connect()
        self.bot = commands.Bot(command_prefix="!")
        self.token = token
        self.prepare_client()
        

    def run(self):
        self.bot.run(self.token)
    

    def prepare_client(self):

        #Triggers when the bot comes online
        #Notifies to console when a successfull connection exists
        #TODO apply changes??
        @self.bot.event
        async def on_ready():
            #self.add_users_to_db()
            print("[*] Connected to Discord as: " + self.bot.user.name)



        #Triggered when any message is sent
        #TODO should remove or apply changes (changes??!?? sure w/e lole just figure it out future me)
        @self.bot.event
        async def on_message(message):
            await self.bot.process_commands(message)
        
        @self.bot.command()
        async def slots(context):
            loc = ""
            try:
                with self.db.cursor() as cursor:
                    sql = "SELECT location FROM users WHERE userid = %s"
                    cursor.execute(sql, (context.message.author.id))
                    result = cursor.fetchone()
                    if not result:
                        print("User does not exist")
                    else:
                        loc = result
                        print(loc)
            except Exception as e:
                print("Error on lookup for user.\n%s" % (e))
            

            if(loc[0] != 40):
                await context.send("You can only play games at the Game Corner!")
            else:
                await context.send(gamecorner.play_slots(3))



        #Triggered when a user sends "!locations"
        #Returns a list of locations
        @self.bot.command()
        async def locations(context):
            img = discord.File(fp="images/maps/kanto_map_new.png", spoiler=False)
            await context.send(file=img)

        #Triggered when a user sends "!whereis location/item/user"
        #Returns a list/string of a location of a user or item
        @self.bot.command()
        async def whereis(context, question):
            thing = ""
            try:
                with self.db.cursor() as cursor:
                    sql = "SELECT users.nickname AS user, locations.name AS name FROM users JOIN locations ON users.location = locations.location_id WHERE users.nickname = %s"
                    cursor.execute(sql, (question))
                    result = cursor.fetchone()
                    if not result:
                        print("User does not exist: %s" % question)
                    else:
                        thing = result
            except Exception as e:
                print("Error on lookup for %s.\n%s" % (question, e))

            if question == thing[0]:
                await context.send("%s is in %s" % (thing[0], thing[1]))
            elif question in gen_mon.get_pokelist():
                await context.send("%s resides in locations" % thing)
            else:
                await context.send("I cant find %s" % thing)



        #Tells the player where they can go from where they are
        #TODO ADD ROUTES TO THIS LIST
        @self.bot.command()
        async def routes(context):
            name = self.get_nick(context.message.author)
            thing = ""
            try:
                with self.db.cursor() as cursor:
                    sql = "SELECT users.location AS loc, locations.name AS name FROM users JOIN locations ON users.location = locations.location_id WHERE users.nickname = %s"
                    cursor.execute(sql, (name))
                    result = cursor.fetchone()
                    if not result:
                        print("ooo: %s" % name)
                    else:
                        thing = result
            except Exception as e:
                print("aaa %s.\n%s" % (name, e))
            
            if result[0] == 1:
                await context.send(f"({result[1]}) You can go - Elite Four - South: Victory Road -> Route 23 -> Route 22 -> Viridian City")
            elif result[0] == 2:
                await context.send(f"({result[1]}) You can go - South: Route 1 -> Pallet Town - North: Route 2")
            elif result[0] == 3:
                await context.send(f"({result[1]}) You can go - North: Route 1 -> Viridian City - South: Route 21 -> Cinnibar Island")
            elif result[0] == 4:
                await context.send(f"({result[1]}) You can go - Pokemon Mansion - North: Route 21 -> Pallet Town - East: Route 20 -> Seafoam Island")
            elif result[0] == 5:
                await context.send(f"({result[1]}) You can go - South: Viridian Forest -> Route 2 -> Viridian City - East: Route 3 -> Mt. Moon")
            elif result[0] == 6:
                await context.send(f"({result[1]}) You can go - West: Route 4 -> Mt. Moon - North: Route 24 -> Route 25 - South: Route 5 -> Saffron City")
            elif result[0] == 7:
                await context.send(f"({result[1]}) You can go - Game Corner - West: Route 16 -> Cycling Road -> Route 18 -> Fushia City - East: Route 8 -> Saffron City")
            elif result[0] == 8:
                await context.send(f"({result[1]}) You can go - Silph Co. - North: Route 5 -> Cerulean City - South: Route 6 -> Vermillion City - East: Route 7 -> Lavender Town - West: Route 8 -> Celadon City")
            elif result[0] == 9:
                await context.send(f"({result[1]}) You can go - North: Route 6 -> Saffron City - East: Route 11 -> Route 12")
            elif result[0] == 10:
                await context.send(f"({result[1]}) You can go - Safari Zone - South: Route 19 -> Seafoam Islands - East: Route 15 -> Route 14 -> Route 13 - West -> Route 18 -> Cycling Road")
            elif result[0] == 11:
                await context.send(f"({result[1]}) You can go - North: Rock Tunnel -> Route 9/Power Plant - South: Route 12 -> Route 11 or 13 - West: Route 7 -> Saffron City")
            elif result[0] == 12:
                await context.send(f"(Location: {result[1]}) North: Pewter City - South: Route 2 -> Viridian City")
            elif result[0] == 13:
                await context.send(f"(Location: {result[1]}) East: Route 3 -> Pewter City - West: Route 4 -> Cerulean City")
            elif result[0] == 14:
                await context.send(f"(Location: {result[1]}) North: Viridian City - South: Pallet Town")
            elif result[0] == 15:
                await context.send(f"(Location: {result[1]}) North: Viridian Forest - South: Viridian City")
            elif result[0] == 16:
                await context.send(f"(Location: {result[1]}) West: Pewter City - East: Mt.Moon")
            elif result[0] == 17:
                await context.send(f"(Location: {result[1]}) West: Mt.Moon - East: Cerulean City")
            elif result[0] == 18:
                await context.send(f"(Location: {result[1]}) North: Cerulean City - South: Saffron City")
            elif result[0] == 19:
                await context.send(f"(Location: {result[1]}) North: Saffron City - South: Vermillion City")
            elif result[0] == 20:
                await context.send(f"(Location: {result[1]}) East: Saffron City - South: Celadon City")
            elif result[0] == 21:
                await context.send(f"(Location: {result[1]}) East: Lavender Town - West: Saffron City")
            elif result[0] == 22:
                await context.send(f"(Location: {result[1]}) East: Rock Tunnel - West: Cerulean City")
            elif result[0] == 23:
                await context.send(f"(Location: {result[1]}) North: Rock Tunnel - South: Lavender Town")
            elif result[0] == 24:
                await context.send(f"(Location: {result[1]}) East: Route 12 - West: Vermillion City")
            elif result[0] == 25:
                await context.send(f"(Location: {result[1]}) North: Lavender Town - South: Route 13")
            elif result[0] == 26:
                await context.send(f"(Location: {result[1]}) North: Route 12 - South: Route 14")
            elif result[0] == 27:
                await context.send(f"(Location: {result[1]}) North: Route 13 - South: Route 15")
            elif result[0] == 28:
                await context.send(f"(Location: {result[1]}) North: Route 14 - West: Fushia City")
            elif result[0] == 29:
                await context.send(f"(Location: {result[1]}) South: Route 17 - East: Celadon City")
            elif result[0] == 30:
                await context.send(f"(Location: {result[1]}) North: Route 16 - South: Route 18 (Requires Surf)")
            elif result[0] == 31:
                await context.send(f"(Location: {result[1]}) North: Route 17 (Requires Surf) - East: Fushia City")
            elif result[0] == 32:
                await context.send(f"(Location: {result[1]}) North: Fushia City - South: (Sea) Route 20")
            elif result[0] == 33:
                await context.send(f"(Location: {result[1]}) West: Seafoam Island - North: Route 19")
            elif result[0] == 34:
                await context.send(f"(Location: {result[1]}) North: Pallet Town - South: Cinnabar Island")
            elif result[0] == 35:
                await context.send(f"(Location: {result[1]}) North: Route 23 - East: Viridian City")
            elif result[0] == 36:
                await context.send(f"(Location: {result[1]}) North: Victory Road - South: Route Route 22")
            elif result[0] == 37:
                await context.send(f"(Location: {result[1]}) North: Route 25 - South: Cerulean City")
            elif result[0] == 38:
                await context.send(f"(Location: {result[1]}) South: Route 24")
            elif result[0] == 39:
                await context.send(f"(Location: {result[1]}) Exit North: Route 2 - Exit South: Route 11")
            elif result[0] == 40:
                await context.send(f"(Location: {result[1]}) Exit: Celadon City")
            elif result[0] == 41:
                await context.send(f"(Location: {result[1]}) Exit: Route 9")
            elif result[0] == 42:
                await context.send(f"(Location: {result[1]}) Exit: Fushia City")
            elif result[0] == 43:
                await context.send(f"(Location: {result[1]}) Exit: Cinnabar Island")
            elif result[0] == 44:
                await context.send(f"(Location: {result[1]}) Exit North: Indigo Plateau - Exit South: Route 23")
            elif result[0] == 45:
                await context.send(f"(Location: {result[1]}) Exit: Saffron City")
            elif result[0] == 46:
                await context.send(f"(Location: {result[1]}) Exit East: Route 20 - Exit West: Cinnabar Island")
            elif result[0] == 47:
                await context.send(f"(Location: {result[1]}) Exit North: Route 9 - Exit South: Route 10")
            else:
                await context.send("idk man its not here lole")


        #Moves the player to the next route/location
        #TODO ADD ROUTES AND OPTIONAL LOCATIONS TO THIS LIST
        @self.bot.command()
        async def move(context, direction):
            name = self.get_nick(context.message.author)
            location_id = 0
            thing = ""
            try:
                with self.db.cursor() as cursor:
                    sql = "SELECT users.location AS loc, locations.name AS name, users.userid FROM users JOIN locations ON users.location = locations.location_id WHERE users.nickname = %s"
                    cursor.execute(sql, (name))
                    result = cursor.fetchone()
                    if not result:
                        print("ooo: %s" % name)
                    else:
                        thing = result
            except Exception as e:
                print("aaa %s.\n%s" % (name, e))

            if result[0] == 1:

                if direction.lower() == "south":
                    self.change_player_location(44, name)
                    await context.send("Moved to Victory Road")
                else:
                    print("cannot move!!!")

            elif result[0] == 2:

                if direction.lower() == "north":
                    self.change_player_location(15, name)
                    await context.send("Moved to Route 2")
                elif direction.lower() == "south":
                    self.change_player_location(14, name)
                    await context.send("Moved to Route 1")
                elif direction.lower() == "west":
                    self.change_player_location(35, name)
                else:
                    print("cannot move!!!")

            elif result[0] == 3:

                if direction.lower() == "north":
                    self.change_player_location(14, name)
                    await context.send("Moved to Route 1")
                elif direction.lower() == "south":
                    self.change_player_location(34, name)
                    await context.send("Moved to Route 21")
                else:
                    print("cannot move!!!")

            elif result[0] == 4:

                if direction.lower() == "north":
                    self.change_player_location(34, name)
                    await context.send("Moved to Route 21")
                elif direction.lower() == "east":
                    self.change_player_location(46, name)
                    await context.send("Moved to Seafoam Island")
                else:
                    print("cannot move!!!")

            elif result[0] == 5:
                
                if direction.lower() == "south":
                    self.change_player_location(12, name)
                    await context.send("Moved to Viridian Forest")
                elif direction.lower() == "east":
                    self.change_player_location(16, name)
                    await context.send("Moved to Route 3")
                else:
                    print("cannot move!!!")

            elif result[0] == 6:
                
                if direction.lower() == "north":
                    self.change_player_location(37, name)
                    await context.send("Moved to Route 24")
                elif direction.lower() == "east":
                    self.change_player_location(22, name)
                    await context.send("Moved to Route 9")
                elif direction.lower() == "south":
                    self.change_player_location(18, name)
                    await context.send("Moved to Route 5")
                elif direction.lower() == "west":
                    self.change_player_location(17, name)
                    await context.send("Moved to Route 4")
                else:
                    print("cannot move!!!")

            elif result[0] == 7:

                if direction.lower() == "west":
                    self.change_player_location(29, name)
                    await context.send("Moved to Route 16")
                elif direction.lower() == "east":
                    self.change_player_location(20, name)
                    await context.send("Moved to Route 7")
                elif direction.lower() == "game":
                    self.change_player_location(40, name)
                    await context.send("Moved to Game Corner")
                else:
                    print("cannot move!!!")

            elif result[0] == 8:

                if direction.lower() == "north":
                    self.change_player_location(18, name)
                    await context.send("Moved to Route 5")
                elif direction.lower() == "south":
                    self.change_player_location(19, name)
                    await context.send("Moved to Route 6")
                elif direction.lower() == "east":
                    self.change_player_location(21, name)
                    await context.send("Moved to Route 8")
                elif direction.lower() == "west":
                    self.change_player_location(20, name)
                    await context.send("Moved to Route 7")
                elif direction.lower() == "silph":
                    self.change_player_location(45, name)
                    await context.send("Moved to Silph Co.")
                else:
                    print("cannot move!!!")
                
            elif result[0] == 9:

                if direction.lower() == "north":
                    self.change_player_location(19, name)
                    await context.send("Moved to Route 6")
                elif direction.lower() == "east":
                    self.change_player_location(24, name)
                    await context.send("Moved to Route 11")
                else:
                    print("cannot move!!!")

            elif result[0] == 10:

                if direction.lower() == "west":
                    self.change_player_location(31, name)
                    await context.send("Moved to Route 18")
                elif direction.lower() == "east":
                    self.change_player_location(28, name)
                    await context.send("Moved to Route 15")
                elif direction.lower() == "south":
                    self.change_player_location(32, name)
                    await context.send("Moved to Route 19")
                elif direction.lower() == "safari":
                    self.change_player_location(42, name)
                    await context.send("Moved to Safari Zone")
                else:
                    print("cannot move!!!")

            elif result[0] == 11:

                if direction.lower() == "north":
                    self.change_player_location(23, name)
                    await context.send("Moved to Route 10")
                elif direction.lower() == "south":
                    self.change_player_location(25, name)
                    await context.send("Moved to Route 12")
                elif direction.lower() == "west":
                    self.change_player_location(21, name)
                    await context.send("Moved to Route 8")
                else:
                    print("cannot move!!!")

            elif result[0] == 12:

                if direction.lower() == "north":
                    self.change_player_location(5, name)
                    await context.send("Moved to Pewter City")
                elif direction.lower() == "south":
                    self.change_player_location(15, name)
                    await context.send("Moved to Route 2")
                else:
                    print("cannot move!!!")

            elif result[0] == 13:

                if direction.lower() == "east":
                    self.change_player_location(17, name)
                    await context.send("Moved to Route 4")
                elif direction.lower() == "west":
                    self.change_player_location(16, name)
                    await context.send("Moved to Route 3")
                else:
                    print("cannot move!!!")
                
            elif result[0] == 14:

                if direction.lower() == "north":
                    self.change_player_location(2, name)
                    await context.send("Moved to Viridian City")
                elif direction.lower() == "south":
                    self.change_player_location(3, name)
                    await context.send("Moved to Pallet Town")
                else:
                    print("cannot move!!!")

            elif result[0] == 15:

                if direction.lower() == "north":
                    self.change_player_location(12, name)
                    await context.send("Moved to Viridian Forest")
                elif direction.lower() == "south":
                    self.change_player_location(2, name)
                    await context.send("Moved to Viridian City")
                else:
                    print("cannot move!!!")
                
            elif result[0] == 16:

                if direction.lower() == "east":
                    self.change_player_location(13, name)
                    await context.send("Moved to Mt.Moon")
                elif direction.lower() == "west":
                    self.change_player_location(5, name)
                    await context.send("Moved to Pewter City")
                else:
                    print("cannot move!!!")

            elif result[0] == 17:

                if direction.lower() == "east":
                    self.change_player_location(6, name)
                    await context.send("Moved to Cerulean City")
                elif direction.lower() == "west":
                    self.change_player_location(13, name)
                    await context.send("Moved to Mt.Moon")
                else:
                    print("cannot move!!!")

            elif result[0] == 18:

                if direction.lower() == "north":
                    self.change_player_location(6, name)
                    await context.send("Moved to Cerulean City")
                elif direction.lower() == "south":
                    self.change_player_location(8, name)
                    await context.send("Moved to Saffron City")
                else:
                    print("cannot move!!!")

            elif result[0] == 19:

                if direction.lower() == "north":
                    self.change_player_location(8, name)
                    await context.send("Moved to Saffron City")
                elif direction.lower() == "south":
                    self.change_player_location(9, name)
                    await context.send("Moved to Vermillion City")
                else:
                    print("cannot move!!!")

            elif result[0] == 20:

                if direction.lower() == "east":
                    self.change_player_location(8, name)
                    await context.send("Moved to Saffron City")
                elif direction.lower() == "west":
                    self.change_player_location(7, name)
                    await context.send("Moved to Celadon City")
                else:
                    print("cannot move!!!")

            elif result[0] == 21:

                if direction.lower() == "east":
                    self.change_player_location(11, name)
                    await context.send("Moved to Lavender Town")
                elif direction.lower() == "west":
                    self.change_player_location(8, name)
                    await context.send("Moved to Saffron City")
                else:
                    print("cannot move!!!")

            elif result[0] == 22:

                if direction.lower() == "east":
                    self.change_player_location(47, name)
                    await context.send("Moved to Rock Tunnel")
                elif direction.lower() == "west":
                    self.change_player_location(6, name)
                    await context.send("Moved to Cerulean City")
                else:
                    print("cannot move!!!")

            elif result[0] == 23:

                if direction.lower() == "north":
                    self.change_player_location(47, name)
                    await context.send("Moved to Rock Tunnel")
                elif direction.lower() == "south":
                    self.change_player_location(11, name)
                    await context.send("Moved to Lavender Town")
                else:
                    print("cannot move!!!")

            elif result[0] == 24:

                if direction.lower() == "east":
                    self.change_player_location(25, name)
                    await context.send("Moved to Route 12")
                elif direction.lower() == "west":
                    self.change_player_location(9, name)
                    await context.send("Moved to Vermillion City")
                else:
                    print("cannot move!!!")

            elif result[0] == 25:

                if direction.lower() == "north":
                    self.change_player_location(11, name)
                    await context.send("Moved to Lavender Town")
                elif direction.lower() == "south":
                    self.change_player_location(26, name)
                    await context.send("Moved to Route 13")
                else:
                    print("cannot move!!!")

            elif result[0] == 26:

                if direction.lower() == "north":
                    self.change_player_location(25, name)
                    await context.send("Moved to Route 12")
                elif direction.lower() == "south":
                    self.change_player_location(27, name)
                    await context.send("Moved to Route 14")
                else:
                    print("cannot move!!!")

            elif result[0] == 27:

                if direction.lower() == "north":
                    self.change_player_location(26, name)
                    await context.send("Moved to Route 13")
                elif direction.lower() == "south":
                    self.change_player_location(28, name)
                    await context.send("Moved to Route 15")
                else:
                    print("cannot move!!!")

            elif result[0] == 28:

                if direction.lower() == "north":
                    self.change_player_location(27, name)
                    await context.send("Moved to Route 14")
                elif direction.lower() == "west":
                    self.change_player_location(10, name)
                    await context.send("Moved to Fushia City")
                else:
                    print("cannot move!!!")

            elif result[0] == 29:

                if direction.lower() == "east":
                    self.change_player_location(7, name)
                    await context.send("Moved to Celadon City")
                elif direction.lower() == "south":
                    self.change_player_location(30, name)
                    await context.send("Moved to Route 17")
                else:
                    print("cannot move!!!")

            elif result[0] == 30:

                if direction.lower() == "south":
                    self.change_player_location(31, name)
                    await context.send("Moved to Route 18")
                elif direction.lower() == "north":
                    self.change_player_location(29, name)
                    await context.send("Moved to Route 16")
                else:
                    print("cannot move!!!")

            elif result[0] == 31:

                if direction.lower() == "east":
                    self.change_player_location(10, name)
                    await context.send("Moved to Fushia City")
                elif direction.lower() == "north":
                    self.change_player_location(30, name)
                    await context.send("Moved to Route 17")
                else:
                    print("cannot move!!!")

            elif result[0] == 32:

                if direction.lower() == "south":
                    self.change_player_location(33, name)
                    await context.send("Moved to Route 20 (Sea)")
                elif direction.lower() == "north":
                    self.change_player_location(10, name)
                    await context.send("Moved to Fushia City")
                else:
                    print("cannot move!!!")

            elif result[0] == 33:

                if direction.lower() == "north":
                    self.change_player_location(32, name)
                    await context.send("Moved to Route 19")
                elif direction.lower() == "west":
                    self.change_player_location(46, name)
                    await context.send("Moved to Seafoam Island")
                else:
                    print("cannot move!!!")

            elif result[0] == 34:

                if direction.lower() == "south":
                    self.change_player_location(4, name)
                    await context.send("Moved to Cinnibar Island")
                elif direction.lower() == "north":
                    self.change_player_location(3, name)
                    await context.send("Moved to Pallet Town")
                else:
                    print("cannot move!!!")

            elif result[0] == 35:

                if direction.lower() == "east":
                    self.change_player_location(2, name)
                    await context.send("Moved to Viridian City")
                elif direction.lower() == "north":
                    self.change_player_location(36, name)
                    await context.send("Moved to Route 23")
                else:
                    print("cannot move!!!")

            elif result[0] == 36:

                if direction.lower() == "south":
                    self.change_player_location(35, name)
                    await context.send("Moved to Route 22")
                elif direction.lower() == "north":
                    self.change_player_location(44, name)
                    await context.send("Moved to Vicroy Road epic")
                else:
                    print("cannot move!!!")

            elif result[0] == 37:

                if direction.lower() == "south":
                    self.change_player_location(6, name)
                    await context.send("Moved to Cerulean City")
                elif direction.lower() == "north":
                    self.change_player_location(38, name)
                    await context.send("Moved to Route 25")
                else:
                    print("cannot move!!!")

            elif result[0] == 38:

                if direction.lower() == "south":
                    self.change_player_location(37, name)
                    await context.send("Moved to Route 24")
                else:
                    print("cannot move!!!")

            elif result[0] == 39:

                if direction.lower() == "south":
                    self.change_player_location(24, name)
                    await context.send("Moved to Route 11")
                elif direction.lower() == "north":
                    self.change_player_location(16, name)
                    await context.send("Moved to Route 2")
                else:
                    print("cannot move!!!")

            elif result[0] == 40:

                if direction.lower() == "exit":
                    self.change_player_location(7, name)
                    await context.send("Moved to Celadon City")
                else:
                    print("cannot move!!!")

            elif result[0] == 41:

                if direction.lower() == "exit":
                    self.change_player_location(22, name)
                    await context.send("Moved to Route 9")
                else:
                    print("cannot move!!!")

            elif result[0] == 42:

                if direction.lower() == "exit":
                    self.change_player_location(10, name)
                    await context.send("Moved to Fushia City")
                else:
                    print("cannot move!!!")

            elif result[0] == 43:

                if direction.lower() == "exit":
                    self.change_player_location(4, name)
                    await context.send("Moved to Cinnabar Island")
                else:
                    print("cannot move!!!")

            elif result[0] == 44:

                if direction.lower() == "north":
                    self.change_player_location(1, name)
                    await context.send("Moved to Indigo Plateau")
                elif direction.lower() == "south":
                    self.change_player_location(36, name)
                    await context.send("Moved to Route 23")
                else:
                    print("cannot move!!!")

            elif result[0] == 45:

                if direction.lower() == "exit":
                    self.change_player_location(8, name)
                    await context.send("Moved to Saffron City")
                else:
                    print("cannot move!!!")

            elif result[0] == 46:

                if direction.lower() == "east":
                    self.change_player_location(4, name)
                    await context.send("Moved to Cinnabar Island")
                elif direction.lower() == "west":
                    self.change_player_location(33, name)
                    await context.send("Moved to Route 20")
                else:
                    print("cannot move!!!")

            elif result[0] == 47:

                if direction.lower() == "north":
                    self.change_player_location(22, name)
                    await context.send("Moved to Route 9")
                elif direction.lower() == "south":
                    self.change_player_location(23, name)
                    await context.send("Moved to Route 10")
                else:
                    print("cannot move!!!")
                
            else:
                await context.send("idk man its not here lole")
            



        #Triggers when a user sends "!join [nickname]"
        #Adds the user to the database
        #Decorator: Command Event
        #Params: context, nick
                #context: user chat message prefix ("!command", specifically the '!' part!!)
                #nick: the users game name
        @self.bot.command()
        async def join(context, nick):
            try:
                print("join %s" % context.message.author)
                self.add_user_to_db(context.message.author, nick)
                self.makePlayerInfo(nick)
                await context.send(f"Welcome, {context.message.author.mention}. Your game name is {nick}, I will be referring you as {nick} from now on.")
            except Exception as e:
                print("(join)Error adding user %s.\n%s" % (context.message.author.id, e))


        #Triggers when a user sends "!stats"
        #Bot sends the users stats to the channel from the database
        #Decorator: Command Event
        #Params: context, nick
                #context: User chat message contex prefix ("!command")
                #nick: the users game name
        @self.bot.command()
        async def stats(context, nick):
            player = self.get_player(nick)
            await context.send("So you want stats?")
            await context.send("""`
Stats for %s
Game Name: %s
EXP: %s`""" % (context.message.author, nick, player))


        @self.bot.command()
        async def commands(context):
            await context.send("""```
Commands:
!join [nickname]                Joins you to the game with a nickname
!mons [nickname] [slot_number]  Shows your pokemon in a slot (1-6 slots)
!routes                         Shows where you can go from your current location
!locations                      Shows a map of the Kanto region
!whereis [player_nickname]      Tells you where a player is
!move [direction]               Moves you North, South, East or West
```""")


        @self.bot.command()
        async def mons(context, nick, slot_no):
            pmons = self.read_player_mons(nick)
            i = ""
            for v in list(pmons.values())[int(slot_no)]:
                title = f"{nick}s mons:"
                name = f"Name: {v['name']}  |  {v['type']}\n"
                hp = f"HP: {v['hp']}/{v['hp']}\n"
                item = f"Item: {v['item']}"
                i = v['dexno']
            
            embed = discord.Embed(
                title = f"{name}",
                description = f"{hp}",
                colour = discord.Colour.blue()
            )
            embed.set_image(url='')
            embed.add_field(name='F1', value=f"{item}", inline=False)
            img = discord.File(fp=f"images/{i}.png", spoiler=False)
            await context.send(file=img, embed=embed)




    #Gets the users data from the database
    #Params: self, nick
            #self: The object RpgBot
            #nick: The users game name
    def get_player(self, nick):
        print("get_player %s" % nick)
        try:
            with self.db.cursor() as cursor:
                sql = "SELECT nickname FROM users WHERE nickname=%s"
                cursor.execute(sql, (nick))
                result = cursor.fetchone()
                if not result:
                    print("User does not exist: %s" % nick)
                else:
                    return result
        except Exception as e:
            print("Error on lookup for %s.\n%s" % (nick, e))
    

    def get_nick(self, member):
        print("get nick %s" % member.id)
        try:
            with self.db.cursor() as cursor:
                sql = "SELECT nickname FROM users WHERE userid = %s"
                cursor.execute(sql, (member.id))
                result = cursor.fetchone()
                print("(getnick) %s " % result)
                return result
                
        except Exception as e:
            print("eee %s" % e)

    
    #Adds a Discord user to the database
    #Params: self, member, nickname
            #self: the object RpgBot
            #member: the actual Discord user
            #nickname: the users game name
    #Return: returns nothing and exits if the user is already added
    def add_user_to_db(self, member, nickname):
        if self.get_player(member.id):
            return
        
        try:
            print("add_user_to_db %s" % member.id)
            with self.db.cursor() as cursor:
                sql = "INSERT INTO users (userid, join_date, xp, nickname)" + \
                    " VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (member.id, member.joined_at, 1, nickname))
                self.db.commit()
                print("(add_user_to_db)Added user %s to database." % member.id)
                
        except Exception as e:
            print("Error adding user %s" % e)
    


    def change_player_location(self, location, nick):
        try:
            with self.db.cursor() as cursor:
                print(location)
                print(nick[0])
                sql = "UPDATE users SET location = %s WHERE nickname = %s"
                cursor.execute(sql, (location, nick[0]))
        except Exception as e:
            print("(%s)Error updating location: %s" % (nick[0],e))
    


    #Generates a json file containing a users pokemon, which are generated using gen_mon.py
    #Params: self, nick
            #self: the object RpgBot
            #nick: the users game nickname
    def makePlayerInfo(self, nick):
        #mons = [gen_mon.built_mon(), gen_mon.built_mon(), gen_mon.built_mon(), gen_mon.built_mon()] 
        #mons = [gen_mon.built_mon()]
        print('start')
        mons = [gen_mon.grab_mon(self.db), gen_mon.grab_mon(self.db)]
        print("got mons")
        types = [gen_mon.gen_type(mons[0][1]), gen_mon.gen_type(mons[1][1])]
        print("got types")
        for things in mons:
            print(f"{nick}s mons: {things}")
        
        data = {
            "name": f"{nick}",
                "slot1": [{
                    "dexno": f"{mons[0][0]}",
                    "level": "5",
                    "name": f"{mons[0][1]}",
                    "type": f"{types[0]}",
                    "hp": f"{mons[0][2]}",
                    "def": f"{mons[0][3]}",
                    "atk": f"{mons[0][4]}",
                    "spatk": f"{mons[0][5]}",
                    "spdef": f"{mons[0][6]}",
                    "speed": f"{mons[0][7]}",
                    "item": "0",

                    "atk1": {
                        "name": "name",
                        "power": "power",
                        "pp": "pp",
                        "acc": "acc",
                    },

                    "atk2": {
                        "name": "name",
                        "power": "power",
                        "pp": "pp",
                        "acc": "acc",
                    },

                    "atk3": {
                        "name": "name",
                        "power": "power",
                        "pp": "pp",
                        "acc": "acc",
                    },

                    "atk4": {
                        "name": "name",
                        "power": "power",
                        "pp": "pp",
                        "acc": "acc",
                    }
                }],
                "slot2": [{
                    "dexno": f"{mons[1][0]}",
                    "level": "5",
                    "name": f"{mons[1][1]}",
                    "type": f"{types[1]}",
                    "hp": f"{mons[1][2]}",
                    "def": f"{mons[1][3]}",
                    "atk": f"{mons[1][4]}",
                    "spatk": f"{mons[1][5]}",
                    "spdef": f"{mons[1][6]}",
                    "speed": f"{mons[1][7]}",
                    "item": "0",

                    "atk1": {
                        "name": "name",
                        "power": "power",
                        "pp": "pp",
                        "acc": "acc",
                    },

                    "atk2": {
                        "name": "name",
                        "power": "power",
                        "pp": "pp",
                        "acc": "acc",
                    },

                    "atk3": {
                        "name": "name",
                        "power": "power",
                        "pp": "pp",
                        "acc": "acc",
                    },

                    "atk4": {
                        "name": "name",
                        "power": "power",
                        "pp": "pp",
                        "acc": "acc",
                    }
                }],
        }

        with open(f"users/{nick}.json", "w") as write_file:
            json.dump(data, write_file, indent=4)

    #loads a users pokemon as a json object
    #Param: nick
           #The users nickname
    def read_player_mons(self, nick):
        with open(f'users/{nick}.json') as jfile:
            data = json.load(jfile)
        return data



    def test_data(self):
        mon = gen_mon.grab_mon(self.db)

        for m in mon:
            print(m)





if __name__ == '__main__':
    bot = RpgBot(BOT_TOKEN)
bot.run()