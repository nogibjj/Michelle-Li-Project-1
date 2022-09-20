#!/usr/bin/env python3
import click
from dblib.querydb import querydb

#build a click command line interface
@click.group()
def cli():
    "A simple CLI to query a database"

#build a click command line interface
@cli.command()
@click.option("--query", default="SELECT experience_level, avg(salary_in_usd) AS avg_salary_usd FROM salaries GROUP BY experience_level")

#function to execute the query
def cli_query(query):
    #execute the query
    querydb(query)

#run the cli
if __name__ == "__main__":
    cli()
