variable "subscription_id" {
    description = "The name of the subscription id in which to create the resource."
    type = string
}

variable "resource_group_name" {
    description = "The name of the resource group in which to create the resource."
    type = string
}

variable "key_vault_name" {
    description = "The name of the keyvault name in which to create the resource."
    type = string
}

variable "secrets" {
    type = map(string)
    default = {
      "secret_name1" = "secret_value1"
      "secret_name2" = "secret_value2"
      "secret_name3" = "secret_value3"
    }
}