class cat:
    def sound(self):
        print("cat meows")
class lion(cat):
    def roar(self):
        print("lion roars")
class cub(lion):
    def mew(self):
        print("cub mews")

c=cub()
c.mew()
c.roar()
c.sound()

print("\n\n\n")
