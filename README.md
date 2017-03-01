https://github.com/QualiSystems/devguide_source/raw/master/logo.png
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





