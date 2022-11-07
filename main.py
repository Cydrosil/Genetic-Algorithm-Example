import random
import copy

def value_generator(v_range, quantity):
    generated_values = []
    for x in range(quantity):
        while True:
            num = random.randint(0, v_range)
            if num  not in generated_values:
                break;
        generated_values.append(num)
    generated_values.sort()
    return generated_values

def genetic_Algorythm(generated_values, size_population, iterations):
    print("Creating population")
    population = []
    for x in range(size_population):
        population.append(copy.deepcopy(generated_values))
        random.shuffle(population[x])
    # print(population)

    best_arrangement = copy.deepcopy(population[0])
    best_arrangement_score = 0

    for i in range(iterations):

        ranking = []

        for idx, x in enumerate(population):
            score = 0
            for r in range(len(x)-1):
                score += abs(x[r] - x[r+1])
            ranking.append(score)
            if score > best_arrangement_score:
                best_arrangement = x
                best_arrangement_score = score
                print("Better score found: ", best_arrangement_score, "By individual: ", idx, " -> ", population[idx])
        # print("Ranking: ", ranking)
        # print("Population pre ranking:")
        # for x in population:
        #     print(x)
        population = [x for _,x in sorted(zip(ranking,population), reverse = True)]
        # print("Population post ranking:")
        # for x in population:
        #     print(x)

        new_population = []

        for x in population:
            parent_1 = copy.deepcopy(population [random.randint(0,int(len(population)*0.1))])
            parent_2 = copy.deepcopy(x)

            cut_points = []
            cut_points.extend([random.randint(0, len(x)), random.randint(0, len(x))])
            cut_points.sort()

            child = []
            dna_1 = []
            dna_2 = []

            for g in range(cut_points[0], cut_points[1]):
                dna_1.append(parent_1[g])
            dna_2 = [item for item in parent_2 if item not in dna_1]
            child = dna_1 + dna_2

            # print("\nParent 1: ", parent_1, "\nParent 2: ", parent_2)
            # print("Genetic cut points: ", cut_points)
            # print("Dna 1: ", dna_1,"\nDna 2: ", dna_2)
            # print("Child: ", child)

            for switch in range(len(child)):
                if random.random() < 0.05:
                    switch_with = random.randint(0,len(child)-1)
                    gene_1, gene_2 = child[switch], child[switch_with]
                    # print("Mutation performed, gene 1 ", gene_1, " switched with gene 2 ", gene_2)
            # print("Child: ", child)

            new_population.append(child)
        new_population[len(new_population)-1] = best_arrangement
        population = copy.deepcopy(new_population)

    return best_arrangement, best_arrangement_score

generated_values = value_generator(10, 5)

score = 0
for x in range(len(generated_values)-1):
    score += abs(generated_values[x] - generated_values[x+1])

print("Starting values = ", generated_values)
print("Starting score = ", score)

best_arrangement, best_arrangement_score = genetic_Algorythm(generated_values, 10, 4)

print("Genetic Algorythm: ", best_arrangement)
print("Genetic Algorythm Score: ", best_arrangement_score)