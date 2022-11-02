# Slot Machines has 3 REELS (A B C) and after spinning presents 3 rows and 3 columns (can be changed dynamically).
# The idea is as above: 
##### A ######## B ######## C ######
#
### REEL1a --- REEL2a --- REEL3a ###
### REEL1b --- REEL2b --- REEL3b ###
### REEL1c --- REEL2c --- REEL3c ###
#
####################################
#REELS!=COLUMNS
# Any of the reels has got 14 symbols from the card decks symbols above. 
# When you spin the Slot Machine, for every column one of the 14 symbols of each REEL is picked randomly

# Importing modules
import random 

# Global constants to keep the program dynamic. Capitals letter is a convenction for constants
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Chosing the symbols used. Structuring as a dictionary
  #"\U00002660": 4  #Unicode char for hearts (not used actually)
symbol_count = {
  "♠": 5,
  "♥": 5,
  "♣": 5,
  "♦": 5
}

# Chosing a value for each symbol to multiply in case of winning with that symbol
symbol_multiplier = {
  "♠": 20,
  "♥": 15,
  "♣": 10,
  "♦": 7
}

# Function to store and return the money deposit as user input
def deposit():
  # Continually asking the user to enter the deposit until a valid amount is chosen
  while True:
    amount = input("What would you like to deposit? €")
    # Check if the inserted user input is a valid number
    if amount.isdigit(): #isdigit checks if the the variable is a whole number (only positive integers)
        amount = int(amount) # Convert amount into int type
        if amount > 0:                        
          break # if the amount is > 0 break the while loop 
        else:
          # Telling the user to try again with a valid number > 0
          print("Amount must be greater than 0.")
    else:
      # Telling the user to try again with a number
      print("Please enter an integer number.")
      # return the amount after reaching break
  return amount

# Function to ask the user how many lines of the slot machines he wants to bet on
def get_number_of_lines():
      # Continually asking the user to enter the lines to bet on until a valid numbers of lines is chosen
  while True:
    lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") #str concatenetion
    # Check if the inserted user input is a valid number
    if lines.isdigit(): # isdigit checks if the the variable is a whole number (only positive integers)
        lines = int(lines) # Convert lines into int type
        if 1 <= lines <= MAX_LINES: 
          break # if the lines are between 1 and MAX_LINES break the while loop and go to return
        else:
          # Telling the user to try again with a valid number > 0
          print("Enter a valid number of lines")
    else:
      # Telling the user to try again with a number
      print("Please enter an integer number between 1-" + str(MAX_LINES) + ") ")
      # return the lines after reaching break
  return lines

  # Function to ask the user how much he wants to bet on each line 
def get_bet():
  # Continually asking the user to enter the bet until a valid number is chosen
  while True:
    amount = input("How much would you like to bet for each line? € ")
    # Check if the inserted user input is a valid number
    if amount.isdigit(): # isdigit checks if the the variable is a whole number (only positive integers)
        amount = int(amount) # Convert amount into int type
        if MIN_BET <= amount <= MAX_BET:
          break # if the amount is between the min and max allowed break the while loop 
        else:
          # Telling the user to try again with a valid bet between the 
          print(f"Bet must be between {MIN_BET} - {MAX_BET}.") # str concat F string (from python 3.6 or above)
    else:
      # Telling the user to try again with a valid bet
      print("Please enter an integer number.")
      # return the amount after reaching break
  return amount

# Function to actually build the slot machine, requiring the rows and columns and the symbol used as parameters
# We need to generate what symbols is gonna be on each column based on the frequency of symbols that we have.
# Randomly pick the number of rows inside of each columns. So if it is 3 rown, we need 3 symbols from each REEL 
# that go inside each of the columns that we have.
def get_slot_machine_spin(rows, cols, symbols):
# Create a list that contains all of the different values we possibly could select from (14 in total)
    all_symbols = [] # List
    # For loop that is going to add however many symbols we have in the List. Since we are iterating through a 
    # dictionary we have to pass in the key and the values of that dictionary with the symbols and symbols count
    for symbols, symbol_count in symbols.items():
    #.items Gives both the key and the value associated with a dictionary:
    # symbols being the key, and symbol_count being the value associated with each key and use both of them rather 
    # then looping through the dictionary, only getting the keys and having to manually referencing the values.
      for _ in range(symbol_count):
      # _ is an anonymous variable. When we iterate through something and we don't need to keep the iteration 
      # number we can simply address the iteration with an anonymous variable.
        all_symbols.append(symbols)
        # Every time we get here, the all_symbols list is updated, adding the symbol at the end of the list. 
        # So we are going to append the Spades 2 times, the Hearts 3 times etc.. The number of times we append the 
        # symbol is given by the "range" of the symbol_count value
        # The output of this would be something like ["♠" 2times,"♥" 3times,"♣" 4times, "♦" 5times]
        # To show this iteration step by step uncomment the follow: 
      #print(all_symbols)

