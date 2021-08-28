# import sqlite3
# con = sqlite3.connect('chinook.db')
#
# def  dict_factory(cursor,row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d
#
# con.row_factory = dict_factory
#
#
# cur = con.cursor()
# sql_query = '''
# SELECT * FROM customers;
# '''
#
# cur.execute(sql_query)
# customers = cur.fetchall()
# con.close()
# #
# for customer in customers:
#     print(customer['CustomersId'], customer['FirstName'], customer['LastName'])


class ContactUs:
    def __init__(self, first_name, last_name, phone, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.mail = mail

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_contact_info(self):
        return f'{self.phone} {self.mail}'


class Rate:
    def __init__(self, sale, buy, created, source, currency_type):
        self.sale = sale
        self.buy = buy
        self.created = created
        self.source = source
        self.currency_type = currency_type

    def get_rate_list(self):
        return f'{self.sale} {self.buy} {self.source} {self.currency_type} {self.created}'