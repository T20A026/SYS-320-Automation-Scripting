# Extract Ip's

$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

foreach ($u in $drop_urls) {

    $temp = $u.split("/")

    $file_name = $temp[-1]

    if (Test-Path $file_name) {
        continue
    } else {

    Invoke-WebRequest -Uri $u -Outfile $file_name
    
        }
}

#Filenames Array
$input_paths = @('.\compromised-ips.txt','.\emerging-botcc.rules')

# Regext Ip Extractor
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Appent IP's to temp list, and append files
select-string -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
Out-File -FilePath "ips-bad.tmp"

#Generates Linux IP tables File rules
(Get-Content -Path ".\ips-bad.tmp") | ForEach-Object `
{ $_ -replace "^","iptables -A INPUT -s" -replace "$"," -j DROP"} | `
Out-File -FilePath ".\iptables.bash"

#Generates Windows Net-Firewall rules
(Get-Content -Path ".\ips-bad.tmp") | ForEach-Object `
{ $_ -replace "^",'New-NetFirewallRule -DisplayName "Known Threat" -Direction Inbound -LocalPort Any -Protocol TCP -Action Block -RemoteAddress ' -replace "$"} | `
Out-File -FilePath ".\firewall.ps1"

#Getting user input
$OS = Read-Host -Prompt 'Please select OS (L for linux, W for windows)'
$Target = Read-Host -Prompt 'Please enter the IP of the Target'
$User = Read-Host -Prompt 'Please enter target user'

switch ( $OS ) 
{
    L
    {
        Set-SCPItem -Computername $Target -Port 2222 -Credential (Get-Credential $User) `
        -Destination '/home' -Path 'C:\Users\abija\Documents\VisualStudio\SYS-320-Automation\iptables.bash'
        continue
    }
    W
    {
        Set-SCPItem -Computername $Target -Port 2222 -Credential (Get-Credential $User) `
        -Destination 'C:\Users' -Path 'C:\Users\abija\Documents\VisualStudio\SYS-320-Automation\firewall.ps1'
        continue
    }
}