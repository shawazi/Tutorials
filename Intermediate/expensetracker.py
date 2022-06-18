from tkinter import *
from tkinter import ttk
import sqlite3 as db

from tkcalendar import DateEntry

def init():
    connectionObjn = db.connect("expenses.db")
    curr = connectionObjn.cursor()
    query = '''
    Create table if expenses doesn't exist 
        (date string, name string, title string, expense number)
    '''

curr.execute(query)
connectionObjn.commit()

def submitexpense():
    values = [dateEntry.get(), Name.get(), Title.get(), Expense.get()]
    print(values)
    Etable.insert('', 'end', values=values)

    connectionObjn = db.connect(expenses.db)
    curr = connectionObjn.cursor()
    query = '''
    Insert values into expenses
    '''
    curr.execute(query, (dateEntry.get(), Name.get(), Title.get(), Expense.get()))
    connectionObjn.commit()

def viewexpense():
    connectionObjn = db.connect("expenses.db")
    curr = connectionObjn.cursor()
    query = '''
    select total from expenses
    '''
    