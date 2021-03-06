from SoccerSimulator import Vector2D, SoccerState, SoccerAction
from SoccerSimulator import settings
from SoccerSimulator.strategies  import Strategy
from SoccerSimulator.mdpsoccer import SoccerTeam, Simulation
from SoccerSimulator.gui import SimuGUI,show_state,show_simu
import math


## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(),Vector2D.create_random())

## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",Strategy()) #Strategie qui ne fait rien
team2.add("Paul",RandomStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
