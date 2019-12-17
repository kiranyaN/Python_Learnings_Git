class custom:
    def printNum(self):
        for i in range(1,51):
            print("i val:",i)
        return
class default:
    def main():
        obj=custom()
        obj.printNum()
        for j in range(1,51):
            print("j val:",j)
        return
default.main()
