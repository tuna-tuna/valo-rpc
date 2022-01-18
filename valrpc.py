from valclient.client import Client
import psutil
from pypresence import Presence
import time
import ctypes

class Color:
	BLACK          = '\033[30m'
	RED            = '\033[31m'
	GREEN          = '\033[32m'
	YELLOW         = '\033[33m'
	BLUE           = '\033[34m'
	MAGENTA        = '\033[35m'
	CYAN           = '\033[36m'
	WHITE          = '\033[37m'
	COLOR_DEFAULT  = '\033[39m'
	BOLD           = '\033[1m'
	UNDERLINE      = '\033[4m'
	INVISIBLE      = '\033[08m'
	REVERCE        = '\033[07m'
	BG_BLACK       = '\033[40m'
	BG_RED         = '\033[41m'
	BG_GREEN       = '\033[42m'
	BG_YELLOW      = '\033[43m'
	BG_BLUE        = '\033[44m'
	BG_MAGENTA     = '\033[45m'
	BG_CYAN        = '\033[46m'
	BG_WHITE       = '\033[47m'
	BG_DEFAULT     = '\033[49m'
	RESET          = '\033[0m'

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
hWnd = kernel32.GetConsoleWindow()
kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100)) #disable inputs to console
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7) #allow for ANSI sequences
ctypes.windll.kernel32.SetConsoleTitleW(f"Valorant Discord Status Ver.0.1")
print('Valorant Discord Status Ver.0.1\n')
launchState = False
discordState = False
valorantState = False
termFlag = False
discordProcess = ["Discord.exe"]
valorantProcess = ["VALORANT-Win64-Shipping.exe", "RiotClientServices.exe"]
processes = []
for proc in psutil.process_iter():
    processes.append(proc.name())
discordState = set(discordProcess).issubset(processes)
valorantState = set(valorantProcess).issubset(processes)
if discordState == False:
    print(f'Please launch {Color.CYAN}Discord{Color.RESET} before using this tool.')
    termFlag = True
if valorantState == False:
    print(f'Please launch {Color.RED}Valorant{Color.RESET} before using this tool.')
    termFlag = True
if discordState == True and valorantState == True:
    launchState = True

if termFlag == True:
    print('Press any key to exit.')
    input()
    exit()

def convertMapId(mapId: str):
    map = ""
    if mapId == "/Game/Maps/Ascent/Ascent":
        map = "Ascent"
    elif mapId == "/Game/Maps/Bonsai/Bonsai":
        map = "Split"
    elif mapId == "/Game/Maps/Canyon/Canyon":
        map = "Fracture"
    elif mapId == "/Game/Maps/Duality/Duality":
        map = "Bind"
    elif mapId == "/Game/Maps/Foxtrot/Foxtrot":
        map = "Breeze"
    elif mapId == "/Game/Maps/Port/Port":
        map = "Icebox"
    elif mapId == "/Game/Maps/Triad/Triad":
        map = "Haven"
    return map

def convertCharaId(charaId: str):
    chara = ""
    if charaId == "5f8d3a7f-467b-97f3-062c-13acf203c006":
        chara = "Breach"
    elif charaId == "f94c3b30-42be-e959-889c-5aa313dba261":
        chara = "Raze"
    elif charaId == "22697a3d-45bf-8dd7-4fec-84a9e28c69d7":
        chara = "Chamber"
    elif charaId == "601dbbe7-43ce-be57-2a40-4abd24953621":
        chara = "KAY/O"
    elif charaId == "6f2a04ca-43e0-be17-7f36-b3908627744d":
        chara = "Skye"
    elif charaId == "117ed9e3-49f3-6512-3ccf-0cada7e3823b":
        chara = "Cypher"
    elif charaId == "ded3520f-4264-bfed-162d-b080e2abccf9" or charaId == "320b2a48-4d9b-a075-30f1-1f93a9b638fa":
        chara = "Sova"
    elif charaId == "1e58de9c-4950-5125-93e9-a0aee9f98746":
        chara = "Killjoy"
    elif charaId == "707eab51-4836-f488-046a-cda6bf494859":
        chara = "Viper"
    elif charaId == "eb93336a-449b-9c1b-0a54-a891f7921d69":
        chara = "Phoenix"
    elif charaId == "41fb69c1-4189-7b37-f117-bcaf1e96f1bf":
        chara = "Astra"
    elif charaId == "9f0d8ba9-4140-b941-57d3-a7ad57c6b417":
        chara = "Brimstone"
    elif charaId == "bb2a4828-46eb-8cd1-e765-15848195d751":
        chara = "Neon"
    elif charaId == "7f94d92c-4234-0a36-9646-3a87eb8b5c89":
        chara = "Yoru"
    elif charaId == "569fdd95-4d10-43ab-ca70-79becc718b46":
        chara = "Sage"
    elif charaId == "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc":
        chara = "Reyna"
    elif charaId == "8e253930-4c05-31dd-1b6c-968525494517":
        chara = "Omen"
    elif charaId == "add6443a-41bd-e414-f6ad-e58d267f4e95":
        chara = "Jett"
    return chara

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
    valorantProcess = ["VALORANT-Win64-Shipping.exe", "RiotClientServices.exe"]
    for proc in psutil.process_iter():
        processes.append(proc.name())
    launchState = set(valorantProcess).issubset(processes)
    print(launchState)
    if launchState == True:
        try:
            data = client.fetch_presence()
            if data["sessionLoopState"] == "INGAME":
                if data["provisioningFlow"] != "ShootingRange":
                    map = convertMapId(data["matchMap"])
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
                    chara = convertCharaId(charaId)

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
                map = convertMapId(data["matchMap"])
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

