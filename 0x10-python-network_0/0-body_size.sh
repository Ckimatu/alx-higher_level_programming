#!/bin/bash
# takes and sends a request to URL, and displays size of the body
curl -s $1 | wc -c
