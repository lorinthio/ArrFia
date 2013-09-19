import sqlite3

conn = sqlite3.connect('MUD.db')
c = conn.cursor()
c.execute('''CREATE TABLE ID (Name, Password, Permission, ChatInstance)''')
c.execute('''CREATE TABLE Placement (Name, Room)''')
c.execute('''CREATE TABLE Character (Name, Class, Level, Exp, Exptnl, Strength, Constitution, Dexterity, Agility, Wisdom, Intellegence, Race)''')
c.execute('''CREATE TABLE Inventory (Name, SLOT1, SLOT2, SLOT3, SLOT4, SLOT5, SLOT6, SLOT7, SLOT8, SLOT9, SLOT10, SLOT11, SLOT12, SLOT13, SLOT14, SLOT15, SLOT16, SLOT17, SLOT18, SLOT19, SLOT20, Gold)''')
c.execute('''CREATE TABLE Equipment (Name, Mainhand, Offhand, Helmet, Body, Lowerbody, Boots)''')
c.execute('''CREATE TABLE Vitals (Name, Health, Mana, ThreatMultiplier)''')
c.execute('''CREATE TABLE Regions (Name, Mobcount)''')
c.execute('''CREATE TABLE RoomExits (ID, Description, NorthDecription, EastDescription, SouthDescription, WestDescription, North, East, South, West, CoordX, CoordY, CoordZ)''')
c.execute('''CREATE TABLE RoomMobs (ID, Slot1, Slot2, Slot3, Slot4, Slot5, Slot6, Slot7, Slot8, Slot9, Slot10)''')
c.execute('''CREATE TABLE RoomItems (ID, Slot1, Slot2, Slot3, Slot4, Slot5, Slot6, Slot7, Slot8, Slot9, Slot10, Slot11, Slot12, Slot13, Slot14, Slot15, Slot16, Slot17, Slot18, Slot19, Slot20)''')
c.execute('''CREATE TABLE RoomPlayers (ID, Slot1, Slot2, Slot3, Slot4, Slot5, Slot6, Slot7, Slot8, Slot9, Slot10, Slot11, Slot12, Slot13, Slot14, Slot15, Slot16, Slot17, Slot18, Slot19, Slot20)''')
c.execute('''CREATE TABLE Monsters (ID, Name, Level, Strength, Constitution, Dexterity, Agility, Wisdom, Intellegence)''')
c.execute('''CREATE TABLE MonsterAttacks (ID, Attack1, Min1, Max1, Attack2, Min2, Max2, Attack3, Min3, Max3, Attack4, Min4, Max4)''')
c.execute('''CREATE TABLE MonsterLoot (ID, Goldmin, Goldmax, Item1, Item2, Item3, Item4, Item5, Item6, Item7)''')
c.execute('''CREATE TABLE ActiveMonster (RandomID, MobID, Level, Name, Health, MaxHealth, Mana, MaxMana, Attack, Defence, Speed, Critical, Accuracy, Dodge, Mattack, Mdefence, Room, AttackBool, Region)''')
c.execute('''CREATE TABLE MonsterThreat (RandomID, Player1, Threat1, Player2, Threat2, Player3, Threat3, Player4, Threat4, Player5, Threat5, Player6, Threat6)''')
c.execute('''CREATE TABLE Gear (ID, Name, Slot, MinValue, MaxValue, Attackspeed)''')
cursor = conn.execute('SELECT * from Gear')
equipment = [(1, 'Rusty Sword', 'Main', 1, 6, 3.0),
             (2, 'Rusty Shield', 'Shield', 4, 4, 0.0),
             (3, 'Rusty Dagger', 'Main', 1, 4, 2.0),
             (4, 'Rusty Dirk', 'Weapon', 1, 3, 2.0),
             (5, 'Rusty Mace', 'Main', 1, 5, 2.5),
             (6, 'Knobbed Staff', 'Main', 1, 6, 3.0),
             (7, 'Chain Shirt', 'Body', 4, 4, 0),
             (8, 'Chain Pants', 'Lowerbody', 3, 3, 0),
             (9, 'Leather Shirt', 'Body', 3, 3, 0),
             (10, 'Leather Pants', 'Lowerbody', 2, 2, 0),
             (11, 'Cloth Shirt', 'Body', 2, 2, 0),
             (12, 'Cloth Pants', 'Lowerbody', 1, 1, 0)
            ]

