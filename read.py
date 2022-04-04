from js import fetch
from matplotlib import image

#change the filenmame to the one in the relevant exercise
filename = "hy_admission_stats_2017.csv"
url= "https://raw.githubusercontent.com/samtuhka/SciProgFiles/main/" + filename

res = await fetch(url)
text = await res.text()

with open(filename, 'w') as f:
    f.write(text)

#ugly hack for images used in exercise set 4
if "png" in filename:
    img = np.loadtxt(filename)
    image.imsave(filename, img,  cmap='gray')

# NORMAL CODE STARTS HERE
# Change lines below to your own code
f = open(filename)
print(f.read())
