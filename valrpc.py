from valclient.client import Client
from pypresence import Presence
import time
import ctypes
from utils.processes import Processes
from utils.converter import Converter


kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
hWnd = kernel32.GetConsoleWindow()
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100)) #disable inputs to console
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7) #allow for ANSI sequences
ctypes.windll.kernel32.SetConsoleTitleW(f"Valorant Discord Status Ver.0.1")
print('Valorant Discord Status Ver.0.1\n')
launchState = False
launchState, termFlag = Processes.checkStartup(launchState=launchState)
if termFlag == True:
    print('Press any key to exit.')
    input()
    exit()

if launchState == True:
    client = Client(region="ap")
    client.activate()
    client_id = '932219902452977697'
    RPC = Presence(client_id=client_id)
    RPC.connect()

map = ""
score = ""
mode = ""
charaId = ""
chara = ""
largeimg = ""
largetext = ""
smallimg = ""
smalltext = ""
while True:
    launchState = Processes.checkInLoop(launchState=launchState)
    if launchState == True:
        try:
            data = client.fetch_presence()
            if data["sessionLoopState"] == "INGAME":
                if data["provisioningFlow"] != "ShootingRange":
                    map = Converter.convertMapId(data["matchMap"])
                    score = str(data["partyOwnerMatchScoreAllyTeam"]) + ' - ' + str(data["partyOwnerMatchScoreEnemyTeam"])
                    if data["provisioningFlow"] == "CustomGame":
                        mode = "Custom"
                    else:
                        if data["queueId"] == "newmap":
                            mode = "New Map"
                        elif data["queueId"] == "competitive":
                            mode = "Competitive"
                        elif data["queueId"] == "unrated":
                            mode = "Unrated"
                        elif data["queueId"] == "spikerush":
                            mode = "Spike Rush"
                        elif data["queueId"] == "deathmatch":
                            mode = "Deathmatch"
                        elif data["queueId"] == "ggteam":
                            mode = "Escalation"
                        elif data["queueId"] == "onefa":
                            mode = "Replication"
                        elif data["queueId"] == "snowball":
                            mode = "Snowball Fight"
                        else:
                            mode = "Custom"
                    myData = client.coregame_fetch_player()
                    puuid = myData["Subject"]
                    myMatchData = client.coregame_fetch_match()
                    for player in myMatchData["Players"]:
                        if player["Subject"] == puuid:
                            charaId = player["CharacterID"]
                            break
                    chara = Converter.convertCharaId(charaId)

                    details = mode + '  ' + score
                    state = "Map: " + map + " Agent: " + chara
                    largeimg = map.lower()
                    largetext = map
                    smallimg = chara.lower()
                    if chara == "KAY/O":
                        smallimg = "kayo"
                    smalltext = chara
                    RPC.update(details=details, state=state, large_image=largeimg, large_text=largetext, small_image=smallimg, small_text=smalltext)

            elif data["sessionLoopState"] == "MENUS":
                details = "In Menu"
                largeimg = "default"
                largetext = "In Menu"
                if data["isIdle"] == True:
                    largeimg = "away"
                    largetext = "AFK"
                    details = "AFK"
                RPC.update(details=details, large_image=largeimg, large_text=largetext)
            
            elif data["sessionLoopState"] == "PREGAME":
                map = Converter.convertMapId(data["matchMap"])
                if data["provisioningFlow"] == "CustomGame":
                        mode = "Custom"
                else:
                    if data["queueId"] == "newmap":
                        mode = "New Map"
                    elif data["queueId"] == "competitive":
                        mode = "Competitive"
                    elif data["queueId"] == "unrated":
                        mode = "Unrated"
                    elif data["queueId"] == "spikerush":
                        mode = "Spike Rush"
                    elif data["queueId"] == "deathmatch":
                        mode = "Deathmatch"
                    elif data["queueId"] == "ggteam":
                        mode = "Escalation"
                    elif data["queueId"] == "onefa":
                        mode = "Replication"
                    elif data["queueId"] == "snowball":
                        mode = "Snowball Fight"
                    else:
                        mode = "Custom"
                details = "PreGame  Mode: " + mode
                state = "Map: " + map
                largeimg = map.lower()
                largetext = map
                RPC.update(details=details, state=state, large_image=largeimg, large_text=largetext)

        except:
            continue

    else:
        RPC.clear()
    
    time.sleep(15)

