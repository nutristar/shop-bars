# def dfs(startPoint, searchRequest, graph, visited):
#     if startPoint == searchRequest:
#         return True
#     if startPoint in visited:
#         return False
#     visited+=[startPoint]
#     for neighbour in graph[startPoint]:
#         if not neighbour in visited:
#             if dfs(neighbour, searchRequest, graph, visited):
#                 return True
#     return False
#
#
#
# graph={"A":["B","C"],"B":["A","D"], "C":["A", "D", "F","E"], "D":["B","C"], "E":["Z","M"]}
#
#
# print(dfs("A", "C", graph, []))
text=" yuyu good a "
bad = ["a", "b", "c"]
good = ["good"]

# def sipf (text):
#
#     for word in text.split():
#         if word in bad:
#             print(f"bad word detected - {word}")
#             return "ne proydena"
#     for word in good:
#         if word not in text.split():
#             return "ne proydena- good word is absent"
#     return "proydena"
#
# print(sipf(text)) #== "proydena"
#
# # print(text.split())

print(type(repr(5/100)))