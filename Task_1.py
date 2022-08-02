import shelve
class PhoneBook:
    def __init__(self, nameBook, dicRec={}):
        self.nameBook = nameBook
        self.dicRec = dicRec
    def loadBook(self):
        db = shelve.open(self.nameBook)
        self.dicRec = dict(db.items())
        db.close()
    def saveBook(self):
        db = shelve.open(self.nameBook)
        for (key, record) in self.dicRec.items():
            db[key] = record
        db.close()
 
    def createRec(self):
        print(self.nameBook)
        label = input('Название записи: ')
        phone = input('В ведите номер телефона : ')
        print('ФИО,коммент. - Если нет, просто нажимайте Enter')
        familyName = input('ФИО: ')
        comment = input('Комментарий: ')
        if len(self.dicRec)>0:
            L = sorted(self.dicRec.items(), key=lambda item: item[0])
            keyRec = str(int(L[-1][0]) + 1)
        else:
            keyRec = "1"
        record = PhoneRec(keyRec,label,phone, familyName, comment)
        self.dicRec[keyRec] = record
    def delPhoneRec(self, key):
        del dicRec[key]
    def readPhoneRec(self):
        for key in t1.dicRec.keys():
            print("{:<3}- {:<25}- {:<20}- {:<30}- {:<30}".format(key, t1.dicRec[key].label, 
                                                                            t1.dicRec[key].phone, 
                                                                            t1.dicRec[key].familyName,  
                                                                            t1.dicRec[key].comment))
class PhoneRec:
    def __init__(self, keyRec, label, phone, familyName, comment):
        self.keyRec = keyRec
        self.label = label
        self.phone = phone
        self.familyName = familyName
        self.comment = comment
 
if __name__ == '__main__':
    t1 = PhoneBook("Телефонный справочник :")
    t1.loadBook()
    t1.createRec()
    t1.readPhoneRec()
 
    t1.saveBook()
 
    # Строка необходима пока нет графического интерфейса, 
    # что бы командное окно с информацией не закрывалось,
    # пока вы не нажмете Enter.
    input('ОКОНЧАНИЕ РАБОТЫ')