regions = [('Exordior Cave', 0),
           ('Exordior Cave Deep', 0)
    ]

# ID, Description, N, E, S, W
rooms = [(1, "This is the town centre. You can rest here.", "To the north lies Pleen's famous armory, as well as the local bar.", "Off to the east there is a Church and a library, as well as a small cave you    used to play in as a child (but always too afraid to explore too deeply).", "To the south is the fish and meat market and the small general store.", "Off to the west is the small grouping of houses you grew upin.", 10, 5, 2, 8, '0', '0', '0'),
         (2, "This path is leading to the Fish Market (w) and General Store (e)", "To the north is the town centre", None, "Further southwest is the creek that leads to the lake Bratus Stagno.", None, 1, 4, None, 3, '0', '-1', '0'),
         (3, "Welcome to Haag's Fish and Meat Market! You can purchase food for your travels  or stay for a hot meal. Our fresh catch of the day is a tasty shrimp, which Haag has boiled with spices, potatoes, corn and broccoli.", None, None, None, None, None, 2, None, None, '-1', '-1', '0'),
         (4, "'Hello adventurer!' comes the always friendly voice of Enten. Have a seat or    look around, here you can buy items like bed rolls, backpacks, or fishing line.", None, None, None, None, None, None, None, 2, '1', '-1', '0'),
         (5, "This path leads to the Church toward the north and the Library toward the south.There's a small cave behind the Church you used to play in as a child, but never adventured too deeply into it.", None, "Due east is the Bratus Nemus forest", None, "To the west is the town centre.", 6, None, 7, 1, '1', '0', '0'),
         (6, "The old Church stands high with the golden cross on its steeple always shining  in the sky. You almost always find someone inside praying, and the Priest here  is one of the most spiritual men you know. Behind the Church is a small cave you used to play in as a child.", None, None, None, None, None, 13, 5, None, '1', '1', '0'),
         (7, "This is the Exordior Library. There are so many books you've never read while you've been here. Tons of lore and knowledge lie in these books", None, None, None, None, 5, None, None, None, '1', '-1', '0'),
         (8, "This path leads to the house you grew up in, along with others you've grown     fond of over the years.", None, None, "Southwest of here is the creek that leads to lake Bratus Stagno.", None, None, 1, None, 9, '-1', '0', '0'),
         (9, "You think you smell home cooking, but it always seems that way when you get close to home.", None, None, None, None, None, 8, None, None, '-2', '0', '0'),
         (10, "This path leads to the famous Armory (north) and the Tavern (west).", "Further north leads to the Elvish town of Hoa Gobel, the keepers of peace withinthe Iugum region, or maybe even all of Arr'fia.", None, None, None, 12, None, 1, 11, '0', '1', '0'),
         (11, "'Come have a drink!' Rehsif shouts. You see some of your old mates here already having their fill.", None, None, None, None, None, 10, None, None, '-1', '1', '0'),
         (12, "You see Pleen. Pleen is considered by many to be one of the most talented       blacksmiths in the entire Iugum region. He is always hard at work and likes to  try crazy things and new weapon designs all the time; but it definitely pays off. You wouldn't call him an artist, though. His weapons are incredibly well made, balanced, and durable. His armor is just the same. Pleen himself is a master of the sword, and will tell you if he thinks you're ready to move on to something a bit more advanced. You can ask Pleen what he recommends.", None, None, None, None, None, None, 10, None, '0', '2', '0'),
         (13, "The small cave. Your childhood memories alwayst riggers the same creepy feeling you got when you entered in, but this time you're feeling a bit more courageous.", None, None, "South leads into the cave.", None, None, None, 14, 6, '0', '2', '-1'),
         (14, "You're in the mouth of the cave. It sounds like there could be things in here,  but it could also just be the sounds of the outside echoing back to you.", None, None, None, None, 13, None, 15, None, '0', '1', '-3'),
         (15, "This is the furthest you would ever go as a child. There tunnels leading left   and right, but you didn't want to get lost. Maybe you should leave breadcrumbs? You can see just well enough to see where you're going. If you ran into any     creatures in here it might be trouble.", None, None, None, None, 14, 17, 18, 16, '0', '0', '-5'),
         (16, "It's dark in here. You can make out a tunnel to the south, and it looks like    there's other tunnels branching off. You hope you don't get lost. The noises you heard are getting louder.", None, None, None, None, None, 15, 21, None, '-1', '0', '-5'),
         (17, "You can't see very well but that's okay. There's already two different tunnels, one leading off to the south and the one you're in keeps going straight east.", None, None, None, None, None, 25, 26, 15, '1', '0', '-5'),
         (18, "You think you can actually make out a small crack in the wall that you can fit  through. It's a bit of a squeeze but you can make it. The tunnel you're in also continues on down, though the hill gets steeper.", None, None, None, None, 15, None, 19, 22, '0', '-1', '-5'),
         (19, "You tread carefully down the steep rocky incline. Staying aware of all the      stalagmites growing off the cold damp ground so you don't run into them. The    sound of your own equipment echoing almost drowns of the odd, almost scurrying  sounds you're hearing.", None, None, None, None, 18, 20, None, None, '0', '-2', '-5'),
         (20, "All around you seems to get smaller and more cramped until you can't move any   further. Unless you were a rat, it looks like the cave ends here.", None, None, None, None, None, None, None, 19, '1', '-2', '-5'),
         (21, "It's pitch black now. Feeling around, it looks like the cave continues on,      though you think you feel an entrance to your left as well.", None, None, None, None, 16, None, 22, 24, '-1', '-1', '-5'),
         (22, "There are small glowing pebbles that give off enough light to barely make out   what is around you. It seems like the cave ends here, but you do notice a small crack you think you can fit through as well.""", None, None, None, None, 21, 18, None, None, '-1', '-2', '-5'),
         (23, "It looks like the tunnel ends here, but it may just be too dark to see if it    goes any further.", None, None, None, None, 24, None, None, None, '-2', '-2', '-5'),
         (24, "You almost feel lost... the tunnel veers off left here, and to your right is    where you just came from. The noises you hear are getting louder, but it could  be because the tunnel itself is getting smaller and smaller around you.", None, None, None, None, None, 21, 23, None, '-2', '-1', '-5'),
         (25, "It's dark in here.", None, None, None, None, 27, 29, 26, 17, '2', '0', '-5'),
         (26, "There's a small tunnel to your left, but you'd have to get on your belly and    crawl because of how low to the ground it is. That seems like the only way to   go, though.", None, None, None, None, 25, None, None, 17, '2', '-1', '-5'),
         (27, "You feel around and notice the tunnel takes a turn to the right now, but you    also notice the cave walls are starting to close in around you.", None, None, None, None, None, 28, 25, None, '2', '1', '-5'),
         (28, "This room is very cramped, it doesn't look like it's going to go any further.", None, None, None, None, None, None, None, 27, '3', '1', '-5'),
         (29, "You've come to a small deadend in the tunnel, a few corpses of rats lie around  the floor", None, None, None, "The only way is back west", None, None, None, 25, '3', '0', '-5')
    ]

