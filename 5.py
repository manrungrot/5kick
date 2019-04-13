# -*- coding: utf-8 -*-
'''
'''
from important import *

# Setup Argparse
parser = argparse.ArgumentParser(description='© 2018 Edit By รัตน์')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--apptype', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CHROMEOS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Chrome_OS')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()

# Login line
line = LINE('')
print ("===============[ADMIN LOGIN]===============\n")
print ('++ Auth Token : %s' % line.authToken)
kicker = LINE('')
print ('++ Auth Token : %s' % kicker.authToken)
print ("===============[KICKER LOGIN NOSELF TOKEN]===============\n")
kicker2 = LINE('')
print ('++ Auth Token : %s' % kicker2.authToken)
print ("===============[KICKER 2 LOGIN SUKSES]===============\n")
kicker3 = LINE('')
print ('++ Auth Token : %s' % kicker3.authToken)
print ("===============[KICKER 3 LOGIN SUKSES]===============\n")
kicker4 = LINE('')
print ('++ Auth Token : %s' % kicker4.authToken)
print ("===============[KICKER 4 LOGIN SUKSES]===============\n")
kicker5 = LINE('')
print ('++ Auth Token : %s' % kicker5.authToken)
print ("===============[KICKER 5 LOGIN SUKSES]===============\n")
g1 = LINE('')
print ("===============[ GHOST LOGIN SUKSES]===============\n")

myMid = line.profile.mid
creator = ["u47d41cc45c4576282d0c52ce4d5b5856"]
owner = ["u47d41cc45c4576282d0c52ce4d5b5856"]
admin = ["u47d41cc45c4576282d0c52ce4d5b5856"]
staff = ["u47d41cc45c4576282d0c52ce4d5b5856"]
Amid = kicker.getProfile().mid
Bmid = kicker2.getProfile().mid
Cmid = kicker3.getProfile().mid
Dmid = kicker4.getProfile().mid
Emid = kicker5.getProfile().mid
g1MID = g1.getProfile().mid
KAC = [line,kicker,kicker2,kicker3,kicker3,kicker5]
ABC = [kicker,kicker2,kicker3,kicker3,kicker5]
Bots = [myMid,Amid,Bmid,Cmid,Dmid,Emid,g1MID]
Ariff = creator + admin + owner + staff + Bots
programStart = time.time()
oepoll = OEPoll(line)
tmp_text = []
lurking = {}
protectqr = []
protectkick = []
protecARoin = []
protectinvite = []
protectcancel = []
protectcanceljs = []
protectantijs = []
ghost = []
zxcvzx = myMid
with open('protectcancel.json', 'r') as fp:
    protectcancel = json.load(fp)
with open('protectcanceljs.json', 'r') as fp:
    protectcanceljs = json.load(fp)    
with open('protectantijs.json', 'r') as fp:
    protectantijs = json.load(fp)
with open('ghost.json', 'r') as fp:
    ghost = json.load(fp)
with open('protectinvite.json', 'r') as fp:
    protectinvite = json.load(fp)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)

settings = livejson.File('setting.json', True, False, 4)

bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}

responsename1 = kicker.getProfile().displayName
responsename2 = kicker2.getProfile().displayName
responsename3 = kicker3.getProfile().displayName
responsename4 = kicker4.getProfile().displayName
responsename5 = kicker5.getProfile().displayName

# Backup profile
profile = line.getContact(myMid)
settings["myProfile"]["displayName"] = profile.displayName
settings["myProfile"]["statusMessage"] = profile.statusMessage
settings["myProfile"]["pictureStatus"] = profile.pictureStatus
cont = line.getContact(myMid)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = line.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

# Check Json Data
def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
    if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Error : {error}'.format(error=error))

def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': myMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def genImageB64(path):
    with open(path, 'rb') as img_file:
        encode_str = img_file.read()
        b64img = base64.b64encode(encode_str)
        return b64img.decode('utf-8')

def genUrlB64(url):
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def replaceAll(text, dic):
    try:
        rep_this = dic.items()
    except:
        rep_this = dic.iteritems()
    for i, j in rep_this:
        text = text.replace(i, j)
    return text

def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help.txt', 'r') as f:
        text = f.read()
    helpMsg = text.format(key=key.title())
    return helpMsg

def helpbot():
    with open('helpbot.txt', 'r') as f:
        text = f.read()
    helpMsg1 = text.format()
    return helpMsg1
    
def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '├', '│', '╰']]:
            result += '\n│ ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

def cloneProfile(myMid):
    contact = line.getContact(myMid)
    if contact.videoProfile == None:
        line.cloneContactProfilev2(myMid)
    else:
        profile = line.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        line.updateProfile(profile)
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = line.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = line.getProfileDetail(myMid)['result']['objectId']
    line.updateProfileCoverById(coverId)

def backupProfile():
    profile = line.getContact(myMid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = line.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
	
def restoreProfile():
    profile = line.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = line.downloadFileURL("http://dl.profile.line-cdn.net/{}".format(settings["myProfile"]["pictureStatus"]), saveAs="tmp/backupPicture.bin")
        line.updateProfilePicture(profile.pictureStatus)
        line.updateProfile(profile)
    else:
        line.updateProfile(profile)
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = line.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    line.updateProfileCoverById(coverId)

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd == 'logoutbot':
        line.sendMessage(to, 'Bot will logged out')
        sys.exit('##----- PROGRAM STOPPED -----##')
    elif cmd == 'logoutdevicee':
        line.logout()
        sys.exit('##----- line LOGOUT -----##')
    elif cmd == 'restart':
        line.sendMessage(to, 'กำลังรีสตาร์ท♪')
        settings['restartPoint'] = to
        restartProgram()
    elif cmd == 'help':
        line.sendReplyMessage(msg_id, to, help())
    elif cmd == 'helpbot':
        line.sendReplyMessage(msg_id, to, helpbot())
    elif cmd == 'speed':
        start = time.time()
        line.sendMessage(to, 'Checking speed')
        elapse = time.time() - start
        line.sendMessage(to, ' %s seconds' % str(elapse))
    elif cmd == 'me':
        line.sendContact(to, myMid)
    elif cmd == 'runtime':
        runtime = time.time() - programStart
        line.sendMessage(to,format_timespan(runtime))
    elif cmd == 'author':
        line.sendMessage(to, 'Author is linepy')
    elif cmd == 'about':
        res = '╭───「 About 」'
        res += '\n├ Type : Selfbot Python3'
        res += '\n├ Version : 3.10.0'
        res += '\n├ Library : linepy (Python3.x)'
        res += '\n├ Creator : Zero Cool'        
        res += '\n╰───「 AoY 」'
        line.sendMessage(to, res)
    elif cmd == 'status':
        res = '╭───「 Status 」'
        res += '\n├ Auto Add : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├ Auto Join : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Auto Respond : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├ Auto Respond Mention : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├ Auto Read : ' + bool_dict[settings['autoRead']][1]
        res += '\n├ Setting Key : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├ Mimic : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├ Greetings Join : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ Greetings Leave : ' + bool_dict[settings['greet']['leave']['status']][1]
        res += '\n├ Check Contact : ' + bool_dict[settings['checkContact']][1]
        res += '\n├ Check Post : ' + bool_dict[settings['checkPost']][1]
        res += '\n├ Check Sticker : ' + bool_dict[settings['checkSticker']][1]
        res += '\n╰───「 AoY」'
        line.sendMessage(to, parsingRes(res))
    elif cmd == 'abort':
        aborted = False
        if to in settings['changeGroupPicture']:
            settings['changeGroupPicture'].remove(to)
            line.sendMessage(to, 'ยกเลิกเปลี่ยนรูปภาพกลุ่มเรียบร้อย')
            aborted = True
        if settings['changePictureProfile']:
            settings['changePictureProfile'] = False
            line.sendMessage(to, 'ยกเลิกเปลี่ยนรูปภาพโปรไฟล์เรียบร้อย')
            aborted = True
        if settings['changeCoverProfile']:
            settings['changeCoverProfile'] = False
            line.sendMessage(to, 'ยกเลิกเปลี่ยนรูปปกเรียบร้อย')
            aborted = True
        if not aborted:
            line.sendMessage(to, 'ไม่สามารถยกเลิกได้\nไม่มีอะไรไห้ยกเลิก')
    elif cmd.startswith("midcopy "):
        target = removeCmd("midcopy", text)
        if target is not None:
            cloneProfile(target)
            line.sendContact(to,myMid)
            line.sendMessage(to,"คัดลอกบัญชีเรียบร้อยแล้ว")								
    elif cmd.startswith("copy "):
        if sender in myMid:
            if 'MENTION' in msg.contentMetadata.keys()!= None:
                names = re.findall(r'@(\w+)', text)
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                lists = []
                for mention in mentionees:
                    if mention["M"] not in lists:
                        lists.append(mention["M"])
                if len(lists) != []:
                    ls = random.choice(lists)
                    cloneProfile(ls)
                    line.sendMessage(to,"คัดลอกบัญชีเรียบร้อยแล้ว")										
    elif cmd == "load":
        if sender in myMid:
            try:
                restoreProfile()
                line.sendMessage(to, "เรียกคืนสถานะบัญชีสำเร็จโปรดรอสักครู่จนกว่าโปรไฟล์จะเปลี่ยน")
            except Exception as e:
                line.sendMessage(to, "ไม่สามารถเรียกคืนสถานะบัญชีได้")
                line.sendMessage(msg.to, str(e))
    elif cmd == "save":
        if sender in myMid:
            try:
                backupProfile()
                line.sendMessage(to, "บันทึกสถานะบัญชีเรียบร้อยแล้ว")
            except Exception as e:
                line.sendMessage(to, "ไม่สามารถบันทึกสถานะบัญชีได้")
                line.sendMessage(msg.to, str(e))
    elif cmd == "addall":
        if wait["selfbot"] == True:
            if msg._from in admin:
                clfr = [Amid,Bmid,Cmid,Dmid,Emid,g1MID]
                kkfr = [myMid,Bmid,Cmid,Dmid,Emid,g1MID]#ki=Amid
                aafr = [myMid,Amid,Cmid,Dmid,Emid,g1MID]#kk=Bmid
                abfr = [myMid,Amid,Bmid,Dmid,Emid,g1MID]#kc=Cmid
                acfr = [myMid,Amid,Bmid,Cmid,Emid,g1MID]#km=Dmid
                adfr = [myMid,Amid,Bmid,Cmid,Dmid,g1MID]#kb=Emid
                aefr = [myMid,Amid,Bmid,Cmid,Dmid]#kb=Emid                
                for addcl in clfr:
                    line.findAndAddContactsByMid(addcl)
                line.sendMessage(to," Add ✓")
                for addki in kkfr:
                    kicker.findAndAddContactsByMid(addki)
                kicker.sendMessage(to," Add ✓")
                for addkk in aafr:
                    kicker2.findAndAddContactsByMid(addkk)
                kicker2.sendMessage(to," Add ✓")
                for addkc in abfr:
                    kicker3.findAndAddContactsByMid(addkc)
                kicker3.sendMessage(to," Add ✓")
                for addkm in acfr:
                    kicker4.findAndAddContactsByMid(addkm)
                kicker4.sendMessage(to," Add ✓")
                for addkb in adfr:
                    kicker5.findAndAddContactsByMid(addkb)
                kicker5.sendMessage(to," Add ✓")
                for addkbe in aefr:
                    g1.findAndAddContactsByMid(addkbe)
                g1.sendMessage(to," Add ✓")
    elif text.lower() == 'เปลี่ยนวีดีโอ':
      if wait["selfbot"] == True:		
        if msg._from in admin:						  
            line.sendMessage(to, "กรุณารอ20-30นาที")							
            picture = line.downloadFileURL("https://i.imgur.com/jfoJgrc.jpg", saveAs="image.jpg")
            video = line.downloadFileURL("https://www.saveoffline.com/get/?i=2she2Ctb02rA7GAkqP3UUPGRIE62OMtN&u=BaJCG5AmHn1RLtTKBT1JbX5d23u4mqxV", saveAs="video.mp4")
            changeVideoAndPictureProfile(picture, video)
            line.sendMessage(to, "เปลี่ยนเรียบร้อย")	
    elif cmd == "respon":
      if wait["selfbot"] == True:
        if msg._from in admin:
            try: 
                kicker.sendMessage(msg.to,responsename1)
                kicker2.sendMessage(msg.to,responsename2)
                kicker3.sendMessage(msg.to,responsename3)
                kicker4.sendMessage(msg.to,responsename4)	
                kicker5.sendMessage(msg.to,responsename5)
            except Exception as e:
                line.sendMessage(msg.to,"เกิดข้อผิดพลาด\n" +str(e))      
    elif cmd == "!in":
      if wait["selfbot"] == True:   
        if msg._from in admin:
            try:
                anggota = [Amid,Bmid,Cmid,Dmid,Emid]
                line.inviteIntoGroup(msg.to, anggota)
                kicker.acceptGroupInvitation(msg.to)
                kicker2.acceptGroupInvitation(msg.to)
                kicker3.acceptGroupInvitation(msg.to)
                kicker4.acceptGroupInvitation(msg.to)								
                kicker5.acceptGroupInvitation(msg.to)								
            except Exception as e:
                line.sendMessage(msg.to,"เกิดข้อผิดพลาด\n" +str(e))   
    elif cmd == "antijs stay":
      if wait["selfbot"] == True:
        if msg._from in admin:
            try:
                ginfo = line.getCompactGroup(msg.to)
                line.inviteIntoGroup(msg.to, [g1MID])
                line.sendMessage(msg.to,"Group 「"+str(ginfo.name)+"」 ทำการเปิดใช้งานโหมดป้องกันJS")
            except Exception as e:
                line.sendMessage(msg.to,"เกิดข้อผิดพลาด\n" +str(e))
    
    elif cmd == "!join":
        if wait["selfbot"] == True:
            if msg._from in admin:        
                if msg.toType == 2:
                    x = line.getCompactGroup(msg.to)
                    if x.preventedJoinByTicket:
                        x.preventedJoinByTicket = False
                        line.updateGroup(x)
                    Ticket = line.reissueGroupTicket(msg.to)
                    kicker.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.008)
                    kicker2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.008)  
                    kicker3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.008)
                    kicker4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.008)
                    kicker5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.008)
                    G = kicker.getCompactGroup(msg.to)
                    time.sleep(0.008)                      
                    G.preventedJoinByTicket = True                  
                    random.choice(ABC).updateGroup(G)
    elif cmd == "!out":
      if wait["selfbot"] == True:
        if msg._from in admin:
            G = line.getCompactGroup(msg.to)
            kicker.sendMessage(msg.to, "Bye bye fams "+str(G.name))
            kicker.leaveGroup(msg.to)
            kicker2.leaveGroup(msg.to)
            kicker3.leaveGroup(msg.to)
            kicker4.leaveGroup(msg.to)
            kicker5.leaveGroup(msg.to)		
    elif cmd == "kicker join":
        if msg._from in admin:
            G = line.getCompactGroup(msg.to)
            ginfo = line.getCompactGroup(msg.to)
            G.preventedJoinByTicket = False
            line.updateGroup(G)
            invsend = 0
            Ticket = line.reissueGroupTicket(msg.to)
            g1.acceptGroupInvitationByTicket(msg.to,Ticket)
            G = g1.getCompactGroup(msg.to)
            G.preventedJoinByTicket = True
            g1.updateGroup(G)

    elif cmd == "kicker bye":
        if msg._from in admin:
            G = line.getCompactGroup(msg.to)
            g1.leaveGroup(msg.to)

    elif cmd == "speedbot":
      if wait["selfbot"] == True:
        if msg._from in admin:
            start = time.time()
            kicker.sendMessage(to, "กำลังทดสอบ")          
            elapsed_time = time.time() - start
            kicker.sendMessage("u47d41cc45c4576282d0c52ce4d5b5856", ".")
            elapsed_time = time.time() - start
            kicker.sendMessage(msg.to, "[ %s Seconds ] " % (elapsed_time))
            start = time.time()
            kicker2.sendMessage("u47d41cc45c4576282d0c52ce4d5b5856", ".")
            elapsed_time = time.time() - start            
            kicker2.sendMessage(msg.to, "[ %s Seconds ] " % (elapsed_time))  
            start = time.time()
            kicker3.sendMessage("u47d41cc45c4576282d0c52ce4d5b5856", ".")
            elapsed_time = time.time() - start                 
            kicker3.sendMessage(msg.to, "[ %s Seconds ] " % (elapsed_time))
            start = time.time()
            kicker4.sendMessage("u47d41cc45c4576282d0c52ce4d5b5856", ".")
            elapsed_time = time.time() - start            
            kicker4.sendMessage(msg.to, "[ %s Seconds ] " % (elapsed_time)) 
            start = time.time()
            kicker5.sendMessage("u47d41cc45c4576282d0c52ce4d5b5856", ".")
            elapsed_time = time.time() - start                
            kicker5.sendMessage(msg.to, "[ %s Seconds ] " % (elapsed_time))
