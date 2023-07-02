# lists 101

def main():
    # lists are used to store lists of information
    # any kind of information you can think of.
    # this is a list of things to do ('to_do' is the name of the list):
    # the syntax for creating a list is '[]'. Anything inside the brackets, separated by a comma, is in the list.
    to_do = ["clean room", "feed the dog", "read scriptures"]

    # this is a list of how much money I spent on junk food last week ('junk_food_expenses' is the name of the list):
    junk_food_expenses = [3.91, 4.11, 6.54, 3.69, 11.21, 9.34, 0.49]

    # this is a list of the days of the week ('days_of_the_week' is the name of the list):
    days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # make a list of the months in the year ('months' is the name of the list)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # now we have a variable named 'months', which is a list of months.
    # just like a variable can hold a number, or a letter, or a word, this variable holds a list.
    # we can print the entire list like this (it looks kind of ugly, but this is useful for debugging):
    print(months)

    # we can loop through EACH item in the list (ie: January, February, March etc).
    # each time through the loop, our loop variable, m (you can name this whatever you like),
    # will contain the NEXT item in the list.
    # after the last item in the list has been reached ("December"), the loop will end.
    for m in months:
        # let's print 'm' to see what it contains
        print(m)

    # now, here's where it gets good.
    # we can get individual items (months) from the list by asking for an item at a specific index.
    # remember, an index is just a location.
    # in python, the first item in a list is always at index = 0.
    # this is because python is a 0-based language.
    # So, if we want to get the name of the first month of the year, what index value do we use?
    # that's right - 0
    first_month = months[0]
    print(f"the first month of the year is {first_month}")

    # how do we get the last month of the year? What index value do we specify?
    # we would use index = 11 (go ahead, count the months of the year, starting with January = 0)
    last_month = months[11]
    print(f"the last month of the year is {last_month}")



    # ---------------------------------------------------------------------------------------------------------------
    # ok, if you've been sleeping, start paying attention here.....
    # lists can contain just about any type of data you can think of - numbers, characters, words....even OTHER LISTS!
    # did you catch that? A list can contain other lists, like this:
    # here is a list containing a class schedule for monday
    monday_class_schedule = [["Religion", "8:00am"], ["Math", "10:00am"], ["Chemistry", "11:00am"]]

    # look VERY closely as that list. Do you see that it is just like ANY OTHER LIST,
    # except instead of being a list of words, or a list of numbers - it's a list of lists!
    # Do you see that? Please tell me you see that!
    # each item in that list, instead of being a number or a word, is a *list*.

    # this is called a compound list. 'compound' means something formed from two or more parts. It's a list of lists.
    # we can print this compound list just like we print a list of words -
    print(monday_class_schedule)

    # again, that's kind of ugly, and really only useful for debugging.

    # we can loop through this list, and print each item in the list, just like we did earlier with the 'months' list:
    # each time through the loop, our loop variable, s (you can name this whatever you like),
    # will contain the NEXT item in the list.
    # after the last item in the list has been reached, the loop will end.
    # the first time through the loop, s = ["Religion", "8:00am"] (which is a list).
    # The next time through the loop, s = ["Math", "10:00am"] (which is a list) etc.
    for s in monday_class_schedule:
        print(s)

    # ok - think about what was just printed - why did it look ugly also?
    # it's because each item in the list...*is* a list, and when you print a list, it looks kind of ugly!
    # how can we make it look cleaner?
    for s in monday_class_schedule:
        # again, 's' is going to contain a list for each item in the list.
        # so, the first time through the loop, s = ["Religion", "8:00am"]. The next time through the loop, s = ["Math", "10:00am"] etc.
        # Now, remember from earlier in this lesson how we get items from a list?
        # we use indexes. In this list, class name is in location 0, and time is in location 1
        class_name = s[0]
        time = s[1]
        print(f"{class_name} meets at {time}")

    # we can also get tricky and do something like this:
    second_class = monday_class_schedule[1]
    # 'second_class' will now contain the 2nd item (remember, python is 0-based) in the list, which is ["Math", "10:00am"].
    # let's make sure that's what we got:
    print(second_class)
    # now we can do this:
    class_name = second_class[0]
    time = second_class[1]
    print(f"{class_name} meets at {time}")
    # do you see how that works?

    # and finally, we can simplify that a bit more, like this:
    # here, we're getting the 2nd (index=1) element from the class schedule list (monday_class_schedule[1]),
    # then we're getting the FIRST and SECOND item out of the list ([0] and [1])
    class_name = monday_class_schedule[0][0]
    time = monday_class_schedule[1][1]
    print(f"{class_name} meets at {time}")
    # make sure you understand what is happening here before moving on to the next lesson


if __name__ == "__main__":
    main()