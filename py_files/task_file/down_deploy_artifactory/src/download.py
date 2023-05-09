import os
import logging
from string import Template
import re
import requests
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

AXIVION_URL = "http://downloads.axivion.com"

platform=['Windows', 'Linux', 'Qualification_Kit']
prefixes=['bauhaus-suite','bauhaus-suite','qualification_kit']
postfixes=['','-x86_64-gnu_linux','']
package_endings=['zip', 'tar.gz', 'zip']


link_template = Template(
    "https://github.com/$PLATFORM/$VERSION"
)

sha_template = Template(
    "https://github.com/$PLATFORM/$VERSION1/sha26sum.txt"
)

class AxivionPackage:
    """this class get the filename,data,sha256 and file links"""
    def __init__(self,name):
        self.name = name
        self.data={}
        
    def add_data(self,platform,link,sha):
        """this function is use to fetch the data of file"""
        self.data.setdefault(platform,{})
        self.__add_link(platform,link)
        self.__add_filename(platform,os.path.basename(link))
        self.__add_sha(platform,sha)
        
    def __add_filename(self,platform,filename):
        """this function os to get the filename"""
        self.data[platform]['filename'] = filename
        
    def __add_link(self,platform,link):
        """this function os to get the link of file"""
        self.data[platform]['link'] = link
        
        
    def __add_sha(self,platform,sha):
        """this function os to get the sha of file"""
        self.data[platform]['sha'] = sha
        
def __get_website_content(url,stream=False):
    """this function is used to call the url"""
    return request.get(url,
                       auth=HTTPDigestAuth(
                           os.getenv("AXIVION_USER"),os.getenv("AXIVION_PASSWORD")),
                        verify=False,
                        stream=stream,timeout=None
                       )
    
def __get_sha(file_content):
    """this function is used to get SHA key values"""
    sha_list={}
    sha_list_tmp=file_content.decode("UTF-8").splitlines()
    for item in sha_list_tmp:
        tmp=item.split(" *")
        sha_list.setdefault(tmp[1],tmp[0])
    return sha_list


def get_links_to_package():
    """this function is used to get version of file"""
    version_dict={}
    for (platform,ending,postfix,prefix) in zip(platform,ending,postfixes,prefixes):
        #connect to the download protal and parse the HTML content
        page=__get_website_content(AXIVION_URL+'/'+str(platform))
        portal_content=BeautifulSoup(page.content,"html.parser")
        #within all links...
        for link in portal_content.find_all('a'):
            #we need href text from the link to read version only
            version=re.findall(
                r'([\d]+[\.][\d]+[\.][\d+)',link.getText())
            if version:
                # add download link to version dictionary
                version_link=link_template.substitute(PLATFORM=platform,
                                                      VERSION=version[0])
                
                #substitute th esha link template,fetch data and tranform them to dict file 
                sha = __get_sha(__get_website_content(sha_template.substitute(
                    PLATFORM=platform, VERSION1=version[0],)).content)
                version_content = BeautifulSoup(
                    __get_website_content(version_link).content,"html.parser")
                
                for archive_link in version_content.find_all('a'):
                    archive=re.findall(
                        rf'({prefix}-[\d]+[_][\d]+{postfix}[a-z0-9-]*.{ending})',
                        archive_link.getText()
                    )
                    
                    if archive:
                        package= AxivionPackage(version[0])
                        ## add data to version if existing in the dict , create if not existing
                        version_dict.setdefault(
                            package.name,package).add_data(platform
                                                           (version_link+archive[0]),sha)
    return version_dict

def download_file(url):
    """to download file from artifactory"""
    local_filename=url.split('/')[-1]
    with __get_website_content(url=url,stream=True) as read_file:
        read_file.raise_for_status()
        with open(local_filename,'wb') as down_file:
            for chunk in read_file.iter_content(chunk_size=8192):
                down_file.write(chunk)
            down_file.close()
        read_file.close()
    logging.info(local_filename)
    return local_filename