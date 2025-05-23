from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
    
    @classmethod
    def create_table(cls):
        """
        Create the department table in the database.
        """
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """
        Drop the department table from the database.
        """
        sql = "DROP TABLE IF EXISTS departments;"
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        """ Insert or update the department in the database. """
        if self.id is None:
            sql = "INSERT INTO departments (name, location) VALUES (?, ?);"
            CURSOR.execute(sql, (self.name, self.location))
            self.id = CURSOR.lastrowid
        else:
            sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?;"
            CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    @classmethod
    def create(cls, name, location):
        """
        Create a new department instance.
        """
        department = cls(name, location)
        department.save()
        return department

    def delete(self):
        """
        Delete the department from the database.
        """
        if self.id is not None:
            sql = "DELETE FROM departments WHERE id = ?;"
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            self.id = None
        else:   
            raise ValueError("Cannot delete an unsaved department.")
    def update(self):
        """
        Update the department in the database.
        """
        if self.id is not None:
            sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?;"
            CURSOR.execute(sql, (self.name, self.location, self.id))
            CONN.commit()
        else:
            raise ValueError("Cannot update an unsaved department.")
