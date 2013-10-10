def Create2():
    import sqlite3
    conn = sqlite3.connect('Backup.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE PlayerSkills (Name, Climblevel, ClimbExp, Sneaklevel, SneakExp, Swimlevel, SwimExp, Foragelevel, ForageExp, Logginglevel, LoggingExp, Mininglevel, MiningExp, Buildinglevel, BuildingExp, Stonecuttinglevel, StonecuttingExp, Tanninglevel, TanningExp, Woodlevel, Woodexp)''')
    c.execute('''CREATE TABLE ID (Name, Password, Permission, ChatInstance)''')
    c.execute('''CREATE TABLE Placement (Name, Room)''')
    c.execute('''CREATE TABLE PlayerBonusStats (Name, MaxHealth, MaxMana, HpRegen, MpRegen, Critical, Dodge, StrDmg, IntDmg, PhsDmgResist, MagDmgResist, Accuracy, MagicAccuracy, MagicDodge)''')
    c.execute('''CREATE TABLE Character (Name, Class, Level, Exp, Exptnl, Strength, Constitution, Dexterity, Agility, Wisdom, Intellegence, Race, Gender)''')
    c.execute('''CREATE TABLE Inventory (Name, SLOT1, SLOT2, SLOT3, SLOT4, SLOT5, SLOT6, SLOT7, SLOT8, SLOT9, SLOT10, SLOT11, SLOT12, SLOT13, SLOT14, SLOT15, SLOT16, SLOT17, SLOT18, SLOT19, SLOT20, Gold)''')
    c.execute('''CREATE TABLE Equipment (Name, Mainhand, Offhand, Helmet, Body, Lowerbody, Boots)''')
    c.execute('''CREATE TABLE Vitals (Name, Health, Mana, ThreatMultiplier)''')
    conn.commit()
    print ""
    print ""
    print ""

