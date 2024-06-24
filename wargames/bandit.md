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

ssh -p 2220 bandit14@bandit.labs.overthewire.org

# Level 15 → Level 16

# Level 16 → Level 17

# Level 17 → Level 18

# Level 18 → Level 19

# Level 19 → Level 20

# Level 20 → Level 21

# Level 21 → Level 22

# Level 22 → Level 23

# Level 23 → Level 24

# Level 24 → Level 25

# Level 25 → Level 26

# Level 26 → Level 27

# Level 27 → Level 28

# Level 28 → Level 29

# Level 29 → Level 30

# Level 30 → Level 31

# Level 31 → Level 32

# Level 32 → Level 33

# Level 33 → Level 34
