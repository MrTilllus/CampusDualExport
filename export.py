#!as3:/usr/local/lib/python2.7/site-packages# cat sitecustomize.py
# encoding=utf8
import os, sys

reload(sys)
sys.setdefaultencoding('utf8')

import json
from collections import namedtuple

import requests as rq
import datetime

from pprint import pprint


def export_to_ics(path, raw_request_string):

    response = rq.get(raw_request_string)
    #pprint(response.text)

    calendar_data = json.loads(response.text)

    calendar_header = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:0000
METHOD:PUBLISH"""

    calendar_footer = "END:VCALENDAR"

    ics_data = []

    for event in calendar_data:
        event = namedtuple("Employee", event.keys())(*event.values())

        subject = event.title
        teacher = event.sinstructor

        date_start = datetime.datetime.fromtimestamp(event.start)
        start_date = date_start.strftime('%y%m%d')
        start_time = date_start.strftime("%H%M")
        start_time_des = date_start.strftime("%H:%M")

        date_end = datetime.datetime.fromtimestamp(event.end)
        end_date = date_end.strftime('%y%m%d')
        end_time = date_end.strftime("%H%M")
        end_time_des = date_end.strftime("%H:%M")

        all_day_event = "False"
        description = event.description
        location = event.sroom
        loc_num = location.replace(".", "")

        if 'K' in loc_num:
            loc_ready = loc_num.replace("K", "")
        else:
            loc_ready = loc_num

        if location == "" or location == 'Unbekannt':
            uid = "UID:" + start_date + start_time + "0F4A" + end_date + end_time
        else:
            uid = "UID:" + start_date + start_time + loc_ready + end_date + end_time


        if 'Gr. 2' in subject:
            pass
        else:
            ics_data.append(
                "BEGIN:VEVENT\n" + uid +
"\nLOCATION:" + location +
"\nSUMMARY:" + subject +
"\nDESCRIPTION:" + start_time_des + " - " + end_time_des + "\\n" + location + "\\n" + teacher + "\\n" + description +
"\nDTSTART;TZID=Europe/Berlin:" + "20" + start_date + "T" + start_time + "00" +
"\nDTEND;TZID=Europe/Berlin:" + "20" + end_date + "T"+ end_time + "00" +
"\nEND:VEVENT" + "\n")

    with open(path, "w") as f:
        f.write(calendar_header + "\n")
        f.writelines(ics_data)
        f.write(calendar_footer)


if __name__ == '__main__':
    export_to_ics("./ioskalender.ics", "https://selfservice.campus-dual.de/room/json?userid=3003645&hash=120cc9f859896523607e8bbae270a4f3&start=1548630000&end=1549234800&_=1548671664260")
