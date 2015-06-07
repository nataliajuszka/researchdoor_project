import time
import calendar
from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf

from calen.forms import EntryForm
from calen.models import Entry


mnames = "January February March April May June July August September October November December"
mnames = mnames.split()



def month(request, year=0, month=13, change=None):

    now=datetime.now()

    if(year==0):
        year=now.year
    if(month==13):
        month=now.month

    year, month = int(year), int(month)

    # apply next / previous change
    if change in ("next", "prev"):
        now, mdelta = date(year, month, 15), timedelta(days=31)
        if change == "next":   mod = mdelta
        elif change == "prev": mod = -mdelta

        year, month = (now+mod).timetuple()[:2]

    # init variables
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    nyear, nmonth, nday = time.localtime()[:3]
    lst = [[]]
    week = 0

    # make month lists containing list of days for each week
    # each day tuple will contain list of entries and 'current' indicator
    for day in month_days:
        entries = current = False   # are there entries for this day; current day?
        if day:
            entries = Entry.objects.filter(Q(date__year=year, date__month=month, date__day=day,is_weekly=False) | Q(date__day=day%7,is_weekly=True))

            if day == nday and year == nyear and month == nmonth:
                current = True

        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    return render_to_response("month.html", dict(year=year, month=month, user=request.user,
                        month_days=lst, mname=mnames[month-1]))

@login_required
def add_entry(request):
    if request.POST:
        form = EntryForm(request.POST)
        if form.is_valid():
                entry = Entry(title=form.cleaned_data['title'], start_time=form.cleaned_data['start_time'], end_time=form.cleaned_data['end_time'], date=form.cleaned_data['date'], person=request.user, is_weekly=form.cleaned_data['is_weekly'])
                entry.save()
                return HttpResponseRedirect('/month')
    else:
        form = EntryForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('add_entry.html', args)