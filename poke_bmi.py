#Calculate the BMI of every Pokemon
#File is in pokedex/pokedex/data/csv, called pokemon.csv
#NOTE: Credits to veekun with their pokedex at https://github.com/veekun/pokedex

import csv

pokemon_csv_in = "pokedex/pokedex/data/csv/pokemon.csv"

#Get the BMI, rounded to two digits, of the Pokemon
def bmi_ify(height, weight):
    if (weight == "0") or (height == "0"):
        return -1

    bmi_h = float(height) / 10 #Bring height to meters
    bmi_w = float(weight) / 10 #Bring weight to kilograms
    bmi = bmi_w / (bmi_h * bmi_h)
    return round(bmi, 2)

#Get what category the WHO would classify the Pokemon
def adult_bmi_category(bmi):
    if ((bmi >= 0) and (bmi < 15)):
        return "Very Severely Underweight"
    elif ((bmi >= 15) and (bmi < 16)):
        return "Severely Underweight"
    elif ((bmi >= 16) and (bmi < 18.5)):
        return "Underweight"
    elif ((bmi >= 18.5) and (bmi < 25)):
        return "Healthy Weight"
    elif ((bmi >= 25) and (bmi < 30)):
        return "Overweight"
    elif ((bmi >= 30) and (bmi < 35)):
        return "Moderately Obese"
    elif ((bmi >= 35) and (bmi < 40)):
        return "Severely Obese"
    elif (bmi > 40):
        return "Very Severely Obese"
    else:
        return "Unknown" #Either height or weight is unknown, a.k.a. set to 0

def main():
    #BMI is measured as kg/m^2
    #Heights will need to be multiplied by 10
    #Weights will need to be divided by 10
    with open(pokemon_csv_in, 'r') as poke_in:
        with open("pokemon_bmi.csv", 'w') as poke_out:
            poke_out.write("Name,Height(dm),Weight(hg),BMI,Category\n") #Header row
            pokecsv_in = csv.reader(poke_in)
            #ID: column 0
            #Name: column 1
            #Pokedex ID: column 2
            #Height: column 3
            #Weight: column 4
            #Base XP: column 5
            #Order: column 6
            #Default: column 7
            row_count = 0
            for row in pokecsv_in:
                if (row_count > 0):
                    pokebmi = bmi_ify(row[3], row[4]) #Get the BMI
                    bmi_cat = adult_bmi_category(pokebmi) #Get the category
                    poke_out.write(row[1] + "," + row[3] + "," + row[4] + "," + str(pokebmi) + "," + bmi_cat + "\n") #Write it to a file, maybe I'll make this use csv later
                row_count += 1
        poke_out.closed

    poke_in.closed

if __name__ == "__main__":
    main()
