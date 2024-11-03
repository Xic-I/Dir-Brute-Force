import requests

def Brute(URL, WORDLIST):
    attempts = 0
    founds = 0
    with open(WORDLIST, 'r') as wordlist:
        lines = wordlist.readlines()
    print('Searching for directorys...')
    for line in lines:
        request = requests.get(f'{URL}/{line.strip()}')
        attempts += 1
        if request.status_code == 200 or request.status_code == 302:
            print(f"Dir founded! ----> {URL}/{line.strip()} | Status Code: {request.status_code}")
            founds +=1
        print(f'Trying {attempts} of {len(lines)} words...', end='\r')
    print(f'\n{founds} Dir Have been Founded!')

target = input('Target> ')
wdl_file = input('Wordlist> ')
Brute(target, wdl_file)
