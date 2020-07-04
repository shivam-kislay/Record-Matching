# Done By Shivam Kislay
# Student Number 119220420
# Date = 18/02/2020
import re


# Function  that prints all pairs of matching records (records of two individuals, one from each list,
# that match up in terms of district, year, quarter, volume and page number).
# The results should be printed in the format shown
maryDictionary = {}
nicholasDict = {}

# Regular Expression to extract each record from the file
recordRegEx = re.compile(r"\s*Marriage\s*of\s*(?P<Fname>[A-Za-z ]+)\s"
                         r"\s*in\s*\d{4}\s"
                         r"\s*Group\s*Registration\s*ID\s*N/R\s"
                         r"\s*SR\s*District/Reg\s*Area\s*(?P<dist>([A-Za-z ]+ *)+)\s"
                         r"\s*Returns\s*Year\s+(?P<year>\d{4})\s"
                         r"\s*Returns\s*Quarter\s+(?P<quarter>\d+)\s"
                         r"\s*Returns\s*Volume\s*No\s+(?P<volume>\d+)\s"
                         r"\s*Returns\s*Page\s*No\s+(?P<page>\d+)\s")

# Read input files of Mary and Nicholas
maryFile = open("mary_roche.txt", 'r')
nicholasFile = open("nicholas.txt", 'r')

maryRecords = maryFile.read()
nicholasRecords = nicholasFile.read()

# Loop to populate the Dictionary with records of Mary
i = 0
for x in recordRegEx.finditer(maryRecords):
    maryDictionary[i] = [x.group("Fname"), x.group("dist"), x.group("year"), x.group("quarter"), x.group("volume"),
                         x.group("page")]
    i += 1

# Loop to populate the Dictionary with records of Nicholas
j = 0
for x in recordRegEx.finditer(nicholasRecords):
    nicholasDict[j] = [x.group("Fname"), x.group("dist"), x.group("year"), x.group("quarter"), x.group("volume"),
                       x.group("page")]
    j += 1

# Loop to print the possible couples record in the mentioned format
for m in maryDictionary.values():
    for n in nicholasDict.values():
        if m[1] == n[1] and m[2] == n[2] and m[3] == n[3] and m[4] == n[4] and m[5] == n[5]:
            print("Possible match!")
            print("%s and %s in %s in %s" % (n[0], m[0], m[1], m[2]))
            print("Quarter = %s, Volume = %s, Page = %s" % (m[2], m[3], m[4]))
            print()
