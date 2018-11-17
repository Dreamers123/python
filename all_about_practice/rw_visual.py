from random_walk_again import RamdomWalk
import matplotlib.pyplot as plt

while True:
    rw=RamdomWalk(5000)
    rw.fillwalk()
    plt.figure(dpi=128, figsize=(10, 6))
    points=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=points, cmap=plt.cm.Blues,
        edgecolor='none', s=1)
    plt.scatter(0,0,c='green',edgecolors='none',s=50)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=50)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_walking=input("Make a walk again?? (y/n)")
    if (keep_walking == 'n'):
        break
