
function Get-WifiPassword(){
    foreach ($SSID in (netsh wlan show profiles | Select-String ": (.*)"|% { $_.Matches.Groups[1].Value })){
        [string]$password = netsh wlan show profiles name=$SSID key=clear | Select-String "关键内容.*:(.*)"|% { $_.Matches.Groups[1].Value }
        "{0,-20} : {1,10}" -f $SSID, $password
    }
}

Get-WifiPassword
