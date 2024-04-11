import random


def init():
    # accessing file for branch register
    branches = list()
    branchAdresses = open("Branches.txt", "r")

    for branch in branchAdresses:
        branch_split = branch.split("\n")[0]
        branches.append(bin(int(branch_split,2)))



    # accessing file for prediction register
    predictions = list()
    predictions_file = open("Predictions.txt", "r")

    for predict in predictions_file:
        predict_split = predict.split("\n")[0]
        predictions.append(bin(int(predict_split,2)))


    return branches, predictions


def branchPredictor(taken):
    branches, predictions = init()

    randomBranch = random.getrandbits(10)
    for branch in branches:

        memoryValue = branch ^ randomBranch
        if taken == True:
            if predictions[memoryValue] == 0b00:
                predictions[memoryValue] = 0b01
            if predictions[memoryValue] == 0b01:
                predictions[memoryValue] = 0b10
            if predictions[memoryValue] == 0b10:
                predictions[memoryValue] = 0b11
        else:
            if predictions[memoryValue] == 0b01:
                predictions[memoryValue] = 0b00
            if predictions[memoryValue] == 0b10:
                predictions[memoryValue] = 0b01
            if predictions[memoryValue] == 0b11:
                predictions[memoryValue] = 0b10

    lines = predictions

    with open("Predictions.txt", "w") as file:
        file.writelines(str(lines))


def random_10_bit():
    return "0b" + "".join(str(random.randint(0, 1)) for _ in range(10))


def random_2_bit():
    return "0b" + "00"


def generate_branches():
    lines = [random_10_bit() + '\n' for _ in range(2000)]

    with open("Branches.txt", "w") as file:
        file.writelines(lines)


def generate_predictions():
    lines = [random_2_bit() + '\n' for _ in range(1024)]

    with open("Predictions.txt", "w") as file:
        file.writelines(lines)

branchPredictor(False)