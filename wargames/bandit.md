# Level 0

ssh -p 2220 bandit0@bandit.labs.overthewire.org
bandit0

# Level 0 → Level 1

The password you are looking for is: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

# Level 1 → Level 2

ssh -p 2220 bandit1@bandit.labs.overthewire.org

cat ./-
263JGJPfgU6LtdEvgfWU1XP5yac29mFx

# Level 2 → Level 3

ssh -p 2220 bandit2@bandit.labs.overthewire.org

cat spaces\ in\ this\ filename
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

# Level 3 → Level 4

ssh -p 2220 bandit3@bandit.labs.overthewire.org

cat ...Hiding-From-You
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

# Level 4 → Level 5

ssh -p 2220 bandit4@bandit.labs.overthewire.org

```sh
for file in ./-file0{0..9}; do
    file "$file"
done
```

cat ./-file07
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

# Level 5 → Level 6

ssh -p 2220 bandit5@bandit.labs.overthewire.org

```sh
find . -type f -size 1033c ! -perm /111 -exec file {} + | grep "ASCII text"
```

cat maybehere07/.file2
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

# Level 6 → Level 7

ssh -p 2220 bandit6@bandit.labs.overthewire.org

find / -user bandit7 -group bandit6 -size 33c 2>/dev/null

cat /var/lib/dpkg/info/bandit7.password
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

# Level 7 → Level 8

ssh -p 2220 bandit7@bandit.labs.overthewire.org

grep "millionth" data.txt
millionth dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

# Level 8 → Level 9

ssh -p 2220 bandit8@bandit.labs.overthewire.org

sort data.txt | uniq -c | grep " 1 "
1 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

# Level 9 → Level 10

ssh -p 2220 bandit9@bandit.labs.overthewire.org

strings data.txt | grep "^==="
========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

# Level 10 → Level 11

ssh -p 2220 bandit10@bandit.labs.overthewire.org

bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
bandit10@bandit:~$ echo "VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==" | base64 -d
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

# Level 11 → Level 12

ssh -p 2220 bandit11@bandit.labs.overthewire.org

cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

# Level 12 → Level 13

ssh -p 2220 bandit12@bandit.labs.overthewire.org

