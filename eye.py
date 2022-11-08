import matplotlib.pyplot as plt


pupil_x = .7
pupil_y = .6
figure, axes = plt.subplots()
axes.set_facecolor('#eafff5')
eyeball = plt.Circle(( 0.5 , 0.5 ), .45, color = "#000000")
pupil = plt.Circle(( pupil_x , pupil_y ), .15, color = "#ffffff")
axes.set_aspect( 1 )
axes.add_artist(eyeball)
axes.add_artist(pupil)
#plt.title( 'Colored Circle' )
plt.axis('off')
plt.show()
