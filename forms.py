from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, Form, FormField, SelectField, DateTimeField, HiddenField, IntegerField, BooleanField
from datetime import datetime
import sys
sys.path.append('/home/site/wwwroot')


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
                         ('f5', 'F5'), ('f5cli', 'F5 CLI'), ('a10', 'A10')])
    devices = FieldList(FormField(DeviceForm), min_entries=1,
                        render_kw={'class': 'input-group mb-3'})
    partition = StringField('partition', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Partition'})
    pools = FieldList(FormField(PoolForm), min_entries=1)
    profiles = FieldList(FormField(SSLProfileForm), min_entries=0)
    virtuals = FieldList(FormField(VirtualForm), min_entries=1)
    timestamp = HiddenField('timestamp', default=datetime.utcnow)
    submit = SubmitField('Submit', render_kw={
                         'class': 'btn btn-outline-secondary'})


class ObjForm(Form):
    objectIP = StringField('objectIP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'IP'})
    objectMask = StringField('objectMask', render_kw={
                             'class': 'form-control-sm', 'placeholder': 'Mask'})


class ObjGrpForm(Form):
    objName = StringField('poolName', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Object Group Name'})
    objectList = FieldList(FormField(ObjForm), min_entries=1)


class NATForm(Form):
    natName = StringField('poolName', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Pool Name'})


class ACLForm(Form):
    ruleName = StringField('change ID', render_kw={
                           'class': 'form-control-sm', 'placeholder': 'Rule Name'})
    lineNum = IntegerField('line num', render_kw={
                           'class': 'form-control-sm', 'placeholder': 'Rule Number'})
    ruleAction = SelectField('Select Action', choices=[
        ('permit', 'permit'), ('deny', 'deny')], render_kw={
        'class': 'form-control-sm'})
    protocol = SelectField('Select Protocol', choices=[
        ('tcp', 'tcp'), ('udp', 'udp'), ('ip', 'ip'), ('icmp', 'icmp')], render_kw={
        'class': 'form-control-sm'})
    source = StringField('source', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Source'})
    destination = StringField('change ID', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Destination'})
    port = IntegerField('line num', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Port'})


class FWForm(FlaskForm):
    changeID = StringField('change ID', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Change ID'})
    customerEmail = StringField('Customer Email', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Customer Email'})
    customerPhone = StringField('Customer Phone', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Customer Phone'})
    FWType = SelectField('Select Firewall Type', choices=[
        ('select', 'Select LB Type'), ('asa', 'Cisco ASA'), ('paloalto', 'Palo Alto'), ('ftd', 'Cisco FTD')])
    devices = FieldList(FormField(DeviceForm), min_entries=1,
                        render_kw={'class': 'input-group mb-3'})
    objgroups = FieldList(FormField(ObjGrpForm), min_entries=1)
    aclrules = FieldList(FormField(ACLForm), min_entries=1)
    nats = FieldList(FormField(NATForm), min_entries=1)
    timestamp = HiddenField('timestamp', default=datetime.utcnow)
    submit = SubmitField('Submit', render_kw={
        'class': 'btn btn-outline-secondary'})


class FWVPNForm(FWForm):
    vpnName = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'VPN Name'})
    objvpngroups = FieldList(FormField(ObjGrpForm), min_entries=1)
    peerIP = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'VPN Peer IP'})
    p1PSK = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'PSK'})
    p1Hash = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Hash'})
    p1Crypt = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Encryption'})
    p1DHgroup = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'DH Group'})
    p1lifetime = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Lifetime'})
    p2transform = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Transform Set'})
    p2lifetime = StringField('Peer IP', render_kw={
        'class': 'form-control-sm', 'placeholder': 'Lifetime'})
    noNat = BooleanField('Add NoNat', render_kw={
        'class': 'form-control-sm', 'placeholder': 'NoNat'})
