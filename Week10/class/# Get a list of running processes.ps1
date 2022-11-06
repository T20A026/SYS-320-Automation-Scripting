# Get a list of running processes

#Get List of members
#Get-Process | get-member

#Get a list of processes: Id, name, path
#Get-Process | Select-Object ProcessName, Path, id

#Save Output to a csv
#Get-Process | Select-Object ProcessName, Path, id | Export-csv -path `
#"C:\Users\abija\Documents\VisualStudio\SYS-320-Automation\Week10\class\prcesses.csv"

$outputName = "C:\Users\abija\Documents\VisualStudio\SYS-320-Automation\Week10\class\runningprcesses.csv"

Get-Service | Where-Object { $_.Status -eq "Running" } | select-object Status, Name, DisplayName, BinaryPathName | export-csv -Path $outputName

# System Services
#Get-Service | Get-Member 
#Get-Service | select-object Status, Name, DisplayName, BinaryPathName | export-csv -Path $outputName
if ( Test-Path $outputName ) {

    write-host -BackgroundColor "Green" -ForegroundColor "white" "Processes file was created!"
} else {

    write-host -BackgroundColor "Red" -ForegroundColor "white" "Processes file failed!"
}