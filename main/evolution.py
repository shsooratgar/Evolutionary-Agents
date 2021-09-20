import random
from copy import deepcopy

from player import Player
import numpy as np
from config import CONFIG

standard_noise_div_weights = 1.0  # best =1
standard_noise_div_biases = 0.8  # best =0.8

scenario1 = True  # scenario one is only mutation without cross over and if is False, means cross over and mutation

b = 0


def cross_over(parent1, parent2):
    babe = deepcopy(parent1)
    babe.nn.w2 = parent2.nn.w2
    babe.nn.b2 = parent2.nn.b2
    return babe


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO
        # child: an object of class `Player`
        child.nn.w1 += np.random.normal(0, standard_noise_div_weights, child.nn.w1.shape)
        child.nn.w2 += np.random.normal(0, standard_noise_div_weights, child.nn.w2.shape)

        child.nn.b1 += np.random.normal(0, standard_noise_div_biases, child.nn.b1.shape)
        child.nn.b2 += np.random.normal(0, standard_noise_div_biases, child.nn.b2.shape)

        return child

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            fitnesses = []
            for pervert in prev_players:
                fitnesses.append(pervert.fitness ^ 4)

            if scenario1:
                chosen = random.choices(prev_players, weights=fitnesses, cum_weights=None, k=num_players)
                babies = []
                for parent in chosen:
                    babies.append(self.mutate(deepcopy(parent)))

            else:
                chosen = random.choices(prev_players, weights=fitnesses, cum_weights=None, k=num_players * 2)
                babies = []
                for i in range(num_players):
                    babies.append(cross_over(chosen[i * 2], chosen[i * 2 + 1]))

                for baby in babies:
                    self.mutate(baby)

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover
            # new_players = prev_players
            # return new_players
            return babies

    def next_population_selection(self, players, num_players):

        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        players.sort(key=lambda x: x.fitness, reverse=True)
        my_players = players[: num_players]





        # TODO (additional): plotting

        summation = 0
        for player in players:
            summation += player.fitness

        mean = summation / len(players)
        min = players[len(players) - 1].fitness
        max = players[0].fitness
        if max > b:
            bp = players[0]

        players.insert(0, bp)

        with open('results.txt', 'a') as file:
            file.write(str(min) + "   ")
            file.write(str(mean) + "   ")
            file.write(str(max) + "   ")

            file.write("\n")
        file.close()

        # TODO (additional): a selection method other than `top-k`
        # probability = []
        # tmp =0
        # for p in players:
        #     tmp += (p.fitness/summation)
        #     probability.append(tmp)
        # my_players =[]
        # for i in range(num_players):
        #     probability_sel = random.uniform(0,1)
        #     for j,prob in enumerate(probability):
        #         if prob > probability_sel:
        #             my_players.append(deepcopy(players[j]))
        #             break

        return my_players
