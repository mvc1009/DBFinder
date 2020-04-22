import sys, os
try:
  import argparse
except:
  print('[!] argparse is not installed. Try "pip install argparse"')
  sys.exit(0)


# Display DBFinder Banner
def banner():
  print("DBFinder")
  print("Version 0.8")
  print("By: @mvc1009")
  print("")


def main():
  banner()
  # Parsing arguments
  parser = argparse.ArgumentParser(description='DBFinder is used for discovering DB with public visibility')
  parser.add_argument('-a', action='store', dest='account', help='Specify a specific user account', type=str)
  parser.add_argument('-d', action='store', dest='directory', help='Download results to a specific directory', type=str)
  parser.add_argument('-o', action='store', dest='organize', help='Organize results by \'new\', \'old\', \'best\', or \'all\'', type=str)
  parser.add_argument('-p', action='store', dest='project', help='Specific project to search. Use with -a', type=str)
  parser.add_argument('-r', action='store', dest='custom_regex', help='Custom regex string', type=str)
  parser.add_argument('-s', action='store', dest='custom_search', help='Custom GitHub search string', type=str)
  parser.add_argument('-u', '--url', action='store_true', help='Output URL of found object')
  parser.add_argument('-v', '--verbose', action='store_true', help='Turn verbose output on. This will output matched lines')
  parser.add_argument('-w', action='store', dest='write_file', help='Write results to a file', type=str)
  global args
  args =  parser.parse_args()




try:
  if __name__ == "__main__":
    main()
except KeyboardInterrupt:
  print("[!] Keyboard Interrupt. Shutting down")
