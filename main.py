from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from twisted.internet import task
import sys
sys.path.insert(0, 'C:\Users\Ben\Downloads\DatabaseInformation')
import Databasecreate
import Databasecreate2
import random
import sqlite3
import string
import time
import datetime

global c
global __name__
global userlist
global localtime

conn = sqlite3.connect('Primary_Database.db')
c = conn.cursor()

def LocalTime():
    global localtime
    ltime = time.localtime()
    Hour = str(ltime[3])
    Minute = str(ltime[4])
    Second = str(ltime[5])
    localtime =  "[" + Hour + ":" + Minute + ":" + Second + "]"
    return localtime

try:
    c.execute("Select * From ServerTime")
except:
    print "No Database... Creating one"
    Databasecreate.Create()
userlist = {}

def StopAll():
    print "Everyone disconnected, safe to close..."
    reactor.stop()

class Chat(LineReceiver):

    def __init__(self, users):
        self.type = "Player"
        self.users = users
        self.name = ''
        self.password = ''
        self.spawn = True
        self.restready = True
        self.pkswitch = True
        self.pk = False
        self.pkilled = 0
        self.room = 1
        self.lastroom = self.room
        self.placement = 20
        self.classname = ''
        self.race = ''
        self.level = 0
        self.exp = 0
        self.exptnl = 0
        self.health = 0
        self.maxhealth = 0
        self.healthregen = 0
        self.mana = 0
        self.maxmana = 0
        self.manaregen = 0
        self.mainhand = ''
        self.mainhandid = 0
        self.mainhandvalmin = 0
        self.mainhandvalmax = 0
        self.mainhandspeed = 0
        self.offhand = ''
        self.offhandspeed = 0
        self.offhandid = 0
        self.offhandtype = ''
        self.offhandvalmin = 0
        self.offhandvalmax = 0
        self.helmet = ''
        self.helmetid = 0
        self.helmetvalue = 0
        self.body = ''
        self.bodyid = 0
        self.bodyvalue = 0
        self.lowerbody = ''
        self.lowerbodyid = 0
        self.lowerbodyvalue = 0
        self.boots = ''
        self.bootsid = None
        self.bootsvalue = 0
        self.strength = 0
        self.constitution = 0
        self.dexterity = 0
        self.agility = 0
        self.intellegence = 0
        self.wisdom = 0
        self.state = ''
        self.whisper = ""
        self.attack = 0
        self.normalattack = 0
        self.defence = 0
        self.normaldefence = 0
        self.mattack = 0
        self.damageresist = 0
        self.magicresist = 0
        self.mdefence = 0
        self.dodge = 0
        self.spot = 0
        self.sneak = 0
        self.accuracy = 0
        self.magicaccuracy = 0
        self.magicdodge = 0
        self.critical = 0
        self.speedmod = 0
        self.strengthdamage = 0
        self.magicdamage = 0
        self.attackspeed = 0
        self.attackready = True
        self.attributepoints = 0
        self.skillpoints = 0
        self.suicide = True
        self.threatmultiplier = 10
        self.gender = ''
        # This is where players will access each others info through this party dictionary
        self.party = []
        self.partybool = False
        self.permission = 'Member'        # Member, Moderator, Admin, Server
        self.adminmode = False

        ### INVENTORY
        self.gold = 0
        self.slot1 = 0
        self.slot1name = ''
        self.slot2 = 0
        self.slot2name = ''
        self.slot3 = 0
        self.slot3name = ''
        self.slot4 = 0
        self.slot4name = ''
        self.slot5 = 0
        self.slot5name = ''
        self.slot6 = 0
        self.slot6name = ''
        self.slot7 = 0
        self.slot7name = ''
        self.slot8 = 0
        self.slot8name = ''
        self.slot9 = 0
        self.slot9name = ''
        self.slot10 = 0
        self.slot10name = ''
        self.slot11 = 0
        self.slot11name = ''
        self.slot12 = 0
        self.slot12name = ''
        self.slot13 = 0
        self.slot13name = ''
        self.slot14 = 0
        self.slot14name = ''
        self.slot15 = 0
        self.slot15name = ''
        self.slot16 = 0
        self.slot16name = ''
        self.slot17 = 0
        self.slot17name = ''
        self.slot18 = 0
        self.slot18name = ''
        self.slot19 = 0
        self.slot19name = ''
        self.slot20 = 0
        self.slot20name = ''
        self.regionname = ''
        self.xcoord = 0
        self.ycoord = 0
        self.zcoord = 0

        # Skill Cooldowns
#        self.skilldict = {1= 'self.skill1 = True', 2= 'self.skill2 = True', 3= 'self.skill3 = True', 4='self.skill4 = True', 5='self.skill5 = True'}
        self.skill1 = True
        self.skill2 = True
        self.skill3 = True
        self.skill4 = True
        self.skill5 = True

        # ADVENTURE SKILLS
        self.Climbing = 1
        self.Climbingtnl = 100
        self.Swimming = 1
        self.Swimmingtnl = 100
        self.Sneakskill = 1
        self.Sneakskilltnl = 100

        # GATHERING SKILLS
        self.Mining = 1
        self.Miningtnl = 100
        self.Foraging = 1
        self.Foragingtnl = 100
        self.Logging = 1
        self.Loggingtnl = 100

        # CRAFTING SKILLS
        self.Woodcutting = 1
        self.Woodcuttingtnl = 100
        self.Stonecutting = 1
        self.Stonecuttingtnl = 100
        self.Tanning = 1
        self.Tanningtnl = 100
        self.Building = 1
        self.Buildingtnl = 100

        # Bonus Stats
        self.maxhealthbonus = 0
        self.maxmanabonus = 0
        self.healthregenbonus = 0
        self.manaregenbonus = 0
        self.criticalbonus = 0
        self.dodgebonus = 0
        self.strengthdamagebonus = 0
        self.magicdamagebonus = 0
        self.damageresistbonus = 0
        self.magicresistbonus = 0
        self.accuracybonus = 0
        self.magicaccuracybonus = 0
        self.magicdodgebonus = 0

        # Admin Room Creation Slots
        self.createroomid = ''
        self.createroomdescrip = ''
        self.createroomdescripN = ''
        self.createroomdescripE = ''
        self.createroomdescripS = ''
        self.createroomdescripW = ''
        self.createroomidN = ''
        self.createroomidNsql = ''
        self.createroomidE = ''
        self.createroomidEsql = ''
        self.createroomidS = ''
        self.createroomidSsql = ''
        self.createroomidW = ''
        self.createroomidWsql = ''
        self.createroomcoordx = ''
        self.createroomcoordy = ''
        self.createroomcoordz = ''
        self.createroomup = ''
        self.createroomdown = ''
        self.updateroom = ''
        self.updateroominfo = ''

    def connectionMade(self):
        self.sendLine("    |^^^|                                                                       ")
        self.sendLine("     }_{    ====================================================================")
        self.sendLine('     }_{    ====================================================================')
        self.sendLine(' /|_/---\_|\        ##                             #     /##                   ')
        self.sendLine(' I _|\_/|_ I     /####                            ###   #/ ###   #             ')
        self.sendLine(' \| | | | |/    /  ###                            #    ##   ### ###            ')
        self.sendLine('    | | |          /##                                ##        #               ')
        self.sendLine("    | | |         /  ##                               ##                  ")
        self.sendLine("    | | |         /  ##     ###  /###   ###  /###   / ######  ###       /###   ")
        self.sendLine('    | | |        /    ##     ###/ #### / ###/ #### /  #####    ###     / ###  /')
        self.sendLine('    | | |        /    ##      ##   ###/   ##   ###/   ##        ##    /   ###/  ')
        self.sendLine('    |   |       /      ##     ##          ##          ##        ##   ##    ##   ')
        self.sendLine('    |   |       /########     ##          ##          ##        ##   ##    ##   ')
        self.sendLine('    |   |      /        ##    ##          ##          ##        ##   ##    ##   ')
        self.sendLine('    |   |      #        ##    ##          ##          ##        ##   ##    ##   ')
        self.sendLine('    |   |     /####      ##   ##          ##          ##        ##   ##    /#   ')
        self.sendLine('    |   |    /   ####    ## / ###         ###         ##        ### / ####/ ##  ')
        self.sendLine('    |   |   /     ##      #/   ###         ###         ##        ##/   ###   ##')
        self.sendLine("     \ /    ====================================================================")
        self.sendLine('      Y     ====================================================================')
        self.sendLine("Successfully connected to Arr'Fia!")
        self.sendLine("If you don't have a username hit enter to create an account!'")
        self.sendLine("Otherwise just login as usual")
        self.sendLine("")
        self.sendLine("Username :")
        self.state = "LOGINCHECK"

    def connectionLost(self, leave):
        self.PartyLeave('Disconnect')
        self.SAVE()
        global c
        room = self.room
        roomc = (room,)
        c.execute('''SELECT * FROM RoomPlayers WHERE ID=?''', roomc)
        test = c.fetchone()
        count = 1
        while count <= 20:
            if test[count] in('', None, 'None'):
                count = count + 1
            else:
                if test[count] == self.name:
                    column = "'Slot" + str(count) + "'"
                    c.execute("UPDATE RoomPlayers SET " + column + "=? WHERE ID=?", ('', self.room))
                    conn.commit()
                count = count + 1
        if self.users.has_key(self.name):
            message = "%s has disconnected" % (self.name)
            del self.users[self.name]
            LocalTime()
            global localtime
            print localtime, message
            for name, protocol in self.users.iteritems():
                protocol.sendLine(message)
        self.stae = 'DISCONNECTED'

# LOAD / SAVE SCRIPTS
    def LOAD(self):
#        try:
        global c
        t = str(self.name)
        t = (t,)
        c.execute('SELECT * FROM Placement WHERE Name=?', t)
        test = c.fetchone()
        if(test == None):
            print self.name, "has no room placing in spawn..."
            self.room = 1
            self.lastroom = 0
            self.xcoord = 0
            self.ycoord = 0
            self.zcoord = 0
            room = self.room
            roomc = (room,)
            c.execute('''SELECT * FROM RoomPlayers WHERE ID=?''', roomc)
            test = c.fetchone()
            count = 1
            while count <= 20:
                if test[count] not in('', None, 'None'):
                    count = count + 1
                else:
                    column = "'Slot" + str(count) + "'"
                    c.execute("UPDATE RoomPlayers SET " + column + "=? WHERE ID=?", (self.name, room))
                    self.lastroom = room
                    self.placement = count
                    self.room = room
                    conn.commit()
                    count = 30
            conn.commit()
            c.execute('''SELECT * FROM RoomPlayers WHERE ID=?''', roomc)
            test = c.fetchone()
        else:
            self.room = test[1]
            self.lastroom = self.room
            room = self.room
            roomc = (self.room,)
            c.execute('''SELECT * FROM RoomExits WHERE ID=?''', roomc)
            roomfetch = c.fetchone()
            self.xcoord = int(roomfetch[10])
            self.ycoord = int(roomfetch[11])
            self.zcoord = int(roomfetch[12])
            c.execute('''SELECT * FROM RoomPlayers WHERE ID=?''', roomc)
            test = c.fetchone()
            count = 1
            while count <= 20:
                if test[count] not in('', None, 'None'):
                    count = count + 1
                else:
                    column = "'Slot" + str(count) + "'"
                    c.execute("UPDATE RoomPlayers SET " + column + "=? WHERE ID=?", (self.name, room))
                    self.lastroom = room
                    self.placement = count
                    self.room = room
                    conn.commit()
                    count = 30
            conn.commit()
            c.execute('''SELECT * FROM RoomPlayers WHERE ID=?''', roomc)
            test = c.fetchone()
        c.execute('SELECT * FROM Character WHERE Name=?', t)
        test = c.fetchone()
        if(test == None):
            print self.name, "has no stats, So no character? Placing in creation sequence..."
            self.handle_CLEARSCREEN
            self.sendLine("***WARNING*** Do not leave during this process! it won't take long!")
            self.RACELIST()
            self.state = "RACESTART"
            return
        if(test != None):
            #Name, Class, Level, Exp, Exptnl, Strength, Constitution, Dexterity, Agility, Wisdom, Intellegence
            self.classname = str(test[1])
            self.level = test[2]
            self.exp = test[3]
            self.exptnl = test[4]
            self.strength = test[5]
            self.constitution = test[6]
            self.dexterity = test[7]
            self.agility = test[8]
            self.wisdom = test[9]
            self.intellegence = test[10]
            self.race = str(test[11])
            self.gender = str(test[12])
            self.StatCreation()
            c.execute('SELECT * FROM Vitals WHERE Name=?', t)
            test = c.fetchone()
            if(test == None):
                print self.name, "has no vitals saved, setting to max vitals"
                self.health = self.maxhealth
                self.mana = self.maxmana
            if(test != None):
                self.health = test[1]
                self.mana = test[2]
                self.sendLine("Character Successfully Loaded")
                c.execute('SELECT * FROM Equipment WHERE Name=?', t)
                test = c.fetchone()
                if(test == None):
                    print self.name, "has no equipment!"
                if(test != None):
                    self.mainhandid = test[1]
                    self.offhandid = test[2]
                    self.helmetid = test[3]
                    self.bodyid = test[4]
                    self.lowerbodyid = test[5]
                    self.bootsid = test[6]
                    self.EQUIPSTART()
                    c.execute('SELECT * FROM Inventory WHERE Name=?', t)
                    test = c.fetchone()
                    if(test == None):
                        print self.name, "has no inventory!"
                    if(test != None):
                        self.slot1 = int(test[1])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot1,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot1name = str(fetch[1])
                        self.slot2 = int(test[2])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot2,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot2name = str(fetch[1])
                        self.slot3 = int(test[3])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot3,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot3name = str(fetch[1])
                        self.slot4 = int(test[4])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot4,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot4name = str(fetch[1])
                        self.slot5 = int(test[5])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot5,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot5name = str(fetch[1])
                        self.slot6 = int(test[6])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot6,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot6name = str(fetch[1])
                        self.slot7 = int(test[7])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot7,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot7name = str(fetch[1])
                        self.slot8 = int(test[8])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot8,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot8name = str(fetch[1])
                        self.slot9 = int(test[9])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot9,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot9name = str(fetch[1])
                        self.slot10 = int(test[10])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot10,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot10name = str(fetch[1])
                        self.slot11 = int(test[11])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot11,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot11name = str(fetch[1])
                        self.slot12 = int(test[12])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot12,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot12name = str(fetch[1])
                        self.slot13 = int(test[13])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot13,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot13name = str(fetch[1])
                        self.slot14 = int(test[14])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot14,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot14name = str(fetch[1])
                        self.slot15 = int(test[15])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot15,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot15name = str(fetch[1])
                        self.slot16 = int(test[16])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot16,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot16name = str(fetch[1])
                        self.slot17 = int(test[17])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot17,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot17name = str(fetch[1])
                        self.slot18 = int(test[18])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot18,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot18name = str(fetch[1])
                        self.slot19 = int(test[19])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot19,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot19name = str(fetch[1])
                        self.slot20 = int(test[20])
                        c.execute('SELECT * FROM Gear WHERE ID=?', (self.slot20,))
                        fetch = c.fetchone()
                        if fetch != None:
                            self.slot20name = str(fetch[1])
                        self.gold = test[21]
                party = self.party
                party.append(self.name)
                member = str(self)
                c.execute('SELECT * FROM PlayerBonusStats WHERE Name=?', (self.name,))
                fetch = c.fetchone()
                if fetch != None:
                    self.maxhealthbonus = fetch[1]
                    self.maxhealth += self.maxhealthbonus
                    self.maxmanabonus = fetch[2]
                    self.maxmana += self.maxmanabonus
                    self.healthregenbonus = fetch[3]
                    self.healthregen += self.healthregenbonus
                    self.manaregenbonus = fetch[4]
                    self.manaregen += self.manaregenbonus
                    self.criticalbonus = fetch[5]
                    self.critical = self.critical + self.criticalbonus
                    self.dodgebonus = fetch[6]
                    self.dodge += self.dodgebonus
                    self.strengthdamagebonus = fetch[7]
                    self.strengthdamage += self.strengthdamagebonus
                    self.magicdamagebonus = fetch[8]
                    self.magicdamage += self.magicdamagebonus
                    self.damageresistbonus = fetch[9]
                    self.damageresist += self.damageresistbonus
                    self.magicresistbonus = fetch[10]
                    self.magicresist += self.magicresistbonus
                    self.accuracybonus = fetch[11]
                    self.accuracy += self.accuracybonus
                    self.magicaccuracybonus = fetch[12]
                    self.magicaccuracy += self.magicaccuracybonus
                    self.magicdodgebonus = fetch[13]
                    self.magicdodge += self.magicdodgebonus
                else:
                    a = self.name
                    b = self.maxhealthbonus
                    cc = self.maxmanabonus
                    d = self.healthregenbonus
                    e = self.manaregenbonus
                    f = self.criticalbonus
                    g = self.dodgebonus
                    h = self.strengthdamagebonus
                    i = self.magicdamagebonus
                    j = self.damageresistbonus
                    k = self.magicresistbonus
                    l = self.accuracybonus
                    m = self.magicaccuracybonus
                    n = self.magicdodgebonus
                    bonus = (a, b, cc, d, e, f, g, h, i, j, k, l, m, n)
                    c.execute("INSERT INTO PlayerBonusStats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", bonus)
                    conn.commit()
                    print 'Created Bonus Stat Entry for', self.name
                name = unicode(self.name)
                c.execute('''UPDATE ID SET ChatInstance=? WHERE Name=?''', (member, name))
                conn.commit()
                name = (self.name,)
                c.execute('''SELECT * FROM PlayerSkills WHERE Name=?''', name)
                fetch = c.fetchone()
                if fetch == None:
                    print "Skills not found for", self.name
                else:
                    self.Climbing = int(fetch[1])
                    self.Climbingtnl = int(fetch[2])
                    self.Sneakskill = int(fetch[3])
                    self.Sneakskilltnl = int(fetch[4])
                LocalTime()
                global localtime
                print localtime, self.name, "has joined the server"
                global userlist
                userlist[self.name] = self
                self.handle_WELCOME()
#        except:
#            print "Error with LOAD()"

    def SAVE(self):
        try:
            global c
            global conn
            r = self.room
            t = self.name
            t = (r, t,)
    #        try:
            c.execute('UPDATE Placement SET Room=? WHERE Name=?', t)
            conn.commit()
            l = self.classname
            b = self.level
            cc = self.exp
            d = self.exptnl
            e = self.strength
            f = self.constitution
            g = self.dexterity
            h = self.agility
            i = self.wisdom
            j = self.intellegence
            k = self.name
            a = (l, b, cc, d, e, f, g, h, i, j, k,)
            # try:
            c.execute('UPDATE Character SET Class=?, Level=?, Exp=?, Exptnl=?, Strength=?, Constitution=?, Dexterity=?, Agility=?, Wisdom=?, Intellegence=? WHERE Name=?', a)
            b = self.mainhandid
            cc = self.offhandid
            d = self.helmetid
            e = self.bodyid
            f = self.lowerbodyid
            g = self.bootsid
            h = self.name
            a = (b, cc, d, e, f, g, h,)
            # try:
            c.execute('UPDATE Equipment SET Mainhand=?, Offhand=?, Helmet=?, Body=?, Lowerbody=?, Boots=? WHERE Name=?', a)
            b = self.health
            cc = self.mana
            d = self.name
            a = (b, cc, d,)
            # try:
            c.execute('UPDATE Vitals SET Health=?, Mana=? WHERE Name=?', a)
            b = self.slot1
            cc = self.slot2
            d = self.slot3
            e = self.slot4
            f = self.slot5
            g = self.slot6
            h = self.slot7
            i = self.slot8
            j = self.slot9
            k = self.slot10
            l = self.slot11
            m = self.slot12
            n = self.slot13
            o = self.slot14
            p = self.slot15
            q = self.slot16
            r = self.slot17
            s = self.slot18
            t = self.slot19
            u = self.slot20
            v = self.gold
            w = self.name
            a = (b, cc, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w)
            c.execute('UPDATE Inventory SET SLOT1=?, SLOT2=?, SLOT3=?, SLOT4=?, SLOT5=?, SLOT6=?, SLOT7=?, SLOT8=?, SLOT9=?, SLOT10=?, SLOT11=?, SLOT12=?, SLOT13=?, SLOT14=?, SLOT15=?, SLOT16=?, SLOT17=?, SLOT18=?, SLOT19=?, SLOT20=?, Gold=? WHERE Name=?', a)
            # Name, Climblevel, ClimbExp, Sneaklevel, SneakExp, Spotlevel, SpotExp, Swimlevel, SwimExp, Foragelevel, ForageExp, Logginglevel, LoggingExp, Mininglevel, MiningExp, Buildinglevel, BuildingExp, Stonecuttinglevel, StonecuttingExp, Tanninglevel, TanningExp, Woodlevel, Woodexp
            a = self.name
            b = self.Climbing
            cc = self.Climbingtnl
            d = self.Sneakskill
            e = self.Sneakskilltnl
            g = self.Swimming
            h = self.Swimmingtnl
            i = self.Foraging
            j = self.Foragingtnl
            k = self.Logging
            l = self.Loggingtnl
            m = self.Mining
            n = self.Miningtnl
            o = self.Building
            p = self.Buildingtnl
            q = self.Stonecutting
            r = self.Stonecuttingtnl
            s = self.Tanning
            t = self.Tanningtnl
            u = self.Woodcutting
            v = self.Woodcuttingtnl
            skills = (b, cc, d, e, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, a)
            c.execute('UPDATE PlayerSkills SET Climblevel=?, ClimbExp=?, Sneaklevel=?, SneakExp=?, Swimlevel=?, SwimExp=?, Foragelevel=?, ForageExp=?, Logginglevel=?, LoggingExp=?, Mininglevel=?, MiningExp=?, Buildinglevel=?, BuildingExp=?, Stonecuttinglevel=?, StonecuttingExp=?, Tanninglevel=?, TanningExp=?, Woodlevel=?, Woodexp=? WHERE Name=?', skills)
            a = self.name
            b = self.maxhealthbonus
            cc = self.maxmanabonus
            d = self.healthregenbonus
            e = self.manaregenbonus
            f = self.criticalbonus
            g = self.dodgebonus
            h = self.strengthdamagebonus
            i = self.magicdamagebonus
            j = self.damageresistbonus
            k = self.magicresistbonus
            l = self.accuracybonus
            m = self.magicaccuracybonus
            n = self.magicdodgebonus
            bonus = (b, cc, d, e, f, g, h, i, j, k, l, m, n,a)
            c.execute("UPDATE PlayerBonusStats SET Maxhealth=?, MaxMana=?, HpRegen=?, MpRegen=?, Critical=?, Dodge=?, StrDmg=?, IntDmg=?, PhsDmgResist=?, MagDmgResist=?, Accuracy=?, MagicAccuracy=?, MagicDodge=? WHERE Name=?", bonus)
            self.sendLine('Save Successful!')
            conn.commit()
        except:
            print "Error with Save()"

    def FIRSTSAVE(self):
        try:
            global c
            global conn
            r = self.room
            t = self.name
            t = (t, r,)
    #        try:
            c.execute('''INSERT INTO Placement VALUES (?,?)''', t)
            l = self.classname
            b = self.level
            cc = self.exp
            d = self.exptnl
            e = self.strength
            f = self.constitution
            g = self.dexterity
            h = self.agility
            i = self.wisdom
            j = self.intellegence
            k = self.name
            n = self.race
            m = self.gender
            a = (k, l, b, cc, d, e, f, g, h, i, j, n, m)
            # try:
            c.execute('INSERT INTO Character VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', a)
            b = self.mainhandid
            cc = self.offhandid
            d = self.helmetid
            e = self.bodyid
            f = self.lowerbodyid
            g = self.bootsid
            h = self.name
            a = (h, b, cc, d, e, f, g,)
            # try:
            c.execute('INSERT INTO Equipment VALUES (?,?,?,?,?,?,?)', a)
            b = self.slot1
            cc = self.slot2
            d = self.slot3
            e = self.slot4
            f = self.slot5
            g = self.slot6
            h = self.slot7
            i = self.slot8
            j = self.slot9
            k = self.slot10
            l = self.slot11
            m = self.slot12
            n = self.slot13
            o = self.slot14
            p = self.slot15
            q = self.slot16
            r = self.slot17
            s = self.slot18
            t = self.slot19
            u = self.slot20
            v = self.gold
            w = self.name
            a = (w, b, cc, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v)
            c.execute('INSERT INTO Inventory VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', a)
            b = self.health
            cc = self.mana
            d = self.name
            a = (d, b, cc, 10)
            # try:
            c.execute('INSERT INTO Vitals VALUES (?,?,?,?)', a)
            # Name, Climblevel, ClimbExp, Sneaklevel, SneakExp, Spotlevel, SpotExp, Swimlevel, SwimExp, Foragelevel, ForageExp, Logginglevel, LoggingExp, Mininglevel, MiningExp, Buildinglevel, BuildingExp, Stonecuttinglevel, StonecuttingExp, Tanninglevel, TanningExp, Woodlevel, Woodexp
            a = self.name
            b = self.Climbing
            cc = self.Climbingtnl
            d = self.Sneakskill
            e = self.Sneakskilltnl
            g = self.Swimming
            h = self.Swimmingtnl
            i = self.Foraging
            j = self.Foragingtnl
            k = self.Logging
            l = self.Loggingtnl
            m = self.Mining
            n = self.Miningtnl
            o = self.Building
            p = self.Buildingtnl
            q = self.Stonecutting
            r = self.Stonecuttingtnl
            s = self.Tanning
            t = self.Tanningtnl
            u = self.Woodcutting
            v = self.Woodcuttingtnl
            skills = (a, b, cc, d, e, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v)
            c.execute('INSERT INTO PlayerSkills VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', skills)
            # (Name, Maxhealth, MaxMana, HpRegen, MpRegen, Critical, Dodge, StrDmg, IntDmg, PhsDmgResist, MagDmgResist, Accuracy, MagicAccuracy, MagicDodge
            a = self.name
            b = self.maxhealthbonus
            cc = self.maxmanabonus
            d = self.healthregenbonus
            e = self.manaregenbonus
            f = self.criticalbonus
            g = self.dodgebonus
            h = self.strengthdamagebonus
            i = self.magicdamagebonus
            j = self.damageresistbonus
            k = self.magicresistbonus
            l = self.accuracybonus
            m = self.magicaccuracybonus
            n = self.magicdodgebonus
            bonus = (a, b, cc, d, e, f, g, h, i, j, k, l, m, n)
            c.execute("INSERT INTO PlayerBonusStats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", bonus)
            conn.commit()
            self.sendLine('Creation Successful!')
        except:
            print "Error in FIRSTSAVE()"

    def lineReceived(self, line):
        if self.state == "CHANGEPASS":
            self.CHANGE_PASSWORD1(line)
            return
        if self.state == "CHANGEPASS2":
            self.CHANGE_PASSWORD2(line)
            return
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
            return
        if self.state == "RACESTART":
            self.RACESTART(line)
            return
        if self.state == 'GENDER':
            self.GenderChoice(line)
            return
        if self.state == 'GENDERCONFIRM':
            self.GenderConfirm(line)
            return
        if self.state == "CHAT":
            self.handle_CHAT(line)
            return
        if self.state == "ATTACK":
            self.handle_ATTACK(line)
            return
        if self.state == 'DISCONNECTED':
            return
        if self.state == "SAY":
            self.handle_SAY(line)
            return
        if self.state == "WHISP":
            self.handle_WHISP_ini(line)
            return
        if self.state == "WHISPER":
            self.handle_WHISPER(line)
            return
        if self.state == "LOGINCHECK":
            self.handle_LOGINCHECK(line)
            return
        if self.state == "CREATE":
            self.handle_CREATE(line)
            return
        if self.state == "NCREATE":
            self.handle_NCREATE(line)
            return
        if self.state == "NCHECK":
            self.handle_NCHECK(line)
            return
        if self.state == "PASSWORD":
            self.handle_PASSWORD(line)
            return
        if self.state == "CPASSWORD":
            self.handle_CPASSWORD(line)
        if self.state == "LOGINPASS":
            self.handle_LOGINPASS(line)
            return
        if self.state == "CHECKPASS":
            self.handle_CHECKPASS(line)
            return
        if self.state == "DOUBLECHECK":
            self.handle_DOUBLECHECK(line)
            return
        if(self.state == "PSTART"):
            self.handle_PSTART(line)
            return
        if(self.state == "INFO"):
            self.handle_INFO(line)
            return
        if(self.state == "AddPoints"):
            self.AdditionalPoints(line)
            return
        if(self.state == "CCCHECK"):
            self.CCCHECK(line)
            return
        if(self.state == "AddPoints2"):
            self.AdditionalPoints2(line)
            return
        if(self.state == "CCCHECK2"):
            self.CCCHECK2(line)
            return
        if(self.state == "PartyResponse"):
            self.PartyResponse(line)
            return
        if(self.state == 'DEAD'):
            self.LOOK()
            self.state = "CHAT"
            return
        if(self.state == 'RoomIDCreate1'):
            self.CreateRoom1(line)
            return
        if(self.state == 'RoomIDCreate2'):
            self.CreateRoom2(line)
            return
        if(self.state == 'RoomIDCreate3'):
            self.CreateRoom3(line)
            return
        if(self.state == 'RoomIDCreate4'):
            self.CreateRoom4(line)
            return
        if(self.state == 'RoomIDCreate5'):
            self.CreateRoom5(line)
            return
        if(self.state == 'RoomIDCreate6'):
            self.CreateRoom6(line)
            return
        if(self.state == 'RoomIDCreate7'):
            self.CreateRoom7(line)
            return
        if(self.state == 'RoomIDCreate8'):
            self.CreateRoom8(line)
            return
        if(self.state == 'RoomIDCreate9'):
            self.CreateRoom9(line)
            return
        if(self.state == 'RoomIDCreate10'):
            self.CreateRoom10(line)
            return
        if(self.state == 'RoomIDCreate11'):
            self.CreateRoom11(line)
            return
        if(self.state == 'RoomIDCreate12'):
            self.CreateRoom12(line)
            return
        if(self.state == 'RoomIDCreate13'):
            self.CreateRoom13(line)
            return
        if(self.state == 'RoomIDCreateConfirm'):
            self.CreateRoomConfirm(line)
            return
        if(self.state == 'RoomIDCreateUpDown1'):
            self.CreateRoomUpDown1(line)
            return
        if(self.state == 'RoomIDCreateUpDown2'):
            self.CreateRoomUpDown2(line)
            return
        if(self.state == 'RoomIDCreateUpDown3'):
            self.CreateRoomUpDown3(line)
            return
        if(self.state == 'RoomIDCreateUpDownConfirm'):
            self.CreateRoomUpDownConfirm(line)
            return
        if(self.state == 'UpdateRoom1'):
            self.UpdateRoomchoice(line)
            return
        if(self.state == 'UpdateRoom2'):
            self.UpdateRoom(line)
            return
        if(self.state == 'UpdateRoom3'):
            self.UpdateRoom1(line)
            return
        if(self.state == 'UpdateRoomConfirm'):
            self.UpdateRoom2(line)
            return

