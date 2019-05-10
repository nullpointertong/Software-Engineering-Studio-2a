from calendar import HTMLCalendar
from helps_admin.models import Session


class Calendar(HTMLCalendar):
    def __init__(self, day=None, year=None, month=None):
        self.day = day
        self.year = year
        self.month = month
        super().__init__()

    def formatday(self, day, sessions):
        sessions_per_day = sessions.filter(session_time__day=day)
        d = ''
        
        # for session in sessions_per_day:
        #     d += f'<li> {session.session_ID} </li>'

        if day != 0:
            day_render = """<td onclick="alert('You are clicking on {0}')">
    <span class='date'>{0}</span>
    <ul> {1} </ul>
</td>""".format(day, d)
            if day == self.day:
                day_render = day_render.replace('<td', '<td bgcolor="#ddddff"')
            if len(sessions_per_day) > 0:
                day_render = day_render.replace('<td', '<td ')
        else:
            day_render = '<td></td>'
        return day_render

    # formats the calendar by week
    def formatweek(self, theweek, sessions):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, sessions)
        return '<tr> {} </tr>'.format(week)

    # formats calendar by month
    def formatmonth(self, withyear=True):
        # filter sessions by year and month
        sessions = Session.objects.filter(session_time__year=self.year, session_time__month=self.month)
        
        cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, sessions)}\n'
        return cal
