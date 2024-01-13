### Follow this tutorial https://www.makeuseof.com/tag/read-write-google-sheets-python/
### See this doc for more info https://docs.google.com/document/d/1jftTGzRyYFKT8HwVXV-mNF5-ySI04ji8WiqFM5AYtNA/edit?usp=sharing

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

from mdutils.mdutils import MdUtils
from mdutils import Html

import re
import os

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("sheets_parser.json", scopes) # access the json key you downloaded earlier
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("[Data 100] Spring 2024 Staff Onboarding (Responses)")  # open sheet
sheet = sheet.sheet1  # all desired info should be in the first sheet

def attribute_parser(row):
    attributes = {}
    print(row)
    attributes["email"] = row[1] # row[1] is "Email Address"
    last_name = re.search(r'\s([^\s]+)$', row[2]) # row[2] is "What's your full name?", matching the last word in the name
    attributes["name"] = row[2].strip() if last_name == None else row[3].strip() + ' ' + re.search(r'\s([^\s]+)$', row[2]).group(0).strip()
    print("Name is", attributes["name"])
    attributes["pronouns"] = row[4]
    attributes["role"] = assign_role(row[8])
    attributes["sid"] = row[10] # Update from fa23, row[9] is returner or not
    attributes["photo_name"] = attributes['name'].replace(' ', '_')
    print("Photo name is", attributes["photo_name"])
    attributes["bio"] = row[14].replace('\n', '').replace('’', "'")
    if len(row) > 14:
        attributes["website"] = row[15]
    else:
        attributes["website"] = ''
    # if attributes["role"] == "Instructor":
    #     attributes["oh"] = row[40]
    return attributes

def assign_role(job):
    if "20" in job:
        return "Lead Teaching Assistant"
    elif "UCS2" in job:
        return "UCS2"
    elif "UCS1" in job:
        return "UCS1"
    elif "Instructor" in job:
        return "Instructor"
    else:
        return "Other"

def get_photo_location(photos, attributes):
    name_0 = attributes['name'].replace(' ', '_')
    name_1 = attributes['photo_name']
    for photo in photos:
        if name_0 in photo or name_1 in photo:
            return photo
    return ''

def main():
    photos = os.listdir('../resources/assets/staff_pics')
    for i in range(51, 54): #modify the second number depending on the number of rows in the sheet.
        row = sheet.row_values(i)
        attributes = attribute_parser(row)
        filename = attributes['name'].lower().replace(' ', '_') + '.md'
        file = open(filename, 'w')
        if attributes['role'] == "Instructor":
            file.write('---\n'
                + 'name: ' + attributes['name'] + '\n'
                + 'role: ' + attributes['role'] + '\n'
                + 'email: ' + attributes['email'] + '\n'
                + 'website: ' + attributes['website'] + '\n'
                + 'photo: http://ds100.org/sp24-testing/resources/assets/staff_pics/' + get_photo_location(photos, attributes) + '\n'
                + 'pronouns: ' + attributes['pronouns'] + '\n'
                # + 'oh: ' + attributes['oh'] + '\n'
                + '---\n'
                + attributes['bio'] + '\n')
        else:
            file.write('---\n'
                + 'name: ' + attributes['name'] + '\n'
                + 'role: ' + attributes['role'] + '\n'
                + 'email: ' + attributes['email'] + '\n'
                + 'website: ' + attributes['website'] + '\n'
                + 'photo: http://ds100.org/sp24-testing/resources/assets/staff_pics/' + get_photo_location(photos, attributes) + '\n'
                + 'pronouns: ' + attributes['pronouns'] + '\n'
                + '---\n'
                + attributes['bio'] + '\n')
        file.close()

if __name__ == "__main__":
    main()
