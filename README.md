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

# how to run unit tests 

```
conda activate mqtt 
(mqtt) c:\dvlp\cgagamj-server\python>pytest
=========================================================================================================== test session starts ============================================================================================================
platform win32 -- Python 3.12.2, pytest-8.0.2, pluggy-1.4.0
rootdir: c:\dvlp\cgagamj-server\python
collected 2 items

tests\test_tilemap.py ..                                                                                                                                                                                                              [100%]

============================================================================================================ 2 passed in 0.06s =============================================================================================================
```

# how to run integration test 
```
(mqtt) c:\dvlp\cgagamj-server\python\src>python integration-test.py
Main program continues after starting process running server.py
Main program continues after starting process running client.py
server Connecting to MQTT Broker: ieea4188.ala.us-east-1.emqxsl.com
Port: 8883
Topic: python/mqtt & flatbuffer_topic: python/mqtt-binary
Username: server
client Connecting to MQTT Broker: ieea4188.ala.us-east-1.emqxsl.com
Port: 8883
Topic: python/mqtt & flatbuffer_topic: python/mqtt-binary
Username: client
server Connected to MQTT Broker!
client Connected to MQTT Broker! <paho.mqtt.client.Client object at 0x000001DF2C8E3E90> None ConnectFlags(session_present=False) Success [AssignedClientIdentifier : MzE1MzQ3OTE4NTQ4MjAxMjcwMzc1NTIwMTUyOTgwNjg0ODA, TopicAliasMaximum : 10, RetainAvailable : 1, MaximumPacketSize : 1048576, WildcardSubscriptionAvailable : 1, SubscriptionIdentifierAvailable : 1, SharedSubscriptionAvailable : 1]
client Send `messages: 0` to topic `python/mqtt`
client Send `(<MQTTErrorCode.MQTT_ERR_SUCCESS: 0>, 2)` to topic `python/mqtt`
server Received `messages: 0` from `python/mqtt` topic
server Received `<common.mahjong.Game.Game object at 0x0000019299F049D0>` from `python/mqtt-binary` topic
Current wind: 0
Current turn: 0
Current round: 1
Discarded tiles: [143   0 122]
client Send `messages: 1` to topic `python/mqtt`
client Send `(<MQTTErrorCode.MQTT_ERR_SUCCESS: 0>, 4)` to topic `python/mqtt`
server Received `messages: 1` from `python/mqtt` topic
server Received `<common.mahjong.Game.Game object at 0x0000019299F04B50>` from `python/mqtt-binary` topic
Current wind: 0
Current turn: 0
Current round: 1
Discarded tiles: [143   0 122]
client Exiting gracefully
Process running client.py received KeyboardInterrupt. Exiting...
server Exiting gracefully
Process running server.py received KeyboardInterrupt. Exiting...
Main program received KeyboardInterrupt. Terminating child processes...
Main program exits gracefully
```