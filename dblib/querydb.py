"""
Requires you to run quickstart notebook first to create the database.
"""
import os
from databricks import sql

def querydb(query="SELECT experience_level, avg(salary_in_usd) AS avg_salary_usd FROM salaries GROUP BY experience_level"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        for row in result:
            print(row)
    return result
