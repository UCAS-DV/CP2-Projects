from datetime import datetime

def get_timestamp():
    now = datetime.now()

    return(f'{now.month}/{now.day}/{now.year} - {now.hour}:{now.minute}')