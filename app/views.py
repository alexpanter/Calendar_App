import time
from datetime import date, datetime

from app import app, models, functions, db_tunnel, db
from models import Task
from flask import render_template, redirect, url_for, request


# error page, 404, any page that could not be loaded
@app.errorhandler(404)
def notFound_page(err):
    return render_template('pageNotFound.html'), 404


# index page
@app.route('/')
def index_page():
    return render_template('index.html')


# calendar main page
@app.route('/calendar')
def calendar_page():
    return render_template('calendar.html')


# tasks main page
@app.route('/tasks')
def tasks_page():
    return render_template('tasks.html')


@app.route('/<y>')
def year_page(y):
    try:
        weeks = functions.generate_weeks(y)
        # weeks = [w for w in range(
        #     1, date(int(y), 12, 28).isocalendar()[1] + 1)]
        return render_template(
            'year.html',
            year=y,
            weeks=weeks
        )
    except:
        return notFound_page("not found")


@app.route('/<y>/week=<w>')
def week_page(y, w):
    # failcheck for wrong year
    if int(y) < 2016 or int(y) > 2099:
        return render_template('pageNotFound.html')
    # failcheck for wrong week
    elif int(w) < 0 or int(w) > 53:
        return render_template('pageNotFound.html')
    # everything is okay
    else:
        # weeks = [str(wk) for wk in range(
        #     1, date(int(y), 12, 28).isocalendar()[1] + 1)]
        weeks = functions.generate_weeks(y)
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
        for task in Task.query.order_by(Task.start.asc()).all():
            start = task.start.date()
            if start == mon:
                mon_t.append(task)
                # j = functions.append_sorted(mon_t, task)
                # mon_t.insert(j, task)
            elif start == tue:
                tue_t.append(task)
                # functions.append_sorted(tue_t, task)
            elif start == wed:
                wed_t.append(task)
                # functions.append_sorted(wed_t, task)
            elif start == thu:
                thu_t.append(task)
                # functions.append_sorted(thu_t, task)
            elif start == fri:
                fri_t.append(task)
                # functions.append_sorted(fri_t, task)
            elif start == sat:
                sat_t.append(task)
                # functions.append_sorted(sat_t, task)
            elif start == sun:
                sun_t.append(task)
                # j = functions.append_sorted(sun_t, task)
                # sun_t.insert(j, task)

        return render_template(
            'week.html',
            year=y,
            week=w,
            weeks=weeks,
            previous_week=str(int(w) - 1),
            next_week=str(int(w) + 1),
            functions=functions,
            days=[mon, tue, wed, thu, fri, sat, sun],
            tasks=[mon_t, tue_t, wed_t, thu_t, fri_t, sat_t, sun_t]
        )


@app.route('/redirect_thisweek')
def this_week():
    dt = datetime.now()
    y = str(dt.year)
    w = str(dt.isocalendar()[1])
    return redirect('http://localhost:3000/' + y + '/week=' + w)


@app.route('/today')
def today_page():
    calendar = date.today().isocalendar()
    today = date.today()
    # year = calendar[0]
    # week = calendar[1]
    # day = calendar[2]
    tasks = [task for task in Task.query.all() if
             task.start.date() == today]

    return render_template(
        'day.html',
        calendar=calendar,
        today=today,
        tasks=tasks
    )


@app.route('/calendar_task/<id>')
def calendar_task(id):
    task = Task.query.get(id)
    year = task.start.date().isocalendar()[0]
    week = task.start.date().isocalendar()[1]
    weeks = functions.generate_weeks(year)
    return render_template('calendar_task.html',
                           task=task,
                           weeks=weeks,
                           year=year,
                           week=week,
                           # modify_title=lambda (title, description):
                           #     db_tunnel.save_task(task, title, description))
                           save_task=db_tunnel.save_task)


@app.route('/calendar_task/<id>/save?y=<y>&w=<w>', methods=['GET', 'POST'])
def save_task(id, y, w):
    if request.method == 'POST':
        task = Task.query.get(id)

        new_title = request.form['title']
        new_description = request.form['description']

        new_start_date = request.form['start-date']
        new_start_hour = request.form['start-hour']
        new_start_minute = request.form['start-minute']
        new_start = new_start_date + ' ' + new_start_hour + ':' + new_start_minute

        new_stop_date = request.form['stop-date']
        new_stop_hour = request.form['stop-hour']
        new_stop_minute = request.form['stop-minute']
        new_stop = new_stop_date + ' ' + new_stop_hour + ':' + new_stop_minute

        task.title = new_title
        task.description = new_description
        task.start = datetime.strptime(new_start, '%Y-%m-%d %H:%M')
        task.stop = datetime.strptime(new_stop, '%Y-%m-%d %H:%M')

        # db.session.add(<some_new_Task>)
        db.session.commit()  # store in database
    return redirect('/' + y + '/week=' + w)


@app.route('/calendar_task/<id>/delete?y=<y>&w=<w>', methods=['GET', 'POST'])
def delete_task(id, y, w):
    if request.method == 'POST':
        task = Task.query.get(id)

        # do something to delete this task!
        db.session.delete(task)

        db.session.commit()
    return redirect('/' + y + '/week=' + w)


# @app.route(...)
# def create_new_task(<some_params>):
#     task = Task()
#     ... set task parameters ...
#
#     db.session.add(task)
#     db.session.commit()
#     return ""
