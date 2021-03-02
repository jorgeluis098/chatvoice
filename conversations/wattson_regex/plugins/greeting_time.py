
from datetime import datetime

def time(*args):
    now = datetime.now()
    var=args[0]
    if now.hour < 12:
        return 'set_slot {0} "{1}"'.format(var,"Buenos días ¿que vas a hacer hoy?")
    elif  now.hour > 12  and now.hour < 18:
        return 'set_slot {0} "{1}"'.format(var,"Buenas tardes, ¿Como va tu dia?")
    else:
        return 'set_slot {0} "{1}"'.format(var,"Buenas noches ¿Como estuvo tu dia?") 


