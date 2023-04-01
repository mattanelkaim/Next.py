from typing import Generator
import itertools

CURRENT_YEAR = 2023
SECS_IN_MINUTE, MINUTES_IN_HOUR, HOURS_IN_DAY, MONTHS_IN_YEAR = 60, 60, 24, 12
DAYS_IN_MONTH = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }


def gen_secs() -> Generator[int, int, None]:
    yield from itertools.cycle(range(SECS_IN_MINUTE))


def gen_minutes() -> Generator[int, int, None]:
    yield from itertools.cycle(range(MINUTES_IN_HOUR))


def gen_hours() -> Generator[int, int, None]:
    yield from itertools.cycle(range(HOURS_IN_DAY))


def gen_time() -> Generator[str, str, None]:
    seconds_gen, minutes_gen, hours_gen = gen_secs(), gen_minutes(), gen_hours()
    secs, minutes, hours = next(seconds_gen), next(minutes_gen), next(hours_gen)
    while True:
        yield "%02d:%02d:%02d" % (hours, minutes, secs)
        if secs == SECS_IN_MINUTE - 1:
            minutes = next(minutes_gen)
            if minutes == 0:  # Had just reset, new hour
                hours = next(hours_gen)
        secs = next(seconds_gen)


def gen_years(start: int = CURRENT_YEAR) -> Generator[int, int, None]:
    yield from itertools.count(start)


def gen_months() -> Generator[int, int, None]:
    yield from itertools.cycle(range(1, MONTHS_IN_YEAR + 1))


def gen_days(month: int, leap_year: bool = True) -> Generator[int, int, None]:
    # Calculate max days in current month
    if month == 2 and leap_year:
        max_days = 29
    else:
        max_days = DAYS_IN_MONTH[month]

    yield from itertools.cycle(range(1, max_days + 1))


def gen_date() -> Generator[str, str, None]:
    months_gen, years_gen, time_gen = gen_months(), gen_years(), gen_time()
    months, years, time = next(months_gen), next(years_gen), next(time_gen)
    is_leap_year = (years % 4 == 0 and years % 100 != 0) or years % 400 == 0
    days_gen = gen_days(months, is_leap_year)  # Updated for every month
    days = next(days_gen)

    while True:
        yield "%02d/%02d/%d %s" % (days, months, years, time)
        if time == "23:59:59":
            if days == DAYS_IN_MONTH[months]:  # Reached max
                months = next(months_gen)
                days_gen = gen_days(months, is_leap_year)  # Recreate for new month
                if months == 1:  # Had just reset, new year
                    years = next(years_gen)
                    # Recalculate leap year
                    is_leap_year = (years % 4 == 0 and years % 100 != 0) or years % 400 == 0
            days = next(days_gen)
        time = next(time_gen)


def main():
    my_date = gen_date()
    for _ in range(1_000_000):  # Calculates in seconds as input
        next(my_date)
    print(next(my_date))


if __name__ == '__main__':
    main()
