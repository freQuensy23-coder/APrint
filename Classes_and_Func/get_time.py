import datetime

def get_time():
    # Returns smth. like this: "12:00" or "02:51"
    return str(datetime.datetime.now().time())[0:5]
