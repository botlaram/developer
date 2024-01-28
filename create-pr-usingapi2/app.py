from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        name = request.form['name']
        gender = request.form['gender']
        phone_number = request.form['phone_number']

        # Call a function to perform the Azure DevOps operations
        update_azure_repository(name, gender, phone_number)

    return render_template('index.html')


from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import json

def update_azure_repository(name, gender, phone_number):
    # Azure DevOps organization URL and personal access token
    organization_url = 'https://dev.azure.com/YOUR_ORG_NAME'
    personal_access_token = 'YOUR_PERSONAL_ACCESS_TOKEN'

    # Connect to Azure DevOps
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)

    # Azure DevOps project and repository information
    project = 'YOUR_PROJECT_NAME'
    repo_name = 'YOUR_REPO_NAME'
    branch_name = 'feature-branch'

    # Create a branch
    git_client = connection.clients.get_git_client()
    new_branch = git_client.create_branch(
        project=project,
        repository_id=repo_name,
        ref_name=f'refs/heads/{branch_name}',
        base_ref_name='refs/heads/master'
    )

    # Update details in a text file
    file_path = 'user_data.txt'
    file_content = f'Name: {name}\nGender: {gender}\nPhone Number: {phone_number}'

    git_client.create_push(
        push={
            'refUpdates': [{
                'name': f'refs/heads/{branch_name}',
                'oldObjectId': new_branch.commit.commit_id
            }],
            'commits': [{
                'comment': 'Update user data',
                'changes': [{
                    'changeType': 'edit',
                    'item': {
                        'path': file_path
                    },
                    'newContent': {
                        'content': file_content,
                        'contentType': 'rawtext'
                    }
                }]
            }]
        },
        repository_id=repo_name,
        project=project
    )

    # Create a pull request
    pr_client = connection.clients.get_pull_request_client()
    pr_client.create_pull_request(
        git_pull_request_to_create={
            'source_ref_name': f'refs/heads/{branch_name}',
            'target_ref_name': 'refs/heads/master',
            'title': 'Update user data'
        },
        repository_id=repo_name,
        project=project
    )


if __name__ == '__main__':
    app.run(debug=True)



