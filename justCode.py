import math
import matplotlib.pyplot as plt
import numpy as np

def solution(x):
    return (1/x) + 1 #если сделать + 2, то будет видно, что графики действительно наложились

def function(x, y):
    return (-1) / (pow(x, 2))#(-1) /(y * pow(x, 2))

#пусть х0 - неизменяеммый старт
def EulerMethod (x0, y0, end_x, h):
    fig2 = plt.Figure
    fig2, ax2 = plt.subplots()
    all_x = []
    all_y = []
    all_x.append(x0)
    all_y.append(y0)

    sol_all_y = []
    sol_all_y.append(y0)

    i = 0
    while (all_x[i] < end_x):#(x1 < x1 + 2):
        all_x.append(all_x[i] + h)#справебыдло добавляю некст х
        all_y.append(all_y[i] + h * function(all_x[i], all_y[i]))#добавляю некст у

        sol_all_y.append((solution(all_x[i])))
        i += 1
    ax2.grid()
    ax2.plot(all_x, all_y)
    ax2.plot(all_x, sol_all_y)
    fig2.savefig('F:/MatModelingEulerSolution.png')
    print("Euler's Method:")
    print(all_x[i], " ", all_y[i])

    realSolution = 1.25
    error = abs(realSolution - all_y[i])
    print("Error: ", error)

def EulerMidpointMethod (x0, y0, end_x, h):
    fig2 = plt.Figure
    fig2, ax2 = plt.subplots()
    all_x = []
    all_y = []
    all_x.append(x0)
    all_y.append(y0)

    sol_all_y = []
    sol_all_y.append(y0)

    i = 0
    while (all_x[i] < end_x):#(x1 < x1 + 2):
        all_x.append(all_x[i] + h)#справебыдло добавляю некст х
        all_y.append(all_y[i] + h * function(all_x[i] + h/2, all_y[i] +
                                             (h/2) * function(all_x[i], all_y[i])))#добавляю некст у

        sol_all_y.append((solution(all_x[i])))
        i += 1
    ax2.grid()
    ax2.plot(all_x, all_y)
    ax2.plot(all_x, sol_all_y)
    fig2.savefig('F:/MatModelingEulerWithReCountingSolution.png')
    print("Euler's midpoint Method:")
    print(all_x[i], " ", all_y[i])

    realSolution = 1.25
    error = abs(realSolution - all_y[i])
    print("Error: ", error)

def RungeKuttaMethod (x0, y0, end_x, h):
    fig2 = plt.Figure
    fig2, ax2 = plt.subplots()
    all_x = []
    all_y = []
    all_x.append(x0)
    all_y.append(y0)

    sol_all_y = []
    sol_all_y.append(y0)

    i = 0
    while (all_x[i] < end_x):  # (x1 < x1 + 2):
        all_x.append(all_x[i] + h)  # справебыдло добавляю некст х
        k1 = h * function(all_x[i], all_y[i])
        k2 = h * function(all_x[i] + h/2, all_y[i] + k1/2)
        k3 = h * function(all_x[i] + h/2, all_y[i] + k2/2)
        k4 = h * function(all_x[i] + h, all_y[i] + k3)
        err_y = (k1 + 2 * k2 + 2 * k3 + k4)/6
        all_y.append(all_y[i] + err_y)  # добавляю некст у

        sol_all_y.append((solution(all_x[i])))
        i += 1
    ax2.grid()
    ax2.plot(all_x, all_y)
    ax2.plot(all_x, sol_all_y)
    fig2.savefig('F:/MatModelingRungeKuttaSolution.png')
    print("Runge-Kutta's method:")
    print(all_x[i], " ", all_y[i])

    realSolution = 1.25
    error = abs(realSolution - all_y[i])
    print("Error: ", error)

x0 = 1
y0 = 2
a = x0
b = 4
n = 1000000
h = (b - a) / n

EulerMethod(x0, y0, b, h)
EulerMidpointMethod(x0, y0, b, h)
RungeKuttaMethod(x0, y0, b, h)

