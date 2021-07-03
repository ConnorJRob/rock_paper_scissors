from models.player import Player

class Game():

    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player


    def match(self):
        if self.first_player.choice == self.second_player.choice:
            return f"Tie - {self.first_player.name} and {self.second_player.name} both picked {self.first_player.choice}"
            #Rock vs Scissors
        elif self.first_player.choice == "rock" and self.second_player.choice == "scissors":
            return f"{self.first_player.name} wins by playing Rock over {self.second_player.name}'s Scissors"
            #Scissors vs Paper
        elif self.first_player.choice == "scissors" and self.second_player.choice == "paper":
            return f"{self.first_player.name} wins by playing Scissors over {self.second_player.name}'s Paper"
            #Paper vs Rock
        elif self.first_player.choice == "paper" and self.second_player.choice == "rock":
            return f"{self.first_player.name} wins by playing Paper over {self.second_player.name}'s Rock"
            #Scissors vs Rock
        elif self.first_player.choice == "scissors" and self.second_player.choice == "rock":
            return f"{self.second_player.name} wins by playing Rock over {self.first_player.name}'s Scissors"
            #Paper vs Scissors
        elif self.first_player.choice == "paper" and self.second_player.choice == "scissors":
            return f"{self.second_player.name} wins by playing Scissors over {self.first_player.name}'s Paper"
            #Rock vs Paper
        elif self.first_player.choice == "rock" and self.second_player.choice == "paper":
            return f"{self.second_player.name} wins by playing Paper over {self.first_player.name}'s Rock"