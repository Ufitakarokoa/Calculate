# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line


#price
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

#average price
sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = sum_one_each / 4




#groceryList
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10


#total price without discount
sum_total = (num_potatoes * potato) + (num_broccolis * broccoli) + (num_leeks * leek)  + (num_brussel_sprouts * brussel_sprout)

#discount percentage
discount_percentage =  sum_total * .30 

#rounded total price with 30% discount
discounted_sum_total = (sum_total - discount_percentage)
print (discounted_sum_total)