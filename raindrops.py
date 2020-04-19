# number = input('Number: ')


def convert(number):
    raindrops = ''

    if int(number) % 3 == 0:
        raindrops += 'Pling'
        has_a_factor = True
        print(raindrops)
    if int(number) % 5 == 0:
        raindrops += 'Plang'
        print(raindrops)
    if int(number) % 7 == 0:
        raindrops += 'Plong'
        print(raindrops)
    if raindrops == '':
        raindrops = str(number)

    return raindrops

# print(convert(number))
