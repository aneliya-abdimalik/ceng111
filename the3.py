from math import exp
def forward_pass(network, X):
    inputs=X
    new_input=[]
    for i in range(len(network)):

        if type(network[i]) == list:
            new_input= list(map(sum, (map(lambda x: ([a * b for a, b in zip(x, inputs)]), network[i][1]))))
            inputs=new_input

        elif type(network[i]) == str:
            for k in range(len(inputs)):
                if network[i][0]=='r':
                    if inputs[k]>0:
                        inputs[k]= max(0,inputs[k])
                    else:
                        inputs[k]=0

                else:
                    if inputs[k] <= -700:
                        inputs[k]=0
                    elif -700<inputs[k]<700:
                        inputs[k] = 1 / (1 + (exp(-inputs[k])))
                    else:
                        inputs[k]=1
    return new_input






