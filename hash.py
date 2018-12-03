from collections import OrderedDict

vote = dict()

def valite_voted(name):
    if vote.get(name):
        print("you have already voted")
    else:
        vote[name] = True
        print("let them vote")

def f(x):
    return{
        1 : "Hello",
        "asdas" : 2,
    }[x]

if __name__ == "__main__":
    while True:
        x = input("please enter your name , and you can press q to quit:")
        if x == 'q':
            break
        else:
            valite_voted(x)