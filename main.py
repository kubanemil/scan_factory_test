import sqlite3
from tools import is_trash_domain, get_regex

db_name = 'domains.db'

with sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    results = cursor.execute('SELECT * FROM domains;').fetchall()
    column_names = [desc[0] for desc in cursor.description]

    domain_ids = set([row[0] for row in results])

    for domain_id in domain_ids:
        domains = [row[1] for row in results if row[0] == domain_id]

        regex = get_regex(domains)  # gets a regex pattern based on a given domains.

        insert_into_db(domain_id, regex)
        cursor.execute(f'INSERT INTO rules (project_id, regexp) VALUES ({domain_id}, "{regex}")')
    conn.commit()

