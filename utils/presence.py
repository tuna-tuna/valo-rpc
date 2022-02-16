from pypresence import Presence
from .colors import Color

class valPresence:
    @staticmethod
    def updatePresence(rpc: Presence,details = None, state = None, large_img = None, large_text = None, small_img = None, small_text = None):
        try:
            rpc.update(details=details,state=state,large_image=large_img,large_text=large_text,small_image=small_img,small_text=small_text)
        except Exception as e:
            print(f"{Color.RED}Something wrong occured while updating DiscordRPC.\nPlease send the traceback below to the developer.")
            print(str(e))
