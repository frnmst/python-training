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

        conn.close()

        return rows

    def export_to_csv(self):
        pass

if __name__ == '__main__':
    d = DataBase()
    d.print_result(d.get_structure())
    d.print_result(d.denormalize())
    d.export_to_csv()

