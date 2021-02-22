# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    
    rem_room = capacity

    val_by_weight = {}
    for i in range(len(weights)):
        val = 0
        if weights[i] > 0:
            val = values[i]/weights[i]
        val_by_weight[i] = val

    val_by_weight = dict(sorted(val_by_weight.items(), key=lambda x: x[1], reverse=True))

    for i in val_by_weight.keys():
        if val_by_weight[i] == 0:
            break
        if rem_room == 0:
            return value
        a = min(weights[i],rem_room)
        weights[i] -= a
        rem_room -= a
        value += a * val_by_weight[i]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
