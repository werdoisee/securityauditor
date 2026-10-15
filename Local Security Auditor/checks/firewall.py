import subprocess
import json

def check_firewall():
    result = (
    subprocess.run(
        ["powershell", "-Command", "Get-NetFirewallProfile | Select-Object Name, Enabled | ConvertTo-Json"], 
        capture_output = True, text = True, check = True
        )
    )
    return json.loads(result.stdout)