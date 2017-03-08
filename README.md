#
# Using App Starter Packages

| **This feature is only available for CloudShell 8.0 and above.** |
| --- |

This article explains how to add, to CloudShell, App templates with preconfigured deployment paths that install VMs with a vanilla Linux or Windows operating system. The packages are provided as ZIP files that can be imported into CloudShell. Once imported, the App templates containing the new deployment paths are associated the  **OS Images**  service category.

The starter pack contains packages for Apps that can be deployed in AWS EC2 and Azure. Apps for the following OSs are available: CentOS, Red hat, Ubuntu, Windows Server 2012 and Windows Server 2016.

## **To add preconfigured Apps: **

1.     In CloudShell Portal, in the  **Inventory**  dashboard, create the  **AWS EC2**  or  **Microsoft Azure**  cloud provider resource to be used to deploy the App template&#39;s VMs on the required region.

2.     Open  [https://github.com/QualiSystems/app-starter-pack/tree/master/Packages](https://github.com/QualiSystems/app-starter-pack/tree/master/Packages).

The repository is organized according to cloud provider&gt;package type&gt;supported regions.

For example, AWS EC2 packages that install Centos 7:

 ![](data:image/*;base64,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)

3.     Navigate to the desired package ZIP file and download locally. Some of the regions don&#39;t have the desired OS.

**Tip:**  The images of the Azure Windows packages can be accessed by Ansible.

4.      Unzip the package and in the  **App Template**  folder, edit the  **App.xml**  as follows:

          In the element starting with  **&lt;DeploymentService** , change the  **CloudProvider**  value to the name of the desired region&#39;s cloud provider resource in CloudShell. For example, &quot;Azure\_northeurope&quot;.

          (Optional) Customize the name of the deployment path to be added to the App template. In the element starting with  **&lt;DeploymentPath** , change the  **Name** , as appropriate. By default, the name comprises the name of the cloud provider resource and the deployment type. For example, &quot;Azure\_northeurope - Azure VM From Marketplace&quot;.

5.    Save the file and rezip the contents.

**Note:**  Only ZIP files are supported.

6.     Import the ZIP file into CloudShell.

A new app template is created that includes the package&#39;s deployment path. The deployment path is set to the cloud provider resource you specified and populated with the preconfigured App&#39;s basic deployment settings.

**Note:**  Importing additional packages of the same OS will create additional deployment paths in this App template.

7.    The App template is assigned to the  **OS Images**  service category but also adds the following categories: Database Servers, Web Servers, and App Servers.. The App template&#39;s category can be changed in the  **App.xml**&#39;s  **&lt;Category&gt;**  element before import and from within CloudShell Portal. Open the App template and edit as appropriate. For example, you might want to modify the size of the VM to be created, in the  **VM Size****  **(Azure) or **Instance Type** (AWS EC2) attribute or associate it to a different category.







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





