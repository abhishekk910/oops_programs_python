class Student:
    __sid = 100

    def set_sid(self,sid):
        self.__sid=sid

    def show_sid(self):
        print(self.__sid)

obj = Student()
#obj.show_sid()
obj.show_sid()
obj.set_sid(105)
obj.show_sid()