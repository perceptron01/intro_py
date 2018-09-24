def get_description():
    """
    select weather randomly
    """
    
    from random import choice
    possibilities = ["rain", "snow", "sleet", "fog", "sun", "unknow"]
    return choice(possibilities)