import doctest



def get_earliest(*args):
    earliest_in_days = 99999999
    earliest_date = ""

    for i in args:
        (m, d, y) = i.split('/')
        in_days = int(y+m+d)

        if (in_days < earliest_in_days):
            earliest_date = i
            earliest_in_days = in_days

    return earliest_date


if __name__ == "__main__":
    print get_earliest("01/27/1832", "01/27/1756")
    print get_earliest("02/29/1972", "12/21/1946")
    print get_earliest("02/24/1946", "03/21/1946")
    print get_earliest("06/21/1958", "06/24/1958")
