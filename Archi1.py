import random


def init():

    # accessing file for branch register
    branches = []
    branchAdresses = open("Branches.txt", "r")
    i = 0
    for branch in branchAdresses: 
        branches[i] = int(branch)
        i+=1
    
    # accessing file for prediction register
    predictions = []
    predictionsFile = open("Predictions.txt", "r")
    i = 0 
    for predict in predictionsFile:
        predictions[i] = int(predict)
        i+=1
    
    
    return branches, predictions


def branchPredictor(taken):

    predictions, branches = init()
    randomBranch = random.getrandbits(10)
    for branch in branches:
        memoryValue = branch ^ randomBranch
        print(f"branch = {memoryValue}")

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

    print(predictions)
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

    lines = ["0b00" + '\n' for _ in range(1024)]

    with open("Predictions.txt", "w") as file:
        file.writelines(lines)

branchPredictor(False)