# ID, Attack1, Min1, Max1, Attack2, Min2, Max2, Attack3, Min3, Max3, Attack4, Min4, Max4
mobattacks = [(1, 'Morningstar', 2, 9, 'Javelin', 2, 9, '', 0, 0, '', 0, 0),
              (2, 'Shortsword', 3, 7, 'Light Crossbow', 3, 9, '', 0, 0, '', 0, 0),
              (3, 'Half Spear', 3, 6, 'Light Crossbow', 3, 9, '', 0, 0, '', 0, 0),
              (4, 'Great Axe', 5, 13, 'Javelin', 3, 9, '', 0, 0, '', 0, 0),
              (5, 'Tentacle Slap', 6, 10, '', 0, 0, '', 0, 0, '', 0, 0),
              (6, 'Slam', 5 ,9, '', 0, 0, '', 0, 0, '', 0, 0),
              (7, 'Bite', 3, 6, '', 0, 0, '', 0, 0, '', 0, 0),
              (8, 'Bite', 4, 8, 'Gnaw', 6, 11, '', 0, 0, '', 0, 0),
              (9, 'Bite', 4, 8, 'Gnaw', 6, 11, '', 0, 0, '', 0, 0),
              (10, 'Bite', 5, 9, 'Gnaw', 5, 10, '', 0, 0, '', 0, 0),
              (11, 'Bone Crunch', 11, 14, 'Gnaw', 5, 10, '', 0, 0, '', 0, 0),
              (12, 'Bone Crunch', 11, 14, 'Leaping Strike', 12, 15, '', 0, 0, '', 0, 0),
              (13, 'Shadow Slice', 9, 12, '', 0, 0, '', 0, 0, '', 0, 0),
              (14, 'Bone Crunch', 11, 14, 'Leaping Strike', 12, 15, '', 0, 0, '', 0, 0),
              (15, 'Bite', 6, 10, 'Gnaw', 8, 11, '', 0, 0, '', 0, 0),
              (16, 'Bite', 8, 14, 'Gnaw', 9, 15, '', 0, 0, '', 0, 0),
              (17, 'Slam', 3, 8, '', 0, 0, '', 0, 0, '', 0, 0),
              (18, 'Dagger', 2, 6, 'Lightning', 4, 10, '', 0, 0, '', 0, 0),
              (19, 'Blunt strike', 3, 7, '', 0, 0, '', 0, 0, '', 0, 0),
              ]

