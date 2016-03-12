#This code will look into the strike Price table and check if any of the prices are up or down and send a text to the user

from stock.controllers.alerts import StrikePriceController
s = StrikePriceController()
s.run()
