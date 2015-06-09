

def one():
    return([x for x in range(2000,3200) if x%7==0 and x%5 !=0])

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))


def two(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans*i
    return(ans)

def three(n):
    ans = dict()
    for i in range(1,n+1):
        ans[i]=i*i
    return(ans)

three(8)

def four(string_of_numbers):
    ans = string_of_numbers.split(",")
    ans2 = tuple(ans)
    return([ans,ans2])

string_of_numbers = "3,6,7,8,12"
four(string_of_numbers)

class five(object):
    def __init__(self):
        self.text = ""
    def getString(self,input):
        self.text = input
    def shoutString(self):
        print(self.text.upper())

five_text = five()
five_text.getString("im learning python quickly")
five_text.shoutString()



