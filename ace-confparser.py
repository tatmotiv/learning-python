#!/usr/bin/python
input_file = "cisco-ace-example.conf"
with open(input_file, "r") as input_lines:
    parsemode = "probes"
    for line in input_lines:
        line_elements = line.split(" ")
        if line.beginswith("rserver host") and parsemode != "rservers":
            parsemode = "rservers"
        elif line.beginswith("serverfarm host") and parsemode != "serverfarms":
            parsemode = "serverfarms"
        elif line.beginswith("sticky-serverfarm") and parsemode != "stickies":
            parsemode = "stickies"
        elif line.beginswith("policy-map type loadbalance") and parsemode != "lb-policy-maps":
            parsemode = "lb-policy-maps"
        elif line.beginswith("class-map") and parsemode != "class-maps":
            parsemode = "class-maps"
        else:
            parsemode = "dump"

    if parsemode == "rservers":
            if line.beginswith("rserver host"):
                rserver_name = line_elements[2]
                rserver_inservice = False
            if line.beginswith("  ip address"):
                rserver_ip = line_elements[4]

