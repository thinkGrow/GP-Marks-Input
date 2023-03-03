name = input('Insert name: ')
sum = 0
i=1

print(f'Insert mark number {i}: ')
number = int(input())

while number>-1:
    sum = number + sum
    print(f'sum so far: {sum}')
    i+=1
    print(f'Insert mark number {i}: ')
    number = int(input())


print(f"The total sum is = {sum}")
print(f'The average of the sum for {name} is {sum}/{(i-1)} = {sum/(i-1)}/40')
    
