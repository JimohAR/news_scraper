from datetime import datetime as dt

months = {
    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "may": "05",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12"
}

months_rev = dict(zip(months.values(), months.keys()))

dayth ={
    1: "st",
    21: "st",
    31: "st",
    2: "nd",
    22: "nd",
    3: "rd",
    23: "rd"
}
    
dayth.update(zip(list(range(4, 21)), ["th"] * (21-4)))
dayth.update(zip(list(range(24, 31)), ["th"] * (31-24)))

def to_datetime(day, month, year, months_rep=months):
    new_day = ""
    for i in day:
        try:
            new_day += str(int(i))
        except ValueError:
            continue
    new_month = months_rep[month.lower()]

    date = dt.fromisoformat(f"{year}-{new_month}-{new_day}")
    return date

def to_datestr(date, months_rep=months_rev, dayth=dayth):
    new_day = f"{date.day:>02}" + dayth[date.day]
    new_month = months_rep[f"{date.month:>02}"]

    new_date = f"{new_day} {new_month} {date.year}"
    return new_date