from flask import Flask, render_template_string
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

# Read the HTML template
with open(r'/workspaces/codespaces-flask/templates/index.html', 'r') as file:
    HTML_TEMPLATE = file.read()

@app.route('/htop')
def htop():
    # Get system username
    try:
        username = subprocess.check_output(['whoami'], text=True).strip()
    except:
        username = os.getenv('USER', os.getenv('USERNAME', 'Unknown'))
    
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Get process information
    try:
        ps_output = subprocess.check_output(['ps', 'aux'], text=True)
    except:
        ps_output = "Error fetching process information"
    
    # Your name (REPLACE THIS WITH YOUR ACTUAL NAME)
    name = "Suprith G Gowda"
    
    # Render the template with the data
    return render_template_string(
        HTML_TEMPLATE,
        name=name,
        username=username,
        server_time=server_time,
        ps_output=ps_output
    )

if __name__ == '_main_':
    # Try different ports if 5001 is in use
    app.run(host='0.0.0.0', port=5000)