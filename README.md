# Project 1
## Key Objectives
The purpose of this project is ot learn how to create scaffolds and work with GitHub CodeSpace. I created a command line tool that that queries Databricks.

## API Architectural Diagram
![Project-1-architecture (2)](https://user-images.githubusercontent.com/70456530/189802283-912b1b0e-1f51-486c-8849-b857557a44fa.jpg)

## Dataset 
The dataset I will be using for this project is from Kaggle. It contains 607 salaries of data scientist roles from 2019 - 2022. I imported the dataset from Kaggle into Databricks and performed exploratory data analysis in Databricks. 
https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

## Setup authorization

[databricks-python](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/python-api)

Place in Codespace secrets
* [unix, linux, mac](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/python-api#unixlinuxandmacos)

```bash
DATABRICKS_HOST
DATABRICKS_TOKEN
```

## Test out CLI

```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```
## Databricks SQL Connector

[Setup table first!](https://docs.databricks.com/dbfs/databricks-datasets.html)

[sql remote](https://docs.databricks.com/dev-tools/python-sql-connector.html)
https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#connection-details-cluster

## Comparing to Dask

An alternative solution to Databricks is https://tutorial.dask.org/00_overview.html[Dask] or [Ray](https://docs.ray.io/en/latest/data/dask-on-ray.html).

### Distributed compute

* [Quickstart distributed compute example](https://distributed.dask.org/en/stable/quickstart.html)
* [For Advanced users (HDFS wordcount Enron)](https://distributed.dask.org/en/stable/examples/word-count.html)

### Hands on Enron

* [Download data](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset) from Kaggle and upload by right-click on explorer in GitHub Codespaces
* place in a "datasets" directory and add this directory to your `.gitignore`.  This ensures you don't check in a 1GB file to GitHub.

### Streamlit Example

Enable enron...

`streamlit hello --server.enableCORS=false`
`streamlit run hello_streamlit_enron.py --server.enableCORS=false`



