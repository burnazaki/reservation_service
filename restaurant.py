class Restaurant:

    def __init__(self, name):
        self.name = name
        self._tables = {}

    def get_tables(self, table=None):
        if table is not None and table in self._tables:
            yield {table.shape: self._tables[table]}
        else:
            for table in self._tables:
                yield {table.shape: self._tables[table]}

    def add_table(self, table, quantity):
        self._tables[table] = self._tables.get(table, 0) + quantity

    def remove_table(self, table, quantity):
        try:
            if quantity <= self._tables[table]:
                self._tables[table] -= quantity
            else:
                raise Exception('Not enough tables in the hall')
        except KeyError:
            raise KeyError('There are no such tables in the hall')