#CREATION SEQUENCE

    def handle_NCREATE(self, name):
        try:
            global c
            na = name
            if len(name) <= 4:
                self.sendLine("Name too short, must be at least 5 characters long")
                return
            if name.isalpha() != True:
                self.sendLine("Name must be made of only alphabetical characters")
                return
            t = str(name)
            n = t
            t = (t,)
            c.execute('SELECT * FROM ID WHERE Name=?', t)
            name = c.fetchone()
            if(name == None):
                self.name = na
                self.sendLine("%s is available" % (n))
                self.sendLine("Is %s correct? (Y/N)" % (n))
                self.state = "NCHECK"
            else:
                self.sendLine("Name is already taken, please choose another...")
        except:
            print "Error in handle_NCREATE()"

    def handle_DOUBLECHECK(self, answer):
        if answer in('yes', 'y', 'Yes', 'Y'):
            self.sendLine("Creating Account!")
            self.users[self.name] = self
            self.permission = 'Member'
            print "Created User  :", self.name
            print "With Password : **********"
            chat = str(self)
            ID = (self.name, self.password, self.permission, chat)
            c.execute('INSERT INTO ID Values (?,?,?,?)', ID)
            conn.commit()                                     #dont forget to include this!
            global userlist
            userlist[self.name] = self
            self.handle_CLEARSCREEN
            self.sendLine("***WARNING*** Do not leave during this process! it won't take long!")
            self.state = 'GENDER'
            self.handle_CLEARSCREEN()
            self.sendLine("Is your character male or female?")
        if answer in('n', 'no', 'N', 'No'):
            self.handle_CLEARSCREEN()
            self.state = "NCREATE"
            self.sendLine("")
            self.sendLine("Please enter your desired username")

    def GenderChoice(self, choice):
        if choice in('m', 'male', 'Male', 'M'):
            self.gender = 'Male'
            self.state = 'GENDERCONFIRM'
            self.sendLine("Is male correct? (yes/no)")
        if choice in('f', 'female', 'Female', 'F'):
            self.gender = 'Female'
            self.state = 'GENDERCONFIRM'
            self.sendLine("Is female correct? (yes/no)")

    def GenderConfirm(self, line):
        if line in('yes', 'y', 'Y', 'Yes'):
            self.state = 'RACESTART'
            self.RACELIST()
        if line in('no', 'n', 'N', 'No'):
            self.state = 'GENDER'
            self.sendLine("Is your character male or female?")

    def RACESTART(self, choice):
        choice1 = choice[0:5]
        if(choice1 == '/pick'):
            choice2 = choice[6:]
            if choice2 in('Planetouched', 'planetouched', 'Bodak', 'bodak', 'Human', "human", 'Slaad', 'slaad', 'halforc', 'Halforc', 'halfelf', 'Halfelf', 'gnome', 'Gnome', 'Elf', 'elf', 'Dwarf', 'dwarf'):
                if choice2 in ('Planetouched', 'planetouched'):
                    self.race = 'Planetouched'
                    self.CLASSLIST()
                    self.state = "PSTART"
                if choice2 in ('Bodak', 'bodak'):
                    self.race = 'Bodak'
                    self.CLASSLIST()
                    self.state = "PSTART"
                if choice2 in('Human', 'human'):
                    self.race = 'Human'
                    self.CLASSLIST()
                    self.state = "PSTART"
                if choice2 in('Slaad', 'slaad'):
                    self.race = 'Slaad'
                    self.CLASSLIST()
                    self.state = "PSTART"
                if choice2 in('halforc', 'Halforc'):
                    self.race = 'Half Orc'
                    self.CLASSLIST()
                    self.state = "PSTART"
                if choice2 in('halfelf', 'Halfelf'):
                    self.race = 'Half Elf'
                    self.CLASSLIST()
                    self.state = "PSTART"
                if choice2 in('Elf', 'elf'):
                    self.race = 'Elf'
                    self.CLASSLIST()
                    self.state = "PSTART"
                if choice2 in('Dwarf', 'dwarf'):
                    self.race = 'Dwarf'
                    self.CLASSLIST()
                    self.state = "PSTART"
                if choice2 in('Gnome', 'gnome'):
                    self.race = 'Gnome'
                    self.CLASSLIST()
                    self.state = "PSTART"
            else:
                self.sendLine("Not a valid race choice try again")
                self.RACELIST()
        if(choice1 == '/info'):
            choice2 = choice[6:]
            if choice2 in('Planetouched', 'planetouched', 'Bodak', 'bodak', 'Human', "human", 'Slaad', 'slaad', 'halforc', 'Halforc', 'halfelf', 'Halfelf', 'gnome', 'Gnome', 'Elf', 'elf', 'Dwarf', 'dwarf'):
                self.RACEINFO(choice2)
            else:
                self.sendLine("invalid input")
        if(choice1 == '/list'):
            self.RACELIST()

    def RACEINFO(self, answer):
        if answer in('Planetouched', 'planetouched'):
            self.handle_CLEARSCREEN()
            self.sendLine("Planetouched are humans that have either a celestial or demon in")
            self.sendLine("their ancestry. This leads them to be more powerful, but also")
            self.sendLine("causes them to usually have a big ego...")
            self.sendLine("")
            self.sendLine("Bonus:                 Disadvantage:")
            self.sendLine(" + 1 Strength           - 1 Agility")
            self.sendLine(" + 1 Constitution")
            self.sendLine(" + 1 Wisdom")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")
        if answer in('Bodak', 'bodak'):
            self.handle_CLEARSCREEN()
            self.sendLine("Bodak are a race of undeads that have risen by their own spiritual")
            self.sendLine("strength. They come back to seek revenge and will not stop till they")
            self.sendLine("achieve their goal... or until they die... again")
            self.sendLine("")
            self.sendLine("Bonus:                 Disadvantage:")
            self.sendLine(" + 2 Strength           - 2 Constitution")
            self.sendLine(" + 1 Dexterity")
            self.sendLine(" + 1 Intellegence")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")
        if answer in('human', 'Human'):
            self.handle_CLEARSCREEN()
            self.sendLine("Humans are the most common race in Arr'Fia. They are ")
            self.sendLine("able to adapt quickly and are great leaders.")
            self.sendLine("")
            self.sendLine("Bonus:")
            self.sendLine(" + 2 Additional stat bonuses")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")
        if answer in('halforc', 'Halforc'):
            self.handle_CLEARSCREEN()
            self.sendLine("Half orcs are a race that was bred in a mix between human and orc.")
            self.sendLine("This crossbreed of a race gives birth to strong brethren")
            self.sendLine("")
            self.sendLine("Bonus:                 Disadvantage:")
            self.sendLine(" + 3 Strength          -1 Wisdom")
            self.sendLine(" + 1 Constitution      -1 Intellegence")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")
        if answer in('elf', 'Elf'):
            self.handle_CLEARSCREEN()
            self.sendLine("A race that dwells in the forest and guards nature. This race is")
            self.sendLine("nimble and intellegent.")
            self.sendLine("")
            self.sendLine("Bonus:                 Disadvantage:")
            self.sendLine(" + 1 Dexterity         - 1 Strength")
            self.sendLine(" + 1 Agility")
            self.sendLine(" + 1 Wisdom")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")
        if answer in('Dwarf', 'dwarf'):
            self.handle_CLEARSCREEN()
            self.sendLine("This race is known for its underground dwellings. They are masters")
            self.sendLine("of combat as well as craftsmanship.")
            self.sendLine("")
            self.sendLine("Bonus:                 Disadvantage:")
            self.sendLine(" + 1 Strength          - 1 Intellegence")
            self.sendLine(" + 2 Constitution")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")
        if answer in('slaad', 'Slaad'):
            self.handle_CLEARSCREEN()
            self.sendLine("This race is of reptilian origin. These are beings with more brains")
            self.sendLine("then brawn. This race consists of mostly magic users.")
            self.sendLine("")
            self.sendLine("Bonus:                 Disadvantage:")
            self.sendLine(" + 1 Wisdom            - 1 Constitution")
            self.sendLine(" + 2 Intellegence")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")
        if answer in('halfelf', 'Halfelf'):
            self.handle_CLEARSCREEN()
            self.sendLine("This race is a cross breed of humans and elves. They are leaner and")
            self.sendLine("more agile. While retaining good health")
            self.sendLine("")
            self.sendLine("Bonus:                 Disadvantage:")
            self.sendLine(" + 1 Constitution      - 1 Intellegence")
            self.sendLine(" + 1 Dexterity")
            self.sendLine(" + 1 Wisdom")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")
        if answer in('gnome', 'Gnome'):
            self.handle_CLEARSCREEN()
            self.sendLine("This race is one that enjoys a good tune, and are very cunning.")
            self.sendLine("They are very quick on their feet and make for great rogues")
            self.sendLine("")
            self.sendLine("Bonus:                 Disadvantage:")
            self.sendLine(" + 2 Agility           - 1 Strength")
            self.sendLine(" + 1 Dexterity")
            self.sendLine("")
            self.sendLine("/list to display races again")
            self.sendLine("/pick <racename> to move on")
            self.sendLine("/info <racename> to see more information")

    def CLASSLIST(self):
            self.sendLine("What class would you like to pick?")
            self.sendLine("Classes:")
            self.sendLine(" - Warrior")
            self.sendLine(" - Rogue")
            self.sendLine(" - Priest")
            self.sendLine(" - Magician")
            self.sendLine("Use /info <class> for more info")

    def RACELIST(self):
            self.sendLine("Races:")
            self.sendLine("- Bodak")
            self.sendLine("- Dwarf")
            self.sendLine("- Elf")
            self.sendLine("- Gnome")
            self.sendLine("- HalfElf")
            self.sendLine("- HalfOrc")
            self.sendLine("- Human")
            self.sendLine("- Planetouched")
            self.sendLine("- Slaad")
            self.sendLine("")
            self.sendLine("Use /info <racename> for detailed info on advantages and disadvantages")
            self.sendLine("Or use /pick <racename> to move into your class decision")

    def handle_CHECKPASS(self, answer):
        if answer in('yes', 'y', 'Yes', 'Y'):
            self.sendLine("Lets double check your info...")
            self.sendLine("Username : %s" % (self.name))
            self.sendLine("Password : %s" % (self.password))
            self.sendLine("")
            self.sendLine("Is this true?")
            self.state = "DOUBLECHECK"
        if answer in('n', 'no', 'N', 'No'):
            self.sendLine("Please enter your desired password")
            self.state = "CPASSWORD"

    def handle_CPASSWORD(self, password):
        p = str(password)
        self.password = p
        self.sendLine("Is the password... %s , correct? (Y/N)" % (p))
        self.state = "CHECKPASS"

    def handle_NCHECK(self, check):
        if check in("Y", "y"):
            self.sendLine("Please enter your desired password")
            self.state = "CPASSWORD"
        if check in("N", "n"):
            self.sendLine("Please enter the username you want, correctly")
            self.state = "NCREATE"

    def handle_CREATE(self, answer):
        if answer in('Retry', 'retry', 'r', 'R'):
            self.sendLine("Username :")
            self.state = "LOGINCHECK"
        if answer in('Create', 'C', 'create', 'c'):
            self.sendLine("Please enter your desired username")
            self.state = "NCREATE"

    def handle_PSTART(self, answer):
        choice = answer
        choice1 = choice[0:5]
        if(choice1 == '/pick'):
            choice2 = choice[6:]
            if choice2 in('Warrior', 'warrior', 'Rogue', 'rogue', 'Priest', 'priest', 'Magician', 'magician'):
                if choice2 in('warrior', 'Warrior'):
                    self.MakeWarrior()
                    self.StatCreation()
                    self.STATS()
                    self.sendLine("Pick a stat to add a point into...")
                    self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                    if self.race == 'Human':
                        self.attributepoints = 7
                    else:
                        self.attributepoints = 5
                    self.sendLine("%s points remaining" % self.attributepoints)
                    print self.name, "created a", self.classname
                    self.state = "AddPoints"
                if choice2 in('rogue', 'Rogue'):
                    self.MakeRogue()
                    self.StatCreation()
                    self.STATS()
                    self.sendLine("Pick a stat to add a point into...")
                    self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                    if self.race == 'Human':
                        self.attributepoints = 7
                    else:
                        self.attributepoints = 5
                    self.sendLine("%s points remaining" % self.attributepoints)
                    print self.name, "created a", self.classname
                    self.state = "AddPoints"
                if choice2 in('priest' 'Priest'):
                    self.MakePriest()
                    self.StatCreation()
                    self.STATS()
                    self.sendLine("Pick a stat to add a point into...")
                    self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                    if self.race == 'Human':
                        self.attributepoints = 7
                    else:
                        self.attributepoints = 5
                    self.sendLine("%s points remaining" % self.attributepoints)
                    print self.name, "created a", self.classname
                    self.state = "AddPoints"
                if choice2 in ('magician', 'Magician'):
                    self.MakeMagician()
                    self.StatCreation()
                    self.STATS()
                    self.sendLine("Pick a stat to add a point into...")
                    self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                    if self.race == 'Human':
                        self.attributepoints = 7
                    else:
                        self.attributepoints = 5
                    self.sendLine("%s points remaining" % self.attributepoints)
                    print self.name, "created a", self.classname
                    self.state = "AddPoints"
            else:
                self.sendLine("Not a valid class choice try again")
                self.sendLine("- Warrior")
                self.sendLine("- Rogue")
                self.sendLine("- Priest")
                self.sendLine("- Magician")
        if(choice1 == '/info'):
            choice2 = choice[6:]
            if choice2 in('Warrior', 'warrior', 'Rogue', 'rogue', 'Priest', 'priest', 'Magician', 'magician'):
                self.INFO(choice2)
        if(choice1 == '/list'):
            self.CLASSLIST()
        if(choice1 == 'more'):
            self.StatCreation()
            self.STATS()
            self.sendLine("Use /pick <class>, or /info <class>, or /list to see the list again")

    def INFO(self, classname):
        if classname in('warrior', 'Warrior'):
            self.handle_CLEARSCREEN()
            self.sendLine("The warrior is a class which is trained in delivering heavy blows,")
            self.sendLine("and taking hits for his allies. He utilizes a higher strength and")
            self.sendLine("constitution to support these roles. Advanced classes are as follows...")
            self.sendLine("")
            self.sendLine("Advanced Class   Requirement")
            self.sendLine("- Berserker      Level 30, 40Str, 30Dex, 30Con")
            self.sendLine("    *A strong brute with high health")
            self.sendLine("- Blademaster    Level 30, 30Str, 35Dex, 35Agi")
            self.sendLine("    *Accurate and deadly strikes")
            self.sendLine("- Paladin        Level 30, 25Str, 35Con, 30Dex, 25Wis")
            self.sendLine("    *Tank focus with healing abilities")
            self.sendLine("- Chaos Knight   Level 30, 35Str, 25Con, 30Dex, 25Int")
            self.sendLine("    *A strong fighter utilizing dark arts")
            self.MakeWarrior()
            self.INFO2()
            self.sendLine("")
            self.sendLine("Use 'more' for an indepth character sheet with stats")
            self.sendLine("Use /pick <class>, or /info <class>, or /list to see the list again")
        if classname in('rogue','Rogue'):
            self.handle_CLEARSCREEN()
            self.sendLine("The rogue is a class which is trained in quick, accurate strikes and,")
            self.sendLine("weakening his(her) enemies. He(she) utilizes a high dexterity for accuracy and")
            self.sendLine("agility to evade many incoming attacks. Advanced classes are as follows...")
            self.sendLine("")
            self.sendLine("Advanced Class   Requirement")
            self.sendLine("- Assassin       Level 30, 20Str, 40Dex, 40Agi")
            self.sendLine("    *A Master of accurate, critical strikes")
            self.sendLine(" - Blademaster   Level 30, 30Str, 35Dex, 35Agi")
            self.sendLine("    *Accurate and deadly strikes")
            self.sendLine("- Ranger         Level 30, 20Str, 30Dex, 30Agi, 25Wis")
            self.sendLine("     *Melee fighter with nature healing / poisons")
            self.sendLine("- Shadow Blades  Level 30, 20Str, 30Dex, 30Agi, 25Int")
            self.sendLine("     *An agile shadow utilizing dark blades of magic")
            self.MakeRogue()
            self.INFO2()
            self.sendLine("")
            self.sendLine("Use 'more' for an indepth character sheet with stats")
            self.sendLine("Use /pick <class>, or /info <class>, or /list to see the list again")
        if classname in('priest','Priest'):
            self.handle_CLEARSCREEN()
            self.sendLine("The priest is a class which has been trained with mental and physical aptitude.")
            self.sendLine("Using its high constitution to survive and high wisdom to heal, the priest is")
            self.sendLine("a necessary companion in any starting group. Advanced classes are as follows...")
            self.sendLine("")
            self.sendLine("Advanced Class   Requirement")
            self.sendLine("- Templar        Level 30, 30Con, 40Wis, 30Int")
            self.sendLine("    *A Magic user that focuses in group healing")
            self.sendLine("- Paladin        Level 30, 25Str, 35Con, 30Dex, 25Wis")
            self.sendLine("    *Tank focus with healing abilities")
            self.sendLine("- Ranger         Level 30, 20Str, 30Dex, 30Agi, 25Wis")
            self.sendLine("    *Melee fighter with nature healing, and poisons")
            self.sendLine("- Sage           Level 30, 20Con, 40Wis, 40Int")
            self.sendLine("    *A Master of magic that can heal and deal damage")
            self.MakePriest()
            self.INFO2()
            self.sendLine("")
            self.sendLine("Use 'more' for an indepth character sheet with stats")
            self.sendLine("Use /pick <class>, or /info <class>, or /list to see the list again")
        if classname in('magician', 'Magician'):
            self.handle_CLEARSCREEN()
            self.sendLine("The Magician is a class which has been trained with a magical focus. Using its")
            self.sendLine("high wisdom for mana, and high intellegence for spell damage, this class")
            self.sendLine("creates some powerful damage. Advanced classes are as follows...")
            self.sendLine("")
            self.sendLine("Advanced Class    Requirement")
            self.sendLine("- Arch Mage       Level 30, 20 Con, 35Wis, 45Int")
            self.sendLine("    *A Master of magic that can deal aoe damage")
            self.sendLine("- Chaos Knight    Level 30, 35Str, 30Con, 35Dex, 25Int")
            self.sendLine("    *A strong fighter utilizing dark arts")
            self.sendLine("- Shadow Blade    Level 30, 20Str, 30Dex, 30Agi, 25Int")
            self.sendLine("    *An agile shadow utilizing dark blades of magic")
            self.sendLine("- Sage            Level 30, 20Con, 40Wis, 40Int")
            self.sendLine("    *A Master of magic that can heal and deal damage")
            self.MakeMagician()
            self.INFO2()
            self.sendLine("")
            self.sendLine("Use 'more' for an indepth character sheet with stats")
            self.sendLine("Use /pick <class>, or /info <class>, or /list to see the list again")

    def INFO2(self):
        self.sendLine("Core Stats")
        self.sendLine("Strength     : %s" % (self.strength))
        self.sendLine("Constitution : %s" % (self.constitution))
        self.sendLine("Dexterity    : %s" % (self.dexterity))
        self.sendLine("Agility      : %s" % (self.agility))
        self.sendLine("Wisdom       : %s" % (self.wisdom))
        self.sendLine("Intellegence : %s" % (self.intellegence))

    def RaceAdds(self):
        if self.race == 'Planetouched':
            self.strength += 1
            self.constitution += 1
            self.wisdom += 1
            self.agility = self.agility - 1
        if self.race == 'Bodak':
            self.strength += 2
            self.constitution = self.constitution - 2
            self.dexterity += 1
            self.intellegence += 1
        if self.race == 'Half Elf':
            self.constitution += 1
            self.dexterity += 1
            self.wisdom += 1
            self.intellegence = self.intellegence - 1
        if self.race == 'Gnome':
            self.agility += 2
            self.dexterity += 1
            self.strength = self.strength - 1
        if self.race == 'Half Orc':
            self.strength += 3
            self.constitution += 1
            self.intellegence = self.intellegence - 1
            self.wisdom = self.wisdom - 1
        if self.race == 'Slaad':
            self.wisdom += 2
            self.constitution = self.constitution - 1
            self.intellegence += 1
        if self.race == 'Dwarf':
            self.strength += 1
            self.constitution += 2
            self.intellegence = self.intellegence - 1
        if self.race == 'Elf':
            self.strength = self.strength - 1
            self.dexterity += 1
            self.agility += 1
            self.wisdom += 1

    def MakeWarrior(self):
        self.level = 1
        self.exp = 0
        self.exptnl = 500
        self.classname = 'Warrior'
        self.strength = 16
        self.constitution = 16
        self.dexterity = 14
        self.agility = 12
        self.wisdom = 12
        self.intellegence = 10
        self.mainhandid = 1
        self.offhandid = 2
        self.helmet = None
        self.bodyid = 7
        self.lowerbodyid = 8
        self.boots = None
        self.RaceAdds()

    def MakeRogue(self):
        self.level = 1
        self.exp = 0
        self.exptnl = 500
        self.classname = 'Rogue'
        self.strength = 14
        self.constitution = 12
        self.dexterity = 16
        self.agility = 16
        self.wisdom = 11
        self.intellegence = 11
        self.mainhandid = 3
        self.offhandid = 4
        self.helmet = None
        self.bodyid = 9
        self.lowerbodyid = 10
        self.boots = None
        self.RaceAdds()

    def MakePriest(self):
        self.level = 1
        self.exp = 0
        self.exptnl = 500
        self.classname = 'Priest'
        self.strength = 14
        self.constitution = 16
        self.dexterity = 11
        self.agility = 11
        self.wisdom = 16
        self.intellegence = 12
        self.mainhandid = 5
        self.offhandid = 2
        self.helmet = None
        self.bodyid = 7
        self.lowerbodyid = 8
        self.bootsid = None
        self.RaceAdds()

    def MakeMagician(self):
        self.level = 1
        self.exp = 0
        self.exptnl = 500
        self.classname = 'Magician'
        self.strength = 11
        self.constitution = 12
        self.dexterity = 11
        self.agility = 14
        self.wisdom = 16
        self.intellegence = 16
        self.mainhandid = 6
        self.offhandid = None
        self.helmet = None
        self.bodyid = 11
        self.lowerbodyid = 12
        self.bootsid = None
        self.RaceAdds()

    def CCCHECK(self, answer):
        if answer in('con', 'Con', 'Continue', 'continue'):
            self.slot1 = 13
            self.slot1name = 'Copper Pick'
            self.slot2 = 14
            self.slot2name = 'Copper Axe'
            self.slot3 = 15
            self.slot3name = 'Gathering Knife'
            self.gold = 100
            self.room = 1
            #if self.classname = 'Warrior':
            #    self.spelllist = {1: self.HeavyHit, 2: self.doubleHit, 3: self.taunt, 4: self.offensiveStance}
            #if self.classname = 'Rogue':
            #    self.spelllist = {1: self.doubleStrike, 2: self.dirtyStrike, 3: self.tripleStrike}
            #if self.classname = 'Priest':
            self.state = "Room"
            party = self.party
            party.append(self.name)
            self.handle_CLEARSCREEN()
            global userlist
            diction = userlist
            for key, value in diction.iteritems():
                player = diction.get(key)
                message ="%s has joined the world of Arr'Fia" % self.name
                player.sendLine(message)
            self.sendLine("Welcome %s to the world of Arr'Fia" % (self.name))
            self.FIRSTSAVE()
            self.EQUIPSTART()
            self.handle_WELCOME()
        if answer in('res', 'Res', 'restart', 'Restart'):
            self.RACELIST()
            self.state = "RACESTART"

    def AdditionalPoints(self, stat):
        if stat in('str', 'Str', 'strength', 'Strength', 's', 'S'):
            if self.strength == 20:
                self.sendLine("You can only go to a stat max of 20 at creation")
                self.sendLine("Please pick a different stat")
                return
            else:
                self.strength = self.strength + 1
                self.attributepoints = self.attributepoints - 1
                self.StatCreation()
                self.STATS()
                if self.attributepoints > 0:
                    self.sendLine("Pick a stat to add a point into...")
                    self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                    self.sendLine("%s points remaining" % self.attributepoints)
                else:
                    self.state = "CCCHECK"
                    self.sendLine("These are the final results of your creation")
                    self.sendLine("Would you like to continue or restart? (con/res)")
        else:
            if stat in('dex', 'Dex', 'dexterity', 'Dexterity', 'd', 'D'):
                if self.dexterity == 20:
                    self.sendLine("You can only go to a stat max of 20 at creation")
                    self.sendLine("Please pick a different stat")
                    return
                else:
                    self.dexterity = self.dexterity + 1
                    self.attributepoints = self.attributepoints - 1
                    self.StatCreation()
                    self.STATS()
                    if self.attributepoints > 0:
                        self.sendLine("Pick a stat to add a point into...")
                        self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                        self.sendLine("%s points remaining" % self.attributepoints)
                    else:
                        self.state = "CCCHECK"
                        self.sendLine("These are the final results of your creation")
                        self.sendLine("Would you like to continue or restart? (con/res)")
            else:
                if stat in('con', 'Con', 'constitution', 'Constitution', 'c', 'C'):
                    if self.constitution == 20:
                        self.sendLine("You can only go to a stat max of 20 at creation")
                        self.sendLine("Please pick a different stat")
                        return
                    else:
                        self.constitution = self.constitution + 1
                        self.attributepoints = self.attributepoints - 1
                        self.StatCreation()
                        self.STATS()
                        if self.attributepoints > 0:
                            self.sendLine("Pick a stat to add a point into...")
                            self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                            self.sendLine("%s points remaining" % self.attributepoints)
                        else:
                            self.state = "CCCHECK"
                            self.sendLine("These are the final results of your creation")
                            self.sendLine("Would you like to continue or restart? (con/res)")
                else:
                    if stat in('agi', 'Agi', 'agility', 'Agility', 'a', 'A'):
                        if self.agility == 20:
                            self.sendLine("You can only go to a stat max of 20 at creation")
                            self.sendLine("Please pick a different stat")
                            return
                        else:
                            self.agility = self.agility + 1
                            self.attributepoints = self.attributepoints - 1
                            self.StatCreation()
                            self.STATS()
                            if self.attributepoints > 0:
                                self.sendLine("Pick a stat to add a point into...")
                                self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                                self.sendLine("%s points remaining" % self.attributepoints)
                            else:
                                self.state = "CCCHECK"
                                self.sendLine("These are the final results of your creation")
                                self.sendLine("Would you like to continue or restart? (con/res)")
                    else:
                        if stat in('wis', 'Wis', 'wisdom', 'Wisdom', 'w', 'W'):
                            if self.wisdom == 20:
                                self.sendLine("You can only go to a stat max of 20 at creation")
                                self.sendLine("Please pick a different stat")
                                return
                            else:
                                self.wisdom = self.wisdom + 1
                                self.attributepoints = self.attributepoints - 1
                                self.StatCreation()
                                self.STATS()
                                if self.attributepoints > 0:
                                    self.sendLine("Pick a stat to add a point into...")
                                    self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                                    self.sendLine("%s points remaining" % self.attributepoints)
                                else:
                                    self.state = "CCCHECK"
                                    self.sendLine("These are the final results of your creation")
                                    self.sendLine("Would you like to continue or restart? (con/res)")
                        else:
                            if stat in('int', 'Int', 'Intellegence', 'intellegence', 'i', 'I'):
                                if self.intellegence == 20:
                                    self.sendLine("You can only go to a stat max of 20 at creation")
                                    self.sendLine("Please pick a different stat")
                                    return
                                else:
                                    self.intellegence = self.intellegence + 1
                                    self.attributepoints = self.attributepoints - 1
                                    self.StatCreation()
                                    self.STATS()
                                    if self.attributepoints > 0:
                                        self.sendLine("Pick a stat to add a point into...")
                                        self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                                        self.sendLine("%s points remaining" % self.attributepoints)
                                    else:
                                        self.state = "CCCHECK"
                                        self.sendLine("These are the final results of your creation")
                                        self.sendLine("Would you like to continue or restart? (con/res)")

    def StatCreation(self):
        strength = self.strength
        constitution = self.constitution
        if self.classname in('Warrior', 'Priest', 'Berserker', 'Paladin', 'Chaos Knight', 'Blademaster', 'Templar'):
            health = strength * 1.75
            health2 = constitution * 2
            health = int(health)
            health2 = int(health2)
        else:
            health = strength * 1.5
            health2 = constitution * 2
            health = int(health)
            health2 = int(health2)
        healthregen = strength / 8
        healthregen2 = constitution / 4
        health = health + health2
        healthregen = healthregen + healthregen2
        attack = strength * 2
        strdmg = strength / 6.0
        strdmg = int(strdmg)
        defence = constitution * 2
        self.strengthdamage = strdmg
        self.health = health
        self.maxhealth = health
        self.healthregen = healthregen
        self.attack = attack
        self.normalattack = attack
        self.defence = defence
        self.normaldefence = defence
        dexterity = self.dexterity
        agility = self.agility
        accuracy = (dexterity * 2) + agility + 50
        accuracy = accuracy + 50
        speedmod = agility + dexterity
        if self.classname in('Shadow Blade', 'Blade Master', 'Ranger', 'Rogue'):
            speedmod = speedmod / 225.00
        else:
            speedmod = speedmod / 200.00
        speedmod = 1 - speedmod
        if self.classname in('Shadow Blade', 'Blade Master', 'Ranger', 'Rogue'):
            dodge = agility * 2
        else:
            dodge = agility * 1.5
            dodge = int(dodge)
        critical = dexterity / 4
        critical1 = agility / 4
        critical = critical + critical1
        sneak = agility * 2
        self.sneak = sneak
        self.speedmod = speedmod
        self.accuracy = accuracy
        self.dodge = dodge
        self.critical = critical
        wisdom = self.wisdom
        intellegence = self.intellegence
        if self.classname in('Warrior', 'Blade Master', 'Berserker', 'Paladin', 'Chaos Knight', 'Assassin' 'Ranger', 'Rogue'):
            mana = wisdom * 2
            mana2 = intellegence * 1.5
            mana2 = int(mana2)
        else:
            mana = wisdom * 2
            mana2 = intellegence * 2
            mana2 = int(mana2)
        manaregen = wisdom / 4
        manaregen2 = intellegence / 8
        mana = mana + mana2
        manaregen = manaregen + manaregen2
        spot = intellegence * 2
        mattack = intellegence * 2
        mdefence = wisdom * 2
        magicaccuracy = (intellegence * 2) +  wisdom + 50
        if self.classname in('Magician', 'Paladin', 'Chaos Knight', 'Ranger', 'Priest', 'Templar', 'Sage', 'Shadow Blade', 'Arch Mage'):
            magicdodge = int(wisdom * 1.75)
        else:
            magicdodge = int(wisdom * 1.5)
        magicdamage = int(intellegence / 6.0)
        self.magicdamage = magicdamage
        self.magicdodge = magicdodge
        self.magicaccuracy = magicaccuracy
        self.spot = spot
        self.mana = mana
        self.maxmana = mana
        self.manaregen = manaregen
        self.mattack = mattack
        self.mdefence = mdefence

