# Send an email using powershell

$toSend = @('abijah.buttendorf@myail.champlain.edu', 'abijah@myail.champlain.edu', 'buttendorf@myail.champlain.edu')

# Message body
$msg = "Hello"

# Send the email

while($true) {

    foreach ($email in $toSend) {

        write-host "Send-MailMessage -from 'abijah.buttendorf@myail.champlain.edu' -To $email -Subject 'Tisk Tisk' `
        -Body $msg -SmtpServer X.X.X.X"
        
        #Pause to save PC
        start-sleep 1
    }
}