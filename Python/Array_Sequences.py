Metro_Area = [('Tokyo', 'JP', 36.993, (35.69, 139.69)),
              ('Delhi NCR', 'IN', 21.935, (28.61, 77.20))]
def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9} ')
    for name, _,_, (lat,lon) in Metro_Area:
        if lon > 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
    main()