def Import():
    import sqlite3
    conn = sqlite3.connect('Primary_Database.db')
    conn2 = sqlite3.connect('Backup.db')
    c = conn.cursor()
    c2 = conn2.cursor()
    c.execute('SELECT * FROM ID')
    rows = c.fetchall()
    for row in rows:
        Name = row[0]
        Password = row[1]
        Permission = row[2]
        ChatInstance = row[3]
        character = (Name, Password, Permission, ChatInstance,)
        c2.execute('SELECT * FROM ID Where Name=?', (Name,))
        fetch = c2.fetchone()
        if fetch == None:
            c2.execute('INSERT INTO ID VALUES (?,?,?,?)', character)

            # Room doubling
            c.execute('SELECT * From Placement Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Room = fetch[1]
            Place = (Name, Room,)
            c2.execute('INSERT INTO Placement VALUES(?,?)', Place)

            # Skills doubling
            c.execute('SELECT * From PlayerSkills Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Climblevel = fetch[1]
            ClimbExp = fetch[2]
            Sneaklevel = fetch[3]
            SneakExp = fetch[4]
            Swimlevel = fetch[5]
            SwimExp = fetch[6]
            Foragelevel = fetch[7]
            ForageExp = fetch[8]
            Logginglevel = fetch[9]
            LoggingExp = fetch[10]
            Mininglevel = fetch[11]
            MiningExp = fetch[12]
            Buildinglevel = fetch[13]
            BuildingExp = fetch[14]
            Stonecuttinglevel = fetch[15]
            StonecuttingExp = fetch[16]
            Tanninglevel = fetch[17]
            TanningExp = fetch[18]
            Woodlevel = fetch[19]
            Woodexp = fetch[20]
            skills = (Name, Climblevel, ClimbExp, Sneaklevel, SneakExp, Swimlevel, SwimExp, Foragelevel, ForageExp, Logginglevel, LoggingExp, Mininglevel, MiningExp, Buildinglevel, BuildingExp, Stonecuttinglevel, StonecuttingExp, Tanninglevel, TanningExp, Woodlevel, Woodexp)
            c2.execute('INSERT INTO PlayerSkills VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', skills)

            # Character Doubling
            c.execute('SELECT * From Character Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Class = fetch[1]
            Level = fetch[2]
            Exp = fetch[3]
            Exptnl = fetch[4]
            Strength = fetch[5]
            Constitution = fetch[6]
            Dexterity = fetch[7]
            Agility = fetch[8]
            Wisdom = fetch[9]
            Intellegence = fetch[10]
            Race = fetch[11]
            gender = fetch[12]
            Character = (Name, Class, Level, Exp, Exptnl, Strength, Constitution, Dexterity, Agility, Wisdom, Intellegence, Race, gender)
            c2.execute('INSERT INTO Character VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', Character)

            # Inventory Doubling
            c.execute('SELECT * From Inventory Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            SLOT1 = fetch[1]
            SLOT2 = fetch[2]
            SLOT3 = fetch[3]
            SLOT4 = fetch[4]
            SLOT5 = fetch[5]
            SLOT6 = fetch[6]
            SLOT7 = fetch[7]
            SLOT8 = fetch[8]
            SLOT9 = fetch[9]
            SLOT10 = fetch[10]
            SLOT11 = fetch[11]
            SLOT12 = fetch[12]
            SLOT13 = fetch[13]
            SLOT14 = fetch[14]
            SLOT15 = fetch[15]
            SLOT16 = fetch[16]
            SLOT17 = fetch[17]
            SLOT18 = fetch[18]
            SLOT19 = fetch[19]
            SLOT20 = fetch[20]
            Gold = fetch[21]
            Inventory = (Name, SLOT1, SLOT2, SLOT3, SLOT4, SLOT5, SLOT6, SLOT7, SLOT8, SLOT9, SLOT10, SLOT11, SLOT12, SLOT13, SLOT14, SLOT15, SLOT16, SLOT17, SLOT18, SLOT19, SLOT20, Gold)
            c2.execute('INSERT INTO Inventory VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', Inventory)

            # Equipment Doubling
            c.execute('SELECT * From Equipment Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Mainhand = fetch[1]
            Offhand = fetch[2]
            Helmet = fetch[3]
            Body = fetch[4]
            Lowerbody = fetch[5]
            Boots = fetch[6]
            Equip = (Name, Mainhand, Offhand, Helmet, Body, Lowerbody, Boots)
            c2.execute('INSERT INTO Equipment VALUES(?,?,?,?,?,?,?)', Equip)

            # Vitals Doubling
            c.execute('SELECT * From Vitals Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Health = fetch[1]
            Mana = fetch[2]
            ThreatMultiplier = fetch[3]
            Vitals = (Name, Health, Mana, ThreatMultiplier)
            c2.execute('INSERT INTO Vitals VALUES(?,?,?,?)', Vitals)

            # Bonus Stat Doubling
            c.execute('SELECT * FROM PlayerBonusStats Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Maxhealth = fetch[1]
            MaxMana = fetch[2]
            HpRegen = fetch[3]
            MpRegen = fetch[4]
            Critical = fetch[5]
            Dodge = fetch[6]
            StrDmg = fetch[7]
            IntDmg = fetch[8]
            PhsDmgResist = fetch[9]
            MagDmgResist = fetch[10]
            Accuracy = fetch[11]
            MagicAccuracy = fetch[12]
            MagicDodge = fetch[13]
            statbonus = (Name, Maxhealth, MaxMana, HpRegen, MpRegen, Critical, Dodge, StrDmg, IntDmg, PhsDmgResist, MagDmgResist, Accuracy, MagicAccuracy, MagicDodge)
            c2.execute('INSERT INTO PlayerBonusStats VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', statbonus)
            print "Created", Name, "in backup"
        else:
            Character = (Password, Permission, ChatInstance, Name,)
            c2.execute('UPDATE ID Set Password=?, Permission=?, ChatInstance=? WHERE Name=?', Character)

            # Room updating
            c.execute('SELECT * From Placement Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Room = fetch[1]
            Place = (Room, Name,)
            c2.execute('UPDATE Placement Set Room=? WHERE Name=?', Place)

            # Skills updating
            c.execute('SELECT * From PlayerSkills Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Climblevel = fetch[1]
            ClimbExp = fetch[2]
            Sneaklevel = fetch[3]
            SneakExp = fetch[4]
            Swimlevel = fetch[5]
            SwimExp = fetch[6]
            Foragelevel = fetch[7]
            ForageExp = fetch[8]
            Logginglevel = fetch[9]
            LoggingExp = fetch[10]
            Mininglevel = fetch[11]
            MiningExp = fetch[12]
            Buildinglevel = fetch[13]
            BuildingExp = fetch[14]
            Stonecuttinglevel = fetch[15]
            StonecuttingExp = fetch[16]
            Tanninglevel = fetch[17]
            TanningExp = fetch[18]
            Woodlevel = fetch[19]
            Woodexp = fetch[20]
            skills = (Climblevel, ClimbExp, Sneaklevel, SneakExp, Swimlevel, SwimExp, Foragelevel, ForageExp, Logginglevel, LoggingExp, Mininglevel, MiningExp, Buildinglevel, BuildingExp, Stonecuttinglevel, StonecuttingExp, Tanninglevel, TanningExp, Woodlevel, Woodexp, Name)
            c2.execute('UPDATE PlayerSkills SET Climblevel=?, ClimbExp=?, Sneaklevel=?, SneakExp=?, Swimlevel=?, SwimExp=?, Foragelevel=?, ForageExp=?, Logginglevel=?, LoggingExp=?, Mininglevel=?, MiningExp=?, Buildinglevel=?, BuildingExp=?, Stonecuttinglevel=?, StonecuttingExp=?, Tanninglevel=?, TanningExp=?, Woodlevel=?, Woodexp=? WHERE Name=?', skills)

            # Character Doubling
            c.execute('SELECT * From Character Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Class = fetch[1]
            Level = fetch[2]
            Exp = fetch[3]
            Exptnl = fetch[4]
            Strength = fetch[5]
            Constitution = fetch[6]
            Dexterity = fetch[7]
            Agility = fetch[8]
            Wisdom = fetch[9]
            Intellegence = fetch[10]
            Race = fetch[11]
            gender = fetch[12]
            Character = (Class, Level, Exp, Exptnl, Strength, Constitution, Dexterity, Agility, Wisdom, Intellegence, Race, Name, gender)
            c2.execute('UPDATE Character SET Class=?, Level=?, Exp=?, Exptnl=?, Strength=?, Constitution=?, Dexterity=?, Agility=?, Wisdom=?, Intellegence=?, Race=?, Gender=? WHERE Name=?', Character)

            # Inventory Doubling
            c.execute('SELECT * From Inventory Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            SLOT1 = fetch[1]
            SLOT2 = fetch[2]
            SLOT3 = fetch[3]
            SLOT4 = fetch[4]
            SLOT5 = fetch[5]
            SLOT6 = fetch[6]
            SLOT7 = fetch[7]
            SLOT8 = fetch[8]
            SLOT9 = fetch[9]
            SLOT10 = fetch[10]
            SLOT11 = fetch[11]
            SLOT12 = fetch[12]
            SLOT13 = fetch[13]
            SLOT14 = fetch[14]
            SLOT15 = fetch[15]
            SLOT16 = fetch[16]
            SLOT17 = fetch[17]
            SLOT18 = fetch[18]
            SLOT19 = fetch[19]
            SLOT20 = fetch[20]
            Gold = fetch[21]
            Inventory = (SLOT1, SLOT2, SLOT3, SLOT4, SLOT5, SLOT6, SLOT7, SLOT8, SLOT9, SLOT10, SLOT11, SLOT12, SLOT13, SLOT14, SLOT15, SLOT16, SLOT17, SLOT18, SLOT19, SLOT20, Gold, Name)
            c2.execute('UPDATE Inventory SET SLOT1=?, SLOT2=?, SLOT3=?, SLOT4=?, SLOT5=?, SLOT6=?, SLOT7=?, SLOT8=?, SLOT9=?, SLOT10=?, SLOT11=?, SLOT12=?, SLOT13=?, SLOT14=?, SLOT15=?, SLOT16=?, SLOT17=?, SLOT18=?, SLOT19=?, SLOT20=?, Gold=? WHERE Name=?', Inventory)

            # Equipment Doubling
            c.execute('SELECT * From Equipment Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Mainhand = fetch[1]
            Offhand = fetch[2]
            Helmet = fetch[3]
            Body = fetch[4]
            Lowerbody = fetch[5]
            Boots = fetch[6]
            Equip = (Mainhand, Offhand, Helmet, Body, Lowerbody, Boots, Name)
            c2.execute('Update Equipment Set Mainhand=?, Offhand=?, Helmet=?, Body=?, Lowerbody=?, Boots=? WHERE Name=?', Equip)

            # Vitals Doubling
            c.execute('SELECT * From Vitals Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Health = fetch[1]
            Mana = fetch[2]
            ThreatMultiplier = fetch[3]
            Vitals = (Health, Mana, ThreatMultiplier, Name)
            c2.execute('UPDATE Vitals SET Health=?, Mana=?, ThreatMultiplier=? WHERE Name=?', Vitals)

            # Bonus Stat Doubling
            c.execute('SELECT * FROM PlayerBonusStats Where Name=?', (Name,))
            fetch = c.fetchone()
            Name = fetch[0]
            Maxhealth = fetch[1]
            MaxMana = fetch[2]
            HpRegen = fetch[3]
            MpRegen = fetch[4]
            Critical = fetch[5]
            Dodge = fetch[6]
            StrDmg = fetch[7]
            IntDmg = fetch[8]
            PhsDmgResist = fetch[9]
            MagDmgResist = fetch[10]
            Accuracy = fetch[11]
            MagicAccuracy = fetch[12]
            MagicDodge = fetch[13]
            statbonus = (Maxhealth, MaxMana, HpRegen, MpRegen, Critical, Dodge, StrDmg, IntDmg, PhsDmgResist, MagDmgResist, Accuracy, MagicAccuracy, MagicDodge, Name)
            c2.execute('UPDATE PlayerBonusStats SET Maxhealth=?, MaxMana=?, HpRegen=?, MpRegen=?, Critical=?, Dodge=?, StrDmg=?, IntDmg=?, PhsDmgResist=?, MagDmgResist=?, Accuracy=?, MagicAccuracy=?, MagicDodge=? WHERE Name=?', statbonus)

    conn.commit()
    conn.close()
    conn2.commit()
    conn2.close()