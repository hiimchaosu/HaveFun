import random
import datetime
import calendar
from mcstatus import JavaServer

event_days = []

def rngLevel():
    RNGCreate = random.randint(0, 100)
    RNGOption = [0, 1, 2, 3, 4]
    if RNGCreate <= 20:
        return RNGOption[0], RNGCreate
    elif 20 < RNGCreate < 60:
        return RNGOption[1], RNGCreate
    elif 60 <= RNGCreate <= 95:
        return RNGOption[2], RNGCreate
    elif 96 <= RNGCreate <= 99:
        return RNGOption[3], RNGCreate
    else:
        return RNGOption[4], RNGCreate

def daysLeftToMatura():
    current_date = datetime.date.today()
    target_date = datetime.date(2022, 5, 4)
    days_left = target_date - current_date
    return days_left

def get_date_info():
    """Returns today's date in multiple formats."""
    date = datetime.date.today()
    today = date.today()
    return {
        "day": today.strftime("%d"),
        "month": today.strftime("%m"),
        "month_name": today.strftime("%B"),
        "year": today.strftime("%Y"),
        "monthDays": calendar.monthrange(int(today.strftime("%Y")), int(today.strftime("%m")))[1]
    }

def calendarEvents():
    return event_days

def calendarEventsAdd(number):
    event_days.append(number)

def testPurposes():
    pass

def get_mc_server_info(host: str, port: str):
    try:
        server = JavaServer.lookup(f"{host}:{port}")
        status = server.status()

        players = status.players.online
        max_players = status.players.max
        motd = status.description
        latency = status.latency
        tps = getattr(status, "tps", "N/A")

        player_list = []
        if status.players.sample:
            player_list = [player.name for player in status.players.sample]

        return {
            "online": True,
            "players_online": players,
            "max_players": max_players,
            "motd": motd,
            "latency": latency,
            "tps": tps,
            "players": player_list
        }
    except Exception:
        return {"online": False}