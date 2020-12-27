from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, TextField, Form, FormField, SelectField


class DeviceForm(Form):
    deviceName = StringField('deviceName', render_kw={
                             'class': 'form-control-sm', 'placeholder': 'Device Name'})
    deviceIP = StringField('deviceIP', render_kw={
                           'class': 'form-control-sm', 'placeholder': 'Device IP'})


class MemberForm(Form):
    memberIP = StringField('memberIP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Member IP'})
    memberPort = StringField('memberPort', render_kw={
                             'class': 'form-control-sm', 'placeholder': 'Member Port'})


class PoolForm(Form):
    poolName = StringField('poolName', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Pool Name'})
    LBMethod = StringField('LBMethod', render_kw={
        'class': 'form-control-sm', 'placeholder': 'LB Method'})
    Health = StringField('Health', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Health Monitor'})
    members = FieldList(FormField(MemberForm), min_entries=1)


class SSLProfileForm(Form):
    profileName = StringField('poolName', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Profile Name'})
    certName = StringField('poolName', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Certificate Name'})
    keyName = StringField('poolName', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Key Name'})
    chainCertName = StringField('poolName', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Chain Cert Name'})


class VirtualForm(Form):
    virtualName = StringField('virtualName', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Virtual Name'})
    destination = StringField('destination', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Destination'})
    serviceport = StringField('Service Port', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Service Port'})
    SSLProfile = StringField('SSL Profile', render_kw={
        'class': 'form-control-sm', 'placeholder': 'SSL Profile'})
    SNAT = StringField('Source Address Translation', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Source Address Translation'})
    rules = StringField('Rules', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Rules'})
    defaultPool = StringField('Default Server Pool', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Default Server Pool'})
    persistence = StringField('Persistence', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Persistence'})


class LBForm(FlaskForm):
    changeID = StringField('change ID', render_kw={
                           'class': 'form-control-sm', 'placeholder': 'Change ID'})
    customerEmail = StringField('change ID', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Customer Email'})
    customerPhone = StringField('change ID', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Customer Phone'})
    LBType = SelectField('Select Load Balancer Type', choices=[
                         ('select', 'Select LB Type'), ('f5', 'F5'), ('f5cli', 'F5 CLI'), ('a10', 'A10')])
    devices = FieldList(FormField(DeviceForm), min_entries=1,
                        render_kw={'class': 'input-group mb-3'})
    partition = StringField('partition', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Partition'})
    pools = FieldList(FormField(PoolForm), min_entries=1)
    profiles = FieldList(FormField(SSLProfileForm), min_entries=0)
    virtuals = FieldList(FormField(VirtualForm), min_entries=1)
    submit = SubmitField('Submit', render_kw={
                         'class': 'btn btn-outline-secondary'})


class FWForm(FlaskForm):
    changeID = StringField('change ID', render_kw={
                           'class': 'form-control-sm', 'placeholder': 'Change ID'})
    customerEmail = StringField('change ID', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Customer Email'})
    customerPhone = StringField('change ID', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Customer Phone'})
    FWType = SelectField('Select Firewall Type', choices=[
                         ('select', 'Select LB Type'), ('asa', 'Cisco ASA'), ('paloalto', 'Palo Alto'), ('ftd', 'Cisco FTD')])
    devices = FieldList(FormField(DeviceForm), min_entries=1,
                        render_kw={'class': 'input-group mb-3'})
    partition = StringField('partition', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Partition'})
    objgroups = FieldList(FormField(PoolForm), min_entries=1)
    aclrules = FieldList(FormField(VirtualForm), min_entries=1)
    submit = SubmitField('Submit', render_kw={
                         'class': 'btn btn-outline-secondary'})
