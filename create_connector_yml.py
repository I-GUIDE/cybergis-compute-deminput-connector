#!/bin/env python3

import yaml
import os

connector_dict = {'$1': {'Input': {'DEMInput': {'site_id':os.environ['param_site_id'],'resolution':os.environ['param_resolution']}}}}

with open('/job/executable/deminput.yml','w') as demfile:
    yaml.dump(connector_dict,demfile)
