import os
import logging
import hashlib
import requests
from dotenv import load_dotenv
load_dotenv()

directory=os.getcwd()

def __calc_sha256(filename):
    """
    this function use to get sha value of filename"""
    sha256_hash=hashlib.sha256()
    with open(filename,"rb") as file_read:
        #read and update hash string value in blocks of 4k
        for byte_block in iter(lambda: file_read.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def __calc_sha1(filename):
    """
    this function is used to get sha1 hash value from file"""
    sha1_hash=hashlib.sha1()
    with open(filename,"rb") as file_read:
        #read and update hash string value in blocks of 4k
        for byte_block in iter(lambda: file_read.read(4096),b""):
            sha1_hash.update(byte_block)
    return sha1_hash.hexdigest() 

def __calc_md5(filename):
    """
    this function is used to get md5 hash of a file"""
    md5_hash=hashlib.md5()
    with open(filename,"rb") as file_read:
        #read and update hash string value in blocks of 4k
        for byte_block in iter(lambda: file_read.read(4096),b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()

def deploy_file(artifactory_url,artifactory_repository,filename,subfolder=""):
    """
    this function is to deploy a file to artifactory
    returns the response status code of the deployment"""
    file=os.path.abspath(filename)
    base_file_name=os.path.basename(file)
    headers={
        'Authentication': os.getenv('ARTIFACTORY_TOKEN'),
        'X-Checksum-Sha256': __calc_sha256(file),
        'X-Checksum-Sha1': __calc_sha1(file),
        'X-Checksum-MD5': __calc_md5(file),        
    }
    url=artifactory_url
    repo=artifactory_repository
    folder=""+subfolder if subfolder != "" else ""
    file=base_file_name
    response=requests.put(f'{url}{repo}{folder}/{file}',
                          data=open(file,'rb'),
                          auth=(os.getenv("artifactory_username"),
                                os.getenv("artifactory_password")),
                          headers=headers,
                          verify=False,timeout=None)
    
    if response.status_code == 201:
        logging.info("file uploaded successfully to artifactory")
    else:
        logging.error("file not uploaded successfully to artifactory, check permissions")
    return response.status_code


def get_sha256_of_file(artifactory_url,artifactory_repository,filename,subfolder=""):
    """this function is used to get the sha256 and return value from artifactory"""
    headers={
        'Authentication':os.getenv('ARTIFACTORY_TOKEN')
    }
    url=artifactory_url
    repo=artifactory_repository
    folder=""+subfolder if subfolder != '' else ''
    file=filename
    try:
        response=requests.get(f"{url}{repo}{folder}/{file}",
                              auth=(os.getenv("artifactory_username"),
                                    os.getenv("artifactory_password")),
                              headers=headers,
                              verify=False,timeout=None)

        if response.status_code == 200:
            logging.info(filename)
            logging.info(retval)
            data = response.headers
            retval =data["X-Checksum-Sha256"]
        else:
            retval=None
        return retval
    except:
        logging.error("no sha value available",exc_info=True)
        return None
    
def delete_files():
    "this function deletes the files after uploading to server"
    files = [f for f in os.listdir('./') if os.path.isfile(f)] 
    
    for file_name in files:
        if file_name.endswith(('.zip', '.gz')):
            os.remove(file_name) 
                               