# LOGIN SEQUENCE
    def handle_LOGINCHECK(self, name):
        global c
        if self.users.has_key(name):  # lint:ok
            self.sendLine("User is already logged in...")
            self.sendLine("Please try another name...")
        else:
            t = str(name)
            t = (t,)
            c.execute('SELECT * FROM ID WHERE Name=?', t)
            namecheck = c.fetchone()
            if(namecheck == None):
                self.sendLine("There is no account with that name")
                self.sendLine("Retry? or Create?")
                self.state = "CREATE"
            else:
                self.name = name
                self.sendLine("Password :")
                self.state = "LOGINPASS"

    def handle_LOGINPASS(self, password):
        global c
        t = str(self.name)
        t = (t,)
        test = password
        test = str(test)
        c.execute('SELECT * FROM ID WHERE Name=?', t)
        check = c.fetchone()
        check1 = check[1]
        if(test == check1):
            self.sendLine("Login Success!")
            self.handle_CLEARSCREEN()
            self.LOAD()
        else:
            self.sendLine("")
            self.sendLine("")
            self.sendLine("Login failed... try again")
            self.sendLine("Username :")
            self.state = "LOGINCHECK"



# ROOM HANDLING
    def displayMobs(self, roomlook=None, direction=None):
        global c
        if roomlook == None:
            roomlook = self.room
        room = (roomlook,)
        c.execute('''SELECT * FROM RoomMobs where ID=?''', room)
        test = c.fetchone()
        count = 1
        mobs = 0
        while count <= 5:
            if test[count] not in('', None):
                mobs = mobs + 1
                count = count + 1
            else:
                count = count + 1
        if mobs >= 1:
            if roomlook != self.room:
                self.sendLine("Mobs toward the %s" % (direction))
            else:
                self.sendLine("Mobs nearby...")
        count = 1
        while count <= 5:
            if test[count] in('', None):
                count = count + 1
            else:
                ID = str(test[count])
                ID = (ID,)
                c.execute('''SELECT * from ActiveMonster WHERE RandomID=?''', ID)
                test2 = c.fetchone()
                cnt = str(count)
                Name = test2[3]
                Name = str(Name)
                CR = test2[2]
                CR = float(CR)
                CR = self.level / CR
                if(CR >= 0.35):
                    Rating = 'Impossible'
                if(CR >= 0.50):
                    Rating = 'Very Hard'
                if(CR >= 0.66):
                    Rating = 'Hard'
                if(CR >= 0.75):
                    Rating = 'Normal-Hard'
                if(CR >= 1.00):
                    Rating = 'Normal'
                if(CR >= 1.50):
                    Rating = 'Normal-Easy'
                if(CR >= 2.00):
                    Rating = 'Easy'
                if(CR >= 5.00):
                    Rating = 'Very Easy'
                mobs = cnt + ")" + "" + Name + '[' + Rating +']'
                count = count + 1
                self.sendLine(mobs)

    def displayPlayers(self, roomlook=None, direction=None):
        global c
        if roomlook == None:
            roomlook = self.room
        room = (roomlook,)
        c.execute('''SELECT * FROM RoomPlayers where ID=?''', room)
        test = c.fetchone()
        if roomlook != self.room:
            players = "Players to the %s" % direction
        else:
            players = "Players nearby"
        count = 1
        while(count <= 20):
            teststr = test[count]
            teststr = str(teststr)
            if teststr in('', None):
                count = count + 1
            else:
                if teststr == self.name:
                    pass
                    count = count + 1
                else:
                    name = teststr
                    players = players + " " + name
                    count = count + 1
        if players == "Players to the %s" % direction:
            pass
        else:
            if players == "Players nearby":
                pass
            else:
                self.sendLine("%s" % players)

    def displayItems(self):
        global c
        room = (self.room,)
        c.execute('''SELECT * FROM RoomItems where ID=?''', room)
        test = c.fetchone()
        players = "Items in room:"
        count = 1
        while(count <= 20):
            teststr = test[count]
            teststr = str(teststr)
            if teststr in('', None):
                count = count + 1
            else:
                c.execute('''SELECT * FROM Gear where ID=?''', (teststr,))
                fetch = c.fetchone()
                name = fetch[1]
                name = "(" + str(count) + ")" + str(name)
                players = players + " " + name
                count = count + 1
        if players == "Items in room:":
            pass
        else:
            self.sendLine("%s" % players)

    def moveRooms(self, answer):
        try:
            room = self.room
            room = (room,)
            c.execute("""SELECT * FROM RoomExits where ID=?""", room)
            test = c.fetchone()
            direction = answer
            if direction in ('N', 'n', 'north', 'North'):
                if test[6] not in ('', None):
                    self.room = test[6]
                    self.updateRoom('North', 'South')
                    self.displayExits()
                else:
                    self.sendLine("Cannot go this direction")
                    self.displayExits()
            if direction in ('S', 's', 'south', 'South'):
                if test[8] not in ('', None):
                    self.room = test[8]
                    self.updateRoom('South', 'North')
                    self.displayExits()
                else:
                    self.sendLine("Cannot go this direction")
                    self.displayExits()
            if direction in ('E', 'e', 'East', 'east'):
                if test[7] not in ('', None):
                    self.room = test[7]
                    self.updateRoom('East', 'West')
                    self.displayExits()
                else:
                    self.sendLine("Cannot go this direction")
                    self.displayExits()
            if direction in ('W', 'w', 'west', 'West'):
                if test[9] not in ('', None):
                    self.room = test[9]
                    self.updateRoom('West', 'East')
                    self.displayExits()
                else:
                    self.sendLine("Cannot go this direction")
                    self.displayExits()
            c.execute('''SELECT * FROM RoomUpDown WHERE ID=?''', room)
            test = c.fetchone()
            if direction in ('D', 'd', 'down', 'Down'):
                if test[2] not in ('', None):
                    self.room = test[2]
                    self.updateRoom('Down', 'Above')
                    self.displayExits()
                else:
                    self.sendLine("Cannot go this direction")
                    self.displayExits()
            if direction in ('U', 'u', 'up', 'Up'):
                if test[1] not in ('', None):
                    self.room = test[1]
                    self.updateRoom('Up', 'Below')
                    self.displayExits()
                else:
                    self.sendLine("Cannot go this direction")
                    self.displayExits()
        except:
            print "Problem in moveRooms()"

    def updateRoom(self, direction, opposite):
        try:
            global c
            room = self.room
            roomc = (room,)
            c.execute('''SELECT * FROM RoomPlayers WHERE ID=?''', roomc)
            test = c.fetchone()
            if test is None:
                self.room = self.lastroom
                self.sendLine("Something happened... Didn't move")
                return
            counter = 1
            while counter <= 20:
                if test[counter] not in('', None, 'None'):
                    counter = counter + 1
                else:
                    lastroom = self.lastroom
                    last = (lastroom,)
                    c.execute('''SELECT * FROM RoomPlayers where ID=?''', last)
                    test = c.fetchone()
                    count = 1
                    while(count <= 20):
                        teststr = test[count]
                        teststr = str(teststr)
                        if teststr in('', None):
                            count = count + 1
                        else:
                            if teststr == self.name:
                                pass
                                count = count + 1
                            else:
                                name = teststr
                                count = count + 1
                                diction = self.users
                                name = str(name)
                                atk = diction.get(name)
                                if direction in('Teleport'):
                                    atk.sendLine("%s has teleported away!" % (self.name))
                                else:
                                    atk.sendLine("%s has moved %s" % (self.name, direction))
                    column = "'Slot" + str(self.placement) + "'"
                    c.execute("UPDATE RoomPlayers SET " + column + "=? WHERE ID=?", ('', lastroom))
                    conn.commit()
                    c.execute('''SELECT * FROM RoomPlayers where ID=?''', roomc)
                    test = c.fetchone()
                    count = 1
                    while(count <= 20):
                        teststr = test[count]
                        teststr = str(teststr)
                        if teststr in('', None):
                            count = count + 1
                        else:
                            if teststr == self.name:
                                pass
                                count = count + 1
                            else:
                                name = teststr
                                count = count + 1
                                diction = self.users
                                name = str(name)
                                atk = diction.get(name)
                                if direction in('Teleport'):
                                    atk.sendLine("%s has teleported in" % (self.name))
                                else:
                                    atk.sendLine("%s has entered from the %s" % (self.name, opposite))
                    column = "'Slot" + str(counter) + "'"
                    c.execute("UPDATE RoomPlayers SET " + column + "=? WHERE ID=?", (self.name, room))
                    self.lastroom = room
                    self.placement = counter
                    self.room = room
                    c.execute("SELECT * FROM RoomExits WHERE ID=?", (self.room,))
                    fetch = c.fetchone()
                    self.xcoord = str(fetch[10])
                    self.ycoord = str(fetch[11])
                    self.zcoord = str(fetch[12])
                    if (self.room >= 1) and (self.room <= 12):
                        self.regionname = 'Exordior'
                    if (self.room >= 13) and (self.room <= 29):
                        self.regionname = 'Cave of Exordior'
                    if (self.room >= 30) and (self.room <= 64):
                        self.regionname = 'Exordior Mine'
                    if (self.room >= 65) and (self.room <= 110):
                        self.regionname = 'Bratus Nemus'
                    if (self.room >= 111) and (self.room <= 125):
                        self.regionname = 'Exordior / Bratus Nemus Path'
                    conn.commit()
                    counter = 30
            conn.commit()
        except:
            self.sendLine("Room move was not successful")

    def displayExits(self, lookdir=None):
        try:
            global c
            if lookdir == None:
                self.LocationPrint()
            room = (self.room,)
            c.execute("""SELECT * FROM RoomExits where ID=?""", room)
            test = c.fetchone()
            if lookdir in('east', 'e', 'East'):
                roomlook = test[7]
                self.sendLine("You look to the east...")
                self.displayPlayers(roomlook, 'east')
                self.displayMobs(roomlook, 'east')
                return
            if lookdir in('north', 'n', 'North'):
                roomlook = test[6]
                self.sendLine("You look to the north...")
                self.displayPlayers(roomlook, 'north')
                self.displayMobs(roomlook, 'north')
                return
            if lookdir in('south', 's', 'South'):
                self.sendLine("You look to the south")
                roomlook = test[8]
                self.displayPlayers(roomlook, 'south')
                self.displayMobs(roomlook, 'south')
                return
            if lookdir in('west', 'w', 'West'):
                self.sendLine("You look to the west")
                roomlook = test[9]
                self.displayPlayers(roomlook, 'west')
                self.displayMobs(roomlook, 'west')
                return
            c.execute('''SELECT * FROM RoomUpDown WHERE ID=?''', room)
            test2 = c.fetchone()
            description = str(test[1])
            ndescription = str(test[2])
            edescription = str(test[3])
            sdescription = str(test[4])
            wdescription = str(test[5])
            self.sendLine("%s" % description)
            if ndescription not in (None, 'None'):
                self.sendLine("%s" % ndescription)
            if edescription not in (None, 'None'):
                self.sendLine("%s" % edescription)
            if sdescription not in (None, 'None'):
                self.sendLine("%s" % sdescription)
            if wdescription not in (None, 'None'):
                self.sendLine("%s" % wdescription)
            self.sendLine("")
            rooms = "available exits are: "
            if self.adminmode == True:
                if test[6] not in ('', None):
                    rooms = rooms + " N(" + str(test[6]) + ')'
                if test[8] not in ('', None):
                    rooms = rooms + " S(" + str(test[8]) + ')'
                if test[7] not in ('', None):
                    rooms = rooms + " E(" + str(test[7]) + ')'
                if test[9] not in ('', None):
                    rooms = rooms + " W(" + str(test[9]) + ')'
                if test2 != None:
                    if test2[1] not in ('', None):
                        rooms = rooms + " U(" + str(test2[1]) + ')'
                    if test2[2] not in ('', None):
                        rooms = rooms + " D(" + str(test2[2]) + ')'
            else:
                if test[6] not in ('', None):
                    rooms = rooms + " N"
                if test[8] not in ('', None):
                    rooms = rooms + " S"
                if test[7] not in ('', None):
                    rooms = rooms + " E"
                if test[9] not in ('', None):
                    rooms = rooms + " W"
                if test2 != None:
                    if test2[1] not in ('', None):
                        rooms = rooms + " U"
                    if test2[2] not in ('', None):
                        rooms = rooms + " D"
            self.sendLine("%s" % rooms)
            self.displayPlayers()
            self.displayItems()
            self.displayMobs()
        except:
            self.sendLine("Display room didn't work...'")
            self.room = self.lastroom

    def LocationPrint(self):
        if self.adminmode == True:
            self.sendLine("Region   : %s" % self.regionname)
            self.sendLine("Room     : %s" % self.room)
            self.sendLine("Position : (%s, %s, %s)" % (self.xcoord, self.ycoord, self.zcoord))
        else:
            self.sendLine("Region   : %s" % self.regionname)
            self.sendLine("Position : (%s, %s, %s)" % (self.xcoord, self.ycoord, self.zcoord))

