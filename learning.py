class Numbers:

    def even_odd(self, start, end):
        for ele in range(start, end):
            if ele%2==0:
                print("even")
            else:
                print("odd")

num = Numbers()
num.even_odd(10, 20)