# Now that we have all the symbols list we need to select what value are going to go in every single columns,
# so basically randomly choosing three of those listed values. 
# ALSO, when we choose a value we want to remove it from the list. So if we have only 2 Spades we cannot get 3 in total.
    columns = [] # This List is going to be a nested list in the form of i.e:[['♥','♥','♣'],['♦','♦','♣'], ['♥','♥','♣']]
    for _ in range(cols):
      column = [] # This List is going to have 3 random generated symbols from the all_symbols list i.e: ['♦','♦','♣']
      current_symbols = all_symbols[:]  # Making a copy of the all_symbols list in order to not remove the symbols already choosed from the original list. : is the SLICE operator
      for _ in range(rows):
        value = random.choice(current_symbols) # Choose a random value from the copied list.
        current_symbols.remove(value) # Removing the choosen value from the copied list.
        column.append(value) # Append the current value to the column list. Output be like:
        # print(column)
      columns.append(column) # Append the current column to the columns list. Output be like:
      # print(columns)
    return columns

# Now we want a way to print this columns out --> so printing the actual output to the user.
# Right now we have an output something like this: [['♥','♥','♣'],['♦','♦','♣'], ['♥','♥','♣']]
# in which the first symbol of the first list (in this case: '♥') is the first symbol of the first row,
# the second symbol of the first list (in this case '♥') is the first symbol of the second row,
# the third symbol of the first list (in this case '♣') is the first symbol of the third row etc...
# So we need to "transpose" this out, to print properly the rows and the columns, obtaining the desired output:
# in this example would be: 
# ♥ ♦ ♥
# ♥ ♦ ♥
# ♣ ♣ ♣ --> LOL win!
# So let's define a function that do this.
def print_slot_machine(columns):
  # We need to determine the number of rows that we have based on our columns. The number of rows is the
  # number of elements in each of our columns. IF that is a column ['♥','♥','♣','♣'], we have 4 rows
    for row in range(len(columns[0])):  # The lenght of how many elements there are at position 0 of the list columns. It would work without this index but only when Cols=Rows
      for i, column in enumerate(columns): # Looping through every individual item inside each column
        # The if statement needed to print the Pipe character in order to separate symbols, 
        # but not print it if at the end of the line. The enumerate operator gives you the index as you loop through, as well as the item, in this case (0, column1), (1, column2), (2, column3), (3, column4)
        if i != len(columns) -1: #len(columns) is 3, we need indexes, so -1
          print(column[row], end=" | ") #end the print statement with the desired char, not allowing to add new line
        else:
          print(column[row], end="\n") #this would be the default end of a print statement \n = \new line
    # So, basically if i is not equale to the maximum index (which is 2)
    # print the pipe, otherwise don't print the pipe and go new line. 
    # In general, the whole function is a matrix transposition rowsXcols with
    # printing implementation added on the go.

# Function to check if there is a winning! 
# Due to how this code is structured, we can choose to bet in 1, 2 oe 3 
# of the Slot Machine. If we bet on 1 line, we are betting on the first only. # If there is a win in the other two lines, we lose anyway. If we bet on 2 # lines, those are only the first two lines. Etc..No implementation of "choosing which line you want to bet on". Yeah, that's evil :)
def check_winnings(columns, lines, bet, multiplier):
  winnings = 0  # Istantiate new variable
  winning_lines = [] # List empty
  for line in range(lines): #line changes dinamically. If we have bet 2 lines, line go 0 to 1 etc..
    symbol = columns[0][line] # Get the item at column0 at the current line (col0, line(i)) etc..
    for column in columns: # Looping through every columns
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break # Breaking if we found that the symbol we are checking is different from the current one. 
              #No need to go on..
    else:
      winnings += multiplier[symbol] * bet  # If all symbols are the same, apply multiplier to bet for each line
      winning_lines.append(line + 1)  #Append the line (row) number + 1, because of indexing
  return winnings, winning_lines # Returning 2 values

#Function that start a new game, calling the other functions and checking balance/bet relationships, 
# printing winnings, updating current balance.
#Also, it allows the player to play multiple round with one single execution of the programm
def spin(balance):
    lines = get_number_of_lines()
  # Checking if the amount to bet is in the range of the user balance
    while True:
      bet = get_bet()
      total_bet = bet * lines
      #Checking if the bet amount is valid --> inferior or equal to current balance
      if total_bet > balance:
        print(f"You do not have enough to bet that amount, your current balance is {balance}")
      else: 
        break
    print(f"You are betting {bet}€ on {lines} lines. Total bet is equal to {total_bet}€")
    slot = get_slot_machine_spin(ROWS,COLS,symbol_count) # Passing globald constantes as parameters
    print_slot_machine(slot)  # Printing rows and columns as wanted
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_multiplier)
    print(f"You won ${winnings}") #Calling hte first values of check_winnings()
    print(f"You won on lines:", *winning_lines) 
    # * is the splat operator and it is going to pass every single value of the List "winning_lines", 
    # or no values if the List is actually empty.
    return winnings - total_bet  #

# Main function of the program
def main():
  # Storing the user inputs calling the defined functions
    balance = deposit()
    while True:
      print(f"Current balance is: {balance}")
      answer = input("Press anything to play (q to Quit)")
      if answer == "q":
        break
      else:
        balance += spin(balance)  #Updating balance via spin(balance) function 
        # --> return (winning - total_bet). 

    print(f"You left with: {balance}")
main()


