#!/usr/bin/env python3
#Sat Sep 27 16:13:10 2025 +0200, 5657e01
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import route_nyc 

### Given contour plot ###
n_fine = 100
t_fine = np.linspace(0, 24, n_fine)
x_fine = np.linspace(0, 60, n_fine)
tt_fine, xx_fine = np.meshgrid(t_fine, x_fine)
zz_fine = route_nyc.route_nyc(tt_fine,xx_fine)
w, h = plt.figaspect(0.4)
fig = plt.figure(figsize=(w, h))
plt.axes().set_aspect(0.2, adjustable='box')
cs = plt.contourf(tt_fine,xx_fine,zz_fine, 50, cmap=cm.get_cmap('jet'))
plt.xlabel('Time [hour of day]',fontsize=18)
plt.ylabel('Distance [km]',fontsize=18)
plt.title('Speed [km/h]',fontsize=18)
fig.colorbar(cs)
### 1B ###
# ADD PLOTTING OF TRAJECTORIES HERE 
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')

plt.plot(route_nyc.plotted_rumi_x, route_nyc.plotted_rumi_y, color = "white", lw = 5)
plt.plot(route_nyc.plotted_mira_x, route_nyc.plotted_mira_y, color = "black", lw = 5)

plt.annotate(text = "Rumi",color = "white",xy=(12, 40), size = 30)
plt.annotate(text = "Mira",color = "black",xy=(20, 40), size = 30)

plt.show()