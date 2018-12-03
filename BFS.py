from collections import deque

graph = dict()

graph["you"] = ["BoB", "CLAIRE", "ALICE"]
graph["BoB"] = ["ANUJ", "PEGGY"]
graph["ALICE"] = ["PEGGY"]
graph["CLAIRE"] = ["THOM", "JONNY"]
graph["ANUJ"] = []
graph["PEGGY"] = []
graph["THOM"] = []
graph["JONNY"] = []

def person_is_seller(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    # this array is used to record the person who has been checked
    while search_queue:
        #while queue is not empty   
        person = search_queue.popleft()    # this function popleft() is used to push the first element out of the queue 
        # get the first person of the queue
        if person not in searched:
            if person_is_seller(person):
                # check the person whether is a mango seller
                print(person + " is a mango seller")
                return True
        else:
            search_queue += graph[person]
            searched.append(person)
            # if this person is not a mango seller so that add the person's friend circle to the search queue and mark this person
    return False

if __name__ == "__main__":
    search("you")