spawnmob = [(1, 'Goblin', 0.50, 8, 11, 13, 12, 11, 10),
            (2, 'Gnome', 0.50, 8, 12, 10, 11, 11, 11),
            (3, 'Kobold', 0.40, 6, 11, 13, 14, 10, 10),
            (4, 'Orc', 1, 15, 11, 10, 9, 8, 9),
            (5, 'Choker', 2, 16, 13, 10, 10, 13, 4),
            (6, 'Dark Mantle', 1, 16, 13, 10, 10, 10, 2,),     # Water Creature
            (7, 'Small Rat', 0.35, 10, 12, 17, 17, 12, 1),
            (8, 'Weasel', 2, 14, 10, 19, 17, 12, 2),
            (9, 'Badger', 2, 14, 19, 17, 17, 12, 2),
            (10, 'Large Bat', 2, 17, 17, 22, 20, 14, 2),
            (11, 'Ape', 3, 22, 14, 15, 14, 12, 2),
            (12, 'Wolverine', 4, 22, 19, 17, 19, 12, 2),
            (13, 'Abyssal Creature', 4, 18, 16, 15, 14, 12, 5),
            (14, 'Wolf', 3, 25, 17, 15, 16, 12, 2),
            (15, 'Boar', 4, 27, 17, 10, 12, 13, 2),
            (16, 'Lion', 5, 25, 17, 15, 15, 12, 2),
            (17, 'Doppelganger', 3, 12, 12, 13, 16, 14, 13),    # Shadow, likes swamps
            (18, 'Dryad', 1, 10, 11, 15, 15, 15, 14),
            (19, 'Dwarf', 0.50, 11, 13, 10, 10, 10, 10),
            (20, 'Elf', 0.50, 10, 8, 13, 12, 11, 11),
            (21, 'Etheral Filcher', 3, 10, 11, 18, 17, 12, 7)
        ]

#c.execute('''DELETE FROM Gear WHERE ID = 1''')
#c.executemany('''INSERT INTO ID VALUES (?,?,?)''', admin)
#print "Admin, and Server Accounts Made"
c.executemany('''INSERT INTO Gear VALUES (?,?,?,?,?,?)''', equipment)
print "Gear Created"
c.executemany('''INSERT INTO Monsters VALUES (?,?,?,?,?,?,?,?,?)''', spawnmob)
c.executemany('''INSERT INTO MonsterAttacks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', mobattacks)
print "Monsters Entered"
c.executemany('''INSERT INTO RoomExits VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', rooms)

# creates 1000 empty rooms for mobs
count = 1
while count <= 1000:
    roommobs = (count, '', '', '', '', '', '', '', '', '', '')
    c.execute('''INSERT INTO RoomMobs VALUES (?,?,?,?,?,?,?,?,?,?,?)''', roommobs)
    count += 1
print "Created 1000 empty rooms to put mobs in"

# creates 1000 empty rooms for players
count = 1
while count <= 1000:
    roomplayers = (count, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    c.execute('''INSERT INTO RoomPlayers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', roomplayers)
    count += 1
print "Created 1000 empty rooms to put players in"

# creates 1000 empty rooms for players
count = 1
while count <= 1000:
    roomitems = (count, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    c.execute('''INSERT INTO RoomItems VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', roomitems)
    count += 1
print "Created 1000 empty rooms to put items in"

c.executemany('''INSERT INTO Regions VALUES (?,?)''', regions)
print "Regions made"

#for row in c.execute('''SELECT * from Monsters ORDER BY ID'''):
#    print row
#c.execute('''UPDATE Gear SET Slot='Weapon' WHERE ID=4''')

print ""
print ""
print "Hit Enter to commit"
raw_input()
conn.commit()
conn.close()