#COMMANDS
    def handle_CLEARSCREEN(self):
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")
        self.sendLine("")

    def handle_CPASS(self, password):
        p = str(password)
        n = self.name
#        x = (n, p)
#        try:
#            c.execute('''INSERT INTO NamePass VALUES (?,?)''', x)
#        except:
        print "Account Creation has failed!"

    def handle_EQUIP(self):
        self.sendLine("================================")
        self.sendLine("Weapons")
        self.sendLine("================================")
        self.sendLine("Mainhand   : %s" % (self.mainhand))
        self.sendLine("  Stats : %s - %s" % (self.mainhandvalmin, self.mainhandvalmax))
        self.sendLine("Offhand    : %s" % (self.offhand))
        if self.offhandtype == 'Weapon':
            self.sendLine("  Stats : %s - %s" % (self.offhandvalmin, self.offhandvalmax))
        else:
            self.sendLine("  Stats : %s" % (self.offhandvalmin))
        self.sendLine("================================")
        self.sendLine("Armor")
        self.sendLine("================================")
        self.sendLine("Helmet     : %s" % (self.helmet))
        self.sendLine("  Armor : %s" % (self.helmetvalue))
        self.sendLine("Chestpiece : %s" % (self.body))
        self.sendLine("  Armor : %s" % (self.bodyvalue))
        self.sendLine("Legpiece   : %s" % (self.lowerbody))
        self.sendLine("  Armor : %s" % (self.lowerbodyvalue))
        self.sendLine("Boots      : %s" % (self.boots))
        self.sendLine("  Armor : %s" % (self.bootsvalue))

    def EQUIPSTART(self):
        try:
            t = self.mainhandid
            t = (t,)
            c.execute('SELECT * FROM Gear WHERE ID=?', t)
            test = c.fetchone()
            if test == None:
                pass
            else:
                self.mainhand = str(test[1])
                self.mainhandvalmin = test[3]
                self.mainhandvalmax = test[4]
                self.mainhandspeed = test[5]
                self.attackspeed = self.mainhandspeed * self.speedmod
            t = self.offhandid
            t = (t,)
            c.execute('SELECT * FROM Gear WHERE ID=?', t)
            test = c.fetchone()
            if test in(None, '', 'None'):
                self.attackspeed = self.mainhandspeed * self.speedmod
            else:
                self.offhand = str(test[1])
                self.offhandtype = str(test[2])
                self.offhandvalmin = test[3]
                self.offhandvalmax = test[4]
                self.offhandspeed = test[5]
                if self.offhandtype == 'Weapon':
                    att = self.mainhandspeed
                    att2 = self.offhandspeed / 2.00
                    attackspeed = att + att2
                    self.attackspeed = attackspeed
                else:
                    self.attackspeed = self.mainhandspeed * self.speedmod
                if self.offhandtype == 'Shield':
                    defence = self.offhandvalmin
                    self.defence = defence + self.defence
                else:
                    pass
            t = self.helmet
            t = (t,)
            c.execute('SELECT * FROM Gear WHERE ID=?', t)
            test = c.fetchone()
            if test == None:
                pass
            else:
                self.helmet = str(test[1])
                self.helmetvalue = test[3]
                defence = self.defence + self.helmetvalue
                self.defence = defence
            t = self.bodyid
            t = (t,)
            c.execute('SELECT * FROM Gear WHERE ID=?', t)
            test = c.fetchone()
            if test == None:
                pass
            else:
                self.body = str(test[1])
                self.bodyvalue = test[3]
                defence = self.defence + self.bodyvalue
                self.defence = defence
            t = self.lowerbodyid
            t = (t,)
            c.execute('SELECT * FROM Gear WHERE ID=?', t)
            test = c.fetchone()
            if test == None:
                pass
            else:
                self.lowerbody = str(test[1])
                self.lowerbodyvalue = test[3]
                defence = self.defence + self.lowerbodyvalue
                self.defence = defence
            t = self.bootsid
            t = (t,)
            c.execute('SELECT * FROM Gear WHERE ID=?', t)
            test = c.fetchone()
            if test == None:
                pass
            else:
                self.boots = str(test[1])
                self.bootsvalue = test[3]
                defence = self.defence + self.bootsvalue
                self.defence = defence
            #self.sendLine("Gear Equipped! Check it with /equipped")
        except:
            print "EQUIPSTART() Failed"

    def STATS(self):
        self.sendLine("======================================================")
        self.sendLine("Name :   %s" % (self.name))
        self.sendLine("======================================================")
        self.sendLine("Class :   %s %s %s" % (self.gender, self.race, self.classname))
        self.sendLine("Level :   %s" % (self.level))
        self.sendLine("Exp :     %-5s" % (self.exp))
        self.sendLine("ExpTNL :  %-5s" % (self.exptnl))
        self.sendLine("======================================================")
        self.VitalBarDisplay('health', self.health, self.maxhealth)
        self.sendLine("      %3s / %3s    HPRegen : %2s" % (self.health, self.maxhealth, self.healthregen))
        self.VitalBarDisplay('mana', self.mana, self.maxmana)
        self.sendLine("      %3s / %3s    MPRegen : %2s" % (self.mana, self.maxmana, self.manaregen))
        self.sendLine("======================================================")
        self.sendLine("Str : %2s   Attack:   %3s   Physical Bonus :   %2s" % (self.strength, self.attack, self.strengthdamage))     # ++health   ++physical attack  +health regen
        self.sendLine("Con : %2s   Defence:  %3s   Damage Reduction:  %2s" % (self.constitution, self.defence, self.damageresist)) # ++health   ++health regen     +physical defence
        self.sendLine("Dex : %2s   Accuracy: %3s   Critical Chance :  %2s" % (self.dexterity, self.accuracy, self.critical))    # ++accuracy                    +critical chance
        self.sendLine("Agl : %2s   Dodge:    %3s   Attack Speed :   %.2f" % (self.agility, self.dodge, self.attackspeed))      # ++dodge                       +critical chance
        self.sendLine("Wis : %2s   Mag Def:  %3s   Magic Resist :     %2s" % (self.wisdom, self.mdefence, self.magicdodge))       # ++mana     ++mana regen       +magic defence
        self.sendLine("Int : %2s   Mag Atk:  %3s   Magic Bonus :      %2s" % (self.intellegence, self.mattack, self.magicdamage)) # ++mana     ++magic attack     +mana regen
# Party Commands!
    def PartyDisplayStats(self):
        try:
            if self.partybool is False:
                self.sendLine('No party to display')
            else:
                party = self.party
                try:
                    party[0]
                    countmax = 0
                except:
                    pass
                try:
                    party[1]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[2]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[3]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[4]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[5]
                    countmax = countmax + 1
                except:
                    pass
                global userlist
                diction = userlist
                count = 0
                party = self.party
                while count <= countmax:
                    member = party[count]
                    person = str(member)
                    if person == self.name:
                        count = count + 1
                    else:
                        member = diction.get(person)
                        self.sendLine("")
                        self.sendLine("%s" % member.name)
                        self.VitalBarDisplay('health', member.health, member.maxhealth)
                        self.sendLine('%3s / %3s' % (member.health, member.maxhealth))
                        self.VitalBarDisplay('mana', member.mana, member.maxmana)
                        self.sendLine('%3s / %3s' % (member.mana, member.maxmana))
                        count = count + 1
        except:
            print "PartyDisplayStats() failed"

    def PartyChat(self, message):
        try:
            if self.partybool is False:
                self.sendLine('No party to display')
            else:
                party = self.party
                try:
                    party[0]
                    countmax = 0
                except:
                    pass
                try:
                    party[1]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[2]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[3]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[4]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[5]
                    countmax = countmax + 1
                except:
                    pass
                global userlist
                diction = userlist
                count = 0
                party = self.party
                while count <= countmax:
                    member = party[count]
                    person = str(member)
                    if person == self.name:
                        self.sendLine("(Party)%s :: %s" %(self.name, message))
                        count += 1
                    else:
                        member = diction.get(person)
                        member.sendLine("(Party)%s :: %s" %(self.name, message))
                        count = count + 1
        except:
            print "Party Chat failing"

    def PartyCount(self):
        party = self.party
        try:
            party[0]
            countmax = 0
        except:
            pass
        try:
            party[1]
            countmax = countmax + 1
        except:
            pass
        try:
            party[2]
            countmax = countmax + 1
        except:
            pass
        try:
            party[3]
            countmax = countmax + 1
        except:
            pass
        try:
            party[4]
            countmax = countmax + 1
        except:
            pass
        try:
            party[5]
            countmax = countmax + 1
        except:
            pass
        if countmax >= 2:
            pass
        else:
            self.partybool = False

    def PartyInvite(self, name):
        try:
            party = self.party
            if party == []:
                self.sendLine("Small party error... relog please")
            else:
                if party[0] == self.name:
                    global userlist
                    diction = userlist
                    user = diction.get(name)
                    if user in('', None):
                        self.sendLine("Invalid user")
                    else:
                        user.sendLine("%s has invited you to party..." % (self.name))
                        user.sendLine("Do you accept? (yes/no)")
                        user.state = "PartyResponse"
                        party.append(name)
                        user.party = party
                        self.sendLine("Invite Sent")
                else:
                    self.sendLine("You are not the party leader")
        except:
            print "PartyInvite() Failed"

    def PartyLeave(self, reason=''):
        try:
            if self.partybool is False:
                if reason == 'Disconnect':
                    pass
                else:
                    self.sendLine('No party to leave')
            else:
                party = self.party
                try:
                    party[0]
                    countmax = 0
                except:
                    pass
                try:
                    party[1]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[2]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[3]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[4]
                    countmax = countmax + 1
                except:
                    pass
                try:
                    party[5]
                    countmax = countmax + 1
                except:
                    pass
                global userlist
                diction = userlist
                count = 0
                if countmax == 0:
                    return
                while count <= countmax:
                    print "Stuck here"
                    member = party[count]
                    person = str(member)
                    if person == self.name:
                        count += 1
                    else:
                        member = diction.get(person)
                        member.sendLine("(Party)%s has left the party" %(self.name))
                        member.PartyCount()
                        count += 1
                member = party[0]
                person = str(member)
                member = diction.get(person)
                memberparty = member.party
                memberparty.remove(self.name)
                self.party = []
                party = self.party
                party.append(self.name)
                self.partybool = False
                self.sendLine("You have left the party")
        except:
            print "PartyLeave() failed for", self.name

    def PartyResponse(self, response):
        try:
            party = self.party
            global userlist
            diction = userlist
            if response in('n', 'no', 'No', 'N'):
                leader = party[0]
                leader = diction.get(leader)
                leader.sendLine("%s has declined the party invite" % (self.name))
                self.party = []
                party = self.party
                party.append(self.name)
                self.state = "CHAT"
            if response in('yes', 'y', 'Yes', 'Y'):
                self.partybool = True
                self.state = "CHAT"
                self.sendLine("You have joined the party")
                leader = party[0]
                leader = diction.get(leader)
                leader.partybool = True
                leader.sendLine("%s has joined the party" % (self.name))
        except:
            print "Something happened in Party Response"
            self.state = "CHAT"

    def VitalBarDisplay(self, vital, value, maxvalue):
        value = float(value)
        maxvalue = float(maxvalue)
        percent = value / maxvalue
        percent = percent * 100
        percent = int(percent)
        percent = str(percent)
        if percent in('100'):
            display = '||||||||||||||||||||'
        if percent in('95', '96', '97', '98', '99'):
            display = '|||||||||||||||||||-'
        if percent in('90', '91', '92', '93', '94'):
            display = '||||||||||||||||||--'
        if percent in('85', '86', '87', '88', '89'):
            display = '|||||||||||||||||---'
        if percent in('80', '81', '82', '83', '84'):
            display = '||||||||||||||||----'
        if percent in('75', '76', '77', '78', '79'):
            display = '|||||||||||||||-----'
        if percent in('70', '71', '72', '73', '74'):
            display = '||||||||||||||------'
        if percent in('65', '66', '67', '68', '69'):
            display = '|||||||||||||-------'
        if percent in('60', '61', '62', '63', '64'):
            display = '||||||||||||--------'
        if percent in('55', '56', '57', '58', '59'):
            display = '|||||||||||---------'
        if percent in('50', '51', '52', '53', '54'):
            display = '||||||||||----------'
        if percent in('45', '46', '47', '48', '49'):
            display = '|||||||||-----------'
        if percent in('40', '41', '42', '43', '44'):
            display = '||||||||------------'
        if percent in('35', '36', '37', '38', '39'):
            display = '|||||||-------------'
        if percent in('30', '31', '32', '33', '34'):
            display = '||||||--------------'
        if percent in('25', '26', '27', '28', '29'):
            display = '|||||---------------'
        if percent in('20', '21', '22', '23', '24'):
            display = '||||----------------'
        if percent in('15', '16', '17', '18', '19'):
            display = '|||-----------------'
        if percent in('10', '11', '12', '13', '14'):
            display = '||------------------'
        if percent in('5', '6', '7', '8', '9'):
            display = '|-------------------'
        if int(percent) <= 4:
            display = '--------------------'
        per = '%'
        if vital == 'health':
            self.sendLine('Health (%s)  %s%s' % (display, per, percent))
        if vital =='mana':
            self.sendLine('Mana   (%s)  %s%s' % (display, per, percent))

    def handle_CHARACTERLOOKUP(self, name):
        diction = self.users
        person = str(name)
        char = diction.get(person)
        if char != None:
            self.sendLine("================================")
            self.sendLine("Name  : %s" % (char.name))
            self.sendLine("Class : %s %s %s" % (char.gender, char.race, char.classname))
            self.sendLine("Level : %s" % (char.level))
            self.sendLine("Region: %s" % (char.regionname))
            self.sendLine("================================")
            self.sendLine("HP: %s / %s" % (char.health, char.maxhealth))
            self.sendLine("MP: %s / %s" % (char.mana, char.maxmana))
            self.sendLine("================================")
            self.sendLine("Str : %s" % (char.strength))
            self.sendLine("Con : %s" % (char.constitution))
            self.sendLine("Dex : %s" % (char.dexterity))
            self.sendLine("Agl : %s" % (char.agility))
            self.sendLine("Wis : %s" % (char.wisdom))
            self.sendLine("Int : %s" % (char.intellegence))
        else:
            self.sendLine("Error : Either player is not online, or does not exist")

    def handle_WELCOME(self):
        try:
            self.sendLine("Use /help for a reference")
            name = self.name
            self.users[name] = self
            for name, protocol in self.users.iteritems():
                if protocol != self:
                    message = "%s has joined" % (self.name,)
                    protocol.sendLine(message)
            self.state = "CHAT"
            self.displayExits()
            self.Regeneration()
        except:
            print "handle_Welcome() failed"

    def handle_DEATH(self, atk):
        try:
            atk.health = atk.maxhealth
            self.pkilled += 1
            atk.sendLine("%s has killed you..." % (self.name))
            atk.sendLine("You have been sent back to spawn...")
            atk.room = 1
            self.sendLine("You have killed %s! Your pk rating is now %s" % (atk.name, self.pk))
        except:
            print "handle_DEATH() failed"

    def handle_PASSWORD(self, password):
        if(password == self.password):
            self.handle_WELCOME()
        else:
            self.sendLine("Returning to login process")
            self.handle_CLEARSCREEN()
            self.sendLine("What's your name?'")
            self.state = "GETNAME"

    def INVENTORY(self):
        self.sendLine("================================")
        self.sendLine("Inventory")
        self.sendLine("================================")
        self.sendLine("Gold : %s" % self.gold)
        self.sendLine("1]  : %s" % self.slot1name)
        self.sendLine("2]  : %s" % self.slot2name)
        self.sendLine("3]  : %s" % self.slot3name)
        self.sendLine("4]  : %s" % self.slot4name)
        self.sendLine("5]  : %s" % self.slot5name)
        self.sendLine("6]  : %s" % self.slot6name)
        self.sendLine("7]  : %s" % self.slot7name)
        self.sendLine("8]  : %s" % self.slot8name)
        self.sendLine("9]  : %s" % self.slot9name)
        self.sendLine("10] : %s" % self.slot10name)
        self.sendLine("11] : %s" % self.slot11name)
        self.sendLine("12] : %s" % self.slot12name)
        self.sendLine("13] : %s" % self.slot13name)
        self.sendLine("14] : %s" % self.slot14name)
        self.sendLine("15] : %s" % self.slot15name)
        self.sendLine("16] : %s" % self.slot16name)
        self.sendLine("17] : %s" % self.slot17name)
        self.sendLine("18] : %s" % self.slot18name)
        self.sendLine("19] : %s" % self.slot19name)
        self.sendLine("20] : %s" % self.slot20name)

    def handle_GETNAME(self, name):
        if self.users.has_key(name):  # lint:ok
            self.sendLine("User is already logged in...")
            return
        else:
            self.name = name
            self.handle_WELCOME(name)
# Admin Commands
    def AdminChange(self, password):
        if password == 'Max':
            self.adminmode = True
            self.sendLine("Now in admin mode")
        else:
            self.sendLine("Incorrect password, or no password entered...")
