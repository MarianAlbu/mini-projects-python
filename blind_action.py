
biders={}
while True:
    name=input('what is your name?')
    bid=input('what is your bid?')
    biders[name]=bid
    other_biders=input('are there other biders?')
    if other_biders=='no':
        bid=0
        highest_bider=0
        for key, value in biders.items():
            if int(value)>bid:
                bid=int(value)
                highest_bider=key
        print(f'the winer is {highest_bider}, ${bid}')


