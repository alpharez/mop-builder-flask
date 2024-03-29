from flask import Flask, render_template, request
from forms import LBForm, FWForm, FWVPNForm
import sys
sys.path.append('/home/site/wwwroot')

app = Flask(__name__)
app.config['SECRET_KEY'] = '3+ZN34jTvhNRNgTCN5mBCXMkSQ3daM7/wlk3NGIJZpw='


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/vpnform', methods=['GET', 'POST'])
def asaform():
    form = FWVPNForm()
    if form.is_submitted():
        result = request.form
        return render_template('asa_mop_vpn_template.j2', form=form)
    return render_template('vpnform.html', form=form)


@app.route('/f5form', methods=['GET', 'POST'])
def f5form():
    form = LBForm()
    if form.is_submitted():
        result = request.form
        if result['LBType'] == "f5":
            return render_template('f5_mop_template.j2', form=form)
        elif result['LBType'] == "f5cli":
            return render_template('f5cli_mop_template.j2', form=form)
        elif result['LBType'] == "a10":
            return render_template('a10_mop_template.j2', form=form)
    return render_template('f5form.html', form=form)

app.run(host='0.0.0.0', port=8080)
