import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)

mean = sum(dice_result) / len(dice_result)
standard_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

first_std_start, first_std_end = mean - standard_deviation, mean + standard_deviation
second_std_start, second_std_end = mean - (2 * standard_deviation), mean + (2 * standard_deviation)
list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_start and result < first_std_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_start and result < second_std_end]

print("Mean is " + str(mean))
print("Standard deviation is " + str(standard_deviation))
print("Median is " + str(median))
print("Mode is " + str(mode))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))

fig = ff.create_distplot([dice_result], ["Result"], show_hist = False)
fig.add_trace(go.Scatter(
    x = [mean, mean],
    y = [0, 0.17],
    mode = "lines",
    name = "MEAN"
))
fig.add_trace(go.Scatter(
    x = [first_std_start, first_std_start],
    y = [0, 0.17],
    mode = "lines",
    name = "STANDARD DEVIATION 1"
))
fig.add_trace(go.Scatter(
    x = [first_std_end, first_std_end],
    y = [0, 0.17],
    mode = "lines",
    name = "STANDARD DEVIATION 1"
))
fig.add_trace(go.Scatter(
    x = [second_std_start, second_std_start],
    y = [0, 0.17],
    mode = "lines",
    name = "STANDARD DEVIATION 2"
))
fig.add_trace(go.Scatter(
    x = [second_std_end, second_std_end],
    y = [0, 0.17],
    mode = "lines",
    name = "STANDARD DEVIATION 2"
))
fig.show()