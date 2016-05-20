#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os.path

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  names = []
  file_pointer = open(filename,'rU')
  fulltext = file_pointer.read()
  file_pointer.close()

  match_year = re.search(r'>Popularity\sin\s(\d\d\d\d)<', fulltext)
  if match_year:
    names.append(match_year.group(1))

    #get a list of matching tuples
    match_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', fulltext)


    # dictonary to persist all the names and order them alphabetically later
    names_dic = {}
    for res_tuple in match_names:
      (index, boy, girl) = res_tuple

      if boy not in names_dic:
        names_dic[boy] = index
      if girl not in names_dic:
        names_dic[girl] = index

    names_sorted_keys = sorted(names_dic)

    for name in names_sorted_keys:
      names.append(name + " " + names_dic[name])

    return names


  else:
    # sys.stderr.write('The file format does not match the expectations')
    # sys.exit(1)
    return['-1','The file format does not match the expectations']


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:

    #check if file exists
    if os.path.isfile(filename):
      result = extract_names(filename)
      if summary:
        year = result[0]
        if year != '-1':
          summary_filename = year + ".sum"
          text = '\n'.join(result)
          file = open(summary_filename, "w")
          file.write(text)
          file.close()
        else:
          print result[1]
      else:
        print result
    else:
      print "The file '%s' does not exist" % filename

  
if __name__ == '__main__':
  main()
