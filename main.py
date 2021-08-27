from matplotlib import pyplot as plt
import time


xv = []
yv = []
print('\t***Data Plotter***\n')
print('Instructions:\t1)Type your x-values.Then type \'end\' when finished\n')
print('             \t2)Type your y-values.Then type \'end\' when finished\n')
print('=> You will see the plot :)\n')
x_name=input('Whats your x-values\' name?\n')
print('\nX-values?\n')
while True:
    a=input()
    if a == 'end':
        break
    elif not a.isdigit():
        print('Just numbers!!!')
        time.sleep(3)
        exit(0)
    else:
        xv.append(float(a))
        print('next:')
y_name = input('Whats your y-values\' name?\n')
print('\ny-values?\n')
while True:
    b=input()
    if b == 'end':
        break
    elif not b.isdigit():
        print('Just numbers!!!')
        time.sleep(3)
        exit(0)
    else:
        yv.append(float(b))
        print('next:')
if len(xv) != len(yv):
    print('Datas dont match!')
    time.sleep(3)
    exit(0)
else:
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.plot(xv, yv, marker='o', color='r')
    plt.grid(True)
    plt.show()
