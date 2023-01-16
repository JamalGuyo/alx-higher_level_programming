#!/bin/bash
# Get The body  size  from outgoing  request to url introduced as argument
curl -s "$1" | wc -c
