# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""
# SearchPath

def searchPath(graph,start,end):
    results = []
    __generatePath(graph,[start],end,results)
    results.sort(key=lambda x:len(x))
    return results

def __generatePath(graph, path, end, results):
    current = path[-1]
    if current == end:
        results.append(path)
    else:
        for i in graph[current]:
            if i not in path:
                __generatePath(graph,path+[i],end,results)

def showPath(result):
    print("The Path from",result[0][0],"to",result[0][-1],"is:")
    for path in result:
        print(path)

if __name__ == '__main__':
    graph = {
        "A": ["B", "C", "D"],
        "B": ["E"],
        "C": ["D","F"],
        "D": ["B","E","G"],
        "E": ["D"],
        "F": ["D","G"],
        "G": ["E"],
    }
    r1 = searchPath(graph,"A","D")
    showPath(r1)