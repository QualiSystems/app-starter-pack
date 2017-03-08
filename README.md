Using App Starter Packages
This feature is only available for CloudShell 8.0 and above.
This article explains how to add, to CloudShell, App templates with preconfigured deployment paths that install VMs with a vanilla Linux or Windows operating system. The packages are provided as ZIP files that can be imported into CloudShell. Once imported, the App templates containing the new deployment paths are associated the OS Images service category.
The starter pack contains packages for Apps that can be deployed in AWS EC2 and Azure. Apps for the following OSs are available: CentOS, Red hat, Ubuntu, Windows Server 2012 and Windows Server 2016. 
To add preconfigured Apps: 
1.     In CloudShell Portal, in the Inventory dashboard, create the AWS EC2 or Microsoft Azure cloud provider resource to be used to deploy the App template’s VMs on the required region.
2.     Open https://github.com/QualiSystems/app-starter-pack/tree/master/Packages.
The repository is organized according to cloud provider>package type>supported regions.
For example, AWS EC2 packages that install Centos 7:
 
3.     Navigate to the desired package ZIP file and download locally. Some of the regions don’t have the desired OS.
Tip: The images of the Azure Windows packages can be accessed by Ansible.
4.      Unzip the package and in the App Template folder, edit the App.xml as follows:
•          In the element starting with <DeploymentService, change the CloudProvider value to the name of the desired region’s cloud provider resource in CloudShell. For example, “Azure_northeurope”.
•          (Optional) Customize the name of the deployment path to be added to the App template. In the element starting with <DeploymentPath, change the Name, as appropriate. By default, the name comprises the name of the cloud provider resource and the deployment type. For example, “Azure_northeurope - Azure VM From Marketplace”. 
5.    Save the file and rezip the contents.
Note: Only ZIP files are supported.
6.     Import the ZIP file into CloudShell.
A new app template is created that includes the package’s deployment path. The deployment path is set to the cloud provider resource you specified and populated with the preconfigured App’s basic deployment settings.
Note: Importing additional packages of the same OS will create additional deployment paths in this App template.
7.    The App template is assigned to the OS Images service category but also adds the following categories: Database Servers, Web Servers, and App Servers.. The App template’s category can be changed in the App.xml’s <Category> element before import and from within CloudShell Portal. Open the App template and edit as appropriate. For example, you might want to modify the size of the VM to be created, in the VM Size (Azure) or Instance Type (AWS EC2) attribute or associate it to a different category. 






# Preconfigured Apps
> A repository for Cloudshell Apps.

This repository hosts Cloudshell Apps for use with cloud services such
as Amazon Web Services and Azure.

These apps have region and type setting pre-populated.

There is also a utility to generate the premade packages based on a source 
template, and an excel invoice file.


## Packages

The preconfigured app packages can be found under Packages folder.


## Regionify

Regionify will create files in the Packages folder based on a source app
and an invoice.

Generating packages:
- Clone the preconfigured-apps repo to your local machine
- Run the main.py file on your local machine.
- Once packages are created under Packages folder, commit and push the new
  packages to Github.

### Source App

There is a different source app for each Cloud Provider, can be found 
under src/cloudshell_package/<Cloud Provider>

### Invoices

To determine which Cloud Provider image generate as a premade package, 
per region that is deployed, there are invoice excel files:
src/regionify/invoices/aws_app_invoice.xlsx
src/regionify/invoices/azure_app_invoice.xlsx

using this invoice you can specify:
region to deploy to
instance type/vm size
os





