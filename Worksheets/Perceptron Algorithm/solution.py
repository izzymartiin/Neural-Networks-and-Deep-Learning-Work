import random

def load_data(filename):
    with open(filename, "r") as f:
        data = [line.strip().split(",") for line in f]
    column1 = []
    column2 = []
    column3 = []
    for i in range (1, len(data)):
        column1.append(int(data[i][0]))
        column2.append(int(data[i][1]))
        column3.append(int(data[i][2]))
    return tuple(column1), tuple(column2), tuple(column3)

age, hg, cls = load_data("stroke_separable.csv")

def perceptron(age, hg, cls):

    random.seed(10)
    w0 = random.random()
    w_age = random.random()
    w_hg = random.random()

    N = 25
    for i in range(0, N):

        index_x = random.randint(0, len(age)-1)
        x = [age[index_x], hg[index_x]]
        print(index_x)
    
        dot_product = x[0]*w_age + x[1]*w_hg + w0

        if cls[index_x] == 0:
            if dot_product < 0:
                continue
            else:
                w0 -= 1
                w_age -= x[0]
                w_hg -= x[1]
        elif cls[index_x] == 1:
            if dot_product >= 0:
                continue
            else:
                w0 += 1
                w_age += x[0]
                w_hg +=x[1]

    return w0, w_age, w_hg

w0, w_age, w_hg = perceptron(age, hg, cls)

print(w0, w_age, w_hg)
