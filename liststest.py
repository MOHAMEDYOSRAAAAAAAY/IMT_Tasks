


file =  open("subw.txt" , 'r',s")

namingLec1 = ["Lecture 1" ,"lecture1", "Lecture_1", "lec1" ,"Lec1" ,"lecture: 1" ,"lecture:1" , "Lec_1"]
namingLec2 = ["Lecture 2" ,"lecture2", "Lecture_2", "lec2" ,"Lec2" ,"lecture: 2" ,"lecture:2", "Lec_2"]
namingLec3 = ["Lecture 3" ,"lecture3", "Lecture_3", "lec3" ,"Lec3" ,"lecture: 3" ,"lecture:3", "Lec_3"]
namingLec4 = ["Lecture 4" ,"lecture4", "Lecture_4", "lec4" ,"Lec4" ,"lecture: 4" ,"lecture:4", "Lec_4"]
namingLec5 = ["Lecture 5" ,"lecture5", "Lecture_5", "lec5" ,"Lec5" ,"lecture: 5" ,"lecture:5", "Lec_5"]
namingLec6 = ["Lecture 6" ,"lecture6", "Lecture_6", "lec6" ,"Lec6" ,"lecture: 6" ,"lecture:6", "Lec_6"]

"Lecture 1" ,"lecture1", "Lecture_1", "lec1" ,"Lec1" ,"lecture: 1" ,"lecture:1" , "Lec_1"
"Lecture 2" ,"lecture2", "Lecture_2", "lec2" ,"Lec2" ,"lecture: 2" ,"lecture:2", "Lec_2"
"Lecture 3" ,"lecture3", "Lecture_3", "lec3" ,"Lec3" ,"lecture: 3" ,"lecture:3", "Lec_3"
"Lecture 4" ,"lecture4", "Lecture_4", "lec4" ,"Lec4" ,"lecture: 4" ,"lecture:4", "Lec_4"
"Lecture 5" ,"lecture5", "Lecture_5", "lec5" ,"Lec5" ,"lecture: 5" ,"lecture:5", "Lec_5"
"Lecture 6" ,"lecture6", "Lecture_6", "lec6" ,"Lec6" ,"lecture: 6" ,"lecture:6", "Lec_6"
liste1 = file.readline()

liste2 = file.readline()

liste3 = list(file.readline())
liste4 = list(file.readline())
liste5 = list(file.readline())
liste6 = list(file.readline())
listeName = [namingLec1,namingLec2,namingLec3,namingLec4,namingLec5,namingLec6]
for name in listeName:
    for i in name:
    
        if i in liste1:
            print ("Found a match in group 1")  
            print(i)
            
        elif i in liste2 :
            print ("Found a match in group 2")  
            print(i)
        elif i in liste3 :
            print ("Found a match in group 3")  
            print(i)
        elif i in liste4 :
            print ("Found a match in group 4")  
            print(i)
        elif i in liste5 :
            print ("Found a match in group 5")  
            print(i)
        elif i in liste6 :
            print ("Found a match in group 6")  
            print(i)
        else :print  (liste1[0])
   
    
file.close()



