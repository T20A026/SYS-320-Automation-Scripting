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

(Get-Content -Path ".\ips-bad.tmp") | ForEach-Object `
{ $_ -replace "^","iptables -A INPUT -s" -replace "$"," -j DROP"} | `
Out-File -FilePath ".\iptables.bash"