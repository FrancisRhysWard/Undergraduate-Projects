import random
 
class Prisoner():
    """
    A class for a prisoner.

    Attributes:
        - choice - betray or confess (a boolean variable)
        - years (a count of the prisoners sentence)
        - strategy (a list of the prisoners choices)

    Methods:
        - __init__
        - optimist (a method that makes a prisoner confess until the opponent betrays)
        - tit_for_tat (a method that causes a prisoner's choice to be the opponent's last choice)
        - random_choice (a method that randomly makes the prisoner's choice True or False)
    """
    def __init__(self, choice, years, strategy):
        self.choice = choice
        self.years = 0
        self.strategy = []
        self.switch = False  #used in the optimist strategy
    def optimist(self, Player, Opponent):
        if self.switch == True:  #innately false 
            return True          #Player.choice == True
        for c in Opponent.strategy:  #Checks items in the opponents strategy
            if c == 'b':  #if they have betrayed once
                self.switch == True  #switch == True and Player loses faith in humanity and betrays from now on
                return True  #Player.choice == True
        return False  #otherwise Player.choice == False and Player confesses
    def tit_for_tat(self, Player, Opponent):
        if Opponent.strategy == []:  #first iteration where the opponent has not yet chosen
            return random.choice([True, False])  #gives a random True or False, either 'b' or 'c' is appended to Player's strategy
        if Opponent.strategy[-1] == 'b':  #if the last choice by opponent was betray
            return True  #Player betrays
        return Player.choice == False  #if opponent's last move was 'c' then Player confesses
    def random_choice(self):
        return random.choice([True, False])  #Player randomly betrays or confesses
   
r = random.choice([True, False])
p1 = Prisoner(r, 0, 0)  #an instance of the Prisoner class with random choice
p2 = Prisoner(r, 0, 0)  #an instance of the Prisoner class with random choice
 
def game_v_random(Player, Opponent):
    """
    A function that gets two prisoners to play one game with random choices

    Arguments:
        Player: an instance of the Prisoner class
        Opponent: an instance of the Prisoner class

    Output:
        The prisoners years, and their strategy
    """
    Opponentchoice = Opponent.random_choice()  #boolean variable - a random choice for this game
    Playerchoice =  Player.random_choice()  #boolean variable - a random choice for this game
    if Playerchoice and Opponentchoice:  #if both boolean's == True
        Player.strategy.append('b')  #Player betrays
        Opponent.strategy.append('b')  #and Opponenet betrays
        Player.years += 3
        Opponent.years += 3    #so they both get 3 years added to their sentence
    if Playerchoice == False and Opponentchoice == False:  #they both confess
        Player.strategy.append('c')
        Opponent.strategy.append('c')  #'c' appended to both prisoner's strategy
        Player.years += 2
        Opponent.years += 2  #2 years each
    if Playerchoice and Opponentchoice == False:  #Player betrays and Opponent confesses
        Player.strategy.append('b')  #append 'b' to Player's strategy
        Opponent.strategy.append('c')  #append 'c' to Opponent's strategy
        Opponent.years += 4   #Opponent gets 4 years added to their years count but Player gets no years added
    elif Playerchoice == False and Opponentchoice:
        Player.strategy.append('c')  #append 'c' to Player's strategy
        Opponent.strategy.append('b')  #append 'b' to Opponent's strategy
        Player.years += 4  #Player gets 4 years added to their years count but Opponent gets no years added
    return Player.years, Opponent.years, Player.strategy, Opponent.strategy  #the function returns Both players years count, and their strategy list
 
def game_v_optimist(Player, Opponent):
    """
    A function that gets two prisoners to play one game, one with a random choice, the other with the optimist's choice

    Arguments:
        Player: an instance of the Prisoner class
        Opponent: an instance of the Prisoner class

    Output:
        The prisoners' years, and their strategys
    """
    Opponentchoice = Opponent.random_choice()  #boolean variable - a random choice for this game
    Playerchoice = Player.optimist(Player, Opponent)  #boolean variable - Player's choice decided by the optomist method
    if Playerchoice and Opponentchoice:  #if both prisoners betray (choice == True)
        Player.strategy.append('b')
        Opponent.strategy.append('b')  #append 'b' to both prisoners' strategy
        Player.years += 3
        Opponent.years += 3    #add 3 years to both counts
    if Playerchoice == False and Opponentchoice == False:  #they both confess
        Player.strategy.append('c')
        Opponent.strategy.append('c')  #append 'c' to both prisoners' strategy
        Player.years += 2
        Opponent.years += 2  #add 2 years to both counts
    if Playerchoice and Opponentchoice == False:  #Player betrays (Player.optimist(Player, Opponent) == True) and Opponent confesses (Opponent.random_choice() == False)
        Player.strategy.append('b')  #Player betrays
        Opponent.strategy.append('c')  #Opponent confesses
        Opponent.years += 4   #Opponent gets 4 more years and Player gets no more years added
    elif Playerchoice == False and Opponentchoice: 
        Player.strategy.append('c')  #append 'c' to Player's stategy
        Opponent.strategy.append('b')  #append 'b' to Opponent's strategy
        Player.years += 4  #Player gets 4 more years and Opponent gets no more years added
    return Player.years, Opponent.years, Player.strategy, Opponent.strategy   #the function returns Both players years count, and their strategy list
 
