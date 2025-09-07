
def fareForEachTrip(trips):

    total_fare = []

    for i in range(len(trips)):
        base_fare = 50
        distance_cost = trips[i]*10 #calculating distance cost
        total = base_fare + distance_cost
        total_fare.append(total)

        print(f"Trip {i+1}: ${total}")

    print(f"Total Fare: ${sum(total_fare)}") #displaying total cost

trips = eval(input("trips = ")) #eval() converts input into list
fareForEachTrip(trips)