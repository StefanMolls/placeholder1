# Willhelm - Discovery Ant

import wmi
import inspect 
c = wmi.WMI()

#os = c.Win32_OperatingSystem
#for method in c.Win32_OperatingSystem.properties.keys():
#	print method

def CountryCodeLookup(countrycode):
	ccode_dict = {
	}

def os_discovery():
	for os in c.Win32_OperatingSystem():
		print "-"*10 + "Operating System Info" + "-"*10
		print 'Version: ', os.Caption 
		print 'Service Pack: ', os.ServicePackMajorVersion,'.',os.ServicePackMinorVersion
		print 'Architecture: ', os.OSArchitecture 
		print 'Registered to: ', os.RegisteredUser
		# ToDo Create atranslate function
		print 'Countrycode: ', os.Countrycode
		print 'Computername: ', os.CSName
		Localtime = str(os.LocalDateTime)
		print 'Local Date: ', Localtime[0:4] + '/' + Localtime[4:6] + '/' + Localtime[6:8] 
		Timezone = int(Localtime.split('-')[1])
		print 'Local Time: ', Localtime[8:10] + ':' + Localtime[10:12] + ' (GMT -%i hours)' %(Timezone/60)
		print 'System Directory: ',os.SystemDirectory 
		print "-"*10,"\n"

def os_network_nic():
	for nic in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
		print "-"*10 + "NIC info", "-"*10
		print "NIC description: ", nic.Description
		print "NIC MAC: ", nic.MACAddress
		for ip_address in nic.IPAddress:
			print "NIC IP(s): ",ip_address
		print "NIC DHCP: ", nic.DHCPEnabled
		print "NIC DHCP Server: ", nic.DHCPServer
		print "NIC DNS Domain: ", nic.DNSDomain
		print "-"*10,"\n"

def os_network_domain():
	for network in c.Win32_NTDomain():
		print "-"*10 + "Domain info for: ",network.Caption, "-"*10
		print "Domain ClientSiteName: ", network.ClientSiteName
		print "Domain DC Site Name: ", network.DcSiteName
		print "Domain Controller IP: ", network.DomainControllerAddress
		print "Domain Controller Name: ", network.DomainControllerName
		print "Domain Network Name: ", network.DomainName
		print "-"*10,"\n"

def user_inDomain():
	print "-"*10 + "User Domain info", "-"*10
	for user_inD in c.Win32_UserInDomain():
		print "User", user_inD.PartComponent.split('Name')[1] 
		print "In Domain: ", user_inD.PartComponent.split('Name')[0].split('Domain')[1]
	print "-"*10,"\n"

def list_processes():
	print "-"*10 + "Process info", "-"*10
	for process in c.Win32_Process():
		print "Proc.-ID: ", process.ProcessId," Parent Proc: ", process.ParentProcessId, "Proc.-Name: ", process.Name
	print "-"*10,"\n"

def main():
	os_discovery()	
	os_network_nic()
	os_network_domain()
	# user_inDomain might throw a .split error ...further testing tbd :-)
	user_inDomain()
	list_processes()

if __name__ == '__main__':
	main()

