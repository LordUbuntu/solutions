class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people = sorted(people, key = lambda p:(p[0], n - p[1]))

        output = [0 for _ in range(n)]
        indices = collections.deque([i for i in range(n)])

        for person in people:
            index = indices[person[1]]
            indices.remove(indices[person[1]])
            output[index] = person
        return output
        