# Create Room Sequence
    def CreateRoom(self):
        self.createroomid = ''
        self.createroomdescrip = ''
        self.createroomdescripN = ''
        self.createroomdescripE = ''
        self.createroomdescripS = ''
        self.createroomdescripW = ''
        self.createroomidN = ''
        self.createroomidNsql = ''
        self.createroomidE = ''
        self.createroomidEsql = ''
        self.createroomidS = ''
        self.createroomidSsql = ''
        self.createroomidW = ''
        self.createroomidWsql = ''
        self.createroomcoordx = ''
        self.createroomcoordy = ''
        self.createroomcoordz = ''
        self.sendLine("At any point you can type /back to fix a previous error. Or /exit to leave this sequence")
        self.sendLine("Enter Room ID")
        self.state = "RoomIDCreate1"

    def CreateRoom1(self, roomid):
        try:
            if roomid == '/back':
                self.state = "CHAT"
                self.sendLine("No error to return to, so exiting")
                return
            if roomid == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if roomid == '':
                self.sendLine("Invalid room entry")
                return
            global c
            self.createroomid = roomid
            createroomid = int(roomid)
            c.execute('SELECT * FROM RoomExits WHERE ID=?', (createroomid,))
            fetch = c.fetchone()
            if fetch == None:
                self.sendLine("Enter Room Description")
                self.state = "RoomIDCreate2"
            else:
                self.sendLine("Room Exists, pick a different ID")
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom2(self, description):
        try:
            if description == '/back':
                self.state = "RoomIDCreate1"
                self.sendLine("Enter Room ID")
                return
            if description == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if description == "":
                self.sendLine("Needs some sort of description")
                return
            self.createroomdescrip = description
            self.sendLine("Enter North Description (if none, then hit enter)")
            self.state = "RoomIDCreate3"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom3(self, description):
        try:
            if description == '/back':
                self.state = "RoomIDCreate2"
                self.sendLine("Enter Room Description")
                return
            if description == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if description == '':
                description = 'None'
            self.createroomdescripN = description
            self.sendLine("Enter East Description (if none, then hit enter)")
            self.state = "RoomIDCreate4"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom4(self, description):
        try:
            if description == '/back':
                self.state = "RoomIDCreate3"
                self.sendLine("Enter North Description (if none, then hit enter)")
                return
            if description == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if description == '':
                description = 'None'
            self.createroomdescripE = description
            self.sendLine("Enter South Description (if none, then hit enter)")
            self.state = "RoomIDCreate5"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom5(self, description):
        try:
            if description == '/back':
                self.state = "RoomIDCreate4"
                self.sendLine("Enter East Description (if none, then hit enter)")
                return
            if description == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if description == '':
                description = 'None'
            self.createroomdescripS = description
            self.sendLine("Enter West Description (if none, then hit enter)")
            self.state = "RoomIDCreate6"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom6(self, description):
        try:
            if description == '/back':
                self.state = "RoomIDCreate5"
                self.sendLine("Enter South Description (if none, then hit enter)")
                return
            if description == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if description == '':
                description = 'None'
            self.createroomdescripW = description
            self.sendLine("Enter Room ID to the North. If None, then leave blank")
            self.state = "RoomIDCreate7"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom7(self, room):
        try:
            if room == '/back':
                self.state = "RoomIDCreate6"
                self.sendLine("Enter West Description (if none, then hit enter)")
                return
            if room == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if room in('', 'None'):
                self.createroomidN = 'None'
                self.createroomidNsql = None
            else:
                self.createroomidN = room
                self.createroomidNsql = int(room)
            self.sendLine("Enter Room ID to the East. If None, then leave blank")
            self.state = "RoomIDCreate8"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom8(self, room):
        try:
            if room == '/back':
                self.state = "RoomIDCreate7"
                self.sendLine("Enter Room ID to the North. If None, then leave blank")
                return
            if room == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if room in('', 'None'):
                self.createroomidE = 'None'
                self.createroomidEsql = None
            else:
                self.createroomidE = room
                self.createroomidEsql = int(room)
            self.sendLine("Enter Room ID to the South. If None, then leave blank")
            self.state = "RoomIDCreate9"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom9(self, room):
        try:
            if room == '/back':
                self.state = "RoomIDCreate8"
                self.sendLine("Enter Room ID to the East. If None, then leave blank")
                return
            if room == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if room in('', 'None'):
                self.createroomidS = 'None'
                self.createroomidSsql = None
            else:
                self.createroomidS = room
                self.createroomidSsql = int(room)
            self.sendLine("Enter Room ID to the West. If None, then leave blank")
            self.state = "RoomIDCreate10"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom10(self, room):
        try:
            if room == '/back':
                self.state = "RoomIDCreate9"
                self.sendLine("Enter Room ID to the South. If None, then leave blank")
                return
            if room == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if room in('', 'None'):
                self.createroomidW = 'None'
                self.createroomidWsql = None
            else:
                self.createroomidW = room
                self.createroomidWsql = int(room)
            self.sendLine("Enter the X Coordinate")
            self.state = "RoomIDCreate11"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom11(self, coord):
        try:
            if coord == '/back':
                self.state = "RoomIDCreate10"
                self.sendLine("Enter Room ID to the West. If None, then leave blank")
                return
            if coord == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if coord in(''):
                self.sendLine("Invalid entry must have a coordinate")
            else:
                self.createroomcoordx = coord
            self.sendLine("Enter the Y Coordinate")
            self.state = "RoomIDCreate12"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom12(self, coord):
        try:
            if coord == '/back':
                self.state = "RoomIDCreate11"
                self.sendLine("Enter the X Coordinate")
                return
            if coord == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if coord in(''):
                self.sendLine("Invalid entry must have a coordinate")
            else:
                self.createroomcoordy = coord
            self.sendLine("Enter the Z Coordinate")
            self.state = "RoomIDCreate13"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoom13(self, coord):
        try:
            if coord == '/back':
                self.state = "RoomIDCreate12"
                self.sendLine("Enter the Y Coordinate")
                return
            if coord == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if coord in(''):
                self.sendLine("Invalid entry must have a coordinate")
            else:
                self.createroomcoordz = coord
            self.sendLine("Is the following information correct? (y/n)")
            if self.createroomdescripN == 'None':
                descripN = 'None'
            else:
                descripN = "'" + self.createroomdescripN + "'"
            if self.createroomdescripE == 'None':
                descripE = 'None'
            else:
                descripE = "'" + self.createroomdescripE + "'"
            if self.createroomdescripS == 'None':
                descripS = 'None'
            else:
                descripS = "'" + self.createroomdescripS + "'"
            if self.createroomdescripW == 'None':
                descripW = 'None'
            else:
                descripW = "'" + self.createroomdescripW + "'"
            line = '(' + self.createroomid + ', "' + self.createroomdescrip + '", ' + descripN + ', ' + descripE + ', ' + descripS + ', ' + descripW + ', '+ self.createroomidN + ', ' + self.createroomidE + ', ' + self.createroomidS + ', ' + self.createroomidW + ', ' + self.createroomcoordx + ', ' + self.createroomcoordy + ', ' + self.createroomcoordz + ')'
            self.sendLine(line)
            self.state = "RoomIDCreateConfirm"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoomConfirm(self, answer):
        try:
            if answer == '/back':
                self.state = "RoomIDCreate13"
                self.sendLine("Enter the Z Coordinate")
                return
            if answer == '/exit':
                self.state = "CHAT"
                self.sendLine("Left room creation sequence")
                return
            if answer in('y', 'yes', 'Yes', 'Y'):
                with open("roomentry.txt", "a") as myfile:
                    if self.createroomdescripN == 'None':
                        descripN = 'None'
                    else:
                        descripN = '"' + self.createroomdescripN + '"'
                    if self.createroomdescripE == 'None':
                        descripE = 'None'
                    else:
                        descripE = '"' + self.createroomdescripE + '"'
                    if self.createroomdescripS == 'None':
                        descripS = 'None'
                    else:
                        descripS = '"' + self.createroomdescripS + '"'
                    if self.createroomdescripW == 'None':
                        descripW = 'None'
                    else:
                        descripW = '"' + self.createroomdescripW + '"'
                    saveline = '(' + self.createroomid + ', "' + self.createroomdescrip + '", ' + descripN + ', ' + descripE + ', ' + descripS + ', ' + descripW + ', '+ self.createroomidN + ', ' + self.createroomidE + ', ' + self.createroomidS + ', ' + self.createroomidW + ', ' + self.createroomcoordx + ', ' + self.createroomcoordy + ', ' + self.createroomcoordz + '),' + '\n'
                    myfile.write(saveline)
                if self.createroomdescripN == 'None':
                    self.createroomdescripN = None
                if self.createroomdescripE == 'None':
                    self.createroomdescripE = None
                if self.createroomdescripS == 'None':
                    self.createroomdescripS = None
                if self.createroomdescripW == 'None':
                    self.createroomdescripW = None
                room = (int(self.createroomid), self.createroomdescrip, self.createroomdescripN, self.createroomdescripE, self.createroomdescripS, self.createroomdescripW, self.createroomidNsql, self.createroomidEsql, self.createroomidSsql, self.createroomidWsql, int(self.createroomcoordx), int(self.createroomcoordy), int(self.createroomcoordz))
                LocalTime()
                global localtime
                print localtime, self.name, "created room", self.createroomid
                c.execute('''INSERT INTO RoomExits VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', room)
                conn.commit()
                self.sendLine("Entry saved and room commited!")
                self.state = "CHAT"
            if answer in('n', 'No', 'no', 'N'):
                self.sendLine("Left creation, back in normal sequence")
                self.state = "CHAT"
        except:
            self.sendLine("Error occured try again or relog")

    def CreateRoomUpDown(self):
        self.createroomid = ''
        self.createroomup = ''
        self.createroomdown = ''
        self.sendLine("Enter Room ID")
        self.state = "RoomIDCreateUpDown1"

    def CreateRoomUpDown1(self, roomid):
        if roomid == '/exit':
            self.state = 'CHAT'
            self.sendLine("Back in CHAT")
        if roomid == '':
            self.sendLine("Invalid room entry")
            return
        global c
        self.createroomid = roomid
        createroomid = int(roomid)
        c.execute('SELECT * FROM RoomExits WHERE ID=?', (createroomid,))
        fetch = c.fetchone()
        if fetch == None:
            self.sendLine("Enter room that is up (If none leave blank)")
            self.state = "RoomIDCreateUpDown2"
        else:
            self.sendLine("Room Exists, pick a different ID")

    def CreateRoomUpDown2(self, room):
        if room == '/exit':
            self.state = "CHAT"
            self.sendLine("Back in CHAT")
        if room == "":
            self.createroomup = None
        else:
            self.createroomup = room
        self.sendLine("Enter room that is down (If none leave blank)")
        self.state = "RoomIDCreateUpDown3"

    def CreateRoomUpDown2(self, room):
        if room == "/exit":
            self.state = 'CHAT'
            self.sendLine("Back in CHAT")
        if room == "":
            self.createroomdown = None
        else:
            self.createroomdown = room
        self.sendLine("Is this correct?")
        line = '(' + self.createroomid + ', ' + self.createroomup + ', ' + self.createroomdown + ')'
        self.state = "RoomIDCreateUpDownConfirm"

    def CreateRoomUpDownConfirm(self, answer):
        if answer in('y', 'yes', 'Yes', 'Y'):
            with open("roomupdownentry.txt", "a") as myfile:
                line = '(' + self.createroomid + ', ' + self.createroomup + ', ' + self.createroomdown + ')'
                myfile.write(saveline)
            room = (int(self.createroomid), int(self.createroomup), int(self.createroomdown))
            c.execute('''INSERT INTO RoomUpDown VALUES (?,?,?)''', room)
            conn.commit()
            self.sendLine("Entry saved and room commited!")
            self.state = "CHAT"
        if answer in('n', 'No', 'no', 'N'):
            self.sendLine("Left creation, back in CHAT")
            self.state = "CHAT"

    def UpdateRoomchoice(self, room):
        if room == '/exit':
            self.state = 'CHAT'
            self.sendLine("Left Update Room Sequence")
            return
        global c
        roomchoice = int(room)
        roomchoice = (roomchoice,)
        c.execute('SELECT * FROM RoomExits WHERE ID=?', roomchoice)
        fetch = c.fetchone()
        if fetch == None:
            self.sendLine("Room details don't exist, create it first'")
        else:
            line = "Room choice was " + str(room)
            self.sendLine(line)
            self.createroomid = room
            self.state = 'UpdateRoom2'
            self.sendLine("Update options... (Case Sensitive)")
            self.sendLine("ID, Description, NorthDescription, EastDescription, SouthDescription, WestDescription")
            self.sendLine("North, East, South, West, CoordX, CoordY, CoordZ")

    def UpdateRoom(self, choice):
        if choice == '/exit':
            self.state = 'CHAT'
            self.sendLine("Back in CHAT")
            return
        if choice in('ID', 'Description', 'NorthDecription', 'EastDescription', 'SouthDescription', 'WestDescription', 'North', 'East', 'South', 'West', 'CoordX', 'CoordY', 'CoordZ'):
            line = 'What do you want to set ' + choice + ' to?'
            self.sendLine(line)
            self.state = 'UpdateRoom3'
            self.updateroom = choice
        else:
            self.sendLine("Update options...")
            self.sendLine("ID, Description, NorthDescription, EastDescription, SouthDescription, WestDescription")
            self.sendLine("North, East, South, West, CoordX, CoordY, CoordZ")
            self.sendLine("")
            self.sendLine("Select /exit to leave this sequence")

    def UpdateRoom1(self, line):
        if line == '/exit':
            self.state = "CHAT"
            self.sendLine("Back in CHAT")
            return
        entry = 'Is, ' + line + ', correct?'
        self.sendLine("C)onfirm, or R)estart")
        self.sendLine(entry)
        self.updateroominfo = line
        self.state = 'UpdateRoomConfirm'

    def UpdateRoom2(self, confirm):
        if confirm == '/exit':
            self.state = "CHAT"
            self.sendLine("Back in CHAT")
            return
        if confirm in('Confirm', 'c', 'C', 'confirm', 'con'):
            room = self.createroomid
            column = self.updateroom
            info = self.updateroominfo
            roominfo = (info, room)
            c.execute('UPDATE RoomExits SET ' + column + '=? WHERE ID=?', roominfo)
            conn.commit()
            self.state = 'CHAT'
            line = 'Updated room, ' + str(room) + 'in column, ' + column + ' with entry, ' + info
            self.sendLine(line)
        if confirm in('Restart', 'res', 'Res', 'r', 'R', 'restart'):
            self.sendLine("What room would you like to update?")
            self.state = 'UpdateRoom1'

    def Teleport(self, room):
        try:
            val = int(room)
            self.handle_CLEARSCREEN()
            self.sendLine("You have teleported to room %s" % val)
            LocalTime()
            global localtime
            print localtime, self.name, "teleported to room", room
            self.room = int(room)
            self.updateRoom('Teleport', 'Teleport')
            self.displayExits()
        except ValueError:
            player = str(room)
            self.handle_CLEARSCREEN()
            global userlist
            diction = userlist
            playerid = userlist.get(player)
            if playerid in(None, ''):
                self.sendLine("Invalid target")
            else:
                self.sendLine("You have teleported to player %s" % player)
                self.room = playerid.room
                self.updateRoom('Teleport', 'Teleport')
                self.displayExits()

    def List(self):
        try:
            global userlist
            diction = userlist
            for key, value in diction.iteritems():
                player = diction.get(key)
                name = player.name
                level = player.level
                classname = player.classname
                regionname = player.regionname
                self.sendLine("%s, Level %s, %s   [%s]" % (name, level, classname, regionname))
        except:
            print "List() failed"

    def Stop(self, reason):
        try:
            global userlist
            diction = userlist
            line = "###SERVER### : Server is being stopped in 30 seconds for : " + reason
            for key, value in diction.iteritems():
                player = diction.get(key)
                player.sendLine(line)
                player.sendLine("Please get somewhere safe...")
            LocalTime()
            global localtime
            print localtime, "[#STOP#] called by...", self.name
            reactor.callLater(3.0, self.StopAll)
        except:
            print "Stop() Didn't work'"

    def LevelSet(self, name, level):
        global userlist
        diction = userlist
        player = diction.get(name)
        if player in(None, ''):
            self.sendLine('Invalid entry')
        else:
            player.level = level
            player.sendLine(str("You have been set to level %s by admin %s" % (level, self.name)))

    def ExpSet(self, name, exp):
        global userlist
        diction = userlist
        player = diction.get(name)
        if player in(None, ''):
            self.sendLine('Invalid entry')
        else:
            player.exptnl = exp
            player.sendLine(str("Your exptnl has been set to %s by admin %s" % (exp, self.name)))

    def StopAll(self):
        try:
            global userlist
            diction = userlist
            for key, value in diction.iteritems():
                player = diction.get(key)
                player.EXIT()
            reactor.callLater(3.0, StopAll)
        except:
            print "Something in StopAll went wrong..."

##########################
##                      ##
##     BEGIN SKILLS     ##
##                      ##
##########################
# targets a single mob for skill attacks
    def TargetMob(self, target):
        global c
        slot = target
        slot = int(slot)
        room = (self.room,)
        c.execute('SELECT * FROM RoomMobs WHERE ID=?', room)
        test= c.fetchone()
        mob = test[slot]
        if mob in('', None):
            return
        mobs = (mob,)
        c.execute('SELECT * FROM ActiveMonster WHERE RandomID=?', mobs)
        test = c.fetchone()
        self.target = test
        # RandomID, MobID, Level, Name, Health, MaxHealth, Mana, MaxMana, Attack, Defence, Speed, Critical, Accuracy, 13Dodge, Mattack, Mdefence

#/skill skillid target
#/skill 1 1

# used only for attacking mobs with skills, doesn't effect normal attack
    def SkillAttackMob(self, damage, skillname):
        global c
        target = self.target
        name = target[3]
        mob = target[0]
        mobhp = target[4]
        mobhp = mobhp - damage
        c.execute('UPDATE ActiveMonster SET Health=? WHERE RandomID=?', (mobhp, mob))
        if(mobhp <= 0): # Mob health < 0 Check
            self.handle_TellRoom(str("%s has slain the %s with %s" % (self.name, name, skillname)))
            self.sendLine(str("You have slain the %s with %s for %s damage" % (name, skillname, damage)))
            self.handle_MOBDEATH(target[0], target[2], self.targetslot)
        else:
            self.sendLine(str("You used %s on the %s for %s damage!" % (skillname, name, damage)))
            self.handle_TellRoom(str("%s used %s on %s for %s damage" % (self.name, skillname, name, damage)))
        conn.commit()

    def MobActiveTest(self, dmg=1):
        target = self.target
        mob = target[0]
        self.threatCalculator(dmg, mob)
        fightbool = str(target[17])
        if fightbool == 'False':
            c.execute('''UPDATE ActiveMonster SET AttackBool='True' WHERE RandomID=?''', (mob,))
            conn.commit()
            reactor.callLater(3.0, MobFight, mob)

###########
# Warrior #
###########
############### WARRIOR ####################
    def HeavyHit(self, target): #level 1, 10MP
        self.targetslot = target
        if self.skill1 is False:
            self.sendLine("Heavy Hit not ready")
            return
        if self.mana < 10:
            self.sendLine("Not enough mana for Heavy Hit")
            return
        self.TargetMob(target)
        try:
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.skill1 = False
        self.mana = self.mana - 10
        hitmax = 100 + int(target[13])
        hit = random.randint(1, hitmax)
        attackmin = self.mainhandvalmin
        attackmax = self.mainhandvalmax
        if(self.offhandtype == 'Weapon'):
            offhandmin = self.offhandvalmin * 0.75
            offhandmin = int(offhandmin)
            offhandmax = self.offhandvalmax * 0.75
            offhandmax = int(offhandmax)
            attackmin = attackmin + offhandmin
            attackmax = attackmax + offhandmax
        attack = random.randint(attackmin, attackmax) + self.strengthdamage
        if(hit <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            damage = attackmod * attack
            HeavyHitDamage = random.randint((self.strengthdamage / 4), (self.strengthdamage / 2))
            damage += HeavyHitDamage
            self.SkillAttackMob(int(damage), 'Heavy Hit')
            self.MobActiveTest(int(damage))
        else:
            self.sendLine(str("You missed the %s with %s" % (target[3], 'Heavy Hit')))
            self.handle_TellRoom(str("%s missed the %s with %s" % (self.name, target[3], 'Heavy Hit')))
            self.MobActiveTest()
        reactor.callLater(20.0, self.SkillCooldown, 1, 'Heavy Hit')


    def taunt(self, target): #level 5,/ 4MP
        if self.skill3 is False:
            self.sendLine("Taunt not ready")
            return
        if self.mana < 4:
            self.sendLine("Not enough mana for Taunt")
            return
        self.TargetMob(target)
        try:
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.mana = self.mana - 4
        self.skill3 = False
        self.MobActiveTest(50)
        self.sendLine(str("You taunted %s" % target[3]))
        reactor.callLater(12.0, self.SkillCooldown, 3, 'Taunt')

    def doubleHit(self, target): #level 4, 8 MP
        self.targetslot = target
        if self.skill2 is False:
            self.sendLine("Double Hit not ready")
            return
        if self.mana < 8:
            self.mana = self.mana - 8
            return
        try:
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.TargetMob(target)
        target = self.target
        hitmax = 100 + int(target[13])
        hit = random.randint(1, hitmax)
        attackmin = self.mainhandvalmin
        attackmax = self.mainhandvalmax

        if(self.offhandtype == 'Weapon'):
            offhandmin = self.offhandvalmin * 0.75
            offhandmin = int(offhandmin)
            offhandmax = self.offhandvalmax * 0.75
            offhandmax = int(offhandmax)
            attackmin = attackmin + offhandmin
            attackmax = attackmax + offhandmax
        attack = random.randint(attackmin, attackmax) + self.strengthdamage
        attack2 = random.randint(attackmin, attackmax) + self.strengthdamage
        attack = int(attack * 0.8)
        attack2 = int(attack2 * 0.8)

        if(hit <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            damage1 = attackmod * attack
            damage2 = attackmod * attack2
            self.SkillAttackMob(damage1, 'Double Hit')
            self.SkillAttackMob(damage2, 'Double Hit')
            totaldamage = damage1 + damage2
            self.MobActiveTest(totaldamage)

        else:
            self.sendLine("You missed the %s with %s" % (target[3], 'Double Hit'))
            self.handle_TellRoom("%s missed the %s with %s" % (self.name, target[3], 'Double Hit'))
            self.MobActiveTest()

        reactor.callLater(12, self.SkillCooldown(2), 'Double Hit')

    def warriorBonusI(self): #level 2
        self.strength += 1
        self.constitution += 1
        self.sendLine("Gained Warrior Bonus I (+1 Strength, +1 Constitution)")

    def warriorStance(self, toggle): #level 7, toggle
        if toggle in('Offensive', 'offense', 'off', 'offensive', 'o'):
            self.attack = int(self.normalattack * 1.25)
            self.defence = int(self.normaldefence * 0.75)
            self.sendLine("You are now in offensive stance")
            self.EQUIPSTART()
            return
        if toggle in('normal', 'norm', 'n', 'Normal'):
            self.attack = self.normalattack
            self.defence = self.normaldefence
            self.sendLine("You are now in normal stance")
            self.EQUIPSTART()
            return
        if toggle in('defensive', 'defence', 'd', 'def', 'defense'):
            self.attack = int(self.normalattack * 0.75)
            self.defence = int(self.normaldefence * 1.25)
            self.sendLine("You are now in defensive stance")
            self.EQUIPSTART()
            return
        else:
            self.sendLine("Invalid Stance Type, available are, offensive, defensive, normal")

#########
# Rogue #
#########


############### ROGUE ####################
    def doubleStrike(self, target): #level 1, 8MP
        self.targetslot = target
        if self.skill1 is False:
            self.sendLine("Double Strike not ready")
            return
        if self.mana < 8:
            self.sendLine("Not enough mana for Double Strike")
            return
        self.TargetMob(target)
        try:
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.mana = self.mana - 8
        self.skill1 = False
        target = self.target
        hitmax = 100 + int(target[13])
        hit = random.randint(1, hitmax)
        hit2 = random.randint(1, hitmax)
        attackmin = self.mainhandvalmin
        attackmax = self.mainhandvalmax

        if(self.offhandtype == 'Weapon'):
            offhandmin = self.offhandvalmin * 0.75
            offhandmin = int(offhandmin)
            offhandmax = self.offhandvalmax * 0.75
            offhandmax = int(offhandmax)
            attackmin = attackmin + offhandmin
            attackmax = attackmax + offhandmax
        attack = random.randint(attackmin, attackmax) + self.strengthdamage
        attack2 = random.randint(attackmin, attackmax) + self.strengthdamage

        damage1 = 0
        damage2 = 0

        if(hit <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            damage1 = attackmod * attack
            damage1 = int(damage1)
            self.SkillAttackMob(damage1, 'Double Strike')
        else:
            self.sendLine(str("You missed the %s with %s" % (target[3], 'Double Strike')))
            self.handle_TellRoom(str("%s missed the %s with %s" % (self.name, target[3], 'Double Strike')))

        if(hit2 <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            damage2 = attackmod * attack2
            damage2 = int(damage2)
            self.SkillAttackMob(damage2, 'Double Strike')
        else:
            self.sendLine(str("You missed the %s with %s" % (target[3], 'Double Strike')))
            self.handle_TellRoom(str("%s missed the %s with %s" % (self.name, target[3], 'Double Strike')))

        totdam = damage1 + damage2
        self.MobActiveTest(totdam)
        reactor.callLater(16, self.SkillCooldown, 1, 'Double Strike')

    def criticalPassive(self): #level 2, passive
        global c
        global conn
        self.critical = self.critical + 5
        c.execute('SELECT * FROM PlayerBonusStats')
        fetch = c.fetchone()
        critical = fetch[5]
        print critical
        critical = critical + 5
        self.criticalbonus = critical
        print critical
        add = (critical, self.name)
        c.execute('UPDATE PlayerBonusStats SET Critical=? WHERE Name=?', add)
        conn.commit()
        self.sendLine("Gained Rogue Critical Bonus (+5% chance to crit)")

    def rogueBonusI(self): #level 3
        self.strength += 1
        self.dexterity += 1
        self.sendLine("Gained Rogue Bonus I (+1 Strength, +1 Dexterity)")

    def dirtySleep(self, value, target):
        c.execute("""UPDATE ActiveMonster SET Accuracy=? WHERE RandomID=?""", (value, target))
        conn.commit()

    def dirtyStrike(self, target): #level 5, 12 MP
        self.targetslot = target
        if self.skill2 is False:
            self.sendLine("Double Strike not ready")
            return
        if self.mana < 12:
            self.sendLine("Not enough mana for Double Strike")
            return
        self.TargetMob(target)
        try:
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.mana = self.mana - 12
        self.skill2 = False
        target = self.target
        hitmax = 100 + int(target[13])
        hit = random.randint(1, hitmax)
        attackmin = self.mainhandvalmin
        attackmax = self.mainhandvalmax

        if(self.offhandtype == 'Weapon'):
            offhandmin = self.offhandvalmin * 0.75
            offhandmin = int(offhandmin)
            offhandmax = self.offhandvalmax * 0.75
            offhandmax = int(offhandmax)
            attackmin = attackmin + offhandmin
            attackmax = attackmax + offhandmax
        attack = random.randint(attackmin, attackmax) + self.strengthdamage
        attack2 = random.randint(attackmin, attackmax) + self.strengthdamage

        if(hit <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            damage1 = attackmod * attack
            damage1 = int(damage1)
            self.SkillAttackMob(damage1, 'Dirty Strike')
            self.MobActiveTest(damage1)
            mobaccuracy = target[12]
            name = str(target[0])
            halved = mobaccuracy
            halved = halved * 0.5
            c.execute("""UPDATE ActiveMonster SET Accuracy=? WHERE RandomID=?""", (halved, name))
            conn.commit()
            reactor.callLater(3.5, self.dirtySleep, mobaccuracy, name)

        else:
            self.sendLine(str("You missed the %s with %s" % (target[3], 'Dirty Strike')))
            self.handle_TellRoom(str("%s missed the %s with %s" % (self.name, target[3], 'Dirty Strike')))
            self.MobActiveTest()
        reactor.callLater(16.0, self.SkillCooldown, 2, 'Dirty Strike')

    def SkillCooldown(self, skill, name):
        line = name + " has been refreshed"
        self.sendLine(line)
        if skill == 1:
            self.skill1 = True
        if skill == 2:
            self.skill2 = True
        if skill == 3:
            self.skill3 = True
        if skill == 4:
            self.skill4 = True
        if skill == 5:
            self.skill5 = True

    def tripleStrike(self, target): #level 7, 16 MP
        self.targetslot = target
        if self.skill3 is False:
            self.sendLine("Triple Strike not ready")
            return
        if self.mana < 16:
            self.sendLine("Not enough mana for Triple Strike")
            return
        self.TargetMob(target)
        try:
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.skill3 = False
        self.mana = self.mana - 16
        damage1 = 0
        damage2 = 0
        damage3 = 0
        target = self.target
        hitmax = 100 + int(target[13])
        hit = random.randint(1, hitmax)
        hit2 = random.randint(1, hitmax)
        hit3 = random.randint(1, hitmax)
        attackmin = self.mainhandvalmin
        attackmax = self.mainhandvalmax

        if(self.offhandtype == 'Weapon'):
            offhandmin = self.offhandvalmin * 0.75
            offhandmin = int(offhandmin)
            offhandmax = self.offhandvalmax * 0.75
            offhandmax = int(offhandmax)
            attackmin = self.mainhandvalmin + offhandmin
            attackmax = self.mainhandvalmax + offhandmax
        attack = random.randint(attackmin, attackmax) + self.strengthdamage
        attack2 = random.randint(attackmin, attackmax) + self.strengthdamage
        attack3 = random.randint(attackmin, attackmax) + self.strengthdamage

        if(hit <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            if attack < 0.5:
                attack = 0.5
            damage1 = int(attackmod * attack)
            self.SkillAttackMob(damage1, 'Triple Strike')
            self.MobActiveTest(totdam)

        if(hit2 <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            if attack < 0.5:
                attack = 0.5
            damage2 = int(attackmod * attack2)
            self.SkillAttackMob(damage2, 'Triple Strike')
            self.SkillAttackMob(damage3, 'Triple Strike')

        if(hit3 <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            if attack < 0.5:
                attack = 0.5
            damage3 = int(attackmod * attack3)
            self.SkillAttackMob(damage3, 'Triple Strike')

        else:
            self.sendLine(str("You missed the %s with %s" % (target[3], 'Triple Strike')))
            self.handle_TellRoom(str("%s missed the %s with %s" % (self.name, target[3], 'Triple Strike')))
            self.MobActiveTest()
        totdam = damage1 + damage2 + damage3
        self.MobActiveTest(totdam)
        reactor.callLater(32, self.SkillCooldown, 3, 'Triple Strike')


##########
# Priest #
##########
############### PRIEST ####################
    def lightSleep(self):
        try:
            global c
            target = self.target
            name = str(target[0])
            c.execute("""UPDATE ActiveMonster SET Stun=? WHERE RandomID=?""", ('False', name))
            self.sendLine(str("Stun wore off of %s" % name))
            conn.commit()
        except:
            pass

    def lightBash(self, target): #level 1, 8MP
        self.targetslot = target
        if self.skill1 is False:
            self.sendLine("Light Bash not ready")
            return
        if self.mana < 8:
            self.sendLine("Not enough mana for Light Bash")
            return
        self.TargetMob(target)
        try:
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.mana = self.mana - 8
        self.skill1 = False
        target = self.target
        hitmax = 100 + int(target[13])
        hit = random.randint(1, hitmax)
        attackmin = self.mainhandvalmin
        attackmax = self.mainhandvalmax

        if(self.offhandtype == 'Weapon'):
            offhandmin = self.offhandvalmin * 0.75
            offhandmin = int(offhandmin)
            offhandmax = self.offhandvalmax * 0.75
            offhandmax = int(offhandmax)
            attackmin = attackmin + offhandmin
            attackmax = attackmax + offhandmax

        attack = random.randint(attackmin, attackmax) + self.magicdamage
        mob_magic_def = target[15]
        accuracy = self.accuracy
        magicaccuracy = self.magicaccuracy
        targetresist = int(target[15] * 1.5)
        magichitmax = 100 + int(targetresist)
        magichit = random.randint(1, magichitmax)

        if(hit <= accuracy):
            af = float(self.mattack)
            attackmod = af / int(target[15])
            attack = float(attack)
            if attack > 2.0:
                attack = 2.0
            damage = int(attack * (self.wisdom * 0.25))
            self.SkillAttackMob(damage, 'Light Bash')
            name = target[0]
            c.execute("""UPDATE ActiveMonster SET Stun=? WHERE RandomID=?""", ('True', name))
            conn.commit()
            reactor.callLater(5.0, self.lightSleep)
            self.MobActiveTest(damage)

        else:
            self.sendLine(str("%s resisted %s" % (target[3], 'Light Bash')))
            self.handle_TellRoom(str("%s resisted %s that was cast by %s" % (target[3], 'Light Bash', self.name)))
            self.MobActiveTest()
        reactor.callLater(16.0, self.SkillCooldown, 1, 'Light Bash')

    def priestBonus(self): #level 2
        self.constitution += 1
        self.wisdom += 1
        self.sendLine("Gained Priest Bonus I (+1 Constitution, +1 Wisdom)")

    def targetHeal(self, target): #level 3, 12MP
        if self.skill2 is False:
            self.sendLine('Heal is not ready yet')
            return
        if self.mana < 12:
            self.sendLine("Not enough mana for Heal")
            return
        diction = self.users
        target = str(target)
        if target in(None, ''):
            self.sendLine('Invalid target name')
            return
        atk = diction.get(target)
        if atk in('', None):
            self.sendLine("Target does not exist")
            return
        if atk.room != self.room:
            self.sendLine("Player is not in the same room as you")
        self.skill2 = False
        self.mana = self.mana - 12
        healamtmax = int((1.5*self.wisdom)+(0.5*self.intellegence))
        healamtmin = healamtmax / 2
        healamt = random.randint(healamtmin, healamtmax)
        atk.health += healamt
        if atk.health > atk.maxhealth:
            healchange = atk.health - atk.maxhealth
            atk.health = atk.maxhealth
            healamt = healamt - healchange
        if atk.name == self.name:
            self.sendLine(str("You have healed yourself for %s HP" % healamt))
        else:
            self.sendLine(str('You have healed %s for %sHP!' % (target, healamt)))
            atk.sendLine(str('You have been healed for %s by %s!' % (healamt, self.name)))
        reactor.callLater(4.0, self.SkillCooldown, 2, 'Heal')

    def lightStrike(self, target): #level 5, 16MP
        self.targetslot = target
        if self.skill3 is False:
            self.sendLine("Light Strike not ready")
            return
        if self.mana < 16:
            self.sendLine("Not enough mana for Light Strike")
            return
        self.mana = self.mana - 16
        self.skill3 = False
        self.TargetMob(target)
        target = self.target
        hitmax = 100 + int(target[13])
        hit = random.randint(1, hitmax)
        attackmin = self.mainhandvalmin
        attackmax = self.mainhandvalmax
        if(self.offhandtype == 'Weapon'):
            offhandmin = self.offhandvalmin * 0.75
            offhandmin = int(offhandmin)
            offhandmax = self.offhandvalmax * 0.75
            offhandmax = int(offhandmax)
            attackmin = attackmin + offhandmin
            attackmax = attackmax + offhandmax
        attack = random.randint(attackmin, attackmax)
        if(hit <= self.accuracy):
            af = float(self.attack)
            attackmod = af / int(target[9])
            attack = float(attack)
            if attack > 2.0:
                attack = 2
            damage = attackmod * attack
            LightStrikeDamagemin = self.wisdom / 5
            LightStrikeDamagemax = self.wisdom / 2
            damage = damage + random.randint(LightStrikeDamagemin, LightStrikeDamagemax) + self.magicdamage
            self.SkillAttackMob(int(damage), 'Light Strike')
            self.MobActiveTest(damage)
        else:
            self.sendLine(str("You missed the %s with %s" % (target[3], 'Light Strike')))
            self.handle_TellRoom(str("%s missed the %s with %s" % (self.name, target[3], 'Light Strike')))
            self.MobActiveTest()
        reactor.callLater(24.0, self.SkillCooldown, 3, 'Light Strike')

    def groupHeal(self): #level 7, 18MP
#        try:
        if self.mana < 18:
            self.sendLine("Not enough mana for Group Heal")
            return
        if self.skill4 == False:
            self.sendLine("Group Heal not refreshed yet")
            return
        if self.partybool is False:
            self.sendLine("Not in a party, so Group Heal didn't execute")
            return
        else:
            self.mana = self.mana - 18
            self.skill4 = False
            party = self.party
            try:
                party[0]
                countmax = 0
            except:
                pass
            try:
                party[1]
                countmax = countmax + 1
            except:
                pass
            try:
                party[2]
                countmax = countmax + 1
            except:
                pass
            try:
                party[3]
                countmax = countmax + 1
            except:
                pass
            try:
                party[4]
                countmax = countmax + 1
            except:
                pass
            try:
                party[5]
                countmax = countmax + 1
            except:
                pass
            global userlist
            diction = userlist
            count = 0
            party = self.party
            while count <= countmax:
                healmin = self.wisdom / 8
                healmax = self.wisdom / 4
                healamt = random.randint(healmin, healmax) + self.magicdamage
                person = party[count]
                atk = diction.get(person)
                atk.health += healamt
                if atk.health > atk.maxhealth:
                    healchange = atk.health - atk.maxhealth
                    atk.health = atk.maxhealth
                    healamt = healamt - healchange
                if atk.name == self.name:
                    self.sendLine(str("You have healed yourself for %s HP" % healamt))
                else:
                    self.sendLine(str('You have healed %s for %sHP!' % (atk.name, healamt)))
                    atk.sendLine(str('You have been healed for %s by %s!' % (healamt, self.name)))
                count = count + 1
            reactor.callLater(30.0, self.SkillCooldown, 4, 'Group Heal')
#        except:
#            print "Group Heal failed"

########
# Mage #
########
############### MAGICIAN ####################
    def fireball(self, target): #level 1, 8MP
        self.targetslot = target
        if self.skill1 is False:
            self.sendLine("Fireball not ready")
            return
        if self.mana < 8:
            self.sendLine("Not enough mana for Fireball")
            return
        self.TargetMob(target)
        try :
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.skill1 = False
        self.mana = self.mana - 8
        hitmax = 100 + int(target[13])
        attackmin = int(self.intellegence * 0.33)
        attackmax = int(self.intellegence * 0.66)
        attack = random.randint(attackmin, attackmax) + self.magicdamage
        mob_magic_def = int(target[15])
        mage_magic_atk = self.mattack
        magicmod = mage_magic_atk / mob_magic_def
        hitmax = 100 + int(0.75 * mob_magic_def)
        hit = random.randint(1, hitmax)
        if magicmod > 1.25:
            magicmod = 1.25
        attack = int(attack * magicmod)
        hitacc = self.accuracy
        if(hit <= self.magicaccuracy):
            damage = attack
            self.SkillAttackMob(damage, 'Fireball')
            self.MobActiveTest(damage)
        else:
            self.sendLine(str("%s resisted your spell, %s!" % (target[3], 'Fireball')))
            self.handle_TellRoom(str("%s resisted %s cast by %s" % (target[3], 'Fireball', self.name)))
            self.MobActiveTest()
        reactor.callLater(8.0, self.SkillCooldown, 1, 'Fireball')

    def mageBonusI(self): #level 2
        self.wisdom += 1
        self.intellegence += 1
        self.sendLine("Gained Magician Bonus I (+1 Wisdom, +1 Intellegence)")

    def manaRegen(self): #level 3
        self.manaregenbonus += 2
        self.manaregen += 2
        self.sendLine("Gained Mana Regen Bonus I (+2 mana regen)")

    def iceBolt(self, target): #level 5, 14 MP
        self.targetslot = target
        if self.skill2 is False:
            self.sendLine("Ice Bolt not ready")
            return
        if self.mana < 14:
            self.sendLine("Not enough mana for Ice Bolt")
            return
        self.TargetMob(target)
        try :
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.skill2 = False
        self.mana = self.mana - 14
        hitmax = 100 + int(target[13])
        attackmin = int(self.intellegence * 0.25)
        attackmax = int(self.intellegence * 0.5)
        attack = random.randint(attackmin, attackmax) + self.magicdamage
        mob_magic_def = int(target[15])
        mage_magic_atk = self.mattack
        magicmod = mage_magic_atk / mob_magic_def
        hitmax = 100 + int(0.75 * mob_magic_def)
        hit = random.randint(1, hitmax)
        if magicmod > 1.25:
            magicmod = 1.25
        attack = int(attack * magicmod)
        hitacc = self.accuracy
        if(hit <= self.magicaccuracy):
            damage = attack
            self.SkillAttackMob(damage, 'Ice Bolt')
            self.MobActiveTest(damage)
            if random.randint(1, 100) <= 60:
                name = target[0]
                c.execute("""UPDATE ActiveMonster SET Stun=? WHERE RandomID=?""", ('True', name))
                conn.commit()
                reactor.callLater(5.0, self.lightSleep)
                self.sendLine(str("Stunned the %s!" % target[3]))
        else:
            self.sendLine(str("%s resisted your spell, %s!" % (target[3], 'Ice Bolt')))
            self.handle_TellRoom(str("%s resisted %s cast by %s" % (target[3], 'Ice Bolt', self.name)))
            self.MobActiveTest()
        reactor.callLater(12.0, self.SkillCooldown, 2, 'Ice Bolt')

    def thunderBolt(self, target): #level 7, 20mp
        self.targetslot = target
        if self.skill3 is False:
            self.sendLine("Thunder Bolt not ready")
            return
        if self.mana < 20:
            self.sendLine("Not enough mana for Thunder Bolt")
            return
        self.TargetMob(target)
        try :
            target = self.target
        except:
            self.sendLine("Invalid Target")
            return
        self.skill1 = False
        self.mana = self.mana - 20
        attackmin = int(self.intellegence * 0.33)
        attackmax = int(self.intellegence * 0.66)
        attack = random.randint(attackmin, attackmax) + self.magicdamage
        mob_magic_def = int(target[15])
        mage_magic_atk = self.mattack
        magicmod = mage_magic_atk / mob_magic_def
        hitmax = 100 + int(0.75 * mob_magic_def)
        hit = random.randint(1, hitmax)
        if magicmod > 1.25:
            magicmod = 1.25
        attack = int(attack * magicmod)
        if(hit <= self.magicaccuracy):
            damage = attack
            critchance = random.randint(1, 100)
            if critchance <= 40:
                damage = damage * 2
                self.sendLine(str("Thunder Bolt pierced through %s's defence!" % target[3]))
            self.SkillAttackMob(damage, 'Thunder Bolt')
            self.MobActiveTest(damage)
        else:
            self.sendLine(str("%s resisted your spell, %s!" % (target[3], 'Thunder Bolt')))
            self.handle_TellRoom(str("%s resisted %s cast by %s" % (target[3], 'Thunder Bolt', self.name)))
            self.MobActiveTest()
        reactor.callLater(24.0, self.SkillCooldown, 3, 'Thunder Bolt')

################################
##                            ##
##         END SKILLS         ##
##                            ##
################################
    def handle_CHAT(self, message):
        if message in ('n', 'N', 'North', 'north'):
            message = str(message)
            self.handle_CLEARSCREEN()
            self.moveRooms(message)
            return
        if message in ('s', 'S', 'South', 'south'):
            message = str(message)
            self.handle_CLEARSCREEN()
            self.moveRooms(message)
            return
        if message in ('W', 'w', 'West', 'west'):
            message = str(message)
            self.handle_CLEARSCREEN()
            self.moveRooms(message)
            return
        if message in ('e', 'E', 'East', 'east'):
            message = str(message)
            self.handle_CLEARSCREEN()
            self.moveRooms(message)
            return
        if message in ('d', 'D', 'Down', 'down'):
            message = str(message)
            self.handle_CLEARSCREEN()
            self.moveRooms(message)
            return
        if message in ('u', 'U', 'Up', 'up'):
            message = str(message)
            self.handle_CLEARSCREEN()
            self.moveRooms(message)
            return
        if(message == '/help'):
            if self.adminmode == False:
                self.sendLine("The commands available to you are...")
                self.sendLine("/a <#>               *Attack the mob assigned to that slot")
                # self.sendLine("/c                   *Return back to command mode")
                self.sendLine("/changepass          *Changes your password")
                self.sendLine("/clear               *clears the screen of text")
                self.sendLine("/equipped            *Looks up personal gear equipped")
                self.sendLine("/exit                *exit cleanly and save properly")
                self.sendLine("/inv                 *Opens your inventory")
                self.sendLine("/look                *Looks around your area")
                self.sendLine("/lookup <user>       *Looks up a users stats")
                self.sendLine("/pa <user>           *Attack a player")
                self.sendLine('/party invite <user> *Invites user to your party')
                self.sendLine("/pk                  *Toggles Player fighting on/off (5min wait)")
                self.sendLine("/skills              *Shows your characters skill levels")
                self.sendLine("/spawn               *Return to spawn immeadiately (30min cooldown)")
                self.sendLine("/spells              *Shows your combat skills/spells")
                self.sendLine("/stats               *Looks up your own stats")
                self.sendLine("/time                *Displays current Arr'Fia time")
                self.sendLine("/w <user>            *Enter private chat mode")
            if self.adminmode == True:
                self.sendLine("The commands available to you are...")
                self.sendLine("/a <#>               *Attack the mob assigned to that slot")
                # self.sendLine("/c                   *Return back to command mode")
                self.sendLine("/changepass          *Changes your password")
                self.sendLine("/clear               *clears the screen of text")
                self.sendLine("/create (room or roomupdown)")
                self.sendLine("/equipped            *Looks up personal gear equipped")
                self.sendLine("/exit                *exit cleanly and save properly")
                self.sendLine("/inv                 *Opens your inventory")
                self.sendLine("/look                *Looks around your area")
                self.sendLine("/lookup <user>       *Looks up a users stats")
                self.sendLine("/pa <user>           *Attack a player")
                self.sendLine('/party invite <user> *Invites user to your party')
                self.sendLine("/pk                  *Toggles Player fighting on/off (5min wait)")
                self.sendLine("/setlevel <user> <level>")
                self.sendLine("/setexp <user> <exptnl>")
                self.sendLine("/skills              *Shows your characters skill levels")
                self.sendLine("/spells              *Shows your combat skills/spells")
                self.sendLine("/spawn               *Return to spawn immeadiately (30min cooldown)")
                self.sendLine("/stop <reason>       *Kicks everyone off the server then stops it")
                self.sendLine("/stats               *Looks up your own stats")
                self.sendLine("/time                *Displays current Arr'Fia time")
                self.sendLine("/tp <user or room>   *Teleports you to a player or roomID")
                self.sendLine("/update (room)")
                self.sendLine("/w <user>            *Enter private chat mode")
            return
        if(message == '/time'):
            self.Time()
            return
        if(message == '/pos'):
            self.LocationPrint()
            return
        if(message == '/exit'):
            self.EXIT()
            return
        if(message == '/inv'):
            self.INVENTORY()
            return
        if(message == '/skills'):
            self.Skilllist()
            return
        if(message == '/update room'):
            if self.adminmode == True:
                self.state = 'UpdateRoom1'
                self.sendLine("Which room would you like to update?")
            else:
                self.sendLine("Command not available")
            return
        if(message[0:9] == '/setlevel'):
            if self.adminmode == True:
                line = message[10:]
                self.playersearch(line, 'level')
        if(message[0:7] == '/setexp'):
            if self.adminmode == True:
                line = message[8:]
                self.playersearch(line, 'exp')
        if(message == '/spells'):
            self.Spells()
            return
        if(message[0:5] == '/cast'):
            st = message[6:]
            self.Cast(st)
            return
        if(message == '/create room'):
            if self.adminmode == False:
                return
            else:
                self.CreateRoom()
        if(message == '/create roomupdown'):
            if self.adminmode == False:
                return
            else:
                self.CreateRoomUpDown()
        if(message == '/stats'):
            self.STATS()
            return
        if(message == '/rest'):
            if self.room in (1, 6):
                if self.restready is True:
                    self.rest()
                else:
                    self.sendLine("You cannot rest so soon")
            else:
                self.sendLine("It is too dangerous to rest here...")
            return
        if(message == '/changepass'):
            self.sendLine("What do you want your password to be?")
            self.state = "CHANGEPASS"
            return
        if(message[0:7] == '/lookup'):
            try:
                message = message[8:]
                if message in(None, ''):
                    self.sendLine("proper use : /lookup <name>")
                else:
                    self.handle_CHARACTERLOOKUP(message)
            except:
                print "Lookup not working"
            return
        if(message[0:3] == '/tp'):
            location = message[4:]
            if self.adminmode == True:
                self.Teleport(location)
            else:
                pass
            return
        if(message[0:5] == '/stop'):
            message = message[6:]
            if self.adminmode == True:
                self.Stop(message)
            else:
                pass
            return
        if(message == '/list'):
            if self.adminmode == True:
                self.List()
            else:
                pass
            return
        if(message[0:5] == '/look'):
            direction = message[6:]
            if direction == '':
                self.LOOK()
            else:
                self.LOOK(direction)
            return
        if(message == '/levelup'):
            self.LevelUP()
            return
        if(message == '/equipped'):
            self.handle_EQUIP()
            return
        if(message[0:6] == '/admin'):
            if self.adminmode == True:
                self.sendLine("Admin mode turned off")
                self.adminmode = False
            else:
                password = message[7:]
                self.AdminChange(password)
        if(message == '/clear'):
            try:
                self.handle_CLEARSCREEN()
            except:
                print "Clear not working"
            return
        if(message == '/info'):
            try:
                self.sendLine("in /info")
                test.Info(self)
            except:
                self.sendLine("Didn't work'")
                self.List()
        if(message[0:13] == '/party invite'):
            person = message[14:]
            if person in(None, ''):
                self.sendLine("Not a valid user")
            else:
                self.PartyInvite(person)
                return
        if(message == '/party leave'):
            self.PartyLeave()
            return
        if(message == '/party'):
            self.PartyDisplayStats()
            return
        if(message == '/suicide'):
            try:
                self.handle_SUICIDE()
            except:
                print "Suicide Failed"
            return
        if(message[0:3] == '/pa'):
            attack = message[4:]
            if attack in(None, ''):
                self.sendLine("Not a valid username")
            else:
                self.handle_PLAYERATTACK(attack)
            return
        if(message[0:6] == '/spawn'):
            if self.spawn is True:
                self.sendLine("Preparing spawn teleport...")
                reactor.callLater(5.0, self.SPAWN)
            else:
                self.sendLine("You can't teleport to spawn yet")
        if(message[0:3] == '/pk'):
            if self.pkswitch is True:
                self.togglePK()
            else:
                self.sendLine("Cannot change pk mode yet...")
        if(message[0:2] == '/a'):
            #try:
            check = message[3:]
            if check in(None, ''):
                self.sendLine('Please specify which mob you would like to attack')
            else:
                self.AttackMOB(check)
            return
            #except:
            #    self.sendLine("Target invalid or Error occured")
        if(message[0:2] == '/w'):
            check = message[3:]
            if check in(None, ''):
                self.state = "WHISP"
                self.sendLine("Who would you like to private chat with?")
            else:
                self.handle_WHISP_ini(check)
            return
        if(message[0:2] == '/p'):
            message = message[3:]
            if self.partybool == True:
                self.PartyChat(message)
            else :
                self.sendLine("No party to talk to")
            return
        if(message[0:1] == '!'):
            message = message[1:]
            self.Shout(message)
        else:
            if(message[0:1] == " "):
                message = message[0:]
                self.handle_SAY(message)

    def togglePK(self):
        self.pkswitch = False
        if self.pk is True:
            self.pk = False
            self.sendLine("PK Mode is now turned off")
            reactor.callLater(300.0, self.handle_PKTOGGLEWAIT)
            return
        if self.pk is False:
            self.pk = True
            self.sendLine("PK Mode is now turned on! Watch yourself")
            reactor.callLater(300.0, self.handle_PKTOGGLEWAIT)
            return

    def Regeneration(self):
        self.health = self.health + self.healthregen
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        self.mana = self.mana + self.manaregen
        if self.mana > self.maxmana:
            self.mana = self.maxmana
        reactor.callLater(20.0, self.Regeneration)

    def CCCHECK2(self, answer):
        if answer in('con', 'Con', 'Continue', 'continue'):
            self.sendLine("You have successfully leveled up to level %s!" % (self.level))
            self.sendLine("You will want to relog to update your info correctly")
            curexptnl = self.exptnl
            nextexptnl = (self.level / 2) * 1000
            self.exptnl = curexptnl + nextexptnl
            self.state = "CHAT"
            if self.classname == 'Warrior':
                if self.level == 2:
                    self.warriorBonusI()
            if self.classname == 'Rogue':
                if self.level == 2:
                    self.criticalPassive()
                if self.level == 3:
                    self.rogueBonusI()
            if self.classname == 'Priest':
                if self.level == 2:
                    self.priestBonus()
            if self.classname == 'Magician':
                if self.level == 2:
                    self.mageBonusI()
                if self.level == 3:
                    self.manaRegen()
            self.maxhealthbonus = self.maxhealthbonus + int(self.constitution / 4)
            self.maxmanabonus = self.maxmanabonus + int(self.wisdom / 4)
            self.maxhealth = self.maxhealth + int(self.constitution / 4)
            self.maxmana = self.maxmana + int(self.wisdom / 4)
            self.EQUIPSTART()

        if answer in('q', 'Q', 'quit', 'Quit'):
            self.sendLine("Returned to previous attributes")
            self.level = self.level - 1
            t = (self.name,)
            c.execute('SELECT * FROM Character WHERE Name=?', t)
            test = c.fetchone()
            if(test != None):
            #Name, Class, Subclass Level, Exp, Exptnl, Strength, Constitution, Dexterity, Agility, Wisdom, Intellegence
                self.strength = test[6]
                self.constitution = test[7]
                self.dexterity = test[8]
                self.agility = test[9]
                self.wisdom = test[10]
                self.intellegence = test[11]
                self.StatCreation()
                self.EQUIPSTART()
                self.state = "CHAT"

    def LevelUP(self):
        if self.exptnl <= 0:
            self.level += 1
            self.StatCreation()
            self.STATS()
            self.sendLine("Pick a stat to add a point into...")
            self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
            if self.level in(5, 10, 15, 20, 25, 30):
                self.attributepoints = 2
            else:
                self.attributepoints = 1
            self.sendLine("%s points remaining" % self.attributepoints)
            self.state = "AddPoints2"
        else:
            self.sendLine("Still need %s more experience to next level" % (self.exptnl))

    def AdditionalPoints2(self, stat):
        if stat in('str', 'Str', 'strength', 'Strength', 's', 'S'):
            self.strength = self.strength + 1
            self.attributepoints = self.attributepoints - 1
            self.StatCreation()
            self.STATS()
            if self.attributepoints > 0:
                self.sendLine("Pick a stat to add a point into...")
                self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                self.sendLine("%s points remaining" % self.attributepoints)
            else:
                self.state = "CCCHECK2"
                self.sendLine("These are the results of your curstomization")
                self.sendLine("Would you like to continue or quit? (con/quit)")
        if stat in('dex', 'Dex', 'dexterity', 'Dexterity', 'd', 'D'):
            self.dexterity = self.dexterity + 1
            self.attributepoints = self.attributepoints - 1
            self.StatCreation()
            self.STATS()
            if self.attributepoints > 0:
                self.sendLine("Pick a stat to add a point into...")
                self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                self.sendLine("%s points remaining" % self.attributepoints)
            else:
                self.state = "CCCHECK2"
                self.sendLine("These are the results of your customization")
                self.sendLine("Would you like to continue or quit? (con/quit)")
        if stat in('con', 'Con', 'constitution', 'Constitution', 'c', 'C'):
            self.constitution = self.constitution + 1
            self.attributepoints = self.attributepoints - 1
            self.StatCreation()
            self.STATS()
            if self.attributepoints > 0:
                self.sendLine("Pick a stat to add a point into...")
                self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                self.sendLine("%s points remaining" % self.attributepoints)
            else:
                self.state = "CCCHECK2"
                self.sendLine("These are the results of your customization")
                self.sendLine("Would you like to continue or quit? (con/quit)")
        if stat in('agi', 'Agi', 'agility', 'Agility', 'a', 'A'):
            self.agility = self.agility + 1
            self.attributepoints = self.attributepoints - 1
            self.StatCreation()
            self.STATS()
            if self.attributepoints > 0:
                self.sendLine("Pick a stat to add a point into...")
                self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                self.sendLine("%s points remaining" % self.attributepoints)
            else:
                self.state = "CCCHECK2"
                self.sendLine("These are the final results of your creation")
                self.sendLine("Would you like to continue or quit? (con/quit)")
        if stat in('wis', 'Wis', 'wisdom', 'Wisdom', 'w', 'W'):
            self.wisdom = self.wisdom + 1
            self.attributepoints = self.attributepoints - 1
            self.StatCreation()
            self.STATS()
            if self.attributepoints > 0:
                self.sendLine("Pick a stat to add a point into...")
                self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                self.sendLine("%s points remaining" % self.attributepoints)
            else:
                self.state = "CCCHECK2"
                self.sendLine("These are the final results of your creation")
                self.sendLine("Would you like to continue or quit? (con/quit)")
        if stat in('int', 'Int', 'Intellegence', 'intellegence', 'i', 'I'):
            self.intellegence = self.intellegence + 1
            self.attributepoints = self.attributepoints - 1
            self.StatCreation()
            self.STATS()
            if self.attributepoints > 0:
                self.sendLine("Pick a stat to add a point into...")
                self.sendLine("Choices : Str, Con, Dex, Agi, Wis, Int")
                self.sendLine("%s points remaining" % self.attributepoints)
            else:
                self.state = "CCCHECK2"
                self.sendLine("These are the final results of your creation")
                self.sendLine("Would you like to continue or quit? (con/quit)")

    def handle_PKTOGGLEWAIT(self):
        self.pkswitch = True
        self.sendLine("Can switch PK Mode again")

    def handle_ATTACKINIT(self):
        self.sendLine("Who are you attacking?")
        self.state = "ATTACK"

    def handle_ATTACKWAIT(self):
        self.attackready = True
        self.sendLine("Attack Ready")

    def handle_RESETSUICIDE(self):
        self.suicide = True

    def handle_SUICIDE(self):
        if self.suicide is True:
            self.sendLine("You have died and been reincarnated at your body")
            self.sendLine("You cannot do this again for 10 minutes")
            self.health = self.maxhealth
            self.suicide = False
            for name, protocol in self.users.iteritems():
        #       if protocol != self: #Use this if you don't want messages to be sent to self'  # lint:ok
                protocol.sendLine("%s has commited suicide..." % (self.name))
                reactor.callLater(600.0, self.handle_RESETSUICIDE)
        else:
            self.sendLine("You cannot suicide for a while still")

    def handle_PLAYERATTACK(self, target):
        if self.pk == False:
            self.sendLine("You are not in pk mode... cannot attack")
            return
        global userlist
        diction = userlist
        target = str(target)
        atk = diction.get(target)
        #diction = self.users
        if target == self.name:
            self.sendLine("You cannot attack yourself...")
            return
        #target = str(target)
        #atk = diction.get(target)
        #global c
        #target = str(target)
        #targets = (target,)
        if atk.pk == False:
            self.sendLine("Player is not in pk mode... cannot attack")
            return
        if atk is None:
            self.sendLine("Attack failed : User not Found")
        else:
            if self.attackready is True:
                hitmax = 100 + atk.dodge
                hit = random.randint(1, hitmax)
                crit = random.randint(1, 100)
                attackmin = self.mainhandvalmin
                attackmax = self.mainhandvalmax
                if(self.offhandtype == 'Weapon'):
                    offhandmin = self.offhandvalmin * 0.75
                    offhandmin = int(offhandmin)
                    offhandmax = self.offhandvalmax * 0.75
                    offhandmax = int(offhandmax)
                    attackmin = self.mainhandvalmin + offhandmin
                    attackmax = self.mainhandvalmax + offhandmax
                attack = random.randint(attackmin, attackmax) + self.strengthdamage
                if(hit <= self.accuracy):
                    af = float(self.attack)
                    attackmod = af / atk.defence
                    attack = float(attack)
                    attack = attackmod * attack
                    attack = int(attack)
                    if crit <= self.critical:
                        attack = attack * 2
                        if(atk.type == 'Player'):
                            atk.sendLine("You have been critically attacked by %s!" % (self.name))
                        self.sendLine("You ***CRITICALLY HIT*** %s for %s damage!" % (atk.name, attack))
                        atk.health = atk.health - attack
                    else:
                        if(atk.type == 'Player'):
                            atk.sendLine("You have been attacked by %s!" % (self.name))
                        self.sendLine("You ***HIT*** %s for %s damage!" % (atk.name, attack))
                        atk.health = atk.health - attack
                    if(atk.health <= 0):
                        self.handle_DEATH(atk)
                    else:
                        atk.sendLine("You now %s health left..." % (atk.health,))  # lint:ok
                        self.state = "CHAT"
                        self.attackready = False
                        reactor.callLater(self.attackspeed, self.handle_ATTACKWAIT)
                else:
                    if(atk.type == 'Player'):
                        atk.sendLine("You have been attacked by %s!" % (self.name))
                        atk.sendLine("However they missed you...")
                    self.sendLine("You ***MISSED*** %s!" % (atk.name))
                    self.state = "CHAT"
                    self.attackready = False
                    reactor.callLater(self.attackspeed, self.handle_ATTACKWAIT)
            else:
                self.sendLine("You need to wait a little bit longer before attacking")

    def AttackMOB(self, target):
        global c
        slot = target
        if slot not in('1', '2', '3', '4', '5'):
            return
        slot = int(slot)
        room = (self.room,)
        c.execute('SELECT * FROM RoomMobs WHERE ID=?', room)
        test= c.fetchone()
        mob = test[slot]
        if mob in('', None):
            self.sendLine("Creature doesn't exist!")
            return
        mobs = (mob,)
        c.execute('SELECT * FROM ActiveMonster WHERE RandomID=?', mobs)
        test = c.fetchone()
        name = str(test[3])
        # RandomID, MobID, Level, Name, Health, MaxHealth, Mana, MaxMana, Attack, Defence, Speed, Critical, Accuracy, 13Dodge, Mattack, Mdefence, room, AttackBool
        if test is None:
            self.sendLine("Attack failed : Target not found")
        else:
            if self.attackready is True:
                hitmax = 100 + int(test[13])
                hit = random.randint(1, hitmax)
                crit = random.randint(1, 100)
                attackmin = self.mainhandvalmin
                attackmax = self.mainhandvalmax
                Critical = False
                if(self.offhandtype == 'Weapon'):
                    offhandmin = self.offhandvalmin * 0.75
                    offhandmin = int(offhandmin)
                    offhandmax = self.offhandvalmax * 0.75
                    offhandmax = int(offhandmax)
                    attackmin = self.mainhandvalmin + offhandmin
                    attackmax = self.mainhandvalmax + offhandmax
                attack = random.randint(attackmin, attackmax) + self.strengthdamage
                if(hit <= self.accuracy):
                    af = float(self.attack)
                    attackmod = af / int(test[9])
                    attack = float(attack)
                    attack = attackmod * attack
                    if crit <= self.critical:
                        attack = attack * 2
                        Critical = True
                    attack = int(attack)
                    mobhp = int(test[4])
                    mobhp = mobhp - attack
                    mob = unicode(mob)
                    self.threatCalculator(attack, mob)
                    c.execute('UPDATE ActiveMonster SET Health=? WHERE RandomID=?', (mobhp, mob))
                    if(mobhp <= 0): # Mob health < 0 Check
                        self.handle_MOBDEATH(test[0], test[2], target)
                        self.sendLine("You have slain the %s" % (name))
                        self.handle_TellRoom("%s has slain the %s" % (self.name, name))
                    else:
                        if Critical is True:
                            self.sendLine("You critically hit the %s for %s damage!" % (name, attack))
                            self.handle_TellRoom("%s critically hit %s for %s damage" % (self.name, name, attack))
                        else:
                            self.sendLine("You hit the %s for %s damage!" % (name, attack))
                            self.handle_TellRoom("%s hit %s for %s damage" % (self.name, name, attack))
                        self.attackready = False
                        reactor.callLater(self.attackspeed, self.handle_ATTACKWAIT)
                else:
                    self.sendLine("You ***MISSED*** the %s!" % (name))
                    self.handle_TellRoom("%s misses the %s" % (self.name, name))
                    self.attackready = False
                    reactor.callLater(self.attackspeed, self.handle_ATTACKWAIT)
                    mob = unicode(mob)
                    self.threatCalculator(1, mob)
                fightbool = str(test[17])
                if fightbool == 'False':
                    c.execute('''UPDATE ActiveMonster SET AttackBool='True' WHERE RandomID=?''', mobs)
                    conn.commit()
                    reactor.callLater(3.0, MobFight, mob)
            else:
                self.sendLine("You need to wait a little bit longer before attacking")
            conn.commit()

    def handle_MOBDEATH(self, randomid, CR, slot):
        random = randomid
        mobs = (randomid,)
        c.execute('SELECT * FROM ActiveMonster WHERE RandomID=?', mobs)
        test = c.fetchone()
        CR = test[2]
        region = str(test[18])
        self.GiveEXP(CR)
        c.execute('''DELETE FROM ActiveMonster WHERE RandomID=?''', mobs)
        c.execute('''DELETE FROM MonsterThreat WHERE RandomID=?''', mobs)
        column = "'Slot" + str(slot) + "'"
        c.execute("UPDATE RoomMobs SET " + column + "=? WHERE ID=?", ('', self.room))
        regionname = (region,)
        c.execute('''SELECT * FROM Regions WHERE Name=?''', regionname)
        fetch = c.fetchone()
        mobs = int(fetch[1])
        mobs = mobs - 1
        update = (mobs, region,)
        c.execute('''UPDATE Regions SET Mobcount=? WHERE Name=?''', update)
        conn.commit()

    def handle_TellRoom(self, line):
        global c
        room = self.room
        room = (room,)
        c.execute('''SELECT * FROM RoomPlayers where ID=?''', room)
        test = c.fetchone()
        count = 1
        while(count <= 20):
            teststr = test[count]
            teststr = str(teststr)
            if teststr in('', None):
                count = count + 1
            else:
                if teststr == self.name:
                    count = count + 1
                else:
                    name = teststr
                    count = count + 1
                    global userlist
                    diction = userlist
                    name = str(name)
                    atk = diction.get(name)
                    atk.sendLine(line)

    def GiveEXP(self, CR):
        if self.partybool is False:
            cr = float(CR)
            expmod = cr / self.level
            exp = 100 * expmod
            exp = int(exp)
            self.sendLine("You have gained %s experience!" % (exp))
            curexp = self.exp
            curexp = exp + curexp
            self.exp = curexp
            self.exptnl = self.exptnl - exp
            self.sendLine("You need %s more to next level." % (self.exptnl))
        else:
            party = self.party
            global userlist
            diction = userlist
            level1 = 0
            level2 = 0
            level3 = 0
            level4 = 0
            level5 = 0
            level6 = 0
            countmax = 0
            try:
                member1 = party[0]
                member1 = diction.get(member1)
                level1 = member1.level
            except:
                pass
            try:
                member2 = party[1]
                member2 = diction.get(member2)
                level2 = member2.level
                countmax = countmax + 1
            except:
                pass
            try:
                member3 = party[2]
                member3 = diction.get(member3)
                level3 = member3.level
                countmax = countmax + 1
            except:
                pass
            try:
                member4 = party[3]
                member4 = diction.get(member4)
                level4 = member4.level
                countmax = countmax + 1
            except:
                pass
            try:
                member5 = party[4]
                member5 = diction.get(member5)
                level5 = member5.level
                countmax = countmax + 1
            except:
                pass
            try:
                member6 = party[5]
                member6 = diction.get(member6)
                level6 = member6.level
                countmax = countmax + 1
            except:
                pass
            level = level1 + level2 + level3 + level4 + level5 + level6
            level = float(level)
            levelmod = level / countmax
            cr = float(CR)
            expmod = cr / levelmod
            exp = 100 * expmod
            bonus = countmax * 0.2
            expbonus = exp * bonus
            exp = expbonus + exp
            exp = exp / countmax
            exp = int(exp)
            count = 0
            while count <= countmax:
                member = party[count]
                member = diction.get(member)
                curexp = member.exp
                curexp = exp + curexp
                member.exp = curexp
                member.exptnl = member.exptnl - exp
                member.sendLine("You gained %s from a party kill." % (exp))
                member.sendLine("You need %s more to next level." % (member.exptnl))
                count = count + 1

    def handle_SAY(self, message):
        if self.adminmode == True:
            message = "(Admin) %s :: %s" % (self.name, message)
        else:
            message = "%s :: %s" % (self.name, message)
        print message
        global userlist
        diction = userlist
        for key, value in diction.iteritems():
            player = diction.get(key)
            room = player.room
            if room == self.room:
                player.sendLine(message)

    def Shout(self, message):
        if self.adminmode == True:
            message = "[Global](Admin) %s :: %s" % (self.name, message)
        else:
            message = "[Global] %s :: %s" % (self.name, message)
        print message
        global userlist
        diction = userlist
        for key, value in diction.iteritems():
            player = diction.get(key)
            room = player.room
            player.sendLine(message)

    def playersearch(self, line, function):
        try:
            searchline = line
            n = 1
            while n < 20:
                if searchline[n] == ' ':
                    name = searchline[0:n]
                    global userlist
                    if name in userlist:
                        n = n + 1
                        if function == 'level':
                            level = int(searchline[n:])
                            self.LevelSet(name, level)
                        if function == 'exp':
                            exp = int(searchline[n:])
                            self.ExpSet(name, exp)
                    break
                else:
                    n = n + 1
                    if n == 21:
                        self.sendLine("Player not found")
        except:
            self.sendLine("Error Occured")

    def handle_WHISP_ini(self, name):
        self.whisper = name
        diction = self.users
        person = str(self.whisper)
        whisp = diction.get(person)
        if whisp != None:
            self.whisper = name
            self.state = "WHISPER"
            self.sendLine("Now in chat with %s" % (name))
        else:
            self.sendLine("No user with that name, try again...")
            self.state = 'CHAT'

    def CHANGE_PASSWORD1(self, password):
        self.password = password
        self.state = "CHANGEPASS2"
        self.sendLine("Is the password, %s, correct? (y/n)" % self.password)

    def CHANGE_PASSWORD2(self, answer):
        if answer in("y", "Y", "yes", "Yes"):
            entry = (self.password, self.name)
            c.execute('''UPDATE ID SET Password=? WHERE Name=?''', entry)
            self.sendLine("Password changed!")
            conn.commit()
            self.state = "CHAT"
        if answer in("n", "N", "no", "No"):
            self.sendLine("What do you want your password to be?")
            self.state = "CHANGEPASS"
            return

    def LOOK(self, direction=None):
        self.displayExits(direction)

    def SPAWN(self):
        self.handle_CLEARSCREEN()
        self.sendLine("You have teleported to spawn")
        self.room = 1
        self.updateRoom('Teleport', 'Teleport')
        self.displayExits()
        self.spawn = False
        reactor.callLater(600.0, self.SpawnReset)
        pass

    def Cast(self, st):
        if self.classname == 'Warrior':
            if st[0:9] == 'Heavy Hit':
                target = st[10:]
                self.HeavyHit(target)
                return
            if self.level < 4:
                return
            if st[0:10] == 'Double Hit':
                target = st[11:]
                self.doubleHit(target)
                return
            if self.level < 5:
                return
            if st[0:5] == 'Taunt':
                target = st[6:]
                self.taunt(target)
                return
            if self.level < 7:
                return
            if st[0:6] == 'Stance':
                type = st[7:]
                self.warriorStance(type)
                return
        if self.classname == 'Priest':
            if st[0:10] == 'Light Bash':
                target = st[11:]
                self.lightBash(target)
                return
            if self.level < 3:
                return
            if st[0:11] == 'Single Heal':
                target = st[12:]
                self.targetHeal(target)
            if self.level < 5:
                return
            if st[0:12] == 'Light Strike':
                target = st[13:]
                self.lightStrike(target)
            if self.level < 7:
                return
            if st[0:10] == 'Group Heal':
                self.groupHeal()
        if self.classname == 'Rogue':
            if st[0:13] == 'Double Strike':
                target = st[14:]
                self.doubleStrike(target)
                return
            if self.level < 5:
                return
            if st[0:12] == 'Dirty Strike':
                target = st[13:]
                self.dirtyStrike(target)
                return
            if self.level < 7:
                return
            if st[0:13] == 'Triple Strike':
                target = st[14:]
                self.tripleStrike(target)
                return
        if self.classname == 'Magician':
            if st[0:8] == 'Fireball':
                target = st[9:]
                self.fireball(target)
                return
            if self.level <  5:
                return
            if st[0:8] == 'Ice Bolt':
                target = st[9:]
                self.iceBolt(target)
                return
            if self.level < 7:
                return
            if st[0:12] == 'Thunder Bolt':
                target =st[13:]
                self.thunderBolt(target)
                return

    def Skilllist(self):
        self.sendLine("Adventure Skills    Level      Exp needed")
        self.sendLine("Climbing              %3s           %5s" % (self.Climbing, self.Climbingtnl))
        self.sendLine("Sneak                 %3s           %5s" % (self.Sneakskill, self.Sneakskilltnl))
        self.sendLine("Swimming              %3s           %5s" % (self.Swimming, self.Swimmingtnl))
        self.sendLine("")
        self.sendLine("Gathering Skills")
        self.sendLine("Foraging              %3s           %5s" % (self.Foraging, self.Foragingtnl))
        self.sendLine("Logging               %3s           %5s" % (self.Logging, self.Loggingtnl))
        self.sendLine("Mining                %3s           %5s" % (self.Mining, self.Miningtnl))
        self.sendLine("")
        self.sendLine("Crafting Skills")
        self.sendLine("Building              %3s           %5s" % (self.Building, self.Buildingtnl))
        self.sendLine("Stonecutting          %3s           %5s" % (self.Stonecutting, self.Stonecuttingtnl))
        self.sendLine("Tanning               %3s           %5s" % (self.Tanning, self.Tanningtnl))
        self.sendLine("Woodcutting           %3s           %5s" % (self.Woodcutting, self.Woodcuttingtnl))

    def Spells(self):
        self.handle_CLEARSCREEN()
        self.sendLine("Spells Available:")
        if self.classname == 'Warrior':
            self.sendLine("Heavy Hit          - Adds half of your strength to a hit (Active - 10MP)")
            if self.level >= 2:
                self.sendLine("Warrior Bonus I    - +1 Strength, + 1 Constitution (Passive)")
            if self.level >= 4:
                self.sendLine("Double Hit         - Attacks the target twice (Active - 8MP)")
            if self.level >= 5:
                self.sendLine("Taunt              - Taunts the target into attacking you (Active - 4MP)")
            if self.level >= 7:
                self.sendLine("Stance (offensive, defensive, normal)   - Augments your attack/defence by to a 125%/75% ratio depending on type (Passive Toggle)")
        if self.classname == 'Rogue':
            self.sendLine("Double Strike      - Attacks the target twice (Active - 8MP)")
            if self.level >= 2:
                self.sendLine("Critical Bonus I   - Adds 5% to your critical chance (Passive)")
            if self.level >= 3:
                self.sendLine("Rogue Bonus I      - +1 Strength, +1 Dexterity (Passive)")
            if self.level >= 5:
                self.sendLine("Dirty Strike       - Temporarily blinds the opponet(Active - 12MP)")
            if self.level >= 7:
                self.sendLine("Triple Strike      - Attacks the target three times (Active - 16MP)")
        if self.classname == 'Priest':
            self.sendLine("Light Bash         - Deals 0.25 * Wisdom damage, and has a chance to stun (Active - 8MP)")
            if self.level >= 2:
                self.sendLine("Priest Bonus I     - +1 Constitution, +1 Wisdom (Passive)")
            if self.level >= 3:
                self.sendLine("Single Heal        - Heals the target for 1.5 * Wisdom + 0.5 * Intellegence (Active - 12MP)")
            if self.level >= 5:
                self.sendLine("Light Strike       - Adds up to half of your wisdom as damage onto your normal attack (Active - 16MP)")
            if self.level >= 7:
                self.sendLine("Group Heal         - Heals each player in your party for up to half of your wisdom (Active - 18MP)")
        if self.classname == 'Magician':
            self.sendLine("Fireball           - Deals between 1/3 * Intellegence to 2/3 * Intellegence + additional magic damage (Active - 8MP)")
            if self.level >= 2:
                self.sendLine("Magician Bonus I   - +1 Wisdom, +1 Intellegence (Passive)")
            if self.level >= 3:
                self.sendLine("Mana Regen Bonus I - +1 to mana regen (Passive)")
            if self.level >= 5:
                self.sendLine("Ice Bolt           - Deals between 1/4 * Intellegence to 1/2 * Intellegence + additional damage. Has chance to stun (Active - 14MP)")
            if self.level >= 7:
                self.sendLine("Thunder Bolt       - Deals between 1/3 * Intellegence to 2/3 * Intellegence + 40% chance to crit (Active - 20MP)")
        self.sendLine("")
        self.sendLine("Use /cast <name> <target> to use a spell")

    def Time(self):
        global c
        c.execute('''SELECT * From ServerTime''')
        fetch = c.fetchone()
        localmin = int(fetch[1])
        if localmin in(0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            localmin = '0' + str(localmin)
        localhour = int(fetch[2])
        night = bool(fetch[3])
        day = int(fetch[4])
        if day == 1:
            day = '1st'
        if day == 2:
            day = '2nd'
        if day == 3:
            day = '3rd'
        else:
            check = isinstance(day, str)
            if check == True:
                pass
            else:
                day = str(day) + 'th'
        month = int(fetch[5])
        if month == 1:
            monthname = 'Ianuarius'
        if month == 2:
            monthname = 'Februarius'
        if month == 3:
            monthname = 'Matrius'
        if month == 4:
            monthname = 'Aprilis'
        if month == 5:
            monthname = 'Maius'
        if month == 6:
            monthname = 'Iunius'
        if month == 7:
            monthname = 'Quintilis'
        if month == 8:
            monthname = 'Augustus'
        if month == 9:
            monthname = 'Lapsus'
        if month == 10:
            monthname = 'Bruma'
        if month == 11:
            monthname = 'Frigus'
        if month == 12:
            monthname = 'Glacialis'
        if night == True:
            localtime = 'Night-time'
        else:
            localtime = 'Day-time'
        line = 'Arrfia Date : It is the ' + str(day) + ' day of ' + monthname
        line2 = 'Arrfia Time : ' + str(localhour) + ':' + str(localmin) + '   ' + localtime
        self.sendLine(line)
        self.sendLine(line2)

    def SpawnReset(self):
        self.spawn = True
        self.sendLine("Spawn teleport has been refreshed")

    def EXIT(self):
        leave = "Disconnected"
        self.handle_CLEARSCREEN()
        self.sendLine("You may now close the window safely")
        self.connectionLost(leave)
        self.state = "DISCONNECTED"

    def rest(self):
        self.health = self.maxhealth
        self.mana = self.maxmana
        self.restready = False
        self.sendLine("You rest for a while, and you vitals are now maxed")

    def handle_WHISPER(self, message1):
        try:
            if(message1 == '/c'):
                self.state = "CHAT"
                self.sendLine("You have left your private chat")
            else:
                message = "(Private)<---[ %s ] : %s" % (self.name, message1)
                diction = self.users
                person = str(self.whisper)
                whisp = diction.get(person)
                if whisp == None:
                    self.sendLine("Person doesn't exist, or is offline please type /c and try again")
                else:
                    print "[PM] (", self.name, ") -->", "(", person, ")", message1
                    whisp.sendLine(message)
                    message = "(Private)--->[ %s ] : %s" % (whisp.name, message1)
                    self.sendLine(message)
        except:
            print "Whisper failed by", self.name
            self.sendLine("Whisper failed, please type /c and try again")

    def threatCalculator(self, damage, RandomID):
        try:
            found = False
            dam = damage
            multi = self.threatmultiplier
            threat = dam * multi
            ID = (RandomID,)
            global c
            c.execute('''SELECT * FROM MonsterThreat WHERE RandomID=?''', ID)
            fetch = c.fetchone()
            count = 1
            while count <= 11:
                name = fetch[count]
                name = str(name)
                if name == self.name:
                    found = True
                    count += 1
                    curthreat = fetch[count]
                    curthreat = curthreat + threat
                    if count == 2:
                        c.execute("UPDATE MonsterThreat SET Threat1=? WHERE RandomID=?", (curthreat, RandomID))
                    if count == 4:
                        c.execute("UPDATE MonsterThreat SET Threat2=? WHERE RandomID=?", (curthreat, RandomID))
                    if count == 6:
                        c.execute("UPDATE MonsterThreat SET Threat3=? WHERE RandomID=?", (curthreat, RandomID))
                    if count == 8:
                        c.execute("UPDATE MonsterThreat SET Threat4=? WHERE RandomID=?", (curthreat, RandomID))
                    if count == 10:
                        c.execute("UPDATE MonsterThreat SET Threat5=? WHERE RandomID=?", (curthreat, RandomID))
                    if count == 12:
                        c.execute("UPDATE MonsterThreat SET Threat6=? WHERE RandomID=?", (curthreat, RandomID))
                else:
                    count = count + 2
            count2 = 1
            if found is False:
                while count2 <= 11:
                    name = fetch[count2]
                    name = str(name)
                    if name in('', None):
                        if count2 == 1:
                            c.execute("UPDATE MonsterThreat SET Player1=? WHERE RandomID=?", (self.name, RandomID))
                            c.execute("UPDATE MonsterThreat SET Threat1=? WHERE RandomID=?", (threat, RandomID))
                            count2 = 12
                        if count2 == 3:
                            c.execute("UPDATE MonsterThreat SET Player2=? WHERE RandomID=?", (self.name, RandomID))
                            c.execute("UPDATE MonsterThreat SET Threat2=? WHERE RandomID=?", (threat, RandomID))
                            count2 = 12
                        if count2 == 5:
                            c.execute("UPDATE MonsterThreat SET Player3=? WHERE RandomID=?", (self.name, RandomID))
                            c.execute("UPDATE MonsterThreat SET Threat3=? WHERE RandomID=?", (threat, RandomID))
                            count2 = 12
                        if count2 == 7:
                            c.execute("UPDATE MonsterThreat SET Player4=? WHERE RandomID=?", (self.name, RandomID))
                            c.execute("UPDATE MonsterThreat SET Threat4=? WHERE RandomID=?", (threat, RandomID))
                            count2 = 12
                        if count2 == 9:
                            c.execute("UPDATE MonsterThreat SET Player5=? WHERE RandomID=?", (self.name, RandomID))
                            c.execute("UPDATE MonsterThreat SET Threat5=? WHERE RandomID=?", (threat, RandomID))
                            count2 = 12
                        if count2 == 11:
                            c.execute("UPDATE MonsterThreat SET Player6=? WHERE RandomID=?", (self.name, RandomID))
                            c.execute("UPDATE MonsterThreat SET Threat6=? WHERE RandomID=?", (threat, RandomID))
                            count2 = 12
                    else:
                        count2 = count2 + 2
            conn.commit()
        except:
            print 'Threat calculator error for', self.name


class ChatFactory(Factory):

    def __init__(self):
        self.users = {}  # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)


class MobSpawner():

    def __init__(self):
        global c

        self.spawnedregions = 'Spawned in... '
# Name, Mobcount, MobMax, SpawnRate, RoomMobMax, Roommin, Roommax
        c.execute('SELECT * FROM Regions')
        regions = c.fetchall()
        for row in regions:
            self.regionname = str(row[0])
            self.MobMax = row[2]
            self.SpawnRate = row[3]
            self.Rooms = []
            rooms = self.Rooms
            counter = row[5]
            countmax = row[6]
            c.execute('SELECT * FROM RegionIgnoreRooms WHERE Name=?', (self.regionname,))
            ignorerooms = c.fetchone()
            while counter <= countmax:
                if counter in ignorerooms:
                    counter += 1
                else:
                    rooms.append(counter)
                    counter += 1
            c.execute('SELECT * FROM RegionMobs WHERE Name=?', (self.regionname,))
            mobs = c.fetchone()
            self.Mobs = []
            mobcounter = 1
            while mobcounter <= 10:
                if mobs[mobcounter] == '':
                    mobcounter = mobcounter + 1
                else:
                    mobid = mobs[mobcounter]
                    self.Mobs.append(mobid)
                    mobcounter = mobcounter + 1
            self.Mobcount = row[1]
            self.RandomMobGenerator()

        # For Mob Spawning
        self.health = 0
        self.mana = 0
        self.strdmg = 0
        self.attack = 0
        self.defence = 0
        self.accuracy = 0
        self.speed = 0
        self.dodge = 0
        self.mattack = 0
        self.mdefence = 0
        self.critical = 0
        self.name = ''
        if self.spawnedregions == 'Spawned in... ':
            pass
        else:
            print self.spawnedregions

    def StatCreation(self, strength, constitution, dexterity, agility, wisdom, intellegence):
        health = strength * 2
        health2 = constitution * 2
        health = int(health)
        health2 = int(health2)
        health = health + health2
        attack = strength * 3
        strdmg = strength / 8.0
        strdmg = int(strdmg)
        defence = constitution * 2
        self.strdmg = strdmg
        self.health = health
        self.attack = attack
        self.defence = defence
        dexterity = dexterity
        agility = agility
        accuracy = dexterity * 2
        accuracy = accuracy + 50
        speedmod = agility + dexterity
        speedmod = speedmod / 250.00
        speedmod = 1 - speedmod
        dodge = agility * 2
        critical = dexterity / 4.0
        critical1 = agility / 4.0
        critical = critical + critical1
        critical = int(critical)
        self.speed = speedmod
        self.accuracy = accuracy
        self.dodge = dodge
        self.critical = critical
        wisdom = wisdom
        intellegence = intellegence
        mana = wisdom * 2
        mana2 = intellegence * 2
        mana2 = int(mana2)
        mana = mana + mana2
        mattack = intellegence * 2
        mdefence = wisdom * 2
        self.mana = mana
        self.mattack = mattack
        self.mdefence = mdefence

    def CreateMob(self, Randid, Mobtype, room, regionname):
        Randid = Randid
        Mobtype = Mobtype
        Randidsql = (Randid,)
        Mobtypesql = (Mobtype,)
        c.execute('''SELECT * From Monsters WHERE ID=?''', Mobtypesql)
        mob = c.fetchone()
        self.name = mob[1]
        level = mob[2]
        stren = mob[3]
        con = mob[4]
        dex = mob[5]
        agi = mob[6]
        wis = mob[7]
        intel = mob[8]
        self.StatCreation(stren, con, dex, agi, wis, intel)
        mob = (Randid, Mobtype, level, self.name, self.health, self.health, self.mana, self.mana, self.attack, self.defence, self.speed, self.critical, self.accuracy, self.dodge, self.mattack, self.mdefence, room, 'False', regionname, 'False')
        c.execute('''INSERT INTO ActiveMonster VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', mob)
        threat = (Randid, '', 0, '', 0,'', 0, '', 0, '', 0, '', 0)
        c.execute('''INSERT INTO MonsterThreat VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', threat)

    def RandomMobGenerator(self):
        global c
        regionname = (self.regionname,)
        c.execute('''SELECT * FROM Regions WHERE Name=?''', regionname)
        mobcount = c.fetchone()
        mobcount = int(mobcount[1])
        spawn = self.SpawnRate
        if mobcount >= self.MobMax:
            return
        self.spawnedregions = self.spawnedregions + self.regionname + ', '
        while spawn > 0:
            region = self.regionname
            regionname = (region,)
            room = random.choice(self.Rooms)
            roomc = (room,)
            c.execute('''SELECT * From RoomMobs WHERE ID=?''', roomc)
            test = c.fetchone()
            if test[1] in ('', None, 'dead'):
                size = 6
                chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
                id0 = ''.join(random.choice(chars) for x in range(size))
                mon = random.choice(self.Mobs)
                self.CreateMob(id0, mon, room, region)
                # print "Created Mob,", self.name, "in room,", room, "in slot1"
                c.execute('''SELECT * FROM Regions WHERE Name=?''', regionname)
                mobcount = c.fetchone()
                mobcount = mobcount[1]
                mobcount = int(mobcount) + 1
                mobcount = str(mobcount)
                regionname = self.regionname
                c.execute('''UPDATE Regions SET Mobcount=? WHERE Name=?''', (mobcount, regionname))
                c.execute('''UPDATE RoomMobs SET Slot1=? WHERE ID=?''', (id0, room))
                conn.commit()
                spawn -= 1
            else:
                if test[2] in ('', None, 'dead'):
                    size = 6
                    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
                    id0 = ''.join(random.choice(chars) for x in range(size))
                    mon = random.choice(self.Mobs)
                    self.CreateMob(id0, mon, room, region)
                    # print "Created Mob,", self.name, "in room,", room, "in slot2"
                    c.execute('''SELECT * FROM Regions WHERE Name=?''', regionname)
                    mobcount = c.fetchone()
                    mobcount = mobcount[1]
                    mobcount = int(mobcount) + 1
                    mobcount = str(mobcount)
                    regionname = self.regionname
                    c.execute('''UPDATE Regions SET Mobcount=? WHERE Name=?''', (mobcount, regionname))
                    c.execute('''UPDATE RoomMobs SET Slot2=? WHERE ID=?''', (id0, room))
                    conn.commit()
                    spawn -= 1
                else:
                    if test[3] in ('', None, 'dead'):
                        size = 6
                        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
                        id0 = ''.join(random.choice(chars) for x in range(size))
                        mon = random.choice(self.Mobs)
                        self.CreateMob(id0, mon, room, region)
                        # print "Created Mob,", self.name, "in room,", room, "in slot3"
                        c.execute('''SELECT * FROM Regions WHERE Name=?''', regionname)
                        mobcount = c.fetchone()
                        mobcount = mobcount[1]
                        mobcount = int(mobcount) + 1
                        mobcount = str(mobcount)
                        regionname = self.regionname
                        c.execute('''UPDATE Regions SET Mobcount=? WHERE Name=?''', (mobcount, regionname))
                        c.execute('''UPDATE RoomMobs SET Slot3=? WHERE ID=?''', (id0, room))
                        conn.commit()
                        spawn -= 1
                    else:
                        pass


class MobFight():

    def __init__(self, rand):
        global c
        self.id = rand
        mob = (rand,)
        c.execute('SELECT * FROM ActiveMonster WHERE RandomID=?', mob)
        result = c.fetchone()
        if result in(None, ''):
            return
        self.room = result[16]
        self.name = result[3]
        self.type = result[1]
        self.targetname = ''
        self.target = ''
        self.targets = {}
        self.attack = result[8]
        self.defence = result[9]
        self.accuracy = result[12]
        self.health = result[4]
        if self.health <= 0:
            return
        self.slot = 0
        self.attackspeed = 3.0
        self.stun = result[19]
        if self.stun == True:
            self.MobTellRoom('Stun', 0)
        self.TryFight()
        if self.target == None:
            c.execute('''UPDATE ActiveMonster SET AttackBool='False' WHERE RandomID=?''', (self.id,))
            conn.commit()
        else:
            reactor.callLater(3.0, MobFight, self.id)

    def AttackChoice(self):
        global c
        mobid = (self.type,)
        c.execute('''SELECT * FROM MonsterAttacks WHERE ID=?''', mobid)
        fetch = c.fetchone()
        choice = random.randint(1, 2)
        if choice == 1:
            attack = str(fetch[1])
            minval = fetch[2]
            maxval = fetch[3]
            damage = random.randint(minval, maxval)
            self.Attack(damage, self.target, attack)
        if choice == 2:
            attack = str(fetch[4])
            minval = fetch[5]
            maxval = fetch[6]
            damage = random.randint(minval, maxval)
            self.Attack(damage, self.target, attack)

    def Attack(self, damage, target, attack):
        defence = float(target.defence)
        modifier = self.attack / defence
        if modifier < 0.5:
            modifier = 0.5
        modifier = damage * modifier
        damage = int(modifier)
        maxhit = 100 + target.dodge
        hit = random.randint(1, maxhit)
        if hit <= self.accuracy:
            if damage <= 0:
                glancechance = random.randint(1, 100)
                if glancechance <= 35:
                    self.MobTellRoom('glancing', 0)
                else:
                    damage = 1
            target.health = target.health - damage
            health = target.health
            if health <= 0:
                self.KillPlayer(target)
            else:
                self.MobTellRoom(attack, damage)
        else:
            self.MobTellRoom('miss', 0)

        #enter damage delt, if crit?, and the target player

    def TryFight(self):
        global c
        self.TargetPlayer()
        global userlist
        diction = userlist
        target = str(self.targetname)
        self.target = diction.get(target)
        target = self.target
        if target == None:
            return
        targetroom = target.room
        if targetroom != self.room:
            self.DropThreat(target)
        else:
            self.AttackChoice()

    def MobTellRoom(self, attack, damage):
        global c
        global userlist
        diction = userlist
        target = self.target
        room = self.room
        room = (room,)
        attack = str(attack)
        damage = str(damage)
        name = str(self.name)
        targetname = str(self.targetname)
        c.execute('''SELECT * FROM RoomPlayers where ID=?''', room)
        test = c.fetchone()
        count = 1
        if attack == 'miss':
            while(count <= 20):
                teststr = test[count]
                teststr = str(teststr)
                if teststr in('', None):
                    count = count + 1
                else:
                    if teststr == targetname:
                        diction = userlist
                        target = str(teststr)
                        target = diction.get(target)
                        line = "%s missed you!" % (name)
                        count = count + 1
                        target.sendLine(line)
                    else:
                        diction = userlist
                        target = str(teststr)
                        target = diction.get(target)
                        count = count + 1
                        line = "%s missed %s" % (name, targetname)
                        target.sendLine(line)
        if self.stun == 'True':
            while(count <= 20):
                teststr = test[count]
                teststr = str(teststr)
                if teststr in('', None):
                    count = count + 1
                else:
                    diction = userlist
                    target = str(teststr)
                    target = diction.get(target)
                    count = count + 1
                    line = "%s is stunned" % (name)
                    target.sendLine(line)
        if attack == 'glancing':
            while(count <= 20):
                teststr = test[count]
                teststr = str(teststr)
                if teststr in('', None):
                    count = count + 1
                else:
                    if teststr == targetname:
                        diction = userlist
                        target = str(teststr)
                        target = diction.get(target)
                        line = "The %s attacked you but the attack glanced off your armor!" % (name)
                        count = count + 1
                        target.sendLine(line)
                    else:
                        diction = userlist
                        target = str(teststr)
                        target = diction.get(target)
                        count = count + 1
                        line = "%s's attack glanced off %s's armor" % (name, targetname)
                        target.sendLine(line)
        else:
            while(count <= 20):
                teststr = test[count]
                teststr = str(teststr)
                if teststr in('', None):
                    count = count + 1
                else:
                    if teststr == self.targetname:
                        diction = userlist
                        target = str(teststr)
                        target = diction.get(target)
                        health = target.health
                        line = "%s hit you with a %s for %s damage!" % (name, attack, damage)
                        count = count + 1
                        target.sendLine(line)
                        line = "Health : %s" % health
                        target.sendLine(line)
                    else:
                        diction = userlist
                        target = str(teststr)
                        target = diction.get(target)
                        count = count + 1
                        line = "%s hit %s with %s for %s damage" % (name, self.targetname, attack, damage)
                        target.sendLine(line)

    def DropThreat(self, target):
        global c
        target = target
        c.execute('''SELECT * FROM MonsterThreat WHERE RandomID=?''', (self.id,))
        fetch = c.fetchone()
        var1 = str(fetch[1])
        var2 = str(fetch[3])
        var3 = str(fetch[5])
        var4 = str(fetch[7])
        var5 = str(fetch[9])
        var6 = str(fetch[11])
        count = 1
        targets = {1: var1, 2: var2, 3: var3, 4: var4, 5: var5, 6: var6}
        while count <= 6:
            name = targets[count]
            if name == target.name:
                count2 = count
                count = 7
            else:
                count = count + 1
        count3 = count2 * 2
        threat = int(fetch[count3])
        threat = threat - 10
        if threat == 0:
            column = "'Player" + str(count2) + "'"
            column2 = "'Threat" + str(count2) + "'"
            c.execute("UPDATE MonsterThreat SET " + column + "=?, " + column2 +"=? WHERE RandomID=?", ('', 0, self.id))
            conn.commit()
        else:
            column = "'Threat" + str(count2) + "'"
            c.execute("UPDATE MonsterThreat SET " + column + "=? WHERE RandomID=?", (threat, self.id))
            conn.commit()
            self.TryFight()

    def KillPlayer(self, target):
        # Kills player and sends back to spawn
        target = target
        name = target.name
        mobname = str(self.name)
        target.room = 1
        target.state = "DEAD"
        line = "You were killed by %s. You were sent back to your most recent checkpoint..." % (mobname)
        target.sendLine(line)
        target.sendLine("Hit enter to respawn")
        target.health = target.maxhealth
        target.mana = target.maxmana
        self.updateRoom(target)
        # Removes player from the mobs threat table...
        global c
        c.execute('''SELECT * FROM MonsterThreat WHERE RandomID=?''', (self.id,))
        fetch = c.fetchone()
        var1 = str(fetch[1])
        var2 = str(fetch[3])
        var3 = str(fetch[5])
        var4 = str(fetch[7])
        var5 = str(fetch[9])
        var6 = str(fetch[11])
        count = 1
        targets = {1: var1, 2: var2, 3: var3, 4: var4, 5: var5, 6: var6}
        while count <= 6:
            name = targets[count]
            if name == target.name:
                count2 = count
                count = 7
            else:
                count = count + 1
        column = "'Player" + str(count2) + "'"
        column2 = "'Threat" + str(count2) + "'"
        c.execute("UPDATE MonsterThreat SET " + column + "=?, " + column2 +"=? WHERE RandomID=?", ('', 0, self.id))
        conn.commit()
        print target.name, "was killed"

    def updateRoom(self, target):
        global c
        global userlist
        diction = userlist
        room = self.room
        roomc = (room,)
        c.execute('''SELECT * FROM RoomPlayers WHERE ID=?''', roomc)
        test = c.fetchone()
        if test is None:
            target.room = self.room
            print self.id, "had trouble killing", target.name, ". Didn't kill or move to spawn'"
            return
        counter = 1
        while counter <= 20:
            if test[counter] not in('', None, 'None'):
                counter = counter + 1
            else:
                lastroom = target.lastroom
                last = (lastroom,)
                c.execute('''SELECT * FROM RoomPlayers where ID=?''', last)
                test = c.fetchone()
                count = 1
                while(count <= 20):
                    teststr = test[count]
                    teststr = str(teststr)
                    if teststr in('', None):
                        count = count + 1
                    else:
                        if teststr == target.name:
                            pass
                            count = count + 1
                        else:
                            name = teststr
                            count = count + 1
                            name = str(name)
                            atk = diction.get(name)
                            atk.sendLine("%s has been slain by %s" % (target.name, self.name))
                column = "'Slot" + str(target.placement) + "'"
                c.execute("UPDATE RoomPlayers SET " + column + "=? WHERE ID=?", ('', self.room))
                conn.commit()
                room = 1
                c.execute('''SELECT * FROM RoomPlayers where ID=?''', (room,))
                test = c.fetchone()
                count = 1
                while(count <= 20):
                    teststr = test[count]
                    teststr = str(teststr)
                    if teststr in('', None):
                        count = count + 1
                    else:
                        if teststr == self.name:
                            pass
                            count = count + 1
                        else:
                            name = teststr
                            count = count + 1
                            name = str(name)
                            atk = diction.get(name)
                            atk.sendLine("%s has respawned" % (target.name))
                column = "'Slot" + str(counter) + "'"
                c.execute("UPDATE RoomPlayers SET " + column + "=? WHERE ID=?", (target.name, room))
                target.lastroom = room
                target.placement = counter
                target.room = room
                c.execute("SELECT * FROM RoomExits WHERE ID=?", (target.room,))
                fetch = c.fetchone()
                target.xcoord = str(fetch[10])
                target.ycoord = str(fetch[11])
                if target.room in (1,2,3,4,5,6,7,8,9,10,11,12):
                    target.regionname = 'Exordior'
                if target.room in (13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29):
                    target.regionname = 'Exordior Cave'
                conn.commit()
                counter = 30
#        else:
#            print "Room is full, please try again later"
        conn.commit()

    def TargetPlayer(self):
        global c
        c.execute('''SELECT * FROM MonsterThreat WHERE RandomID=?''', (self.id,))
        fetch = c.fetchone()
        var1 = int(fetch[2])
        var2 = int(fetch[4])
        var3 = int(fetch[6])
        var4 = int(fetch[8])
        var5 = int(fetch[10])
        var6 = int(fetch[12])
        count = 1
        count2 = 2
        target = {1: var1, 2: var2, 3: var3, 4: var4, 5: var5, 6: var6}
        while count2 <= 6:
            highest = target[count]
            compared = target[count2]
            if highest >= compared:
                count2 += 1
            else:
                count = count2
                count2 += 1
        if highest == 0:
            return
        if count == 1:
            self.targetname = str(fetch[1])
        if count == 2:
            self.targetname = str(fetch[3])
        if count == 3:
            self.targetname = str(fetch[5])
        if count == 4:
            self.targetname = str(fetch[7])
        if count == 5:
            self.targetname = str(fetch[9])
        if count == 6:
            self.targetname = str(fetch[11])


class DayNight():

    def __init__(self):
        global c
        c.execute('''SELECT * From ServerTime''')
        fetch = c.fetchone()
        self.minute = int(fetch[1])
        self.hour = int(fetch[2])
        self.night = bool(fetch[3])
        self.day = int(fetch[4])
        self.month = int(fetch[5])
        self.Time()
        c.execute('''UPDATE ServerTime SET Minutes=?, Hours=?, Night=?, Day=?, Month=? WHERE Server='Server' ''', (self.minute, self.hour, self.night, self.day, self.month))
        conn.commit()

    def Time(self):
        currentmin = self.minute
        rate = 1
        newmin = currentmin + rate
        if newmin >= 60:
            self.hour += 1
            if self.hour == 6:
                if self.night == True:
                    self.AlmostDay()
                else:
                    self.AlmostNight()
            if self.hour == 8:
                if self.night == True:
                    self.Day()
                else:
                    self.Night()
            if self.hour >= 13:
                if self.night == True:
                    self.day += 1
                    if self.day >= 31:
                        self.month += 1
                        self.day = 1
                self.hour -= 12
            newmin = newmin - 60
            self.minute = newmin
        else:
            self.minute = newmin

    def Night(self):
        self.night = True
        global userlist
        diction = userlist
        for key, value in diction.iteritems():
            player = diction.get(key)
            player.sendLine("##TIME## : It is now night time")
        print "It is now Night"

    def AlmostNight(self):
        global userlist
        diction = userlist
        for key, value in diction.iteritems():
            player = diction.get(key)
            player.sendLine("##TIME## : It is starting to get dark...")

    def Day(self):
        self.night = False
        global userlist
        diction = userlist
        for key, value in diction.iteritems():
            player = diction.get(key)
            player.sendLine("##TIME## : It is now day time")
        print "It is now Day"

    def AlmostDay(self):
        global userlist
        diction = userlist
        for key, value in diction.iteritems():
            player = diction.get(key)
            player.sendLine("##TIME## : The sun begins to rise")

LocalTime()
print localtime, "Server Started at localhost on Port : 8123"
timer = task.LoopingCall(DayNight)
timer.start(4.0)
l = task.LoopingCall(MobSpawner)
l.start(10.0)
reactor.listenTCP(8123, ChatFactory())
reactor.run()

def EmptyRooms():
    global c
    count10 = 1
    while count10 <= 1000:
        room = count10
        roomc = (room,)
        c.execute('''SELECT * FROM RoomPlayers WHERE ID=?''', roomc)
        test = c.fetchone()
        if test is None:
            count10 = 10000
        else:
            counter = 1
            while counter <= 20:
                if test[counter] in('', None, 'None'):
                    counter += 1
                else:
                    column = "'Slot" + str(counter) + "'"
                    c.execute("UPDATE RoomPlayers SET " + column + "=? WHERE ID=?", ('', room))
                    conn.commit()
                    counter += 1
        count10 += 1

print "Server has been stopped!"
print "Window will close in 3 seconds"
EmptyRooms()
conn.commit()
Databasecreate2.Import()
time.sleep(3)
sys.exit()