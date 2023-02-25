#!/usr/bin/env python

# -------------------------------------------------------------------------------------------------
# Version    : 1.0
# Date       : 24-FEB-2023
#--------------------------------------------------------------------------------------------------
import os
import json
import requests
import re

def get_creds_from_env():
    client_id = os.environ.get('AZURE_CLIENT_ID', None)
    client_secret = os.environ.get('AZURE_CLIENT_SECRET', None)
    tenant_id = os.environ.get('AZURE_TENANT_ID', None)
    subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID', None)
    subscription_name = "viki-subscription"
    exclude_host_filters = os.getenv("EXCLUDE_HOST_FILTERS", "").split(",")
    exclude_rg_filters = os.getenv("EXCLUDE_RG_FILTERS", "").split(",")
    viki_var = os.getenv("VIKI_VAR")
    
    output = "Dear {}, subscription:{} has id:{}".format(viki_var,subscription_name,subscription_id) 

    return output


if __name__ == "__main__":
    # Replace "your_resource_group_name" with the actual name of your resource group
    resource_group_name = 'viki-rg'
    print(get_creds_from_env())