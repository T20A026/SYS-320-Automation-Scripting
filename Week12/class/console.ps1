# Login to a remote SSH server
#New-SSHSession -ComputerName '10.0.0.4' -Credential (Get-Credential root)
<#

Im a Multiline Comment!!!!

#>
<#
while ($true) {

    # Add a prompt to run commands
    $cmdVar = read-host -Promt "Please enter a command"

    # Run command on remote SSH Server
    (Invoke-SSHCommand -Index 0 $cmdVar).Output

}
#>

Set-SCPItem -Computername '10.0.0.46' -Credential (Get-Credential root) `
-Destination '/home' -Path 'C:\Users\abija\Documents\VisualStudio\SYS-320-Automation\Week12\class\meme.jpg'

#Remove-SSHSession -SessionId 0