with open("text.txt", 'w') as f:
    f.write("Fake Python"+"\n")
    f.write("Real Python"+"\n")



with open("text.txt", 'a') as f:
    f.write("new python, old python")