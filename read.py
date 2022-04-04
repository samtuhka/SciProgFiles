from pyodide import open_url

#change filename to the filename in the exercise, fetches it from online
filename = "hy_admission_stats_2017.csv"
url= "https://raw.githubusercontent.com/samtuhka/SciProgFiles/main/" + filename
content = open_url(url).read()

with open(filename, 'w') as f:
    f.write(content)

# now we can start coding normally
file = open("hy_admission_stats_2017.csv")
print(file.read())
