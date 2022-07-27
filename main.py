import sys
import copy

n = int(input())
matriz = []
for j in range(n):
	matriz.append([int(i) for i in input().split()])

g = {}
pointer = []

def main():
    for x in range(1, n):
        g[x + 1, ()] = matriz[x][0]
    
    cost = getMinimum(1, range(2,n+1))
    
    solution = pointer.pop()
    route = [1]
    route.append(solution[1][0])

    for x in range(n - 2):
        for new_solution in pointer:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                route.append(solution[1][0])
                break
    route.append(1)
   
    print("distancia: ", cost)
    print("Melhor Rota: ", route)
    
    return

def getMinimum(k, a):
    if (k, a) in g:
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = getMinimum(j, tuple(set_a))
        values.append(matriz[k-1][j-1] + result)

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    pointer.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]

if __name__ == '__main__':
    main()
sys.exit(0) 
