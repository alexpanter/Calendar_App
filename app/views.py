import time
from datetime import date, datetime

from app import app, models
from models import Task
from flask import render_template

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/<y>')
def year_page(y):
    weeks = [w for w in range(
        1,date(int(y),12,28).isocalendar()[1] + 1)]
    return render_template(
        'year.html',
        year=y,
        weeks=weeks
    )


@app.route('/<y>/week=<w>')
def week_page(y,w):
    # failcheck for wrong year
    if int(y) < 2016 or int(y) > 2099:
        return render_template('pageNotFound.html')
    # failcheck for wrong week
    elif int(w) < 0 or int(w) > 53:
        return render_template('pageNotFound.html')
   # everything is okay 
    else:
        weeks = [str(wk) for wk in range(
            1,date(int(y),12,28).isocalendar()[1] + 1)]
        mon = datetime.strptime(y + '-W' + w + '-1', '%Y-W%W-%w').date()
        tue = datetime.strptime(y + '-W' + w + '-2', '%Y-W%W-%w').date()
        wed = datetime.strptime(y + '-W' + w + '-3', '%Y-W%W-%w').date()
        thu = datetime.strptime(y + '-W' + w + '-4', '%Y-W%W-%w').date()
        fri = datetime.strptime(y + '-W' + w + '-5', '%Y-W%W-%w').date()
        sat = datetime.strptime(y + '-W' + w + '-6', '%Y-W%W-%w').date()
        sun = datetime.strptime(y + '-W' + w + '-0', '%Y-W%W-%w').date()
        mon_t = []
        tue_t = []
        wed_t = []
        thu_t = []
        fri_t = []
        sat_t = []
        sun_t = []
        for task in Task.query.all():
            start = task.start.date()
            if start == mon:
                mon_t.append(task)
            elif start == tue:
                tue_t.append(task)
            elif start == wed:
                wed_t.append(task)
            elif start == thu:
                thu_t.append(task)
            elif start == fri:
                fri_t.append(task)
            elif start == sat:
                sat_t.append(task)
            elif start == sun:
                sun_t.append(task)
        return render_template(
            'week.html',
            year=y,
            week=w,
            weeks=weeks,
            previous_week=str(int(w) - 1),
            next_week=str(int(w) + 1),
            mon_t=mon_t,
            tue_t=tue_t,
            wed_t=wed_t,
            thu_t=thu_t,
            fri_t=fri_t,
            sat_t=sat_t,
            sun_t=sun_t
        )

@app.route('/today')
def today_page():
    calendar = date.today().isocalendar()
    today = date.today()
    year = calendar[0]
    week = calendar[1]
    day = calendar[2]
    tasks = [task for task in Task.query.all() if
             task.start.date() == today]

    return render_template(
        'day.html',
        calendar=calendar,
        today=today,
        tasks=tasks
    )

@app.errorhandler(404)
def notFound_page(err):
    return render_template('pageNotFound.html'), 404
