#Append adds an element at the end of a list, while extend takes all the element in the lis, tuple severally.
#create a program that sorts the list below
	
Is = [18,2,16,4,1]
Is.sort(reverse=True)
print(Is)
#create a program that counts the occurence of number 4 in the list below

x=[1, 2, 9, 4, 5, 4, 1]
occurrencesOf4 = x.count(4)
print(occurrencesOf4)

#Select the correct way to access the value of a history subject
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(print(sampleDict["class"]["student"]["marks"]["history"]))
#Create a program that will empty the dictionary below
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}
student.clear()
print(student)

#create a program that will remove 'marks' from the dictionary below
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}
student.pop("marks")
print(student)