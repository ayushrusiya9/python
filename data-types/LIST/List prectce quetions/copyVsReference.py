# You're given: `x = [1, 2, 3]`, `y = x`
#- Change the first item in `y` to `999`.
# - Print both `x` and `y`.
# - Now use `copy()` on `x` and assign to `z`, change `z[1] = 888`.
# - Print all three: `x`, `y`, `z`.
# - What do you observe?

x = [1,2,3]
y = x

y[0] = 23#that i observe

z = x.copy()
z[1] = 888

print(x)
print(y)
print(z)

#i observe ki jab hum kisi verable ki values kisi dusre veriable me assighn krte toh wo same hi hota hai like ager x ki values y ma hai or hum ma change kre toh x bhi change hoga because woh dono same hi memory addres ko refer kr rhe hai
