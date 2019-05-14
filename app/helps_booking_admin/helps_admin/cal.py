from calendar import HTMLCalendar
from helps_admin.models import Session


class Calendar(HTMLCalendar):
    def __init__(self, day=None, year=None, month=None):
        self.day = day
        self.year = year
        self.month = month
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
            if day == self.day:
                day_render = day_render.replace('date\'>', 'date\'><u>').replace('</span>', '</u></span>')
                
                # print (day_render)
                    
            # if len(sessions_per_day) > 0:
            #     day_render = day_render.replace('<td', '<td ')
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
    def formatmonth(self, withyear=True):
        # filter sessions by year and month
        sessions = Session.objects.filter(session_time__year=self.year, session_time__month=self.month)
        
        cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, sessions)}\n'
        return cal
