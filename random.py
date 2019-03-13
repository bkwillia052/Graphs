import collections


def findLadders(beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'List[List[str]]':

    if endWord not in wordList:
        return []
    m, conn = len(beginWord), collections.defaultdict(list)

    def genKeys(word):
        for i in range(m):
            print(i)
            yield word[:i] + '*' + word[i+1:]
    for w in wordList:
        for key in genKeys(w):
            print(key)
            conn[key].append(w)

    que, prev = collections.deque([beginWord]), collections.defaultdict(list)
    dis, shortest, res = {beginWord: 1}, float("inf"), []
    while que:
        word = que.popleft()
        if word == endWord:
            shortest = dis[word]
            break
        if dis[word] >= shortest:
            continue
        for key in genKeys(word):
            for nxt in conn[key]:
                if nxt not in dis:
                    dis[nxt] = dis[word] + 1
                    que.append(nxt)
                if dis[word] + 1 == dis[nxt]:
                    prev[nxt].append(word)

    def backtrace(path):
        if len(path) == shortest:
            res.append(path[::-1])
        for w in prev[path[-1]]:
            path.append(w)
            backtrace(path)
            path.pop()
    backtrace([endWord])
    return res


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
l = findLadders(beginWord, endWord, wordList)
print(l)
