# Terraform

## Provider

[Terraform providers](https://registry.terraform.io/browse/providers) are plugins or modules in Terraform that let it interact with external systems or services.

How They Work:

Connect to Systems: Providers are like translators that help Terraform communicate with cloud platforms (like AWS, Azure, or Google Cloud), on-premises tools, or third-party services.  

Define Resources: They define the types of resources you can manage, like virtual machines, databases, or storage buckets.  

Manage Resources: Providers handle creating, reading, updating, and deleting those resources in the system.  

Examples of Providers:

Cloud Providers: AWS, Azure, Google Cloud  
Service Providers: Kubernetes, GitHub, Datadog  
Infrastructure Providers: VMware, OpenStack

Key Points:

Each provider needs configuration, usually credentials or access keys, to connect to the system.  
Terraform uses providers to translate your .tf files (infrastructure code) into API calls to the respective services.

To install a provider

```terraform
terraform {
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = "4.14.0"
        }
    }
}
```

command : `terraform init`

## Lock file

Dependency Lock File

Purpose: Ensures consistent versions of Terraform providers are used across environments.

How It Works:  
When you run terraform init, Terraform creates or updates the terraform.lock.hcl file.  
This file contains the exact versions of the providers Terraform is configured to use.

Benefits:  
Prevents breaking changes by ensuring the same provider versions are used, even if newer versions are released.  
Ensures reproducibility across teams and environments.

Managing the Lock File:

To update provider versions, run:

```bash
terraform init -upgrade
```

## State file

The state file contains details about the resources created by Terraform, including their current configuration and metadata like resource IDs and attributes.

When you run terraform plan, Terraform compares the desired configuration (defined in your .tf files) with the actual state of the infrastructure (in the state file). Any differences are shown in the plan output

## **azure cli to get list of secret**

```bash
az keyvault secret list --vault-name <key_vault_name> --query "[].id" -o tsv
```

### Import

Terraform import is command that allows you to incorporate existing infrastructure resources into your
Terraform configuration and state management.

Steps:

create main.tf containing resource name, subscription id

```bash
terraform init
terraform import azurerm_key_vault_secret.example /subscriptions/5896dffd-29db-dd8g-b786-dgdg8dgdg8/resourceGroups/pss-common/providers/Microsoft.KeyVault/vaults/terraform-kv-001/secrets/terraform-secret-name
```

display imported resources

```bash
terraform state list #to display configured resource
terraform state show azurerm_key_vault_secret.example # to display resource values
```

to verify resources using terraform plan, update main.tf with details display in terminal

```bash
terraform plan
```

### Verbose

Levels of TF_LOG

TF_LOG=TRACE: This is the most verbose logging level. It logs every detail about the process, including internal operations and data being sent between the Terraform CLI and providers.

TF_LOG=DEBUG: This level provides detailed information but omits some internal operations that aren’t normally needed for most users. It's useful for debugging the configuration and interactions with providers.

TF_LOG=INFO: This is the default level and provides general information about what Terraform is doing, like showing the resources being created, updated, or destroyed.

TF_LOG=WARN: Shows warnings, such as deprecated functionality, but doesn't provide much information otherwise.

TF_LOG=ERROR: Only shows error messages when something goes wrong.

```bash
# set terraform log
export TF_LOG="TRACE"
export TF_LOG_PATH="filepath.log"

# unset var
unset TF_LOG
unset TF_LOG_PATH
```

show state file in json format

```bash
terraform show -json > terraform_state.json
```

## Modules

In Terraform, a module is a container for multiple resources that are used together. It allows you to group resources into reusable, self-contained units of configuration. Modules help organize Terraform code, improve reusability, and reduce duplication. They can be simple, like a single resource, or more complex, containing a set of resources for creating an entire infrastructure component.

Modules in Terraform allow for logical separation of infrastructure code and enable reusability. They are fundamental to writing clean, maintainable, and modular infrastructure code.

Types of Terraform Modules

**Root Module**: This is the starting point for Terraform execution and contains all the Terraform configuration files in the current working directory. It is the main module where you run terraform init, terraform plan, and terraform apply.

**Child Modules**: Modules that are used within the root module or other modules. You can create and call these modules to encapsulate parts of your configuration logic.

**External Modules**: Terraform modules that are stored outside of your project, typically shared in a module registry, like the Terraform Module Registry. You can use external modules to avoid "reinventing the wheel" and make use of pre-existing infrastructure code written by others.

```bash
/project
  ├── main.tf           (root module)
  ├── modules/
  │    └── s3_bucket/
  │        ├── main.tf  (child module to create an S3 bucket)
  │        └── variables.tf
  ├── outputs.tf
  └── variables.tf
```
