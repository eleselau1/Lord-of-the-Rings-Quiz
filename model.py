# user_choices = []
# user_choices.append(weather).append(hobby).append(treasure)
# loop over the list to see if a particular place has a clear majority number (in this case, it would be 2/3). Then make conditional statements such as "Mordor" >= 2, return "You will live best in Mordor"

def place(weather, hobby, treasure):
  if weather == "mordor" and hobby == "mordor":
    return "You will live best in Mordor!"
  elif weather == "mordor" and treasure == "mordor":
    return "You will live best in Mordor!"
  elif hobby == "mordor" and treasure == "mordor":
    return "You will live best in Mordor!"
  elif weather == "gondor" and hobby == "gondor":
    return "You will live best in Gondor!"
  elif weather == "gondor" and treasure == "gondor":
    return "You will live best in Gondor!"
  elif hobby == "gondor" and treasure == "gondor":
    return "You will live best in Gondor!"
  elif weather == "rivendell" and hobby == "rivendell":
    return "You will live best in Rivendell! Time to learn Elvish."
  elif weather == "rivendell" and treasure == "rivendell":
    return "You will live best in Rivendell! Time to learn Elvish."
  elif hobby == "rivendell" and treasure == "rivendell":
    return "You will live best in Rivendell! Time to learn Elvish."
  elif weather == "shire" and hobby == "shire":
    return "You will live best in the Shire! Enjoy the simple life of hobbits."
  elif weather == "shire" and treasure == "shire":
    return "You will live best in the Shire! Enjoy the simple life of hobbits."
  elif hobby == "shire" and treasure == "shire":
    return "You will live best in the Shire! Enjoy the simple life of hobbits."
  elif weather == "rohan" and hobby == "rohan":
    return "You will live best in Rohan!"
  elif weather == "rohan" and treasure == "rohan":
    return "You will live best in Rohan!"
  elif hobby == "rohan" and treasure == "rohan":
    return "You will live best in Rohan!"
    
  else:
    return "You could live anywhere in Middle Earth"