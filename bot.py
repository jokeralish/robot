from linepy import *
import time

cl = LINE("EzRs9fmhRq64GaifW9ba.iWUy5hFsviofrvd8vX8GwG.sqmGzv357rewfD59KyV4LuFBZuII+EFhY++3QxQpk6g=")
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))
poll = OEPoll(cl)

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops != None:
            for op in ops:
                if (op.type == 13):
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,'By Alish joker add  to line.me/ti/p/~infoalish')
                    cl.sendMessage(op.param1,'cancelling~')
                if (op.type == 25):
                    msg = op.message
                    if (msg.text.lower() == 'start!'):
                        s = time.time()
                        cl.sendMessage('Speed!')
                        e = time.time() - s
                        cl.sendMessage('{:.14f}'.format(e))
                    if ('cancelling~' in msg.text.lower()):
                        g = cl.getCompactGroup(msg.to)
                        mids = [i.mid for i in g.invitee]
                        for mid in mids:
                            try:
                                cl.cancelGroupInvitation(msg.to,[mid])
                            except Exception as e:
                                pass
         #               cl.sendMessage(msg.to,'id bot!\nline://ti/p/~a.cancelbot\n admin line.me/ti/p/~alish-joker\n\n\n channel @linethemes\n\n\n @alihack011\n\n\n ᴘᴇʀsɪᴀɴ ᴛᴇᴀᴍ ᴠʜᴅ.ᴠ \n\n ᴀ.ᴊ')
                        cl.leaveGroup(msg.to)
                poll.setRevision(op.revision)
    except Exception as e:
        cl.log("[SINGLE_TRACE] ERROR : " + str(e))
