#!/usr/bin/env python3

#
# ......py
#
# Copyright (c) 2017 Franco Masotti
#
# See the LICENSE file.
#

import sqlite3
conn = sqlite3.connect('exercise01.sqlite')

class DataBase():

    def print_result(self,cursor):
        for row in cursor.fetchall():
            print (row)

    def get_structure(self):
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        self.print_result(c)
        c.close()

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
        self.print_result(c)

        conn.close()

if __name__ == '__main__':
    d = DataBase()
    d.get_structure()
    d.denormalize()


