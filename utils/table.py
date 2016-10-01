from prettytable import PrettyTable


class Table(object):
    def __init__(self):
        pass

    @staticmethod
    def obj(data):
        # new a table
        table = PrettyTable()
        # define a row
        row = []
        # start for
        for key in data:
            table.field_names.append(key)
            row.append(data[key])
        table.add_row(row)
        # print it
        print table

    @staticmethod
    def ary(data):
        print data
