# """Movie theatre ticketing system - v6
# Update totals
# Created by James Mulholland"""


#Component 6 print summary
def print_summary(tickets_sold, adult_ticket, student_ticket, child_ticket, gift_ticket, total_sales):
    print("="*45)
    print(f"The total tickets sold today was {tickets_sold}\n"
          f"This was made up of: \n"
          f"\t{adult_ticket} for adults; and\n"
          f"\t{student_ticket} for students; and \n"
          f"\t{child_ticket} for children; and \n"
          f"\t{gift_ticket} for gift vouchers \n"
          f"Sales for the day came to ${total_sales}:.2f")
    print("="*45)





# Component 4 - Confirm order
def confirm_order(ticket, number, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nYou have ordered {number} {ticket} ticket(s)"
                        f"at a cost of ${cost * num_tickets:.2f}\n"
                        f"'Y' or 'N': ")
        if confirm == "Y":
            return  True

        else:
            return False


# Component 3 - Calculate ticket price
def get_price(type_):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Component 1 - Welcome screen and set up variables
def sell_ticket():
    print("********** Panfare Movies - ticketing system **********\n")

adult_ticket = 0
student_ticket = 0
child_ticket = 0
gift_ticket = 0
tickets_sold = 0
total_sales = 0


# component 2 - Get the category and number of tickets required

ticket_wanted = "Y"
while ticket_wanted == "Y":
    ticket_type = input("What kind of ticket do you want: \n"
                        "\t'A' for Adult, or\n"
                        "\t'S' for Student, or\n"
                        "\t'C' for Child, or\n"
                        "\t'G' for Gift Voucher\n"
                        ">> ").upper()
    num_tickets = int(input(f"How many {ticket_type} tickets do you want: "
                                         f""))
    cost = get_price(ticket_type)

    if confirm_order(ticket_type, num_tickets, cost):
        print("Order confirmed")

        # Component 5 - update totals
        total_sales += cost * num_tickets
        tickets_sold += num_tickets
        if ticket_type == "A":
            adult_ticket += num_tickets
        elif ticket_type == "S":
            student_ticket += num_tickets
        elif ticket_type == "C":
            child_ticket += num_tickets
        else:
            gift_ticket += num_tickets
    else:
        print("Order cancelled")

    ticket_wanted = input(" Do you want to sell another ticket? Y/N: "
                          "").upper()

    # Component 6 - produce summary of sales
    print_summary(tickets_sold, adult_ticket, student_ticket, child_ticket, gift_ticket, total_sales)


# Main routine
sell_ticket()
print("Goodbye\nThanks for using Panfare Movies")






