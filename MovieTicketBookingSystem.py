
def seatBookingCancellation(total_seats,booked_seats,book_seat,cancel_seat):

    if(len(booked_seats) != total_seats):

        if(book_seat not in booked_seats):
            booked_seats = booked_seats + [book_seat] #booking seat

        if(cancel_seat in booked_seats):
            booked_seats.remove(cancel_seat) #cancelling seat
    
    available_seats = [] #available seats
    for i in range(1,total_seats+1):

        if ((i not in booked_seats) and (i != cancel_seat)):
            available_seats.append(i)
    
    return available_seats


total_seats = int(input("total_seats = "))
booked_seats = eval(input("booked_seats = ")) #converting input into list
book_seat = int(input("book_seat = "))
cancel_seat = int(input("cancel_seat = "))
print("Available seats:",seatBookingCancellation(total_seats,booked_seats,book_seat,cancel_seat)) #displaying available seats