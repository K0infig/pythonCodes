class Students(object):
    def __init__(self,name, age, grade):

        self.name =name
        self.age = age
        self.grade= grade

    def display(self):
        print("name: "+self.name)


andy = Students("Andy", 15,9)

andy.display();

sree = Students("Lalalala", 6797,87)

sree.display()



    
