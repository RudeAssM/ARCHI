import random


def init():
    # accessing file for branch register
    branches = list()
    branchAdresses = open("Branches.txt", "r")

    for branch in branchAdresses:
        branch_split = branch.split("\n")[0]
        branches.append(int(branch_split,2))



    # accessing file for prediction register
    predictions = list()
    predictions_file = open("Predictions.txt", "r")

    for predict in predictions_file:
        predict_split = predict.split("\n")[0]
        predictions.append(int(predict_split,2))


    return branches, predictions


def branch_predictor(taken):
    branches, predictions = init()

    rand_str =  "0b" + "".join(str(random.randint(0, 1)) for _ in range(10))

    randomBranch =int(rand_str, 2)
    for branch in branches:

        memoryValue = (branch ^ randomBranch) % 1024
        if taken == True:
            if predictions[memoryValue] < 3:
                predictions[memoryValue] += 1
        else:
            if predictions[memoryValue] > 0:
                predictions[memoryValue] -= 1


    file = open("predictions.txt", "w")
    for entries in predictions:
        file.writelines(f"{bin(entries)}\n")


def random_10_bit():
    return "0b" + "".join(str(random.randint(0, 1)) for _ in range(10))


def random_2_bit():
    return "0b" + "00"


def generate_branches():
    lines = [random_10_bit() + '\n' for _ in range(5000)]

    with open("Branches.txt", "w") as file:
        file.writelines(lines)


def generate_predictions():
    lines = [random_2_bit() + '\n' for _ in range(1024)]

    with open("Predictions.txt", "w") as file:
        file.writelines(lines)
branch_predictor(False)