```sh
temp_dir=$(mktemp -d)
echo "Temporary directory created at: $temp_dir"

cp data.txt $temp_dir

cd $temp_dir

bandit12@bandit:/tmp/gxuvimr$ xxd -r data.txt > data
bandit12@bandit:/tmp/gxuvimr$ ls
data  data.txt

bandit12@bandit:/tmp/gxuvimr$ file data
data: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/gxuvimr$ mv data data.gz
bandit12@bandit:/tmp/gxuvimr$ gzip -d data.gz

bandit12@bandit:/tmp/gxuvimr$
bandit12@bandit:/tmp/gxuvimr$ file data
data: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/gxuvimr$ mv data data.bz2
bandit12@bandit:/tmp/gxuvimr$ bzip2 -d data.bz2

bandit12@bandit:/tmp/gxuvimr$ file data
data: gzip compressed data, was "data4.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/gxuvimr$ mv data data.gz
bandit12@bandit:/tmp/gxuvimr$ gzip -d data.gz

bandit12@bandit:/tmp/gxuvimr$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/gxuvimr$ mv data data.tar
bandit12@bandit:/tmp/gxuvimr$ tar -xvf data.tar
data5.bin
bandit12@bandit:/tmp/gxuvimr$ ls
data5.bin  data.tar  data.txt

bandit12@bandit:/tmp/gxuvimr$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/gxuvimr$ mv data5.bin data5.tar
bandit12@bandit:/tmp/gxuvimr$ tar -xvf data5.tar
data6.bin

bandit12@bandit:/tmp/gxuvimr$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/gxuvimr$ mv data6.bin data6.bz2
bandit12@bandit:/tmp/gxuvimr$ bzip2 -d data6.bz2

bandit12@bandit:/tmp/gxuvimr$ file data6
data6: POSIX tar archive (GNU)
bandit12@bandit:/tmp/gxuvimr$ mv data6 data6.tar
bandit12@bandit:/tmp/gxuvimr$ tar -xvf data6.tar
data8.bin

bandit12@bandit:/tmp/gxuvimr$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/gxuvimr$ mv data8.bin data8.gz
bandit12@bandit:/tmp/gxuvimr$ gzip -d data8.gz

bandit12@bandit:/tmp/gxuvimr$ file data8
data8: ASCII text
bandit12@bandit:/tmp/gxuvimr$ cat data8
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

# Level 13 → Level 14

ssh -p 2220 bandit13@bandit.labs.overthewire.org

cat sshkey.private

ssh -i sshkey.private -p 2220 bandit14@localhost

cat /etc/bandit_pass/bandit14
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

# Level 14 → Level 15

telnet localhost 30000

Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

# Level 15 → Level 16

ssh -i sshkey.private -p 2220 bandit15@localhost

openssl s_client -quiet -connect localhost:30001

Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

# Level 16 → Level 17

ssh -p 2220 bandit16@bandit.labs.overthewire.org

nmap -p 31000-32000 localhost

openssl s_client -connect localhost:31518

```sh
bandit16@bandit:~$ openssl s_client -quiet -connect localhost:31790
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```

# Level 17 → Level 18

ssh -i C:\Users\jesus\projects\other\otw\private\bandit17.txt -p 2220 bandit17@bandit.labs.overthewire.org

```sh
bandit17@bandit:~$ diff passwords.new passwords.old
42c42
< x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
---
> FtePUTiLiwPzjIFw2T7o57oBS4zUvPpg
```

# Level 18 → Level 19

ssh -p 2220 bandit18@bandit.labs.overthewire.org cat readme

cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

# Level 19 → Level 20

ssh -p 2220 bandit19@bandit.labs.overthewire.org

ls -l

./bandit20-do cat /etc/bandit_pass/bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO

# Level 20 → Level 21

ssh -p 2220 bandit20@bandit.labs.overthewire.org

```sh
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ nc -lvp 12345
Listening on 0.0.0.0 12345
Connection received on localhost 59664
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
bandit20@bandit:~$
```

```sh
bandit20@bandit:~$ ./suconnect 12345
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
```

EeoULMCra2q0dSkYj561DX7s1CpBuOBt

# Level 21 → Level 22

ssh -p 2220 bandit21@bandit.labs.overthewire.org

```sh
bandit21@bandit:~$ ls  /etc/cron.d
cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  e2scrub_all  otw-tmp-dir  sysstat
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```

# Level 22 → Level 23

ssh -p 2220 bandit22@bandit.labs.overthewire.org

```sh
bandit22@bandit:~$ ls -la /etc/cron.d
total 44
drwxr-xr-x   2 root root  4096 Jun 20 04:08 .
drwxr-xr-x 121 root root 12288 Jun 20 21:05 ..
-rw-r--r--   1 root root   120 Jun 20 04:07 cronjob_bandit22
-rw-r--r--   1 root root   122 Jun 20 04:07 cronjob_bandit23
-rw-r--r--   1 root root   120 Jun 20 04:07 cronjob_bandit24
-rw-r--r--   1 root root   201 Apr  8 14:38 e2scrub_all
-rwx------   1 root root    52 Jun 20 04:08 otw-tmp-dir
-rw-r--r--   1 root root   102 Mar 31 00:06 .placeholder
-rw-r--r--   1 root root   396 Jan  9 20:31 sysstat
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
```

# Level 23 → Level 24

ssh -p 2220 bandit23@bandit.labs.overthewire.org

```sh
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

bandit23@bandit:~$ mkdir -p /tmp/poli
bandit23@bandit:~$ cd /tmp/poli

echo '#!/bin/bash' > /tmp/poli/my_script.sh
echo 'cat /etc/bandit_pass/bandit24 > /tmp/bandit23_pass.txt' >> /tmp/poli/my_script.sh

chmod +x /tmp/poli/my_script.sh

cp /tmp/poli/my_script.sh /var/spool/bandit24/foo/

cat /tmp/bandit23_pass.txt
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
```

# Level 24 → Level 25

ssh -p 2220 bandit24@bandit.labs.overthewire.org

```sh
bandit24@bandit:/tmp$ mktemp -d
/tmp/tmp.zoH1sk6a1R
bandit24@bandit:/tmp$ cd /tmp/tmp.zoH1sk6a1R
bandit24@bandit:/tmp/tmp.zoH1sk6a1R$ touch brute_force_pin.sh
bandit24@bandit:/tmp/tmp.zoH1sk6a1R$ chmod +x brute_force_pin.sh
bandit24@bandit:/tmp/tmp.zoH1sk6a1R$ nano brute_force_pin.sh
```

````sh
#!/bin/bash

for i in {0000..9999}
do
        echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i >> possibilities.txt
done

cat possibilities.txt | nc localhost 30002 > result.txt```
````

```sh
bandit24@bandit:/tmp/tmp.zoH1sk6a1R$ ./brute_force_pin.sh
bandit24@bandit:/tmp/tmp.zoH1sk6a1R$ ls
brute_force_pin.sh  possibilities.txt  result.txt
bandit24@bandit:/tmp/tmp.zoH1sk6a1R$ sort result.txt | grep -v "Wrong!"

Correct!
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
bandit24@bandit:/tmp/tmp.zoH1sk6a1R$
```

# Level 25 → Level 26

ssh -p 2220 bandit25@bandit.labs.overthewire.org

# Level 26 → Level 27

# Level 27 → Level 28

# Level 28 → Level 29

# Level 29 → Level 30

# Level 30 → Level 31

# Level 31 → Level 32

# Level 32 → Level 33

# Level 33 → Level 34
