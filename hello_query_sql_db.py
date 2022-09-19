#!/usr/bin/env python3
import os
import click
from dblib.querydb import querydb

#build a click command line interface
@click.group()
def cli():
    "A simple CLI to query a database"

#build a click command line interface
@cli.command()
@click.option("--query", default="SELECT * FROM default.diamonds LIMIT 2", help="SQL query to execute")

def cli_query(query):
    #execute the query
    querydb(query)

#run the cli
if __name__ == "__main__":
    cli()