xh = input ("Enter hours:")
xr = input ("Enter rate:")

try:
    fh = float (xh)
    fr = float (xr)
except:
    print('Error!')
    quit()

print(fh, fr)
