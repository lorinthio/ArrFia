import sqlite3
import rooms
import items

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
c.execute('''CREATE TABLE RoomUpDown (ID, Up, Down)''')
c.execute('''CREATE TABLE ServerTime (Server, Minutes, Hours, Night)''')
c.execute('''CREATE TABLE ClassSkills (Class, Skilldictionary)''')
conn.commit()

#skills = [('Warrior', '{1: }')
#    ]

#c.executemany()
c.execute('''INSERT INTO ServerTime VALUES (?,?,?,?)''', ('Server', 0, 0, False))

regions = [('Exordior Cave', 0),
           ('Exordior Mine', 0)
    ]

roomupdown = [(20, None, 30),
              (30, 20, None)
    ]

# ID, Description, N, E, S, W
roomentries = rooms.roomentries
items = items.items

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
            (15, 'Boar', 4, 25, 17, 10, 12, 13, 2),
            (16, 'Lion', 5, 21, 17, 15, 15, 12, 2),
            (17, 'Doppelganger', 3, 12, 12, 13, 16, 14, 13),    # Shadow, likes swamps
            (18, 'Dryad', 1, 10, 11, 15, 15, 15, 14),
            (19, 'Dwarf', 0.50, 11, 14, 10, 10, 10, 10),
            (20, 'Elf', 0.50, 10, 12, 13, 12, 11, 11),
            (21, 'Etheral Filcher', 3, 20, 11, 18, 17, 12, 7)
        ]

#c.execute('''DELETE FROM Gear WHERE ID = 1''')
#c.executemany('''INSERT INTO ID VALUES (?,?,?)''', admin)
#print "Admin, and Server Accounts Made"
c.executemany('''INSERT INTO Gear VALUES (?,?,?,?,?,?)''', items)
print "Gear Created"
c.executemany('''INSERT INTO Monsters VALUES (?,?,?,?,?,?,?,?,?)''', spawnmob)
c.executemany('''INSERT INTO MonsterAttacks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', mobattacks)
print "Monsters Entered"
c.executemany('''INSERT INTO RoomUpDown VALUES (?,?,?)''', roomupdown)

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

c.executemany('''INSERT INTO RoomExits VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', roomentries)
print "Rooms entered"
#for row in c.execute('''SELECT * from Monsters ORDER BY ID'''):
#    print row
#c.execute('''UPDATE Gear SET Slot='Weapon' WHERE ID=4''')

print ""
print ""
print "Hit Enter to commit"
raw_input()
conn.commit()
conn.close()