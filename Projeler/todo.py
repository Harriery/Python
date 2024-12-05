

Todo = []
while(True):
    guncelTodo = Todo

    print("Todolist Programina Hosgeldiniz!")
    print("1-Yeni Todo eklemek,")
    print("2-Todo silmek,")
    print("3-Tum Todo'lari goster,")

    islem = input("Yapmak istediginiz islem icin bir 1-3 arasinda bir numara giriniz")

    if (islem == "1"):
        yeniTodo = input("Lutfen Todo Giriniz: ")
        guncelTodo.append(yeniTodo)
        print("Todo Eklendi")
    elif (islem == "2"):
        silinecekTodo = guncelTodo.pop(input("Silmek istediginiz Todo'yu seciniz!"))
        print("Silme islemi Basariyla gerceklesti..!")
    elif (islem == 3):
        
    
