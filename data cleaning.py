import csv
import math
from datetime import datetime

#Where I want the information to be stored
output = 'fifa_clean_project.csv'

#set new headers
new_headers = [('Team', 9), ('Contract', 10), ('Height (feet)', 12), ('Height (cm)', 13), ('Weight (lbs)', 14), ('Weight (kg)', 15), (' Joined Year', 20), (' Joined Month', 21), ('Joined Day', 22),('Value', 24), ('Wage', 25), ('Release Clause', 26), ('Weak Foot', 70), ('Skill Moves', 71), ('International Reputation', 74), ('Hits', 81)]


# Open the CSV file
with open('fifa21_raw_data.csv', 'r') as fifa:
    # Create a CSV reader object
    csvReader = csv.reader(fifa)
    
    # Create list to store
    cleaned_data = []
    
    csv_headers = next(csvReader, None)
    
    # Iterate CSV file
    for row in csvReader:
        # Where the date column is
        date_str = row[17] 
        
        # Make into datetime object
        date = datetime.strptime(date_str, '%b %d, %Y')
        year = date.year
        month = date.strftime('%B')
        day = date.day
        
        #Where the heigh column is
        height_str = row[11] 

        # Make feet and inches into a decimal number and turn feet and inches into ints to convert to cm later on
        feet, inches = height_str.split("'")
        feet_inch = feet.strip() + "." + inches.strip('"')
        feet = int(feet.strip()) 
        inches = int(inches.strip('"'))  

        # Convert height to centimeters
        height_cm = int(math.ceil((feet * 12 + inches) * 2.54))
        
        #Where the weight column is
        weight_string = row[12]  

        # Convert weight to pounds 
        weight_lbs = int((weight_string[0:3]))
        
        # Convert weight to kilograms 
        weight_kg = int(math.ceil(weight_lbs * 0.45359237))
        
        #iniate value,wage, and release clause values to disregard the euro sign and to make sure that a number below a thousand is covered.
        value_string = row[19]
        value = value_string[1:]
        wage_string = row[20]
        wage = wage_string[1:]
        release_clause_str = row[21]
        release_clause = release_clause_str[1]
        
        #if a player's value is in the millions
        if value_string[-1] == "M":
            value = value_string[1:-1]
            if "." not in value:
                value = value + "000000"
            else:
                value_comma = value.split(".")
                value = value_comma[0] + value_comma[1] + "00000"
                
        #if it is in the thousands
        elif value_string[-1] == "K":
            value = value_string[1:-1]
            if "." not in release_clause:
                value = value + "000"
            else:
                value_comma = value.split(".")
                value = value_comma[0] + value_comma[1] + "00"
                
        #If a player's wage is in the thousands
        if wage_string[-1] == "K":
            wage = wage_string[1:-1]
            if "." not in wage:
                wage = wage + "000"
            else:
                wage_comma = wage.split(".")
                wage = wage_comma[0] + wage_comma[1] + "00"
                
        #If a player's release clause is in the millions       
        if release_clause_str[-1] == "M":
            release_clause = release_clause_str[1:-1]
            if "." not in release_clause:
                release_clause = release_clause + "000000"
            else:
                release_comma = release_clause.split(".")
                release_clause = release_comma[0] + release_comma[1] + "00000"
                
        #If a player's release clause is in the thousands 
        elif release_clause_str[-1] == "K":
            release_clause = release_clause_str[1:-1]
            if "." not in release_clause:
                release_clause = release_clause + "000"
            else:
                release_comma = release_clause.split(".")
                release_clause = release_comma[0] + release_comma[1] + "00"
                
        #set value,wage and release clause to integers        
        value = int(value)
        wage = int(wage)
        release_clause = int(release_clause)
        
        #Where the team and contracts are
        team_contract = row[9].strip()
        
        #make sure that contract info is stored in the contract variable and team info in the team one.
        if "On Loan" in team_contract:
            team = team_contract[:-20]
            contract = team_contract[-20:-1] + team_contract[-1]
        elif "Free" in team_contract:
            contract = team_contract[-4:-1] + team_contract[-1]
            team = team_contract[:-4]
        else:
            team = team_contract[:-12]
            contract = team_contract[-11:-1] + team_contract[-1]
            
        #Where the hits column is
        hits = row[-1].strip()
        
        #Where the weak foot column is and specified to only extract the number and not the star. Converted it to an int.
        weak_foot = row[-12]
        delete_star = weak_foot.find("★")
        weak_foot = int(weak_foot[:delete_star])
        
        #Where the skill moves column is and specified to only extract the number and not the star. Converted it to an int.
        skill_moves = row[-11]
        delete_star = skill_moves.find("★")
        skill_moves = int(skill_moves[:delete_star])
        
        #Where the international reputation column is and specified to only extract the number and not the star. Converted it to an int.
        international_rep = row[-8]
        delete_star = international_rep.find("★")
        international_rep = int(international_rep[:delete_star])
        
        # Add all changes made to the row.
        cleaned_row = row[0:9] + [team, contract] + row[10:11] + [feet_inch, height_cm] + [weight_lbs, weight_kg] + row[13:17] + [year, month, day] + row[18:19] + [value, wage, release_clause] + row[22:65] + [weak_foot, skill_moves] + row[67:69] + [international_rep] + row[70:76] + [hits]
        
        # Append row to new list
        cleaned_data.append(cleaned_row)

# Replaced old headers with new.
csv_headers.remove(csv_headers[9])
csv_headers.remove(csv_headers[10])
csv_headers.remove(csv_headers[10])
csv_headers.remove(csv_headers[14])
csv_headers.remove(csv_headers[15])
csv_headers.remove(csv_headers[15])
csv_headers.remove(csv_headers[15])
csv_headers.remove(csv_headers[58])
csv_headers.remove(csv_headers[58])
csv_headers.remove(csv_headers[60])
csv_headers.remove(csv_headers[66])


# Insert new headers at specified index.
for header, index in new_headers:
    csv_headers.insert(index, header)

with open(output, 'w', newline='') as fifa_updated:
    csv_writer = csv.writer(fifa_updated)
    # put updated headers
    csv_writer.writerow(csv_headers)
    
    # and data rows
    csv_writer.writerows(cleaned_data)

        
    
        