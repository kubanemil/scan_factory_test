import sqlite3
from tools import Tools


class DBRegex(Tools):
    def __init__(self, db_name='domains.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.data = self.cursor.execute('SELECT * FROM domains;').fetchall()  # all rows from 'domains' table
        self.create_rules()

    def insert_into_rules_db(self, domain_id, regex):
        """
        Inserts data into rules (project_id, regexp).
        """
        results = self.cursor.execute(f'SELECT * FROM rules WHERE project_id={domain_id};').fetchall()
        if len(results) == 0:
            self.cursor.execute(f'INSERT INTO rules (project_id, regexp) VALUES ({domain_id}, "{regex}");')
        else:
            self.cursor.execute(f'UPDATE rules SET regexp="{regex}" where project_id={domain_id};')
        self.conn.commit()

    def create_rules(self):
        """
        Creates Regular expressions for each project and inserts
        it into 'rules' table.
        """
        domain_ids = set([row[0] for row in self.data])

        for domain_id in domain_ids:
            domains = [row[1] for row in self.data if row[0] == domain_id]

            regex = self.get_regex(domains)  # gets a regex pattern based on a given domains.

            self.insert_into_rules_db(domain_id, regex)
            self.conn.commit()

    def filtered_domains(self):
        """Returns 'domains' table but without 'trash' domains."""
        filtered_rows = []
        for row in self.data:
            regex = self.cursor.execute(f'SELECT regexp FROM rules WHERE project_id={row[0]};').fetchone()[0]
            if not self.is_trash_domain(row[1], regex):
                filtered_rows.append(row)
        return filtered_rows

    def rules_table(self):
        """
        Returns 'rules' table that contains (project_id, regexp) columns from database.
        """
        return self.cursor.execute('SELECT * FROM rules;').fetchall()


if __name__ == '__main__':
    instance = DBRegex()
    print(instance.data)
    print(instance.rules_table())
    print(instance.filtered_domains())
