
def add_time(time, duration, day=False):
    days = {'Saturday': 0, 'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6}
    
    time_day = time.split()[0]
    halfday = time.split()[1]
    hour = int(time_day.split(':')[0])
    minutes = int(time_day.split(':')[1])

    if halfday == "PM":
        hour += 12

    duration_hr, duration_mins = duration.split(':')
    duration_hr = int(duration_hr)
    duration_mins = int(duration_mins)

    
    total_mins = minutes + duration_mins
    final_mins = total_mins % 60
    extra_hr = total_mins // 60
    total_hr = hour + duration_hr + extra_hr

    
    final_hr = (total_hr % 24) % 12

    if final_hr == 0:
        final_hr = 12
    final_hr = str(final_hr)

    total_day = (total_hr // 24)


    final_halfday = ""
    if (total_hr % 24) <= 11:
        final_halfday = "AM"
    else:
        final_halfday = "PM"

    final_mins = "{:02d}".format(final_mins)
    
    final_time = final_hr + ":" + final_mins + ' ' + final_halfday
    if day == False:
        if total_day == 0:
            return final_time
        if total_day == 1:
            return final_time + ' (next day)'
        return final_time + ' (' + str(total_day) + ' days later)'
    else:
        final_day = (days[day.lower().capitalize()] + total_day) % 7
        for i, j in days.items():
            if j == final_day:
                final_day = i
                break
        if total_day == 0:
            return final_time + ', ' + final_day
        if total_day == 1:
            return final_time + ', ' + final_day + ' (next day)'
        return final_time + ', ' + final_day + ' (' + str(
            total_day) + ' days later)'


    