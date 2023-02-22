from colorthief import ColorThief as CT
import matplotlib.pyplot as plt


ct = CT("img.jpg")
dominant = (ct.get_color(quality=1))

plt.imshow([[dominant]])
plt.show()

palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

