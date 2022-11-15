
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
