# Shopping-Cart-Project
Shopping Cart Project - NYU

This is my version of the shopping cart program exercise. 

Fork the repository and create a virtual environment
    conda create -n shopping-env python=3.7

Then run the program
    python shoppingcart.py

Enter in the ID number for each product you wish to purchase, then type Done when finished.


shoppingcart-lc.py is the same general code, only the uses list comprehension at the end for the receipt, which I realized was necessary if the grocery story list skipped IDs (ie: the list of 2,4,8 would have broken my code, which required 1-20 sequential)