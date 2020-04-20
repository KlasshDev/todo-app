"""
Title   :   SQlite Support File
Author  :   Cameron Schweeder
Date    :   2020.04.12
Time    :   

Simplified SQLite3 uses for reference.
"""

import sqlite3
import time
import datetime

class databaseInteract:
    """
    Objects for creating, viewing, editing and deleting database tables
    WARNING: if importing this class, end your operation with a closeDB() call.
    """
    def __init__(self, database):
        """
        Initialize the requested DB file and create a cursor
        Create table for Projects, context, notes and inbox
        Input   :   STR : database file name (database.db)
        """
        self.con = sqlite3.connect(str(database))   # Create connection variant
        self.c = self.con.cursor()                       # Create Cursor variant

        # Create Projects Table
        self.c.execute('CREATE TABLE IF NOT EXISTS projects(project_id INTEGER PRIMARY KEY, \
                                                            title       TEXT NOT NULL, \
                                                            description TEXT, \
                                                            task_id     INTEGER, \
                                                            context_id  INTEGER, \
                                                            note_id     INTEGER, \
                                                            created_date DATETIME, \
                                                            modified_date DATETIME)')

        # Create todo table
        self.c.execute('CREATE TABLE IF NOT EXISTS task(task_id INTEGER PRIMARY KEY, \
                                                            title       TEXT NOT NULL, \
                                                            description TEXT, \
                                                            project_id     INTEGER, \
                                                            context_id  INTEGER, \
                                                            note_id     INTEGER, \
                                                            created_date DATETIME, \
                                                            modified_date DATETIME, \
                                                            due_date DATETIME, \
                                                            archived BOOLEAN, \
                                                            reocurring BOOLEAN)')

        # Create Context table
        self.c.execute('CREATE TABLE IF NOT EXISTS context(context_id INTEGER PRIMARY KEY, \
                                                            title       TEXT NOT NULL, \
                                                            created_date DATETIME)')
                                    
        # Create Notes table
        self.c.execute('CREATE TABLE IF NOT EXISTS notes(note_id INTEGER PRIMARY KEY, \
                                                            title       TEXT NOT NULL, \
                                                            description TEXT, \
                                                            task_id     INTEGER, \
                                                            context_id  INTEGER, \
                                                            created_date DATETIME, \
                                                            modified_date DATETIME)')


    
    def __enter__(self):
        return self

    def __exit__(self, exec_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()
    """
    CRUD (Create, Read, Update and Delete)
    """   
      
    def insertToTable(self, tableChoice, operators, values):
        """
        Input   : tableChoice   : name of the table in the DB
        Input   : operators     : ?,?,? for each value to pass
        Input   : values        : a string of values
        """
        self.con.execute("INSERT OR IGNORE INTO "+tableChoice+" VALUES("+operators+')', values)
        return
    
    def closeDB(self):
        """
        Function to close out the DB when done operation.
        Run this at the end of quary.
        """
        self.c.close()
        self.con.close()
