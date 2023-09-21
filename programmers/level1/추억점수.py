def solution(name, yearning, photo):
    index = {name: yearning[i] for i, name in enumerate(name)}
    answer = []
    for pc in photo:
        value = 0
        for v in pc:
            if v in index:
                value += index[v]
        answer.append(value)
    return answer


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

solution(name, yearning, photo)
