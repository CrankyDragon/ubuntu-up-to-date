#!/usr/bin/env python

import os
import json

def prompt(format, default=None):
    message = format
    if default:
        message = format % default 
        
    return (message, default)
        
def get_config():
    options = {}
    access_key = os.environ.get('AWS_ACCESS_KEY')
    secret_key = os.environ.get('AWS_SECRET_KEY')
    prompts = [
       ('aws_access_key', prompt("Enter your AWS access key: [%s] ", access_key)),
       ('aws_secret_key', prompt("Enter your AWS secret key: [%s] ", secret_key)),
       ('aws_image_id'  , prompt("Enter the source AMI: [%s] ", "ami-290fee6d")),
       ('aws_region'    , prompt("Enter the AWS region you wish to use: [%s] ", "us-west-1")),
       ('instance_type' , prompt("Enter the instane type: [%s] ", "t2.small"))
    ]
    
    for k,v in prompts:
        message,default = v
        options[k] = raw_input(message) or  default

    return options

def write_config(config):
    with open('./variables.json', 'w') as f:
        dump = json.dumps(config)
        f.write(dump)
    
if __name__ == '__main__':
   config = get_config() 
   write_config(config)
