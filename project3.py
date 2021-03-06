import csv
import random

for i in range(1,10):
    store_number = 'store%d.csv' % i
    with open('items.csv','r') as csvinput:
        with open(store_number, 'w') as csvoutput: # this section of code creates random prices for all items in the item database and creates a new file with these values for each store
            writer = csv.writer(csvoutput)
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('price')
            all.append(row)

            for row in reader:
                row.append((random.randint(50,500)) / 100)
                all.append(row)

            writer.writerows(all)

recipelist = ['chickenbaconpasta', 'cake']
recipe = str(random.choice(recipelist)) + '.csv'

recipeingredients = {}

with open(recipe, 'r') as csvinput:  # this section of code pulls data from the recipe documents and converts to a dictionary
    reader = csv.reader(csvinput)
    next(reader)
    
    for row in reader:
        recipeingredients['%s' % row[0]] = {'weight': row[1], 'quantity': row[2]}

ingredientslist = []

for key in recipeingredients:
    ingredientslist.append(key)  # makes a list of JUST the ingredients needed for each recipe

shopprices = {}
where_to_get_item = {} # declaring dictionaries and a list
shops_to_visit = []

for ingredients in ingredientslist:
    for i in range(1,10):
        store_number = 'store%d.csv' % i
        with open(store_number, 'r') as csvinput:
            reader = csv.reader(csvinput)
            next(reader)
                                            # this section of code finds where each ingredient is cheapest and store these values in a dictionary
            for row in reader:
                if ingredients in row:
                    price_per_quantity = float(row[2]) / float(row[3])
                    shopprices.update({'store%d' % i: "{0:.2f}".format(round(price_per_quantity,2))})
                    
    cheapeststore = min(shopprices, key=shopprices.get)
    where_to_get_item.update({ingredients: cheapeststore})
    if cheapeststore not in shops_to_visit:
        shops_to_visit.append(cheapeststore) # this list tells the program which stores it needs to visit, hence ignoring unneeded stores





