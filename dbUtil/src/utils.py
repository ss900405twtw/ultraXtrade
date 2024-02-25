import datetime
def get_today():
    return datetime.date.today()

def sub_N_Days(
        days#=1
        ,date=datetime.date.today()
        ):
    return date - datetime.timedelta(days)

def add_N_Days(
        days#=1
        ,date=datetime.date.today()
        ):
    return date + datetime.timedelta(days)