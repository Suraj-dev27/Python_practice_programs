#yt link: https://youtu.be/hI0A_UOgdD8

def rain_water(arr):
    size=(len(arr))

    left=size *[0]
    right=size *[0]

    left[0]=arr[0]
    water=0

    max_sofar=arr[0]
    for i in range (0,size):
        if max_sofar < arr[i]:
            max_sofar=arr[i]
            left[i]=max_sofar
        else:
            left[i]=max_sofar

    max_sofar_right=arr[-1]   
    for i in range (size-1,-1,-1):
        if max_sofar_right < arr[i]:
            max_sofar_right=arr[i]
            right[i]=max_sofar_right
        else:
            right[i]=max_sofar_right
    

    for i in range(0,size):
        water= water + min(left[i],right[i]) - arr[i] #this last is original index 
    return water

arr=[1,0,2,0,1,0,3,1,0,2]
print(rain_water(arr))