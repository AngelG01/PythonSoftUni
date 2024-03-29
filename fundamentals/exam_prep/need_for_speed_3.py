cars_data = {}
number_of_cars = int(input())

for car in range(number_of_cars):
    car_info = input().split('|')
    car_model, mileage, fuel = car_info[0], car_info[1], car_info[2]
    cars_data[car_model] = [int(mileage), int(fuel)]
command = input().split(' : ')
while command[0] != 'Stop':

    if command[0] == 'Drive':
        car, distance, fuel = command[1], command[2], command[3]
        if cars_data[car][0] < 100_000:
            if cars_data[car][1] < int(fuel):
                print('Not enough fuel to make that ride')
            else:
                cars_data[car][0] += int(distance)
                cars_data[car][1] -= int(fuel)
                print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars_data[car][0] >= 100_000:
            print(f'Time to sell the {car}!')
            del cars_data[car]
    elif command[0] == 'Refuel':
        car, refill = command[1], command[2]
        to_refill = cars_data[car][1] + int(refill)
        fuel_tank = 75
        if to_refill <= fuel_tank:
            cars_data[car][1] += int(refill)
            print(f'{car} refueled with {refill} liters')
        else:
            difference = 75 - cars_data[car][1]
            cars_data[car][1] += difference
            print(f'{car} refueled with {difference} liters')
    elif command[0] == 'Revert':
        car, kilometers = command[1], command[2]
        decrease = cars_data[car][0] - int(kilometers)
        if decrease < 10_000:
            cars_data[car][0] = 10_000
        else:
            cars_data[car][0] -= int(kilometers)
            print(f'{car} mileage decreased by {kilometers} kilometers')
    command = input().split(' : ')

for current_car, element in cars_data.items():
    print(f'{current_car} -> Mileage: {element[0]} kms, Fuel in the tank: {element[1]} lt.')

