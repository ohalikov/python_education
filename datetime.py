import datetime
import time
state_date = {
    "user_time": {
        "hour": 15,
        "minute": 0,
        "text": "15:00",
        "time": 900
    },
    "question_time": 920,
    # "time_tickets": [480,520,580,880,700,1000,980,960,860,940]
    "time_tickets": None
}


if state_date.get("time_tickets", False):
    state_date["time_tickets"] = sorted(
        state_date["time_tickets"],
        key=lambda x: abs(x - state_date["user_time"]["time"])
    )
    state_date["time_tickets"].reverse()
    dt = datetime.timedelta(minutes=state_date["question_time"])
    print("NE LOX")
else:
    print("LOX")
#print(str(dt)[:-3])

# str(datetime.timedelta(minutes=state_date["question_time"]))

if state_date.get("time_tickets", False):
    state_date["time_tickets"] = sorted(
        state_date["time_tickets"],
        key=lambda x: abs(x["time"] - state_date["user_time"]["time"])
    )
    state_date["time_tickets"].reverse()
else:
    reaction("redirect")
    set_node()
    set_break()
    return