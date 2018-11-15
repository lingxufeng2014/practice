graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person, " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")

# 运行时间
# 如果你在你的整个人际关系网中搜索芒果销售商，
# 就意味着你将沿每条边前行(记住，边是 从一个人到另一个人的箭头或连接)，因此运行时间至少为O(边数)。
# 你还使用了一个队列，其中包含要检查的每个人。
# 将一个人添加到队列需要的时间是固定的， 即为O(1)，因此对每个人都这样做需要的总时间为O(人数)。
# 所以，广度优先搜索的运行时间为 O(人数 + 边数)，这通常写作O(V + E)，其中V为顶点(vertice)数，E为边数
