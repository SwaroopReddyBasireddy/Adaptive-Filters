c = 2
cur_x = 1 # The algorithm starts at x=1
lamda = 0.9999 # Weighting factor
delta = 4
previous_step_size = 1 
max_iters = 10000 # maximum number of iterations
iters = 0 #iteration counter
P = 1.0/delta
df = lambda x: 3*x**2 - 3*c
W = 0.0
while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1

print("The local minimum occurs at", cur_x)
