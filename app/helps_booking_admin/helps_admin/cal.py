from calendar import HTMLCalendar
from helps_admin.models import Session
from datetime import datetime


class Calendar(HTMLCalendar):
    def __init__(self, day=None, year=None, month=None):
        self.day = day
        self.year = year
        self.month = month
        self.today = datetime.today()
        super().__init__()

    def formatday(self, day, month, year, sessions):
        # sessions_per_day = sessions.filter(session_time__year=year).filter(session_time__month=month).filter(session_time__day=day)
        # for session in sessions_per_day:
        #     d += f'<li> {session.session_ID} </li>'

        if day != 0:
            formatted_date = "%04d-%02d-%02d" % (year, month, day)
            day_render = """<td id="{0}" onclick="selectDate('{0}');">
    <span class='date'>{1}</span>
</td>""".format(formatted_date, day)
            if day == self.day and month == self.month and year == self.year:
                day_render = day_render.replace('<td ', '<td onload="selectedDate=this;" style="background-color:#a7bdf5;" ')
            if day == self.today.day and month == self.today.month and year == self.today.year:
                day_render = day_render.replace('date\'>', 'date\'><u>').replace('</span>', '</u></span>')
                # print (day_render)
        else:
            day_render = '<td></td>'
        return day_render

    # formats the calendar by week
    def formatweek(self, theweek, sessions):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, self.month, self.year, sessions)
        return '<tr> {} </tr>'.format(week)

    # formats calendar by month
    def formatmonth(self, withyear=True, prev_month=None, next_month=None):
        # filter sessions by year and month
        sessions = Session.objects.filter(start_time__year=self.year, start_time__month=self.month) # session_time -> start_time
        
        cal = '<table id="calendar" border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        month_row = f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        # <tr><th colspan="5" class="month">May 2019</th></tr>
        month_row = month_row.replace('colspan="7"', 'colspan="5"')
        if prev_month:
            month_row = month_row.replace('<tr>', '<tr><td class="calendar td"><a href="/create_session?{}" style="display:block;height=100%;"> < </a></td>'.format(prev_month)).replace('</tr>', '<td class="calendar td"><a href="/create_session?{}" style="display:block;height=100%;"> > </a></td></tr>'.format(next_month))
        cal += month_row
        # print(month_row)
        
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, sessions)}\n'
        return cal

    def new_date(self, y, m, d):
        self.day = d
        self.month = m
        self.year = y
        return self