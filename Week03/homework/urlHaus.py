#
import csv
import re
# FIX: Renamed ur1HausOpen to urlHausOpen
# FIX: changed searchTerm to searchTerms
def urlHausOpen(filename, searchTerms):
# Open the file as "file" and then read the contents
    with open(filename) as file:
        # FIX: changed csv.reveiw to csv.reader
        # FIX: changed the == to =
        # FIX: changed f to file
        contents = csv.reader(file)
        # skip the first 9 lines to get rid of the csv header
        for row in range(9):
            next(contents)
            # Find the third entry in each line, which is the url used, and find the url's with the search term contained.
            # FIX: removed the extra for loop here
        for eachLine in contents:
            x = re.findall(r"" + searchTerms + "", eachLine[2])

            # Format the output for more user frtiendly output
            for _ in x:

                the_url = eachLine[2].replace("http","hxxp")
                the_src = eachLine[-2]
                print(
                    """
                URL: {}
                Info: {}
                {}""".format(the_url, the_src, "*" * 60))
                # FIX: replaced +60 with *60
                # FIX: replaced """,format with proper syntax """.format
                # FIX: added dictionaries for URL and Info