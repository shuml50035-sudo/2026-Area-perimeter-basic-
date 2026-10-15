def num_check (question):

    error = "please enter a number that is more than zero\n "
    while True:

            try:
                # ask user for a number

                response = float (input(question))

                # check that the number is more than zero
                if response > 0:
                  return response
                else:
                    print(error)

            except ValueError:
                print(error)


# main routine start here...

keep_going=""
while keep_going == "":

    # get width and height
    width = num_check("width: ")
    height = num_check("height: ")
    cost = num_check("cost: ")

    # calculate perimeter and price for the fence
    perimeter = 2 * (width + height)
    price = (perimeter * cost)

    # display output
    print()
    print(f"perimeter:{perimeter} units")
    print(f"price:${price:.2f }")