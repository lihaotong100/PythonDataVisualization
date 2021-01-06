import matplotlib.pyplot as plt
sqaures = [1,4,9,16,25]
input_values = [1,2,3,4,5]
x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]
#plt.plot(input_values,sqaures,linewidth=5)

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.twilight_shifted,edgecolors='none',s=400)

plt.title("Sqaures Numbers",fontsize=24)
plt.xlabel("Value",fontsize=24)
plt.ylabel("Square of Value",fontsize=24)

plt.tick_params(axis="both",labelsize=14)

plt.axis([0,5100,0,125000000000])

plt.show()

plt.savefig('squares_plot.png',bbox_inches='tight')