"""
this is main funct for executing the task"""
import os
import logging
from dotenv import load_dotenv
from getartifactorydelivery import gateway
from getartifactorydelivery import download
load_dotenv()
artifactory_url=os.getenv('ARTIFACTORY_URL')
artifactory_repository=os.getenv('ARTIFACTORY_REPO')

def check_file_exists(version,filename,sha256):
    """Check if the file exists in artifact"""
    if sha256 == gateway.get_sha256_of_file(artifactory_url,artifactory_repository,filename,
                                            version):
        return True
    return False

def main():
    """ this funct is to dwonlaod the and deploying files"""
    logging.basicConfig(filename="log_file.log".level=logging.INFO,
                        format="%(asctime)s %(levelname)-8s",filemode='w')
    axivion_package=download.get_links_to_packages()
    for version, package in axivion_package.items():
        for platform,data in package.data.items():
            download_link=data['link']
            filename=data['filename']
            sha256=data['sha256'][filename]
            if False is check_file_exists(version=version,filename=filename,sha256=sha256):
                local_file=download.download_file(download_link)
                gateway.deploy_file(artifactory_url,artifactory_repository,
                                    local_file,subfolder=version)
            gateway.delete_files()
        
if __name__ == '__main__':
    main()