from datetime import date, datetime

def age_calc(dob: date) -> int:
    today: datetime = datetime.today()
    age: int = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age