import time
from datetime import date, datetime


def datetime_to_string(dt):
    hour = str(dt.hour)
    minute = str(dt.minute)

    if dt.hour < 10:
        hour = '0' + str(dt.hour)
    if dt.minute < 10:
        minute = '0' + str(dt.minute)

    return "%s:%s" % (hour, minute)


def timespan_to_string(dt1, dt2):
    return "%s - %s" % (datetime_to_string(dt1),
                        datetime_to_string(dt2))


def date_to_string(dt):
    return "%s %i." % (dt.strftime('%B'), dt.day)


def append_sorted(task_list, task):
    cnt = task_list.__len__()
    j = 0
    for i in range(0, cnt):
        j = i
        # task should be inserted before current position
        if task.start.hour < task_list[i].start.hour:
            print(task.title, "HOUR <", task_list[i].title)
            break
        else:
            print("NOT TAKEN")
        # tasks have equal start hour, thus comparing start minute
        if task.start.hour == task_list[i].start.hour:
            print(task.title, "HOUR ==", task_list[i].title)
            if task.start.minute <= task_list[i].start.minute:
                print(task.title, "MINUTE <=", task_list[i].title)
                break
        else:
            print("NOT TAKEN")
    return j


def generate_weeks(year):
    return [w for w in range(1, date(int(year), 12, 28).isocalendar()[1] + 1)]

# TESTING
# datetime_to_string(datetime.now())

# print (timespan_to_string(datetime.now(), datetime(2016,8,16,0,42)))
