#ZXhhbXBsZWJhc2U2NHRvc3RyaW5nCg==
#commonı ımport et
#test fonksıyonlarını calıstır (buraya def ıle yaz)
#sonra gel
from common import Common

def testDecodeString(base64_string):
    common = Common()
    decoded_string = common.from_base64(base64_string)
    return decoded_string

if __name__ == "__main__":
    # Decode the base64 string
    from_base64 = "ewogInV1aWQiOiAiMTQ4MTQwNjIiLAogImluZm8iOiB7CiAgIm5hbWUiOiAiMDMxMTU4MDc3MjA0MTYzMDgyIiwKICAiZ3JvdXAiOiAiZ3JvdXAxIiwKICAibG9jYXRpb24iOiAibWljYWUtTlZSIiwKICAiZ2F0ZXdheSI6ICJtaWNhZS1OVlIiCiB9LAogInN0cmVhbVNldHRpbmdzIjogewogICJzdGF0aWNVcmwiOiB7CiAgICJ1cmwiOiBbCiAgICAicnRzcDovLzEwLjUuNS4yOjU1NC9IMjY0P2NoPTEmc3VidHlwZT0wJnByb3RvPU9udmlmIiwKICAgICJydHNwOi8vMTAuNS41LjI6NTU0L0gyNjQ/Y2g9MSZzdWJ0eXBlPTEmcHJvdG89T252aWYiCiAgIF0KICB9LAogICJzdHJlYW1zIjogWwogICB7CiAgICAibmFtZSI6ICJzdHJlYW0xIiwKICAgICJzdHJlYW1JRCI6ICIxNDgxNDA2Mi1zdHJlYW0xIiwKICAgICJ1cmwiOiAicnRzcDovLzEwLjUuNS4yOjU1NC9IMjY0P2NoPTEmc3VidHlwZT0wJnByb3RvPU9udmlmIgogICB9LAogICB7CiAgICAibmFtZSI6ICJzdHJlYW0yIiwKICAgICJzdHJlYW1JRCI6ICIxNDgxNDA2Mi1zdHJlYW0yIiwKICAgICJ1cmwiOiAicnRzcDovLzEwLjUuNS4yOjU1NC9IMjY0P2NoPTEmc3VidHlwZT0xJnByb3RvPU9udmlmIgogICB9CiAgXQogfQp9Cg=="
    decoded_string = testDecodeString(from_base64)
    print("Decoded string:", decoded_string)

    # Encode the sentence to base64
    to_base64 = "examplestring"
    encoded_string = Common().to_base64(to_base64)
    print("Encoded string:", encoded_string)
    print("Re-decoded string: " + Common().from_base64(encoded_string))

