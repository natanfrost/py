# declaring a quantity of 100 cars
cars = 100
#declaring how many spaces there is in a car
space_in_a_car = 4.0
# how many drivers
drivers = 30
# total os passagenrs
passengers = 90
#total os cars no driven, subtracting the number of drivers in
#the number of total available cars
cars_not_driven = cars - drivers
#total of occupied cars
cars_driven = drivers
#total os capacity of all cars together
carpool_capacity = cars_driven * space_in_a_car
# average number os passengers per car
average_passengers_per_car = passengers / cars_driven

print 'There are', cars, 'cars available'
print 'There are only', drivers, 'drivers available'
print 'There will be', cars_not_driven, 'empty cars today'
print 'We can transport', carpool_capacity, 'people today'
print 'We have', passengers, 'to carpool today'
print 'We need to put about', average_passengers_per_car, 'in each car'
