#Ask user to enter the hours, minutes, and also duration
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#calculate the total minutes
total_min=mins+dura


hour+=(total_min//60) #find hours and add to existing hours
mins=(total_min%60) #find balance minutes and equal it to mins variable
print(hour,mins,sep=":",end=" ") #print the result according by the question