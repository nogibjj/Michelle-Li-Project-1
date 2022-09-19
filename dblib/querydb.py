from databricks import sql
import os

"""
Requires you to run quickstart notebook first to create the database.
"""

def querydb(query="SELECT * FROM default.diamonds LIMIT 2"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM default.diamonds LIMIT 2")
            result = cursor.fetchall()
            for row in result:
                print(result)
    return result
