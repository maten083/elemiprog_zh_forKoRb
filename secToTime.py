def splitSec(sec):
    minuteDividor = 60
    hourDividor = minuteDividor * 60
    dayDividor = hourDividor * 24
    weekDividor = dayDividor * 7

    week = sec // weekDividor
    day = (sec - week * weekDividor) // dayDividor
    hour = (sec - week * weekDividor - day * dayDividor) // hourDividor
    minute = (sec - week * weekDividor - day * dayDividor - hour * hourDividor) // minuteDividor
    sec = (sec - week * weekDividor - day * dayDividor - hour * hourDividor - minute * minuteDividor)

    texts = []
    if week > 1:
        texts.append(str(week) + " weeks")
    elif week > 0:
        texts.append(str(week) + " week")

    if day > 1:
        texts.append(str(day) + " days")
    elif day > 0:
        texts.append(str(day) + " day")

    if hour > 1:
        texts.append(str(hour) + " hours")
    elif hour > 0:
        texts.append(str(hour) + " hour")

    if minute > 1:
        texts.append(str(minute) + " minutes")
    elif minute > 0:
        texts.append(str(minute) + " minute")

    if sec > 1:
        texts.append(str(sec) + " seconds")
    elif sec > 0:
        texts.append(str(sec) + " second")

    l = len(texts)
    if l == 0:
        return ""
    elif l == 1:
        return texts[0]
    else:
        last = texts.pop()
        return ", ".join(texts) + " and " + last

print(splitSec(14605261))