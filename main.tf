/*
* main.tf
*/

provider "azurerm" {
  environment = ""
}

module "windows-instance" {
  source  = "dcos-terraform/windows-instance/azurerm"
  version = "0.0.2"
  # Name of the azure resource group
  resource_group_name = ""
  # Azure Region
  location = ""
  # Name of the DC/OS cluster
  cluster_name = ""
  # How many instances should be created
  num = ""
  # Subnet ID
  subnet_id = ""
  # Azure virtual machine size
  vm_size = ""
}
