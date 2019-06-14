
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matplotlib.rcParams.update({'font.size': 30})

def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

###############################################################################

fig1 = plt.figure()
fig1.set_size_inches(9, 7)

x = np.linspace(0, 4*np.pi, 101)
y = np.sin(x)
data = np.array([x, y])
l, = plt.plot([], [], 'b-', linewidth=8)
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
plt.xlim(-0.2, 4*np.pi + 0.2)
plt.ylim(-1 - 0.2, 1 + 0.2)
plt.xlabel('Posição da Bobina')
plt.ylabel('Tensão elétrica')
plt.grid(True)
line_ani = animation.FuncAnimation(fig1, update_line, 101, fargs=(data, l),
                                   interval=20, blit=True)

line_ani.save('senoide.mp4')

plt.show()
