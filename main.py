import restaurant
import table
import notificator
import datetime

new_rest = restaurant.Restaurant(name="Leto")
new_table = table.Table(seats_capacity=2, shape='Rectangular', coordinates=(50, 30), dimensions=(20, 10))
new_notificator = notificator.Notificator(name="Hostess")
new_rest.add_table(new_table, 1)
iter_tables = new_rest.get_tables()
for table in iter_tables:
    print(table)
reservation_date = datetime.date(year=2018, month=5, day=17)
new_table.reserve(date=reservation_date, notificator=new_notificator, name="John", email="john@gmail.com")
new_table.check_availability(date=reservation_date, notificator=new_notificator)
new_table.cancel_reserve(reservation_date)
new_table.check_availability(date=reservation_date, notificator=new_notificator)



