# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:36:52 2022

@author: pash
"""



import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

import cartopy.crs as ccrs
import cartopy.feature as cfeature


def my_rus_lat_formatter(x, pos):
    '''
    x - value
    pos - position
    '''
    print(x, pos)
    
    if x > 0:
        pos = '{}$^\circ$c.ш.'.format(x)
    elif x < 0:
        pos = '{}$^\circ$ю.ш.'.format(abs(x))
    elif x == 0:
        pos = '{}$^\circ$'.format(x)
        
    return pos


def my_rus_lon_formatter(x, pos):
    '''
    x - value
    pos - position
    '''
    print(x, pos)
    
    if x > 0:
        pos = '{}$^\circ$в.д.'.format(x)
    elif x < 0:
        pos = '{}$^\circ$з.д.'.format(abs(x))
    elif x == 0:
        pos = '{}$^\circ$'.format(x)
        
        
    return pos



data_crs=ccrs.PlateCarree()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-20, 60, -40, 45], crs=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)

gl = ax.gridlines(crs=data_crs, draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle=':',
                  zorder=35)
#gl.yformatter = FormatStrFormatter('%g$^\circ$c.ш.')  #('{%d}W')  #direction_label=False)
#gl.xformatter = FormatStrFormatter('%g$^\circ$в.д.')  #('{%d}W')  #direction_label=False)
    

gl.ylocator = mticker.FixedLocator(range(-40, 50, 10))
gl.yformatter = mticker.FuncFormatter(my_rus_lat_formatter)

gl.xlocator = mticker.FixedLocator(range(-40, 50, 10))
gl.xformatter = mticker.FuncFormatter(my_rus_lon_formatter)


gl.left_labels = True
gl.right_labels = False  # True
gl.top_labels = True
gl.bottom_labels = False  # True


plt.show()
