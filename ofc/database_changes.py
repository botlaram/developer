import os
import logging
import sqlite3
import sys
import argparse
import requests
from urllib3 import Retry
from requests.adapters import HTTPAdapter
from dataclasses import dataclass, field

# Set up the logger
logging.basicConfig(level=logging.INFO)

@dataclass
class DataBase:
    """configuration values to update DATABASE
    """
    artifactory_url: str = field(default="https://repo-manager.com/")
    file_path: str = field(default="common/dashboard2.db")

    def _check_file_size(self, destination_path):
        """check file successfully cloned or corrupted
        Args:
            destination_path(str): Database file path
        Returns:
            exit(1) > if file corrupted
        """
        '''194560 BYTE = 190 KB'''
        if os.path.getsize(destination_path) > 194560:
            return logging.info("File successfully cloned")
        logging.error("File size is not more than 190 KB. Terminating script.")
        sys.exit(1)

    def _download_file(self, token, destination_path):
        """downlaod file from Artifactory
        Args:
            token (str): Api-key
            destination_path (str): Database File path
        """
        file_url = f"{self.artifactory_url}/{self.file_path}"
        headers = {"X-JFrog-Art-Api": token}
        retry_strategy = Retry(
            total=3,
            backoff_factor=2,
            status_forcelist=[401,403],
        )

        http_adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", http_adapter)
        response = session.get(file_url,
                               headers=headers,
                               verify=False,
                               timeout=None)
        logging.info("Status Code %s",response.status_code)

        with open(destination_path, "wb") as file:
            file.write(response.content)
        logging.info(f"File downloaded to '{destination_path}'.")
        self._check_file_size(destination_path)

    def _update_database(self, database_path, zim_group):
        """Update ZIM group to Database file
        Args:
            database_path (str): Database File path
            zim_group (str): ZIM group
        """
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
            
        statement = (f'UPDATE axUserRef SET Name = "{zim_group}" WHERE Name="AZP-12_Discovery"')
        cursor.execute(statement)
        conn.commit()
        logging.info("Group Name updated")

    def _check_group_name(self,database_path,zim_group):
        """
        Display Databse table
        if not ZIM grp updated, create new ROW
        Args:
            database_path (str): _description_
            zim_group (str): _description_
        """
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        query = f'SELECT COUNT(*) FROM axUserRef WHERE name = {zim_group}'
        # cursor.execute(query, (f"{zim_group}",))
        cursor.execute(query)
        result = cursor.fetchone()

        # Check if any rows match the condition
        if result[0] > 0:
            print(f'The name "{zim_group}" exists in the table.')
        else:
            print(f'The name "{zim_group}" does not exist in the table.')
            logging.warning("Updating ZIM grp with new ROW")


            query = f'INSERT INTO axUserRef (ID, Type, Name) VALUES (?, ?, ?)'
            cursor.execute(query, (5, 4, zim_group))                                 # fixed
            conn.commit()


        '''display table in console'''
        query = 'SELECT * FROM axUserRef'
        cursor.execute(query)
        rows = cursor.fetchall()

        column_names = [description[0] for description in cursor.description]     # Print the column names
        print('\t'.join(column_names))

        for row in rows:                                                          # Print the table data
            print('\t'.join(str(cell) for cell in row))
        
        conn.close()

    def _main(self,zim_group,database,token):
        """execute all functions
        Args:
            zim_group (str): Database File path
            database (str): Name of the ZIM group
            token (str): Api-key
        """
        if not os.path.isfile(database):
            logging.info("File not found in the PVC. Downloading from artifactory...")
            try:
                self._download_file(token,database)
                self._update_database(database,zim_group)
                self._check_group_name(database,zim_group)
            except Exception as e:
                logging.error(f"Error occurred during initialization: {str(e)}")
                return 1
        else:
            logging.info("File already exists in the PVC. Skipping download.")
        return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser("database-changes")
    parser.add_argument(
        "-db",
        "--database",
        help="Database File path",
        required=True,
    )
    parser.add_argument(
        "-g", "--zimgroup", help="Name of the ZIM group", required=True
    )
    parser.add_argument(
        "-t", "--token", help="artifactory API-key", required=True
    )
    args = parser.parse_args()
        
    db = DataBase()
    db._main(zim_group=args.zimgroup,database=args.database,token=args.token)