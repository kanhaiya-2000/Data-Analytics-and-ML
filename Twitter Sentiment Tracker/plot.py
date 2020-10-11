import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    pullData = open('twitter-out.txt', 'r').read()
    lines = pullData.split('\n')
    xar = []
    yar = []
    x = 0
    y = 0

    for l in lines[-200:]:
        x += 1
        if 'pos' in l:
            y += 1
        else:
            y -= 1
        xar.append(x)
        yar.append(y)

    ax1.clear()
    ax1.plot(xar, yar)
    plt.xlabel('Tweets')
    plt.ylabel('Sentiments')

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
