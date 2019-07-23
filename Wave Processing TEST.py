from pydub import AudioSegment

whitelist = open('vox_dictionary.txt', 'r').read().replace('.wav', '').split()
print(whitelist)

voice_file = 'DONE.wav'


def wordTest():
    sentence = input('Enter a scentence: ').lower()
    file_name = sentence.replace(' ', '_').replace(',', '')
    for c in '!@#$%^*?"\';:``':
        sentence = sentence.replace(c, '')
    print(sentence)

    words = sentence.replace(',', ' _comma ').replace('.', ' _period ').split()
    print(words)

    blacklist = []

    for word in words:
        if word not in whitelist:
            blacklist.append(word)

    if len(blacklist) == 0:
        final_sentence = AudioSegment.empty()
        for word in words:
            word_file = 'VOX/' + word + '.wav'
            final_sentence += AudioSegment.from_wav(word_file)
        final_sentence.export(file_name + '.wav', format='wav')

    elif len(blacklist) == 1:
        print('The word "' + '", "'.join(blacklist) + '" is not available.')
        wordTest()
    elif len(blacklist) == 2:
        print('The words "' + '" and "'.join(blacklist) + '" are not available.')
        wordTest()
    elif len(blacklist) > 2:
        print('The words "' + '", "'.join(blacklist[0:-1]) + '", and "' + blacklist[-1] + '" are not available.')
        wordTest()


wordTest()
