def positiveFeedbackPercentage(ratings):

    if(len(ratings) == 0):
        return "no ratings are available"
    
    total_ratings = len(ratings) #count of total ratings
    positive_ratings = 0

    for i in ratings:
        if(i == 4 or i == 5):
            positive_ratings += 1 #count of positive ratings

    percentage = (positive_ratings/total_ratings)*100  #calculating positive feedback percentage
    return percentage


rating_list = eval(input("ratings = "))
print(f"Positive Feedback: {positiveFeedbackPercentage(rating_list)}%") #displaying positive feedback percentage