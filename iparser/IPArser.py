# import argparse
# parser = argparse.ArgumentParser(description='Add some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='interger list')
# parser.add_argument('--sum', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
# args = parser.parse_args()
# print(args.sum(args.integers))

import zipfile
import plistlib
import mobileprovision
import json
import os
import shutil

class IPArser(object):

    @staticmethod
    def parse(path, output, no_output):
        with zipfile.ZipFile(path) as myzip:
            files = myzip.infolist()
            data = {}
            for index in range(len(files)):
                if(files[index].filename.find("Info.plist") != -1):
                    dict = plistlib.loads(myzip.read(files[index].filename))
                    if("CFBundleDisplayName" in dict):
                        data.update(dict)
                if(files[index].filename.find(".mobileprovision") != -1):
                    myzip.extract(files[index], path="tmp")
                    provision = mobileprovision.MobileProvisionModel(os.getcwd()+"/tmp/"+files[index].filename)
                    data["created_at"] = provision.creation_timestamp
                    data["expire_at"] = provision.expiration_timestamp
                    certs = []
                    cert = {}
                    for index in range(len(provision.developer_certificates)):
                        cert["common_name"] = provision.developer_certificates[index].common_name
                        certs.append(cert)
                    data["certificates"] = certs
                    shutil.rmtree("tmp")
            if(no_output != True):
                if(output != None):
                    f = open(os.path.join(os.path.join(os.getcwd(), output), "info.json"), 'w+')
                else:
                    f = open(os.path.join(os.getcwd(), "info.json"), 'w+')
                f.write(json.dumps(data, indent=True))
                f.close()
            print(data)

    @staticmethod
    def extractIcon(path, output):
        with zipfile.ZipFile(path) as myzip:
            files = myzip.infolist()
            iconFiles = []
            for index in range(len(files)):
                if (files[index].filename.find("Info.plist") != -1):
                    dict = plistlib.loads(myzip.read(files[index].filename))
                    if ("CFBundleIcons" in dict):
                        subdict = dict["CFBundleIcons"]
                        if ("CFBundlePrimaryIcon" in subdict):
                            subsubdict = subdict["CFBundlePrimaryIcon"]
                            if ("CFBundleIconFiles" in subsubdict):
                                icons = subsubdict["CFBundleIconFiles"]
                                for icn in icons:
                                    if (icn not in iconFiles):
                                        iconFiles.append(icn)
                    if ("CFBundleIcons~ipad" in dict):
                        subdict = dict["CFBundleIcons~ipad"]
                        if ("CFBundlePrimaryIcon" in subdict):
                            subsubdict = subdict["CFBundlePrimaryIcon"]
                            if ("CFBundleIconFiles" in subsubdict):
                                icons = subsubdict["CFBundleIconFiles"]
                                for icn in icons:
                                    if (icn not in iconFiles):
                                        iconFiles.append(icn)
            print(iconFiles)
            # icon_path = ipa.findFile(icn)
            # print
            # icon_path
            # ipa.saveFileTo(icon_path, "%s-%s" % (arguments['IPA'].split('/')[-1].split('.')[0], icn))