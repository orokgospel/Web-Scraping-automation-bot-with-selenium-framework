from booking.booking import Booking
inst = Booking()
try:
    with Booking() as bot:
        # a=2/0
        bot.land_first_page()
        # print('Exiting')
        bot.change_currency(currency='USD')
        bot.select_place_to_go(input("Where do you want to go?"))
        bot.select_dates(check_in_date=input("What is the check in date?"),
                         check_out_date=input("What is the check out date?"))
        bot.select_adults(input=int(input("How many people?")))
        bot.click_search()
        bot.apply_filtrations()
        # print(len(bot.report_results()))
        bot.refresh()  # A work round to let our bot grab our data properly
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print('There is a problem running this programme from command line interface \n'
        'for windows: PATH=%PATH%;path_to_your_folder \n'
              'for Linux:PATH=$PATH:/path/to your folder/')
    else:
        raise
    