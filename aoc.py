from subprocess import call

for i in range(1, 25+1):
    try:
        print('Day', i)
        if call(['python3', f'{i}.py']): break
    except:
        break