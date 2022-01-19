import psutil
from .colors import Color

class Processes:
    @staticmethod
    def checkStartup(launchState: bool):
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
        return launchState, termFlag

    @staticmethod
    def checkInLoop(launchState: bool):
        processes = []
        valorantProcess = ["VALORANT-Win64-Shipping.exe", "RiotClientServices.exe"]
        for proc in psutil.process_iter():
            processes.append(proc.name())
        launchState = set(valorantProcess).issubset(processes)
        return launchState