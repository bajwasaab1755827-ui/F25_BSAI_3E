1. #Minimax with Counter
import math

count = 0

def minimax(depth, index, maxTurn, scores, targetDepth):
    global count

    if depth == targetDepth:
        count += 1
        return scores[index]

    if maxTurn:
        return max(
            minimax(depth+1, index*2, False, scores, targetDepth),
            minimax(depth+1, index*2+1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(depth+1, index*2, True, scores, targetDepth),
            minimax(depth+1, index*2+1, True, scores, targetDepth)
        )

scores = [3, 5, 2, 9, 0, 7, 0, 0]
depth = int(math.log2(len(scores)))

print("Minimax Value:", minimax(0, 0, True, scores, depth))
print("Evaluated Leaves:", count)



print("____________________________")



#2. Alpha-Beta Pruning with Counter
count = 0

def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global count

    if depth == target:
        count += 1
        return scores[index]

    if maxTurn:
        value = float('-inf')

        for i in range(2):
            value = max(value, alphabeta(
                depth+1, index*2+i, False,
                scores, target, alpha, beta
            ))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for i in range(2):
            value = min(value, alphabeta(
                depth+1, index*2+i, True,
                scores, target, alpha, beta
            ))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


count = 0
print("Alpha-Beta Value:", alphabeta(
    0, 0, True, scores, depth,
    float('-inf'), float('inf')
))
print("Evaluated Leaves:", count)