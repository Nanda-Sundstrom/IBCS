import requests
page = 'https://www.gutenberg.org/cache/epub/2554/pg2554.txt'
with requests.get(page, stream=True) as net:
    net_iter = net.iter_lines(decode_unicode=True)
    for (n, line) in enumerate (net_iter):
        if n>=20:
            break
        print(line.rstrip())