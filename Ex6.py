from math import sqrt

# calculate euclidean distance
def e_distance(row1, row2):
    d = 0.0
    for i in range(len(row1)-1):
        d += (row1[i] - row2[i])**2
    return sqrt(d)

# locate most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        d = e_distance(test_row, train_row)
        distances.append((train_row, d))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append((distances[i][0]))
    return neighbors

# make a classification prediction with neighbors
def predict_class(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

# test distance function
dataset = [[2.7856, 3.6589, 0],
    [5.4268, 6.39698, 0],
    [6.9870, 2.39887, 0],
    [9.2014, 5.1478, 1],
    [4.8975, 2.59874, 1],
    [1.58547, 3.6542, 0]]

prediction = predict_class(dataset, dataset[0], 3)
print('expected %d, got %d.' % (dataset[0][-1], prediction))