#===========Protection============#
    elif 'Protecturl ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Protecturl ','')
          if spl == 'on':
              if msg.to in protectqr:
                   msgs = "ป้องกัน URL ถูกเปิดใช้งานอยู่แล้ว"
              else:
                   protectqr.append(msg.to)
                   ginfo = line.getCompactGroup(msg.to)
                   msgs = "ป้องกัน URL เปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectqr:
                     protectqr.remove(msg.to)
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ป้องกัน URL ปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกัน URL ปิดใช้งานอยู่แล้ว"
                line.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)

    elif 'Protectkick ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Protectkick ','')
          if spl == 'on':
              if msg.to in protectkick:
                   msgs = "ป้องกันเตะถูกเปิดใช้งานอยู่แล้ว"
              else:
                   protectkick.append(msg.to)
                   ginfo = line.getCompactGroup(msg.to)
                   msgs = "ป้องกันเตะเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT KICK」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectkick:
                     protectkick.remove(msg.to)
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ป้องกันเตะปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันเตะปิดใช้งานอยู่แล้ว"
                line.sendMessage(msg.to, "「STATUS PROTECT KICK」\n" + msgs)

    elif 'Protectjoin ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Protecjoin ','')
          if spl == 'on':
              if msg.to in protecARoin:
                   msgs = "ป้องกันคนเข้าถูกเปิดใช้งานอยู่แล้ว"
              else:
                   protecARoin.append(msg.to)
                   ginfo = line.getCompactGroup(msg.to)
                   msgs = "ป้องกันคนเข้าเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT JOIN」\n" + msgs)
          elif spl == 'off':
                if msg.to in protecARoin:
                     protecARoin.remove(msg.to)
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ป้องกันคนเข้าปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันคนเข้าถูกปิดใช้งานอยู่แล้ว"
                line.sendMessage(msg.to, "「STATUS PROTECT JOIN」\n" + msgs)

    elif 'Protectcanceljs ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Protectcanceljs ','')
          if spl == 'on':
              if msg.to in protectcanceljs:
                   msgs = "ป้องกันยกเลิกเชิญบอทเปิดใช้งาน"
              else:
                   protectcanceljs[msg.to] = True
                   f=codecs.open('protectcanceljs.json','w','utf-8')
                   json.dump(protectcanceljs, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getCompactGroup(msg.to)
                   msgs = "ป้องกันยกเลิกเชิญบอทเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectcanceljs:
                     del protectcanceljs[msg.to]
                     f=codecs.open('protectcanceljs.json','w','utf-8')
                     json.dump(protectcanceljs, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ป้องกันยกเลิกเชิญบอทปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันยกเลิกเชิญบอทปิดใช้งาน"
                line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
 
    elif 'Protectcancel ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Protectcancel ','')
          if spl == 'on':
              if msg.to in protectcancel:
                   msgs = "ป้องกันยกเลิกเชิญถูกเปิดใช้งานอยู่แล้ว"
              else:
                   protectcancel[msg.to] = True
                   f=codecs.open('protectcancel.json','w','utf-8')
                   json.dump(protectcancel, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getCompactGroup(msg.to)
                   msgs = "ป้องกันยกเลิกเชิญเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectcancel:
                     del protectcancel[msg.to]
                     f=codecs.open('protectcancel.json','w','utf-8')
                     json.dump(protectcancel, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ป้องกันยกเลิกเชิญปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันยกเลิกเชิญถูกปิดใช้งานอยู่แล้ว"
                line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
        
    elif 'Protectinvite ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Protectinvite ','')
          if spl == 'on':
              if msg.to in protectinvite:
                   msgs = "ป้องกันเชิญถูกเปิดใช้งานอยู่แล้ว"
              else:
                   protectinvite[msg.to] = True
                   f=codecs.open('protectinvite.json','w','utf-8')
                   json.dump(protectinvite, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getCompactGroup(msg.to)
                   msgs = "ป้องกันเชิญเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectinvite:
                     del protectinvite[msg.to]
                     f=codecs.open('protectinvite.json','w','utf-8')
                     json.dump(protectinvite, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ป้องกันเชิญปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันเชิญถูกปิดใช้งานอยู่แล้ว"
                line.sendMessage(msg.to, "「STATUS PROTECT CANCEL」\n" + msgs)

    elif 'Antijs ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Antijs ','')
          if spl == 'on':
              if msg.to in protectantijs:
                   msgs = "ป้องกันJSถูกเปิดใช้งานอยู่แล้ว"
              else:
                   protectantijs[msg.to] = True
                   f=codecs.open('protectantijs.json','w','utf-8')
                   json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getCompactGroup(msg.to)
                   msgs = "ป้องกันJSเปิดใช้งาน\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT JS」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectantijs:
                     del protectantijs[msg.to]
                     f=codecs.open('protectantijs.json','w','utf-8')
                     json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)												 
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ป้องกันJSปิดใช้งาน\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ป้องกันJSถูกปิดใช้งานอยู่แล้ว"
                line.sendMessage(msg.to, "「STATUS PROTECT JS」\n" + msgs)
    elif "whois " in msg.text.lower():
        spl = re.split("whois ",msg.text,flags=re.IGNORECASE)
        if spl[0] == "":
            msg.contentType = 13
            msg.text = None
            msg.contentMetadata = {"mid":spl[1]}
            line.sendMessage(msg.to,text = None,contentMetadata = {"mid":spl[1]},contentType = 13)
                
    elif 'Ghost ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Ghost ','')
          if spl == 'on':
              if msg.to in ghost:
                   msgs = "เปิดใช้งานโหมด Ghost"
              else:
                   ghost[msg.to] = True
                   f=codecs.open('ghost.json','w','utf-8')
                   json.dump(ghost, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                   ginfo = line.getCompactGroup(msg.to)
                   msgs = "เปิดใช้งานโหมด Ghost\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT JS」\n" + msgs)
          elif spl == 'off':
                if msg.to in ghost:
                     del ghost[msg.to]
                     f=codecs.open('ghost.json','w','utf-8')
                     json.dump(ghost, f, sort_keys=True, indent=4,ensure_ascii=False)												 
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ปิดใช้งานโหมด Ghost\nIn Group : " +str(ginfo.name)
                else:
                     msgs = "ปิดใช้งานโหมด Ghost"
                line.sendMessage(msg.to, "「STATUS PROTECT JS」\n" + msgs)            

    elif 'Semua pro ' in msg.text:
       if msg._from in admin:
          spl = msg.text.replace('Semua pro ','')
          if spl == 'on':
              if msg.to in protectqr:
                   msgs = ""
              else:
                   protectqr.append(msg.to)
              if msg.to in protectkick:
                  msgs = ""
              else:
                  protectkick.append(msg.to)
              if msg.to in protectinvite:
                  msgs = ""
              else:
                  protectinvite.append(msg.to)                  
              if msg.to in protecARoin:
                  msgs = ""
              else:
                  protecARoin.append(msg.to)
              if msg.to in protectcancel:
                  ginfo = line.getCompactGroup(msg.to)
                  msgs = "การป้องกันทั้งหมดที่เปิดอยู่\nIn Group : " +str(ginfo.name)
              else:
                  protectcancel[msg.to] = True
                  f=codecs.open('protectcancel.json','w','utf-8')
                  json.dump(protectcancel, f, sort_keys=True, indent=4,ensure_ascii=False)									  
                  ginfo = line.getCompactGroup(msg.to)
                  msgs = "เปิดใช้การป้องกันทั้งหมด\nIn Group : " +str(ginfo.name)
              line.sendMessage(msg.to, "「STATUS PROTECT ALL」\n" + msgs)
          elif spl == 'off':
                if msg.to in protectqr:
                     protectqr.remove(msg.to)
                else:
                     msgs = ""
                if msg.to in protectkick:
                     protectkick.remove(msg.to)
                else:
                     msgs = ""
                if msg.to in protectinvite:
                     protectinvite.remove(msg.to)
                else:
                     msgs = ""                     
                if msg.to in protecARoin:
                     protecARoin.remove(msg.to)
                else:
                     msgs = ""
                if msg.to in protectcancel:
                     del protectcancel[msg.to]
                     f=codecs.open('protectcancel.json','w','utf-8')
                     json.dump(protectcancel, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "การป้องกันทั้งหมดที่ปิดอยู่\nIn Group : " +str(ginfo.name)
                else:
                     ginfo = line.getCompactGroup(msg.to)
                     msgs = "ปิดใช้การป้องกันทั้งหมด\nIn Group : " +str(ginfo.name)
                line.sendMessage(msg.to, "「STATUS PROTECT ALL」\n" + msgs)
    elif cmd == "refresh" or text.lower() == 'refresh':
        if msg._from in admin:
            wait["addadmin"] = False
            wait["delladmin"] = False
            wait["addstaff"] = False
            wait["dellstaff"] = False
            wait["addbots"] = False
            wait["dellbots"] = False
            wait["wblacklist"] = False
            wait["dblacklist"] = False
            wait["Talkwblacklist"] = False
            wait["Talkdblacklist"] = False
            line.sendMessage(msg.to,"รีเซ็ตข้อมูลแล้ว....")
    elif ("Ban " in msg.text):
      if wait["selfbot"] == True:
        if msg._from in admin:
           key = eval(msg.contentMetadata["MENTION"])
           key["MENTIONEES"][0]["M"]
           targets = []
           for x in key["MENTIONEES"]:
                targets.append(x["M"])
           for target in targets:
                   try:
                       wait["blacklist"][target] = True
                       line.sendMessage(msg.to,"เพิ่มบัญชีดำสำเร็จแล้ว")
                   except:
                       pass

    elif ("Unban " in msg.text):
      if wait["selfbot"] == True:
        if msg._from in admin:
           key = eval(msg.contentMetadata["MENTION"])
           key["MENTIONEES"][0]["M"]
           targets = []
           for x in key["MENTIONEES"]:
                targets.append(x["M"])
           for target in targets:
                   try:
                       del wait["blacklist"][target]
                       line.sendMessage(msg.to,"ลบบัญชีดำสำเร็จแล้ว")
                   except:
                       pass

    elif cmd == "ban":
      if wait["selfbot"] == True:
        if msg._from in admin:
            wait["wblacklist"] = True
            line.sendMessage(to,"Send contact you will be blacklist")

    elif cmd == "unban":
      if wait["selfbot"] == True:
        if msg._from in admin:
            wait["dblacklist"] = True
            line.sendMessage(to,"Send contact you will be whitelist")

    elif cmd == "bc" or text.lower() == 'banlist':
      if wait["selfbot"] == True:
        if msg._from in admin:
          if wait["blacklist"] == {}:
            line.sendMessage(msg.to,"ไม่พบคนติดดำ")
          else:
            ma = ""
            a = 0
            for m_id in wait["blacklist"]:
                a = a + 1
                end = '\n'
                ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
            line.sendMessage(msg.to,"❧ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

    elif cmd == "bc":
      if wait["selfbot"] == True:
        if msg._from in admin:
          if wait["blacklist"] == {}:
                line.sendMessage(msg.to,"ไม่พบคนติดดำ")
          else:
                ma = ""
                for i in wait["blacklist"]:
                    ma = line.getContact(i)
                    line.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

    elif cmd == "cb":
      if wait["selfbot"] == True:
        if msg._from in admin:
          wait["blacklist"] = {}
          ragets = line.getContacts(wait["blacklist"])
          mc = "「%i」 ᴜꜱᴇʀ ʙʟᴀᴄᴋʟɪꜱᴛ" % len(ragets)
          line.sendMessage(msg.to,"ล้างบัญชีดำแล้ว " +mc)
          kicker.sendMessage(msg.to,"ล้างบัญชีดำแล้ว " +mc)
          kicker2.sendMessage(msg.to,"ล้างบัญชีดำแล้ว " +mc)
          kicker3.sendMessage(msg.to,"ล้างบัญชีดำแล้ว " +mc)
          kicker4.sendMessage(msg.to,"ล้างบัญชีดำแล้ว " +mc)
          kicker5.sendMessage(msg.to,"ล้างบัญชีดำแล้ว " +mc)      
    elif cmd.startswith('error'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Error 」'
        res += '\n├ Usage : '
        res += '\n│ • {key}Error'
        res += '\n│ • {key}Error Logs'
        res += '\n│ • {key}Error Reset'
        res += '\n│ • {key}Error Detail <errid>'
        res += '\n╰───「 AOY 」'
        if cmd == 'error':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'logs':
            try:
                filee = open('errorLog.txt', 'r')
            except FileNotFoundError:
                return line.sendMessage(to, 'ไม่สามารถแสดงบันทึกข้อผิดพลาดได้\nไม่พบไฟล์')
            errors = [err.strip() for err in filee.readlines()]
            filee.close()
            if not errors: return line.sendMessage(to, 'ไม่สามารถแสดงบันทึกข้อผิดพลาดได้\nบันทึกข้อผิดพลาดว่างเปล่า')
            res = '╭───「 Error Logs 」'
            res += '\n├ List :'
            parsed_len = len(errors)//200+1
            no = 0
            for point in range(parsed_len):
                for error in errors[point*200:(point+1)*200]:
                    if not error: continue
                    no += 1
                    res += '\n│ %i. %s' % (no, error)
                    if error == errors[-1]:
                        res += '\n╰───「 AOY 」'
                if res:
                    if res.startswith('\n'): res = res[1:]
                    line.sendMessage(to, res)
                res = ''
        elif cond[0].lower() == 'reset':
            filee = open('errorLog.txt', 'w')
            filee.write('')
            filee.close()
            shutil.rmtree('tmp/errors/', ignore_errors=True)
            os.system('mkdir tmp/errors')
            line.sendMessage(to, 'Success reset error logs')
        elif cond[0].lower() == 'detail':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            errid = cond[1]
            if os.path.exists('tmp/errors/%s.txt' % errid):
                with open('tmp/errors/%s.txt' % errid, 'r') as f:
                    line.sendMessage(to, f.read())
            else:
                return line.sendMessage(to, 'Failed display details error, errorid not valid')
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif txt.startswith('setkey'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Setting Key 」'
        res += '\n├ Status : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├ Key : ' + settings['setKey']['key'].title()
        res += '\n├ Usage : '
        res += '\n│ • Setkey'
        res += '\n│ • Setkey <on/off>'
        res += '\n│ • Setkey <key>'
        res += '\n╰───「 AOY」'
        if txt == 'setkey':
            line.sendMessage(to, parsingRes(res))
        elif texttl == 'on':
            if settings['setKey']['status']:
                line.sendMessage(to, 'Failed activate setkey, setkey already active')
            else:
                settings['setKey']['status'] = True
                line.sendMessage(to, 'Success activated setkey')
        elif texttl == 'off':
            if not settings['setKey']['status']:
                line.sendMessage(to, 'Failed deactivate setkey, setkey already deactive')
            else:
                settings['setKey']['status'] = False
                line.sendMessage(to, 'Success deactivated setkey')
        else:
            settings['setKey']['key'] = texttl
            line.sendMessage(to, 'Success change set key to (%s)' % textt)
    elif cmd.startswith('autoadd'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Add 」'
        res += '\n├ Status : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoAdd']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoAdd']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoAdd'
        res += '\n│ • {key}AutoAdd <on/off>'
        res += '\n│ • {key}AutoAdd Reply <on/off>'
        res += '\n│ • {key}AutoAdd <message>'
        res += '\n╰───「 AOY」'
        if cmd == 'autoadd':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoAdd']['status']:
                line.sendMessage(to, 'เปิดรับแอดออโต้')
            else:
                settings['autoAdd']['status'] = True
                line.sendMessage(to, 'เปิดรับแอดออโต้')
        elif texttl == 'off':
            if not settings['autoAdd']['status']:
                line.sendMessage(to, 'ปิดรับแอดออโต้')
            else:
                settings['autoAdd']['status'] = False
                line.sendMessage(to, 'ปิดรับแอดออโต้')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoAdd']['reply']:
                    line.sendMessage(to, 'เปิดข้อความทักคนแอด')
                else:
                    settings['autoAdd']['reply'] = True
                    line.sendMessage(to, 'เปิดข้อความทักคนแอด')
            elif cond[1].lower() == 'off':
                if not settings['autoAdd']['reply']:
                    line.sendMessage(to, 'ปิดข้อความทักคนแอด')
                else:
                    settings['autoAdd']['reply'] = False
                    line.sendMessage(to, 'ปิดข้อความทักคนแอด')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoAdd']['message'] = textt
            line.sendMessage(to, 'เปลี่ยนข้อความออโต้แอดเป็น `%s`' % textt)
    elif cmd.startswith('autojoin'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Join 」'
        res += '\n├ Status : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoJoin']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoJoin']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoJoin'
        res += '\n│ • {key}AutoJoin <on/off>'
        res += '\n│ • {key}AutoJoin Ticket <on/off>'
        res += '\n│ • {key}AutoJoin Reply <on/off>'
        res += '\n│ • {key}AutoJoin <message>'
        res += '\n╰───「 AOY」'
        if cmd == 'autojoin':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoJoin']['status']:
                line.sendMessage(to, 'เปิดเข้าร่วมกลุ่มออโต้')
            else:
                settings['autoJoin']['status'] = True
                line.sendMessage(to, 'เปิดเข้าร่วมกลุ่มออโต้')
        elif texttl == 'off':
            if not settings['autoJoin']['status']:
                line.sendMessage(to, 'ปิดเข้าร่วมกลุ่มออโต้')
            else:
                settings['autoJoin']['status'] = False
                line.sendMessage(to, 'ปิดเข้าร่วมกลุ่มออโต้')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['reply']:
                    line.sendMessage(to, 'เปิดความทักคนเชิญเข้ากลุ่ม')
                else:
                    settings['autoJoin']['reply'] = True
                    line.sendMessage(to, 'เปิดความทักคนเชิญเข้ากลุ่ม')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['reply']:
                    line.sendMessage(to, 'ปิดความทักคนเชิญเข้ากลุ่ม')
                else:
                    settings['autoJoin']['reply'] = False
                    line.sendMessage(to, 'ปิดความทักคนเชิญเข้ากลุ่ม')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'ticket':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['ticket']:
                    line.sendMessage(to, 'เปิดเข้ากลุ่มออโต้ด้วยลิ้ง')
                else:
                    settings['autoJoin']['ticket'] = True
                    line.sendMessage(to, 'เปิดเข้ากลุ่มออโต้ด้วยลิ้ง')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['ticket']:
                    line.sendMessage(to, 'ปิดเข้ากลุ่มออโต้ด้วยลิ้ง')
                else:
                    settings['autoJoin']['ticket'] = False
                    line.sendMessage(to, 'ปิดเข้ากลุ่มออโต้ด้วยลิ้ง')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoJoin']['message'] = textt
            line.sendMessage(to, 'ข้อความทักคนเชิญเข้ากลุ่มเปลี่ยนเป็น `%s`' % textt)
    elif cmd.startswith('autorespondmention'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Auto Respond 」'
        res += '\n├ Status : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├ Reply Message : ' + settings['autoRespondMention']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoRespondMention'
        res += '\n│ • {key}AutoRespondMention <on/off>'
        res += '\n│ • {key}AutoRespondMention <message>'
        res += '\n╰───「 AOY 」'     
        if cmd == 'autorespondmention':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespondMention']['status']:
                line.sendMessage(to, 'เปิดตอบกลับคนแทค')
            else:
                settings['autoRespondMention']['status'] = True
                line.sendMessage(to, 'เปิดตอบกลับคนแทค')
        elif texttl == 'off':
            if not settings['autoRespondMention']['status']:
                line.sendMessage(to, 'ปิดตอบกลับคนแทค')
            else:
                settings['autoRespondMention']['status'] = False
                line.sendMessage(to, 'ปิดตอบกลับคนแทค')
        else:
            settings['autoRespondMention']['message'] = textt
            line.sendMessage(to, 'ข้อความตอบกลับคนแทคเปลี่ยนเป็น `%s`' % textt)
    elif cmd.startswith('autorespond'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Auto Respond 」'
        res += '\n├ Status : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├ Reply Message : ' + settings['autoRespond']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoRespond'
        res += '\n│ • {key}AutoRespond <on/off>'
        res += '\n│ • {key}AutoRespond <message>'
        res += '\n╰───「 AOY 」'
        if cmd == 'autorespond':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespond']['status']:
                line.sendMessage(to, 'เปิดตอบกลับอัตโนมัติ')
            else:
                settings['autoRespond']['status'] = True
                line.sendMessage(to, 'เปิดตอบกลับอัตโนมัติ')
        elif texttl == 'off':
            if not settings['autoRespond']['status']:
                line.sendMessage(to, 'ปิดตอบกลับอัตโนมัติ')
            else:
                settings['autoRespond']['status'] = False
                line.sendMessage(to, 'ปิดตอบกลับอัตโนมัติ')
        else:
            settings['autoRespond']['message'] = textt
            line.sendMessage(to, 'ข้อความเปิดตอบกลับอัตโนมัติถูกเปลี่ยนเป็น `%s`' % textt)
    elif cmd.startswith('autoread '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['autoRead']:
                line.sendMessage(to, 'เปิดอ่านออโต้')
            else:
                settings['autoRead'] = True
                line.sendMessage(to, 'เปิดอ่านออโต้')
        elif texttl == 'off':
            if not settings['autoRead']:
                line.sendMessage(to, 'ปิดอ่านออโต้')
            else:
                settings['autoRead'] = False
                line.sendMessage(to, 'ปิดอ่านออโต้')
    elif cmd.startswith('checkcontact '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkContact']:
                line.sendMessage(to, 'เปิดเช็คคท')
            else:
                settings['checkContact'] = True
                line.sendMessage(to, 'เปิดเช็คคท')
        elif texttl == 'off':
            if not settings['checkContact']:
                line.sendMessage(to, 'ปิดเช็คคท')
            else:
                settings['checkContact'] = False
                line.sendMessage(to, 'ปิดเช็คคท')
    elif cmd.startswith('checkpost '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkPost']:
                line.sendMessage(to, 'เปิดเช็คโพส')
            else:
                settings['checkPost'] = True
                line.sendMessage(to, 'เปิดเช็คโพส')
        elif texttl == 'off':
            if not settings['checkPost']:
                line.sendMessage(to, 'ปิดเช็คโพส')
            else:
                settings['checkPost'] = False
                line.sendMessage(to, 'ปิดเช็คโพส')
    elif cmd.startswith('checksticker '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkSticker']:
                line.sendMessage(to, 'เปิดเช็คสติ๊กเกอร์')
            else:
                settings['checkSticker'] = True
                line.sendMessage(to, 'เปิดเช็คสติ๊กเกอร์')
        elif texttl == 'off':
            if not settings['checkSticker']:
                line.sendMessage(to, 'ปิดเช็คสติ๊กเกอร์')
            else:
                settings['checkSticker'] = False
                line.sendMessage(to, 'ปิดเช็คสติ๊กเกอร์')
    elif cmd.startswith('myprofile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getProfile()
        res = '╭───「 My Profile 」'
        res += '\n├ MID : ' + profile.mid
        res += '\n├ Display Name : ' + str(profile.displayName)
        res += '\n├ Usage : '
        res += '\n│ • {key}MyProfile'
        res += '\n│ • {key}MyProfile MID'
        res += '\n│ • {key}MyProfile Name'
        res += '\n│ • {key}MyProfile Bio'
        res += '\n│ • {key}MyProfile Pict'
        res += '\n│ • {key}MyProfile Cover'
        res += '\n│ • {key}MyProfile Change Name <name>'
        res += '\n│ • {key}MyProfile Change Bio <bio>'
        res += '\n│ • {key}MyProfile Change Pict'
        res += '\n│ • {key}MyProfile Change Cover'
        res += '\n╰───「 AOY」'
        if texttl == 'mid':
            line.sendMessage(to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendMessage(to, '「 Picture Status 」\n' + path)
            else:
                line.sendMessage(to, 'ไม่สามารถแสดงรูปได้เนื่องจากผู้ใช้นี้ไม่ได้ใส่รูป')
        elif texttl == 'cover':
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('change '):
            texts = textt[7:]
            textsl = texts.lower()
            if textsl.startswith('name '):
                name = texts[5:]
                if len(name) <= 20:
                    profile.displayName = name
                    line.updateProfile(profile)
                    line.sendMessage(to, 'เปลี่ยนชื่อสำเร็จ\nเปลี่ยนชื่อเป็น`%s`' % name)
                else:
                    line.sendMessage(to, 'ไม่สามารถเปลี่ยนชื่อได้\nความยาวของชื่อต้องไม่เกิน 20')
            elif textsl.startswith('bio '):
                bio = texts[4:]
                if len(bio) <= 3000:
                    profile.statusMessage = bio
                    line.updateProfile(profile)
                    line.sendMessage(to, 'เปลี่ยนสถานะเรียบร้อย\nเปลี่ยนสถนานะเป็น `%s`' % bio)
                else:
                    line.sendMessage(to, 'ไม่สามารถเปลี่ยนสถานะได้\nความยาวของข้อความสถานะต้องไม่เกิน3000')
            elif textsl == 'pict':
                settings['changePictureProfile'] = True
                line.sendMessage(to, 'กรุณาส่งภาพเพื่อเปลี่ยนรูปโปรไฟล์, พิม `{key}Abort` ถ้าต้องการยกเลิก\nคำเตือน:การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพนานเกินไป'.format(key=setKey.title()))
            elif textsl == 'cover':
                settings['changeCoverProfile'] = True
                line.sendMessage(to, 'กรุณาส่งภาพเพื่อเปลี่ยนรูปปก, พิม `{key}Abort` ถ้าต้องการยกเลิก\nคำเตือน:การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพนานเกินไป'.format(key=setKey.title()))
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('profile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getContact(to) if msg.toType == 0 else None
        res = '╭───「 My Profile 」'
        if profile:
            res += '\n├ MID : ' + profile.mid
            res += '\n├ Display Name : ' + str(profile.displayName)
            if profile.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(profile.displayNameOverridden)
            res += '\n├ Status Message : ' + str(profile.statusMessage)
        res += '\n├ Usage : '
        res += '\n│ • {key}Profile'
        res += '\n│ • {key}Profile Mid'
        res += '\n│ • {key}Profile Name'
        res += '\n│ • {key}Profile Bio'
        res += '\n│ • {key}Profile Pict'
        res += '\n│ • {key}Profile Cover'
        res += '\n│ • {key}Profile Steal Profile <mention>'
        res += '\n│ • {key}Profile Steal Mid <mention>'
        res += '\n│ • {key}Profile Steal Name <mention>'
        res += '\n│ • {key}Profile Steal Bio <mention>'
        res += '\n│ • {key}Profile Steal Pict <mention>'
        res += '\n│ • {key}Profile Steal Cover <mention>'
        res += '\n╰───「 AOY 」'
        if texttl == 'mid':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            line.sendMessage(to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendMessage(to, '「 Picture Status 」\n' + path)
            else:
                line.sendMessage(to, 'ไม่สามารถแสดงรูปได้เนื่องจากผู้ใช้นี้ไม่ได้ใส่รูป')
        elif texttl == 'cover':
            if msg.toType != 0: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้ในแชทส่วนตัวเท่านั้น')
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('steal '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl.startswith('profile '):
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        profile = line.getContact(mention['M'])
                        if profile.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                        cover = line.getProfileCoverURL(profile.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Profile 」'
                        res += '\n├ MID : ' + profile.mid
                        res += '\n├ Display Name : ' + str(profile.displayName)
                        if profile.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(profile.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(profile.statusMessage)
                        res += '\n╰───「 Edit by รัตน์」'
                        line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงรูปโปรไฟล์ได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('mid '):
                res = '╭───「 MID 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        return line.sendMessage(to, '「 MID 」\n' + mid)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        res += '\n│ %i. %s' % (no, mid)
                    res += '\n╰───「 Edit by รัตน์」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงmidได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('name '):
                res = '╭───「 Display Name 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.displayName)
                    res += '\n╰───「 Edit by รัตน์」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงชื่อได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('bio '):
                res = '╭───「 Status Message 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.statusMessage)
                    res += '\n╰───「 Edit by รัตน์」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงสถานะได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('pict '):
                res = '╭───「 Picture Status 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            return line.sendMessage(to, '「 Picture Status 」\n' + path)
                        else:
                            return line.sendMessage(to, 'ไม่สามารถดึงรูปได้, บุคคนนี้ `%s` doesn\'ไม่ได้ใส่รูปภาพโปรไฟล์' % profile.displayName)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            res += '\n│ %i. %s' % (no, path)
                        else:
                            res += '\n│ %i. Not Found' % no
                    res += '\n╰───「 Edit by รัตน์」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงรูปได้, กรุณาแทคผู้ใช้ด้วย')
            elif textsl.startswith('cover '):
                res = '╭───「 Cover Picture 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        res += '\n│ %i. %s' % (no, cover)
                    res += '\n╰───「 Edit by รัตน์」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'ไม่สามารถดึงปกได้, กรุณาแทคผู้ใช้ด้วย')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('mimic'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        targets = ''
        if settings['mimic']['target']:
            no = 0
            for target, status in settings['mimic']['target'].items():
                no += 1
                try:
                    name = line.getContact(target).displayName
                except TalkException:
                    name = 'Unknown'
                targets += '\n│ %i. %s//%s' % (no, name, bool_dict[status][1])
        else:
            targets += '\n│ Nothing'
        res = '╭───「 Mimic 」'
        res += '\n├ Status : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├ List :'
        res += targets
        res += '\n├ Usage : '
        res += '\n│ • {key}Mimic'
        res += '\n│ • {key}Mimic <on/off>'
        res += '\n│ • {key}Mimic Reset'
        res += '\n│ • {key}Mimic Add <mention>'
        res += '\n│ • {key}Mimic Del <mention>'
        res += '\n╰───「 AOY」'
        if cmd == 'mimic':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['mimic']['status']:
                line.sendMessage(to, 'เริ่มการล้อเลียน')
            else:
                settings['mimic']['status'] = True
                line.sendMessage(to, 'เริ่มการล้อเลียน')
        elif texttl == 'off':
            if not settings['mimic']['status']:
                line.sendMessage(to, 'ยกเลิกการล้อเลียน')
            else:
                settings['mimic']['status'] = False
                line.sendMessage(to, 'ยกเลิกการล้อเลียน')
        elif texttl == 'reset':
            settings['mimic']['target'] = {}
            line.sendMessage(to, 'รีเช็ตรายชื่อที่จะล้อเลี่ยนเรียบร้อย')
        elif texttl.startswith('add '):
            res = '╭───「 Mimic 」'
            res += '\n├ Status : Add Target'
            res += '\n├ Added :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    settings['mimic']['target'][mid] = True
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 Edit by รัตน์」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'ไม่สามารถเพื่มรายชื่อได้, กรุณาแทคผู้ใช้ด้วย')
        elif texttl.startswith('del '):
            res = '╭───「 Mimic 」'
            res += '\n├ Status : Del Target'
            res += '\n├ Deleted :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in settings['mimic']['target']:
                        settings['mimic']['target'][mid] = False
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 Edit by รัตน์」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'ไม่สามารถลบรายชื่อได้, กรุณาแทคผู้ใช้ด้วย')
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('broadcast'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Broadcast 」'
        res += '\n├ Broadcast Type : '
        res += '\n│ 1 : Friends'
        res += '\n│ 2 : Groups'
        res += '\n│ 0 : All'
        res += '\n├ Usage : '
        res += '\n│ • {key}Broadcast'
        res += '\n│ • {key}Broadcast <type> <message>'
        res += '\n╰───「 AOY 」'
        if cmd == 'broadcast':
            line.sendMessage(to, parsingRes(res).format(key=setKey.title()))
        elif cond[0] == '1':
            if len(cond) < 2:
                return line.sendMessage(to, 'ไม่สามารถประกาศได้, ไม่พบข้อความ')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 AOY 」'
            targets = line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'ประกาศเรียบร้อย, จำนวน %i คน' % len(targets))
        elif cond[0] == '2':
            if len(cond) < 2:
                return line.sendMessage(to, 'ไม่สามารถประกาศได้, ไม่พบข้อความ')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 AOY 」'
            targets = line.getGroupIdsJoined()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'ประกาศเรียบร้อย, จำนวน %i กลุ่ม' % len(targets))
        elif cond[0] == '0':
            if len(cond) < 2:
                return line.sendMessage(to, 'ไม่สามารถประกาศได้, ไม่พบข้อความ')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 AOY」'
            targets = line.getGroupIdsJoined() + line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'ประกาศเรียบร้อย, จำนวน %i ' % len(targets))
        else:
            line.sendMessage(to, parsingRes(res).format(key=setKey.title()))
    elif cmd.startswith('friendlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getAllContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───「 Friend List 」'
        res += '\n├ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}FriendList'
        res += '\n│ • {key}FriendList Info <num/name>'
        res += '\n│ • {key}FriendList Add <mention>'
        res += '\n│ • {key}FriendList Del <mention/num/name/all>'
        res += '\n╰───「 AOY 」'
        ress.append(res)
        if cmd == 'friendlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendMessage(to, 'แสดงข้อมูลเพื่อนล้มเหลว, ไม่พบเพื่อน')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───「 Contact Info 」'
                    res += '\n├ MID : ' + contact.mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 AOY 」'
                    line.sendMessage(to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Contact Info 」'
                        res += '\n├ MID : ' + contact.mid
                        res += '\n├ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───「 AOY 」'
                        line.sendMessage(to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───「 Friend List 」'
            res += '\n├ Status : Add Friend'
            res += '\n├ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.findAndAddContactsByMid(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 Edit by รัตน์」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'ไม่สามารถแอดเพื่อนได้, กรุณาแทคผู้ใช้ด้วย')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendMessage(to, 'เปิดข้อผิดพลาดที่ไม่แน่ชัด')
            res = '╭───「 Friend List 」'
            res += '\n├ Status : Del Friend'
            res += '\n├ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.deleteContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.deleteContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        line.sendMessage(to, 'Failed del friend with name `%s`, ไม่พบชื่อกลุ่มนี้ ♪' % name)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───「 AOY 」'
            line.sendMessage(to, res)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('blocklist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getBlockedContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───「 Block List 」'
        res += '\n├ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}BlockList'
        res += '\n│ • {key}BlockList Info <num/name>'
        res += '\n│ • {key}BlockList Add <mention>'
        res += '\n│ • {key}BlockList Del <mention/num/name/all>'
        res += '\n╰───「 AOY」'
        ress.append(res)
        if cmd == 'blocklist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendMessage(to, 'แสดงข้อมูลผู้ใช้ที่ถูกบล็อกล้มเหลว, ไม่มีผู้ใช้ในรายการ')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───「 Contact Info 」'
                    res += '\n├ MID : ' + contact.mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 AOY」'
                    line.sendMessage(to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Contact Info 」'
                        res += '\n├ MID : ' + contact.mid
                        res += '\n├ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───「 AOY」'
                        line.sendMessage(to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───「 Block List 」'
            res += '\n├ Status : Add Block'
            res += '\n├ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.blockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 AOY」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed block contact, กรุณาแทคผู้ใช้ด้วย')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendMessage(to, 'ไม่สามาถปลกบล็อคได้, ไม่มีผู้ใช้ในรายการ')
            res = '╭───「 Block List 」'
            res += '\n├ Status : Del Block'
            res += '\n├ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.unblockContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.unblockContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        line.sendMessage(to, 'ไม่สามารถปลดบล็อกรายชื่อนี้ได้ `%s`, ชื่อไม่อยู่ในรายการ ♪' % name)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───「 AOY 」'
            line.sendMessage(to, res)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
#===========BOT UPDATE============#
    elif msg.text.lower().startswith("mentionall"):
      if msg._from in admin:						
        data = msg.text[len("mentionall"):].strip()
        if data == "":
            group = line.getCompactGroup(msg.to)
            nama = [contact.mid for contact in group.members if contact.mid != zxcvzx]
            cb = ""
            cb2 = ""
            count = 1
            strt = len(str(count)) + 2
            akh = int(0)
            cnt = 0
            for md in nama:
                akh = akh + len(str(count)) + 2 + 5
                cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                strt = strt + len(str(count+1)) + 2 + 6
                akh = akh + 1
                cb2 += str(count)+". @name\n"
                cnt = cnt + 1
                if cnt == 20:
                            cb = (cb[:int(len(cb)-1)])
                            cb2 = cb2[:-1]
                            msg.contentType = 0
                            msg.text = cb2
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                            try:
                                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                            except:
                                line.sendMessage(msg.to,"[[NO MENTION]]")
                            cb = ""
                            cb2 = ""
                            strt = len(str(count)) + 2
                            akh = int(0)
                            cnt = 0
                count += 1
            cb = (cb[:int(len(cb)-1)])
            cb2 = cb2[:-1]
            msg.contentType = 0
            msg.text = cb2
            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
            try:
                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
            except:
                line.sendMessage(msg.to,"[[NO MENTION]]")
        elif data[0] == "<":
            mentargs = int(data[1:].strip())
            group = line.getCompactGroup(msg.to)
            nama = [contact.mid for contact in group.members if contact.mid != zxcvzx]
            cb = ""
            cb2 = ""
            count = 1
            strt = len(str(count)) + 2
            akh = int(0)
            cnt = 0
            for md in nama:
                if count > mentargs:
                            break
                akh = akh + len(str(count)) + 2 + 5
                cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                strt = strt + len(str(count+1)) + 2 + 6
                akh = akh + 1
                cb2 += str(count)+". @name\n"
                cnt = cnt + 1
                if cnt == 20:
                            cb = (cb[:int(len(cb)-1)])
                            cb2 = cb2[:-1]
                            msg.contentType = 0
                            msg.text = cb2
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                            try:
                                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                            except:
                                line.sendMessage(msg.to,"[[NO MENTION]]")
                            cb = ""
                            cb2 = ""
                            strt = len(str(count)) + 2
                            akh = int(0)
                            cnt = 0
                count += 1
            cb = (cb[:int(len(cb)-1)])
            cb2 = cb2[:-1]
            msg.contentType = 0
            msg.text = cb2
            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
            try:
                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
            except:
                line.sendMessage(msg.to,"[[NO MENTION]]")
        elif data[0] == ">":
            mentargs = int(data[1:].strip())
            group = line.getCompactGroup(msg.to)
            nama = [contact.mid for contact in group.members if contact.mid != zxcvzx]
            cb = ""
            cb2 = ""
            count = 1
            if mentargs >= 0:
                strt = len(str(mentargs)) + 2
            else:
                strt = len(str(count)) + 2
            akh = int(0)
            cnt = 0
            for md in nama:
                if count < mentargs:
                            count += 1
                            continue
                akh = akh + len(str(count)) + 2 + 5
                cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                strt = strt + len(str(count+1)) + 2 + 6
                akh = akh + 1
                cb2 += str(count)+". @name\n"
                cnt = cnt + 1
                if cnt == 20:
                            cb = (cb[:int(len(cb)-1)])
                            cb2 = cb2[:-1]
                            msg.contentType = 0
                            msg.text = cb2
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                            try:
                                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                            except:
                                line.sendMessage(msg.to,"[[NO MENTION]]")
                            cb = ""
                            cb2 = ""
                            strt = len(str(count)) + 2
                            akh = int(0)
                            cnt = 0
                count += 1
            cb = (cb[:int(len(cb)-1)])
            cb2 = cb2[:-1]
            msg.contentType = 0
            msg.text = cb2
            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
            try:
                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
            except:
                line.sendMessage(msg.to,"[[NO MENTION]]")
        elif data[0] == "=":
            mentargs = int(data[1:].strip())
            group = line.getCompactGroup(msg.to)
            nama = [contact.mid for contact in group.members if contact.mid != zxcvzx]
            cb = ""
            cb2 = ""
            count = 1
            akh = int(0)
            cnt = 0
            for md in nama:
                if count != mentargs:
                            count += 1
                            continue
                akh = akh + len(str(count)) + 2 + 5
                strt = len(str(count)) + 2
                cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                strt = strt + len(str(count+1)) + 2 + 6
                akh = akh + 1
                cb2 += str(count)+". @name\n"
                cnt = cnt + 1
                if cnt == 20:
                            cb = (cb[:int(len(cb)-1)])
                            cb2 = cb2[:-1]
                            msg.contentType = 0
                            msg.text = cb2
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                            try:
                                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                            except:
                                line.sendMessage(msg.to,"[[NO MENTION]]")
                            cb = ""
                            cb2 = ""
                            strt = len(str(count)) + 2
                            akh = int(0)
                            cnt = 0
                count += 1
            cb = (cb[:int(len(cb)-1)])
            cb2 = cb2[:-1]
            msg.contentType = 0
            msg.text = cb2
            msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
            try:
                line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
            except:
                line.sendMessage(msg.to,"[[NO MENTION]]")
    elif cmd == 'groupinfo':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถดูข้อมูลกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getCompactGroup(to)
        try:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        except:
            ccreator = None
            gcreator = 'Not found'
        if not group.invitee:
            pendings = 0
        else:
            pendings = len(group.invitee)
        qr = 'Close' if group.preventedJoinByTicket else 'Open'
        if group.preventedJoinByTicket:
            ticket = 'Not found'
        else:
            ticket = 'https://line.me/R/ti/g/' + str(line.reissueGroupTicket(group.id))
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = '╭───「 Group Info 」'
        res += '\n├ ID : ' + group.id
        res += '\n├ Name : ' + group.name
        res += '\n├ Creator : ' + gcreator
        res += '\n├ Created Time : ' + created
        res += '\n├ Member Count : ' + str(len(group.members))
        res += '\n├ Pending Count : ' + str(pendings)
        res += '\n├ QR Status : ' + qr
        res += '\n├ Ticket : ' + ticket
        res += '\n╰───「 AOY 」'
        line.sendImageWithURL(to, path)
        if ccreator:
            line.sendContact(to, ccreator)
        line.sendMessage(to, res)
    elif cmd.startswith('grouplist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsJoined()
        gnames = []
        ress = []
        res = '╭───「 Group List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}GroupList'
        res += '\n│ • {key}GroupList Leave <num/name/all>'
        res += '\n╰───「 AOY 」'
        ress.append(res)
        if cmd == 'grouplist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('leave '):
            texts = textt[6:].split(', ')
            leaved = []
            if not gids:
                return line.sendMessage(to, 'ไม่สามารถออกลุ่มได้\nไม่พบชื่อกลุ่มนี้')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in leaved:
                            line.sendMessage(to, 'ออกจากลุ่มเรียบร้อย %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'ออกจากลุ่มเรียบร้อย %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed leave group number %i, เลขเกิน!' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in leaved:
                            line.sendMessage(to, 'ออกจากลุ่มเรียบร้อย %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'ออกจากลุ่มเรียบร้อย %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in leaved:
                                continue
                            line.leaveGroup(gid)
                            leaved.append(gid)
                            time.sleep(0.8)
                        if to not in leaved:
                            line.sendMessage(to, 'ออกทุกกลุ่มเรียบร้อย ♪')
                    else:
                        line.sendMessage(to, 'ไม่สามารถออกกลุ่มชื่อ `%s`นี้ได้\nไม่พบชื่อกลุ่มนี้ ♪' % name)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('invitationlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsInvited()
        gnames = []
        ress = []
        res = '╭───「 Invitation List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}InvitationList'
        res += '\n│ • {key}InvitationList Accept <num/name/all>'
        res += '\n│ • {key}InvitationList Reject <num/name/all>'
        res += '\n╰───「 AOY 」'
        ress.append(res)
        if cmd == 'invitationlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('accept '):
            texts = textt[7:].split(', ')
            accepted = []
            if not gids:
                return line.sendMessage(to, 'ไม่สามารถเข้าร่วมกลุ่มได้\nไม่มีคำเชิญเข้ากลุ่ม')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in accepted:
                            line.sendMessage(to, 'ทำการเข้าร่วมกลุ่ม %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendMessage(to, 'ทำการเข้าร่วมกลุ่ม %s' % group.name)
                    else:
                        line.sendMessage(to, 'ไม่สามารถเข้าร่วมกลุ่มได้ เนื่องจากมายเลข %i นี้มากว่าคำเชิญที่คุณมี' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in accepted:
                            line.sendMessage(to, 'ทำการเข้าร่วมกลุ่ม %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendMessage(to, 'ทำการเข้าร่วมกลุ่ม %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in accepted:
                                continue
                            line.acceptGroupInvitation(gid)
                            accepted.append(gid)
                            time.sleep(0.8)
                        line.sendMessage(to, 'ทำการเข้าร่วมกลุ่มทั้งหมดแล้ว ♪')
                    else:
                        line.sendMessage(to, 'ไม่สามารถเข้าร่วมกลุ่มได้ `%s`, ไม่พบชื่อกลุ่มนี้ ♪' % name)
        elif texttl.startswith('reject '):
            texts = textt[7:].split(', ')
            rejected = []
            if not gids:
                return line.sendMessage(to, 'ไม่สามารถคำเชิญเข้าร่วมกลุ่มได้\nไม่มีคำเชิญเข้าร่วมกลุ่ม')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in rejected:
                            line.sendMessage(to, 'ทำการยกเลิกค้างเชิญ %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendMessage(to, 'ทำการยกเลิกค้างเชิญ %s' % group.name)
                    else:
                        line.sendMessage(to, 'ไม่สามายกเลิกค้างเชิญหมายเลข %iนี้ได้เนื่องจากเลขเกิน!' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in rejected:
                            line.sendMessage(to, 'ทำการยกเลิกค้างเชิญ %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendMessage(to, 'ทำการยกเลิกค้างเชิญ %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in rejected:
                                continue
                            line.rejectGroupInvitation(gid)
                            rejected.append(gid)
                            time.sleep(0.8)
                        line.sendMessage(to, 'ยกเลิกคำเชิญเข้าร่วมกลุ่มทั้งหมดแล้ว ♪')
                    else:
                        line.sendMessage(to, 'ไม่สามารถยกเลิกคำเชิญเข้าร่วมกลุ่มชื่อ`%s`นี้ได้เนื่องจากไม่พบชื่อกลุ่มนี้ ♪' % name)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'memberlist':
        if msg.toType == 1:
            room = line.getRoom(to)
            members = room.contacts
        elif msg.toType == 2:
            group = line.getGroup(to)
            members = group.members
        else:
            return line.sendMessage(to, 'ไม่สามารถแสดงจำนวนสมาชิกในกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        if not members:
            return line.sendMessage(to, 'ไม่สามารถแสดงจำนวนสมาชิกในกลุ่มได้\nไม่มีสมาชิกในกลุ่ม')
        res = '╭───「 Member List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───「 AOY 」'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendMessage(to, res)
            res = ''
    elif cmd == 'pendinglist':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถแสดงจำนวนค้างเชิญในกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getGroup(to)
        members = group.invitee
        if not members:
            return line.sendMessage(to, 'ไม่สามารถแสดงจำนวนค้างเชิญในกลุ่มได้\nไม่พบค้างเชิญ')
        res = '╭───「 Pending List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───「 AOY 」'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendMessage(to, res)
            res = ''
    elif cmd == 'openqr':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเปิดลิ้งกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = False
        line.updateGroup(group)
        line.sendMessage(to, 'เปิดลิ้งกลุ่มแล้ว')
    elif cmd == 'closeqr':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเปิดลิ้งกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = True
        line.updateGroup(group)
        line.sendMessage(to, 'ปิดลิ้งกลุ่มแล้ว')
    elif cmd.startswith('changegroupname '):
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเปลี่ยนชื่อกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getCompactGroup(to)
        gname = removeCmd(text, setKey)
        if len(gname) > 50:
            return line.sendMessage(to, 'ไม่สามารถเปลี่ยนชื่อกลุ่มได้\nชื่อกลุ่มต้องไม่เกิน 50')
        group.name = gname
        line.updateGroup(group)
        line.sendMessage(to, 'เปลี่ยนชื่อกลุ่มเป็น `%s`' % gname)
    elif cmd == 'changegrouppict':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเปลี่ยนรุปกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        if to not in settings['changeGroupPicture']:
            settings['changeGroupPicture'].append(to)
            line.sendMessage(to, 'กรุณาส่งภาพ, พิม `{key}Abort` ถ้าต้องการยกเลิก\nคำเตือน:การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพนานเกินไป'.format(key=setKey.title()))
        else:
            line.sendMessage(to, 'คำสั่งนี้ถูกงานอยู่แล้ว, กรุณาส่งภาพ หรือ พิม `{key}Abort` ถ้าต้องการยกเลิก\nคำเตือน:การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพนานเกินไป'.format(key=setKey.title()))
    elif cmd == 'kickall':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getCompactGroup(to)
        if not group.members:
            return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้\nไม่มีคนไห้เตะ')
        for member in group.members:
            if member.mid == myMid:
                continue
            try:
                line.kickoutFromGroup(to, [member.mid])
            except TalkException as talk_error:
                return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้เนื่องจาก `%s`' % talk_error.reason)
            time.sleep(0.8)
        line.sendMessage(to, 'เตะสมาชิกทั้งหมด, จำนวน %i คน' % len(group.members))
    elif cmd == 'cancelall':
        if msg.toType != 2: return line.sendMessage(to, 'ไม่สามารถยกเลิกค้างเชิญได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        group = line.getCompactGroup(to)
        if not group.invitee:
            return line.sendMessage(to, 'ไม่สามารถยกเลิกค้างเชิญได้\nไม่มีสมาชิกค้างเชิญ')
        for member in group.invitee:
            if member.mid == myMid:
                continue
            try:
                line.cancelGroupInvitation(to, [member.mid])
            except TalkException as talk_error:
                return line.sendMessage(to, 'ไม่สามารถยกเลิกค้างเชิญได้เนื่องจาก `%s`' % talk_error.reason)
            time.sleep(0.8)
        line.sendMessage(to, 'ยกเลิกค้างเชิญทั้งหมดแล้ว\nจำนวน %i คน' % len(group.invitee))
    elif cmd.startswith('lurk'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if msg.toType in [1, 2] and to not in lurking:
            lurking[to] = {
                'status': False,
                'time': None,
                'members': [],
                'reply': {
                    'status': False,
                    'message': settings['defaultReplyReader']
                }
            }
        res = '╭───「 Lurking 」'
        if msg.toType in [1, 2]: res += '\n├ Status : ' + bool_dict[lurking[to]['status']][1]
        if msg.toType in [1, 2]: res += '\n├ Reply Reader : ' + bool_dict[lurking[to]['reply']['status']][1]
        if msg.toType in [1, 2]: res += '\n├ Reply Reader Message : ' + lurking[to]['reply']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}Lurk'
        res += '\n│ • {key}Lurk <on/off>'
        res += '\n│ • {key}Lurk Result'
        res += '\n│ • {key}Lurk Reset'
        res += '\n│ • {key}Lurk ReplyReader <on/off>'
        res += '\n│ • {key}Lurk ReplyReader <message>'
        res += '\n╰───「 AOY」'
        if cmd == 'lurk':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif msg.toType not in [1, 2]:
            return line.sendMessage(to, 'ไม่สามารถใช้คำสั่งนี้ได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
        elif texttl == 'on':
            if lurking[to]['status']:
                line.sendMessage(to, 'เปิดโหมดตรวจจับคนอ่าน')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMessage(to, 'เปิดแล้ว')
        elif texttl == 'off':
            if not lurking[to]['status']:
                line.sendMessage(to, 'ปิดโหมดตรวจจับคนอ่าน')
            else:
                lurking[to].update({
                    'status': False,
                    'time': None,
                    'members': []
                })
                line.sendMessage(to, 'ปิดแล้ว')
        elif texttl == 'result':
            if not lurking[to]['status']:
                line.sendMessage(to, 'รีเช็ตคนอ่านเรียบร้อย')
            else:
                if not lurking[to]['members']:
                    line.sendMessage(to, 'ไม่สามารถรีเช็ตคนอ่านได้\nเนื่องจากไม่พบคนอ่าน')
                else:
                    members = lurking[to]['members']
                    res = '╭───「 Lurking 」'
                    if msg.toType == 2: res += '\n├ Group Name : ' + line.getGroup(to).name
                    parsed_len = len(members)//200+1
                    no = 0
                    for point in range(parsed_len):
                        for member in members[point*200:(point+1)*200]:
                            no += 1
                            try:
                                name = line.getContact(member).displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            if member == members[-1]:
                                res += '\n│'
                                res += '\n├ Time Set : ' + lurking[to]['time']
                                res += '\n╰───「 AOY 」'
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendMessage(to, res)
                        res = ''
        elif texttl == 'reset':
            if not lurking[to]['status']:
                line.sendMessage(to, 'ไม่สามารถรีเช็ตคนอ่านได้\nยังไม่ได้เปิดโหมดตรวจจับคนอ่าน')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMessage(to, 'รีเช็ตเรียบร้อย')
        elif texttl.startswith('replyreader '):
            texts = textt[12:]
            if texts == 'on':
                if lurking[to]['reply']['status']:
                    line.sendMessage(to, 'ข้อความทักคนอ่านเปิดใช้งานอยู่แล้ว')
                else:
                    lurking[to]['reply']['status'] = True
                    line.sendMessage(to, 'เปิดข้อความทักคนอ่าน')
            elif texts == 'off':
                if not lurking[to]['reply']['status']:
                    line.sendMessage(to, 'ข้อความทักคนอ่านถุกปิดใช้งานอยู่แล้ว')
                else:
                    lurking[to]['reply']['status'] = False
                    line.sendMessage(to, 'ปิดข้อความทักคนอ่าน')
            else:
                lurking[to]['reply']['message'] = texts
                line.sendMessage(to, 'เปลี่ยนข้อความทักคนอ่านเป็น `%s`' % texts)
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('greet'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Greet Message 」'
        res += '\n├ Greetings Join Status : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ Greetings Join Message : ' + settings['greet']['join']['message']
        res += '\n├ Greetings Leave Status : ' + bool_dict[settings['greet']['leave']['status']][0]
        res += '\n├ Greetings Join Message : ' + settings['greet']['leave']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}Greet'
        res += '\n│ • {key}Greet Join <on/off>'
        res += '\n│ • {key}Greet Join <message>'
        res += '\n│ • {key}Greet Leave <on/off>'
        res += '\n│ • {key}Greet Leave <message>'
        res += '\n╰───「 AOY 」'
        if cmd == 'greet':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('join '):
            texts = textt[5:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['join']['status']:
                    line.sendMessage(to, 'ข้อความทักคนเข้ากลุ่มถูกเปิดใช้งานอยู่แล้ว')
                else:
                    settings['greet']['join']['status'] = True
                    line.sendMessage(to, 'เปิดข้อความทักคนเข้ากลุ่ม')
            elif textsl == 'off':
                if not settings['greet']['join']['status']:
                    line.sendMessage(to, 'ข้อความทักคนเข้ากลุ่มถูกปิดใช้งานอยู่แล้ว')
                else:
                    settings['greet']['join']['status'] = False
                    line.sendMessage(to, 'ปิดข้อความทักคนเข้ากลุ่ม')
            else:
                settings['greet']['join']['message'] = texts
                line.sendMessage(to, 'เปลี่ยนข้อความทักคนเข้ากลุ่มเป็น `%s`' % texts)
        elif texttl.startswith('leave '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['leave']['status']:
                    line.sendMessage(to, 'ข้อความทักคนออกกลุ่มถุกเปิดใช้งานอยู่แล้ว')
                else:
                    settings['greet']['leave']['status'] = True
                    line.sendMessage(to, 'เปิดข้อความทักคนออกกลุ่ม')
            elif textsl == 'off':
                if not settings['greet']['leave']['status']:
                    line.sendMessage(to, 'ข้อความทักคนออกกลุ่มถูกปิดใช้งานอยู่แล้ว')
                else:
                    settings['greet']['leave']['status'] = False
                    line.sendMessage(to, 'ปิดข้อความทักคนออกกลุ่ม')
            else:
                settings['greet']['leave']['message'] = texts
                line.sendMessage(to, 'เปลี่ยนข้อความทักคนออกกลุ่มเป็น `%s`' % texts)
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('kick '):
        if msg.toType != 2: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                except TalkException as talk_error:
                    return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกได้\nเนื่องจาก `%s`' % talk_error.reason)
                time.sleep(0.8)
            line.sendMessage(to, 'เตะสมาชิกเรียบร้อย\nจำนวน %i คน' % len(mentions['MENTIONEES']))
        else:
            line.sendMessage(to, 'ไม่สามารถเตะสมาชิกได้\nกรุณาแท็กคนที่จะเตะ')
    elif cmd.startswith('vkick '):
        if msg.toType != 2: return line.sendMessage(to, 'คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                except TalkException as talk_error:
                    return line.sendMessage(to, 'ไม่สามารถเตะสมาชิกได้\nเนื่องจาก `%s`' % talk_error.reason)
                time.sleep(0.8)
            line.sendMessage(to, 'เตะสมาชิกเรียบร้อย\nจำนวน %i คน' % len(mentions['MENTIONEES']))
        else:
            line.sendMessage(to, 'ไม่สามารถเตะสมาชิกได้\nกรุณาแท็กคนที่จะเตะ')

def executeOp(op):
    try:
        print ('[* %i ] %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings['autoAdd']['status']:
                line.findAndAddContactsByMid(op.param1)
            if settings['autoAdd']['reply']:
                if '@!' not in settings['autoAdd']['message']:
                    line.sendMessage(op.param1, settings['autoAdd']['message'])
                else:
                    line.sendMentionV2(op.param1, settings['autoAdd']['message'], [op.param1])
        if op.type == 13:
            if settings['autoJoin']['status'] and myMid in op.param3:
                line.acceptGroupInvitation(op.param1)
                if settings['autoJoin']['reply']:
                    if '@!' not in settings['autoJoin']['message']:
                        line.sendMessage(op.param1, settings['autoJoin']['message'])
                    else:
                        line.sendMentionV2(op.param1, settings['autoJoin']['message'], [op.param2])
        if op.type == 15:
            if settings['greet']['leave']['status']:
                if '@!' not in settings['greet']['leave']['message']:
                    line.sendMessage(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 17:
            if settings['greet']['join']['status']:
                if '@!' not in settings['greet']['join']['message']:
                    line.sendMessage(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 11:		
            if op.param1 in protectqr:
                try:
                    if line.getCompactGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            random.choice(ABC).reissueGroupTicket(op.param1)
                            X = line.getCompactGroup(op.param1)
                            X.preventedJoinByTicket = True
                            wait["blacklist"][op.param2] = True                            
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])                            
                            random.choice(ABC).updateGroup(X)
                            random.choice(ABC).sendMessage(op.param1,"Do not open group url. (｀・ω・´)")					
                except:
                    pass
        if op.type == 13:
            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                pass
            if op.param1 in protectinvite:
                wait["blacklist"][op.param2] = True
                random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param3])
                G = random.choice(ABC).getCompactGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(ABC).updateGroup(G)

        if op.type == 32:
            if op.param1 in protectcanceljs:
                if op.param3 in Bots:    
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                line.inviteIntoGroup(op.param1,[g1MID])		
                                G.preventedJoinByTicket = True
                                random.choice(ABC).updateGroup(G)
                        except:
                            pass
                    return
        if op.type == 32:
            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                pass
            if op.param1 in protectcancel:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                kicker.findAndAddContactsByMid(op.param3)
                kicker.inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True

        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    G = line.getCompactGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    random.choice(ABC).updateGroup(G)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    G = line.getCompactGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    random.choice(ABC).updateGroup(G)			
        if op.type == 17:
            if op.param1 in protecARoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return
#================================================================================
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass            
        if op.type == 19:
            if op.param1 in ghost:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    G = line.getCompactGroup(op.param1)
                    time.sleep(0.008)
                    G.preventedJoinByTicket = False                     
                    random.choice(ABC).updateGroup(G)
                    invsend = 0
                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)                    
                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)     
                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)      
                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)      
                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)      
                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                    g1.acceptGroupInvitationByTicket(op.param1,Ticket)                    
                    g1.kickoutFromGroup(op.param1,[op.param2])                                    
                X = line.getCompactGroup(op.param1)
                time.sleep(0.008)
                X.preventedJoinByTicket = True
                random.choice(ABC).updateGroup(X)
        if op.type == 19:
            if op.param1 in protectantijs:
                if myMid in op.param3:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        try:
                            g1.acceptGroupInvitation(op.param1)         
                            g1.inviteIntoGroup(op.param1,[myMid])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            line.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                            g1.leaveGroup(op.param1)
                            line.inviteIntoGroup(op.param1,[g1MID])
                        except:
                            pass
#-------------------------------------------------------------------------------      
        if op.type == 19:
            if myMid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008)                        
                        kicker.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker2.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008)                            
                            kicker2.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker3.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008)                                
                                kicker3.inviteIntoGroup(op.param1,[op.param3])
                                line.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker.kickoutFromGroup(op.param1,[op.param2])
                                    kicker.updateGroup(G)
                                    Ticket = kicker.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kicker.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker.updateGroup(G)
                                    Ticket = kicker.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker4.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008)                                        
                                        kicker4.inviteIntoGroup(op.param1,[op.param3])
                                        line.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                                            time.sleep(0.008)                                            
                                            kicker5.inviteIntoGroup(op.param1,[op.param3])
                                            line.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker2.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008)                        
                        kicker2.inviteIntoGroup(op.param1,[op.param3])
                        kicker.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008)                            
                            kicker3.inviteIntoGroup(op.param1,[op.param3])
                            kicker.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker4.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008)                                
                                kicker4.inviteIntoGroup(op.param1,[op.param3])
                                kicker.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker2.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker2.kickoutFromGroup(op.param1,[op.param2])
                                    kicker2.updateGroup(G)
                                    Ticket = kicker2.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kicker2.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker2.updateGroup(G)
                                    Ticket = kicker2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008)                                        
                                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                                        kicker.acceptGroupInvitation(op.param1)
                                    except:
                                        try:                                      
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            kicker.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker3.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008)                        
                        kicker3.inviteIntoGroup(op.param1,[op.param3])
                        kicker2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker4.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008)                            
                            kicker4.inviteIntoGroup(op.param1,[op.param3])
                            kicker2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008)                                
                                kicker.inviteIntoGroup(op.param1,[op.param3])
                                kicker2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker3.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker3.kickoutFromGroup(op.param1,[op.param2])
                                    kicker3.updateGroup(G)
                                    Ticket = kicker3.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kicker3.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker3.updateGroup(G)
                                    Ticket = kicker3.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008)                                        
                                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                                        kicker2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:                                
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            kicker2.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker4.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008)                        
                        kicker4.inviteIntoGroup(op.param1,[op.param3])
                        kicker3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker5.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008)                            
                            kicker5.inviteIntoGroup(op.param1,[op.param3])
                            kicker3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008)                                
                                kicker.inviteIntoGroup(op.param1,[op.param3])
                                kicker3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker4.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker4.kickoutFromGroup(op.param1,[op.param2])
                                    kicker4.updateGroup(G)
                                    Ticket = kicker4.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kicker4.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker4.updateGroup(G)
                                    Ticket = kicker4.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker2.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008)                                        
                                        kicker2.inviteIntoGroup(op.param1,[op.param3])
                                        kicker3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:                                         
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            kicker3.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker5.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008)                        
                        kicker5.inviteIntoGroup(op.param1,[op.param3])
                        kicker4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008)                            
                            kicker3.inviteIntoGroup(op.param1,[op.param3])
                            kicker4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008)                                
                                kicker.inviteIntoGroup(op.param1,[op.param3])
                                kicker4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker5.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker5.kickoutFromGroup(op.param1,[op.param2])
                                    kicker5.updateGroup(G)
                                    Ticket = kicker5.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kicker5.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker5.updateGroup(G)
                                    Ticket = kicker5.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker2.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008)                                        
                                        kicker2.inviteIntoGroup(op.param1,[op.param3])
                                        kicker4.acceptGroupInvitation(op.param1)
                                    except:
                                        try:                                         
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            kicker4.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        time.sleep(0.008)                        
                        kicker2.inviteIntoGroup(op.param1,[op.param3])
                        kicker5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kicker3.kickoutFromGroup(op.param1,[op.param2])
                            time.sleep(0.008)                            
                            kicker.inviteIntoGroup(op.param1,[op.param3])
                            kicker5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kicker4.kickoutFromGroup(op.param1,[op.param2])
                                time.sleep(0.008)                                
                                kicker3.inviteIntoGroup(op.param1,[op.param3])
                                kicker5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kicker2.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kicker4.kickoutFromGroup(op.param1,[op.param2])
                                    kicker2.updateGroup(G)
                                    Ticket = kicker2.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kicker5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kicker2.getCompactGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kicker2.updateGroup(G)
                                    Ticket = kicker2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kicker4.kickoutFromGroup(op.param1,[op.param2])
                                        time.sleep(0.008)                                        
                                        kicker.inviteIntoGroup(op.param1,[op.param3])
                                        kicker5.acceptGroupInvitation(op.param1)
                                    except:
                                        try:                 
                                            kicker3.inviteIntoGroup(op.param1,[op.param3])
                                            kicker5.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:            	
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    G = line.getCompactGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    random.choice(ABC).updateGroup(G)                            		
        if op.type == 25:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            cmd      = command(text)
            setKey   = settings['setKey']['key'] if settings['setKey']['status'] else ''
            if text in tmp_text:
                return tmp_text.remove(text)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendMessage(to, 'เข้าร่วมกลุ่ม' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendMessage(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendMessage(to, 'เข้าร่วมกลุ่ม' + group.name)
                try:
                    executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    line.sendMessage(to, 'เกิดข้อผิดพลาด\n' + str(talk_error))
                    time.sleep(3)
                except Exception as error:
                    logError(error)
                    line.sendMessage(to, 'เกิดข้อผิดพลาด\n' + str(error))
                    time.sleep(3)
            elif msg.contentType == 1: # Content type is image
                if settings['changePictureProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                    line.updateProfilePicture(path)
                    line.sendMessage(to, 'เปลี่ยนรูปโปรไฟล์เรียบร้อย')
                    settings['changePictureProfile'] = False
                elif settings['changeCoverProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                    line.updateProfileCover(path)
                    line.sendMessage(to, 'เปลี่ยนรูปปกเรียบร้อย')
                    settings['changeCoverProfile'] = False
                elif to in settings['changeGroupPicture'] and msg.toType == 2:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                    line.updateGroupPicture(to, path)
                    line.sendMessage(to, 'เปลี่ยนรูปกลุ่มแล้ว')
                    settings['changeGroupPicture'].remove(to)
            elif msg.contentType == 7: # Content type is sticker
                if settings['checkSticker']:
                    res = '╭───「 Sticker Info 」'
                    res += '\n├ Sticker ID : ' + msg.contentMetadata['STKID']
                    res += '\n├ Sticker Packages ID : ' + msg.contentMetadata['STKPKGID']
                    res += '\n├ Sticker Version : ' + msg.contentMetadata['STKVER']
                    res += '\n├ Sticker Link : line://shop/detail/' + msg.contentMetadata['STKPKGID']
                    res += '\n╰───「 AOY 」'
                    line.sendMessage(to, parsingRes(res))
            elif msg.contentType == 13: # Content type is contact
                if settings['checkContact']:
                    mid = msg.contentMetadata['mid']
                    try:
                        contact = line.getContact(mid)
                    except:
                        return line.sendMessage(to, 'เกิดข้ผิดพลาดเฉียบพลัน ' + mid)
                    res = '╭───「 Details Contact 」'
                    res += '\n├ MID : ' + mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 AOY 」'
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(mid)
                    line.sendImageWithURL(to, str(cover))
                    line.sendMessage(to, parsingRes(res))
            elif msg.contentType == 16: # Content type is album/note
                if settings['checkPost']:
                    if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                        if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                            contact = line.getContact(sender)
                            author = contact.displayName
                        else:
                            author = msg.contentMetadata['serviceName']
                        posturl = msg.contentMetadata['postEndUrl']
                        res = '╭───「 Details Post 」'
                        res += '\n├ Creator : ' + author
                        res += '\n├ Post Link : ' + posturl
                        res += '\n╰───「 AOY 」'
        elif op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            if settings['autoRead']:
                line.sendChatChecked(to, msg_id)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendMessage(to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendMessage(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendMessage(to, 'Success join to group ' + group.name)
                if settings['mimic']['status']:
                    if sender in settings['mimic']['target'] and settings['mimic']['target'][sender]:
                        try:
                            line.sendMessage(to, text, msg.contentMetadata)
                            tmp_text.append(text)
                        except:
                            pass
                if settings['autoRespondMention']['status']:
                    if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9]:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                        if myMid in mentionees:
                            if line.getProfile().displayName in text:
                                if '@!' not in settings['autoRespondMention']['message']:
                                    line.sendMessage(to, settings['autoRespondMention']['message'])
                                else:
                                    line.sendMentionV2(to, settings['autoRespondMention']['message'], [sender])
                if settings['autoRespond']['status']:
                    if msg.toType == 0:
                        contact = line.getContact(sender)
                        if contact.attributes != 32 and 'MENTION' not in msg.contentMetadata.keys():
                            if '@!' not in settings['autoRespond']['message']:
                                line.sendMessage(to, settings['autoRespond']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoRespond']['message'], [sender])
        if op.type == 55:
            if op.param1 in lurking:
                if lurking[op.param1]['status'] and op.param2 not in lurking[op.param1]['members']:
                    lurking[op.param1]['members'].append(op.param2)
                    if lurking[op.param1]['reply']['status']:
                        if '@!' not in lurking[op.param1]['reply']['message']:
                            line.sendMessage(op.param1, lurking[op.param1]['reply']['message'])
                        else:
                            line.sendMentionV2(op.param1, lurking[op.param1]['reply']['message'], [op.param2])
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)

def runningProgram():
    if settings['restartPoint'] is not None:
        try:
            line.sendMessage(settings['restartPoint'], 'รีสตาร์ทเรียบร้อย ♪')
        except TalkException:
            pass
        settings['restartPoint'] = None
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('##---- KEYBOARD INTERRUPT -----##')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                executeOp(op)
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print ('##---- RUNNING PROGRAM -----##')
    runningProgram()