def tit_for_tat_game(Player, Opponent):
    """
    A function that gets two prisoners to play one game, one with a random choice, the other with the tit_for_tat choice

    Arguments:
        Player: an instance of the Prisoner class
        Opponent: an instance of the Prisoner class

    Output:
        The prisoners' years, and their strategys
    """
    Opponentchoice = Opponent.random_choice()  #boolean variable - Opponent has a randomly True or False choice for this game
    Playerchoice = Player.tit_for_tat(Player, Opponent)  #boolean variable - Player's choice decided by the tit_for_tat method
    if Playerchoice and Opponentchoice:  #if both prisoners betray (choice == True)
        Player.strategy.append('b')
        Opponent.strategy.append('b')  #append 'b' to both prisoners' strategy
        Player.years += 3
        Opponent.years += 3    #add 3 years to both counts
    if Playerchoice == False and Opponentchoice == False:  #both confess
        Player.strategy.append('c')
        Opponent.strategy.append('c')
        Player.years += 2
        Opponent.years += 2  #2 years each
    if Playerchoice and Opponentchoice == False:  #Player betrays and Opponent confesses
        Player.strategy.append('b')
        Opponent.strategy.append('c')
        Opponent.years += 4    #Opponent gets 4 years
    elif Playerchoice == False and Opponentchoice:  #Player.tit_for_tat(Player, Opponent) == False and Opponent.random_choice() == True
        Player.strategy.append('c')
        Opponent.strategy.append('b')
        Player.years += 4  #Player gets 4 years
    return Player.years, Opponent.years, Player.strategy, Opponent.strategy   #the function returns Both players years count, and their strategy list

def tit_for_tat_v_optimist(Player, Opponent):
    """
    A function that gets two prisoners to play one game, one with a random choice, the other with the optimist's choice

    Arguments:
        Player: an instance of the Prisoner class
        Opponent: an instance of the Prisoner class

    Output:
        The prisoners' years, and their strategys
    """
    Opponentchoice = Opponent.tit_for_tat(Player, Opponent)  #boolean variable - Opponent's choice decided by the tit_for_tat method
    Playerchoice = Player.optimist(Player, Opponent)  #boolean variable - Player's choice decided by the optomist method
    if Playerchoice and Opponentchoice:  #if both prisoners betray (choice == True)
        Player.strategy.append('b')
        Opponent.strategy.append('b')  #append 'b' to both prisoners' strategy
        Player.years += 3
        Opponent.years += 3    #add 3 years to both counts
    if Playerchoice == False and Opponentchoice == False:  #they both confess
        Player.strategy.append('c')
        Opponent.strategy.append('c')  #append 'c' to both prisoners' strategy
        Player.years += 2
        Opponent.years += 2  #add 2 years to both counts
    if Playerchoice and Opponentchoice == False:  #Player betrays (Player.optimist(Player, Opponent) == True) and Opponent confesses (Opponent.random_choice() == False)
        Player.strategy.append('b')  #Player betrays
        Opponent.strategy.append('c')  #Opponent confesses
        Opponent.years += 4   #Opponent gets 4 more years and Player gets no more years added
    elif Playerchoice == False and Opponentchoice: 
        Player.strategy.append('c')  #append 'c' to Player's stategy
        Opponent.strategy.append('b')  #append 'b' to Opponent's strategy
        Player.years += 4  #Player gets 4 more years and Opponent gets no more years added
    return Player.years, Opponent.years, Player.strategy, Opponent.strategy   #the function returns Both players years count, and their strategy list

def iterate_rand(n, Player, Opponent):
    '''
    A function which is an iterive version of game_v_random that plays the game n times and returns the strategy lists of choices made by each player
    '''
    for i in range(n):  #for integers in range (0, n]
        game_v_random(Player, Opponent)  #play the game - i.e. plays the game n times 
    return Player.years, Opponent.years, Player.strategy, Opponent.strategy  #returns the cumulitive scores - the total amount of years each player has recieved and each players strategy (list of choices)
 
def iterate_opt(n, Player, Opponent):
    '''
    A function which is an iterive version of game_v_optimist that plays the game n times
    '''
    for i in range(n):
        game_v_optimist(Player, Opponent)  #plays the game_v_optimist n times
    if Player.years < Opponent.years:  #if Player has fewer years than Opponent
        print 'Optimist wins.'  #Player wins
    elif Player.years > Opponent.years:  #or Player has more years accumulated
        print 'Random wins.'  #and Opponent wins
    else:
        print 'Draw.'  #otherwise they have the same number of years and draw
    return Player.years, Opponent.years, Player.strategy, Opponent.strategy  #returns the cumulitive scores - the total amount of years each player has recieved and each players' strategy (list of choices)

def iterate_tit_for_tat(n, Player, Opponent):
    '''
    A function which is an iterative version of tit_for_tat_game that plays the game n times
    '''
    for i in range(n):
        tit_for_tat_game(Player, Opponent)  #plays the tit_for_tat_game n times
    if Player.years < Opponent.years:  #if Player has fewer years than Opponent
        print 'Player wins.'  #Player wins
    elif Player.years > Opponent.years:  #or Player has more years accumulated
        print 'Random wins.'  #and Opponent wins
    else:
        print 'Draw.'  #otherwise they draw
    return Player.years, Opponent.years, Player.strategy, Opponent.strategy  #returns the cumulative scores - the total amount of years each player has recieved and each players' strategy (list of choices)

def iterate_opt_v_tit(n, Player, Opponent):
    '''
    A function which is an iterive version of game_v_optimist that plays the game n times
    '''
    for i in range(n):
        tit_for_tat_v_optimist(Player, Opponent)  #plays the tit_for_tat_v_optimist n times
    if Player.years < Opponent.years:  #if Player has fewer years than Opponent
        print 'Optimist wins.'  #Player wins
    elif Player.years > Opponent.years:  #or Player has more years accumulated
        print 'Tit_for_tat wins.'  #and Opponent wins
    else:
        print 'Draw.'  #otherwise they have the same number of years and draw
    return Player.years, Opponent.years, Player.strategy, Opponent.strategy  #returns the cumulitive scores - the total amount of years each player has received and each players' strategy (list of choices) 
