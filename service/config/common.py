import os

import boto3

LCS_EC2_AWS_ACCESS_KEY_ID = os.environ["LCS_EC2_AWS_ACCESS_KEY_ID"]
LCS_EC2_AWS_SECRET_ACCESS_KEY = os.environ["LCS_EC2_AWS_SECRET_ACCESS_KEY"]


def get_parameters(region, path):
    ssm = boto3.client(
        "ssm",
        region_name=region,
        aws_access_key_id=LCS_EC2_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=LCS_EC2_AWS_SECRET_ACCESS_KEY,
    )
    params = ssm.get_parameters_by_path(Path=path, WithDecryption=True)
    parameters = {i["Name"].replace(path, ""): i["Value"] for i in params["Parameters"]}
    # aws response is limited to 10 parameters in response
    while "NextToken" in params:
        params = ssm.get_parameters_by_path(
            Path=path, WithDecryption=True, NextToken=params["NextToken"]
        )
        for i in params["Parameters"]:
            parameters[i["Name"].replace(path, "")] = i["Value"]
    return parameters
