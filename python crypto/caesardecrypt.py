def main():
    message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        translated = ''
        
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wraparound:
                if translatedIndex < 0:
                    translatedIndex += len(SYMBOLS)

                translated += SYMBOLS[translatedIndex]

            else:
                translated += symbol

        print('Key #%s: %s' % (key, translated))



if __name__ == '__main__':
    main()
