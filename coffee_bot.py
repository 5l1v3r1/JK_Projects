#Define your functions
def get_drink_type():
  res = input('What type of drink would you like \n[a] Brewed Coffe \n[b] Mocha \n[c] Latte \n')
  if res == 'a':
    return "Brewed Coffe"
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return 'Latte'
  else:
    print_message()
    return get_drink_type()

#Defines cream preferance
def cream_pref():
  res = input('And what kind of milk for your drink? \n[a] None \n[b] 2% milk \n[c] Non-fat milk \n[d] Soy milk \n[e] Almond milk \n')
  if res == 'a':
    return "None"
  elif res == 'b':
    return '2% milk'
  elif res == 'c':
    return 'non-fat milk'
  elif res == 'd':
    return 'Soy milk'
  elif res == 'e':
    return 'Almond milk'
  else:
    print_message()
    return milk_pref()

#Error message used to loop selection.
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

#Defines available sizes
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n')
  if res == 'a':
    return "small"
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

#Runs Coffee order
def coffee_bot():
  print("Welcome to the cafe!")
  drink_type = get_drink_type()
  size = get_size()
  cream = cream_pref()
  name = input("Can i get your name please \n[]")
  print("Alright, that's a " + size, drink_type + " with " + cream)
  print("Thanks, " + name + "! Your drink will be ready shortly.")

coffee_bot()
