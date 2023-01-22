import requests
from tabulate import tabulate
import pandas as pd
from bs4 import BeautifulSoup

api_url = "https://app-api.dune.com/v1/graphql"

payload = {
    "operationName": "GetExecution",
    "query": "query GetExecution($execution_id: String!, $query_id: Int!, $parameters: [Parameter!]!) {\n  get_execution(\n    execution_id: $execution_id\n    query_id: $query_id\n    parameters: $parameters\n  ) {\n    execution_queued {\n      execution_id\n      execution_user_id\n      position\n      execution_type\n      created_at\n      __typename\n    }\n    execution_running {\n      execution_id\n      execution_user_id\n      execution_type\n      started_at\n      created_at\n      __typename\n    }\n    execution_succeeded {\n      execution_id\n      runtime_seconds\n      generated_at\n      columns\n      data\n      __typename\n    }\n    execution_failed {\n      execution_id\n      type\n      message\n      metadata {\n        line\n        column\n        hint\n        __typename\n      }\n      runtime_seconds\n      generated_at\n      __typename\n    }\n    __typename\n  }\n}\n",
    "variables": {
        "execution_id": "01GNSF2AC45WFJYS6ZR35XNE4T",
        "parameters": [],
        "query_id": 1809348,
    },
}

data = requests.post(api_url, json=payload).json()

print(data)
