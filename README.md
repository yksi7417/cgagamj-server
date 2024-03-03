# cgagamj-server
cgagamj

# Flatc 

download latest version of flatc from https://github.com/google/flatbuffers/releases, place it into proto folder.

```
(mqtt) c:\dvlp\cgagamj-server>dir proto
 Volume in drive C is Windows
 Volume Serial Number is F0B9-C1E7

 Directory of c:\dvlp\cgagamj-server\proto

03/03/2024  10:04 AM    <DIR>          .
03/03/2024  10:04 AM    <DIR>          ..
03/03/2024  10:04 AM         3,364,864 flatc.exe
03/03/2024  09:19 AM                 0 mahjong.json
03/02/2024  08:40 PM             1,126 mahjong.proto
               3 File(s)      3,365,990 bytes
               2 Dir(s)  53,127,581,696 bytes free
```

```
(mqtt) c:\dvlp\cgagamj-server\>cd python\src\common
(mqtt) c:\dvlp\cgagamj-server\python\src\common>..\..\..\proto\flatc.exe --python mahjong.fbs
```

# Requirements.txt for python 

pip install -r src/python/requirements.txt 


# .env files 

the environment variables are handled as secrets and hence not checked into the git repo.   Currently the files are stored here and you'd need permission to obtain the env variables 

https://drive.google.com/drive/folders/10jrwQPDNv1Gswi_wRddnNs54UpBhIpaC?usp=drive_link


# to install package:

```
C:\dvlp\cgagamj-server\python>pip install -e .
```

# to get vosk models 

https://alphacephei.com/vosk/models