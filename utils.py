def pb_date_format(date_time):
    dt_format = "%Y-%m-%dT%H:%M:%SZ"
    return date_time.strftime(dt_format)


def bool_to_yesno(value, default=False):
    lookup = {
        True: 'yes',
        False: 'no',
    }
    return lookup.get(value, lookup.get(default, False))
