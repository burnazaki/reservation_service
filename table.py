class Table:
    _last_table_number = 0

    def __init__(self, seats_capacity, shape, coordinates, dimensions):
        Table._last_table_number += 1
        self.table_number = Table._last_table_number
        self.seats_capacity = seats_capacity
        self.shape = shape
        self.coordinates = coordinates
        self.dimensions = dimensions
        self.reserved_dates = {}

    def reserve(self, date, notificator, name, email):  # datetime module supposed to be used
        if self.reserved_dates[date] is True:
            raise Exception("Table is not available for required date")
        else:
            self.reserved_dates[date] = True
            notificator.send_email(receiver_email=email, name=name)

    def cancel_reserve(self, date):  # datetime module supposed to be used
        if self.reserved_dates[date] is False or date not in self.reserved_dates:
            raise Exception("Table has not been booked for the date")
        else:
            self.reserved_dates[date] = False

    def check_availability(self, date):  # datetime module supposed to be used
        if self.reserved_dates[date] is True:
            print("Reserved")
        else:
            print("Available")
