#!/usr/bin/env python3

#
# read_db.py
#
# Copyright (c) 2017 Franco Masotti
#
# See the LICENSE file.
#

import sqlite3
import csv

conn = sqlite3.connect('exercise01.sqlite')
conn_2 = sqlite3.connect('exercise01_imported.sqlite')

class DataBase():

    def print_result(self,rows):
        for row in rows:
            print (row)

    # Print the name of the tables in the database.
    def get_structure(self):
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        rows = c.fetchall()
        c.close()

        return rows

    # Get the database so that it can be exported to a CSV file.
    def denormalize(self):

        fields="records.id,records.age,workclasses.name,education_levels.name,\
                races.name,capital_gain,capital_loss,hours_week,countries.name,over_50k"

        tables = "workclasses,education_levels,races,countries"

        condition = "records.workclass_id=workclasses.id \
                     AND records.country_id=countries.id \
                     AND records.education_level_id=education_levels.id \
                     AND records.race_id = races.id"

        query = "SELECT " + fields + " FROM records INNER JOIN " \
                + tables + " ON " + condition

        c = conn.cursor()

        print(query)
        c.execute(query)

        rows = c.fetchall()

        c.close()

        return rows

    def export_to_csv(self,flattened):
        # Overwrite existing file.
        with open('backup.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in flattened:
                writer.writerow(row)

    def import_from_csv(self):
        with open('backup.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                pass

    def create_flattened(self):
        c = conn_2.cursor()
        c.execute('''CREATE TABLE flattened(id integer, age integer, workclasses text, education_levels text, races text, capital_gain integer, capital_loss integer, hours_week integer, countries text, over_50k integer)''')
        c.close()

if __name__ == '__main__':
    d = DataBase()
    d.print_result(d.get_structure())
    flattened = d.denormalize()
    d.print_result(flattened)
    d.export_to_csv(flattened)

    e = DataBase()
    e.create_flattened()
    # e.import_from_csv()

    conn.close()
    conn_2.close()
