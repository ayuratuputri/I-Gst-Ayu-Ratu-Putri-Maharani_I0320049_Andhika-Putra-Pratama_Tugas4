usia = 21
a = int(input("Berapa usia anda : "))
if usia <= a :
    print("Anda memenuhi usia")
    b = str(input("Apakah anda lulus ujian klasifikasi (Y/T)" ))
    if b == "Y" :
        print("Anda dapat mendaftar di kursus")
    elif b == "T" :
        print("Anda tidak dapat mendaftar di kursus")

else :
    print("Anda tidak memenuhi usia")


