#!/usr/bin/env python3

import argparse
import json
import sys


def host( hostname ):

   hostData = {
      "vagrant1": { "ansible_host":"127.0.0.1", "ansible_port":2222 },
      "vagrant2": { "ansible_host":"127.0.0.1", "ansible_port":2200 },
      "vagrant3": { "ansible_host":"127.0.0.1", "ansible_port":2201 }
   }

   host = hostData[hostname];
   
   print( json.dumps(host) )

# end host()

def list():
   # print( "list" )

   data = {
    "all": {
        "hosts": ["vagrant1", "vagrant2", "vagrant3"]
        }
   }
     
   print( json.dumps(data) )

# end list()

def main():

   parser = argparse.ArgumentParser(description='Dynamic inventory script example')
   
   parser.add_argument('--host', help='returns details of a specified host')

   parser.add_argument('--list', action="store_true", help='returns group details')

   args = parser.parse_args()

   #  print( args )
   
   if( args.list == True ):
      list()
   else:

      if( args.host is None ):
         parser.print_help(sys.stderr)
         sys.exit(1)
      else:
         host( args.host )

#end main()


if __name__=="__main__":
    main()
