from src.regionify.app_invoice import AppInvoice
from src.regionify.cloudshell_package import CloudshellPackage
from distutils import dir_util
import os

AWS_DIRECTORY = '..\\..\\Packages\\Amazon'
AZURE_DIRECTORY = '..\\..\\Packages\\Azure'


def main():
    aws_package = CloudshellPackage('../cloudshell_package/azure')
    aws_invoice = AppInvoice('../regionify/invoices/azure_app_invoice.xlsx')
    for params in aws_invoice.azure_cloud_provider_params():
        target_path = os.path.join(AWS_DIRECTORY, params.app_name)
        dir_util.mkpath(target_path)
        aws_package.prepare_azure_package(params, target_path)

    azure_package = CloudshellPackage('../cloudshell_package/azure')
    azure_invoice = AppInvoice('../regionify/invoices/azure_app_invoice.xlsx')
    for params in azure_invoice.azure_cloud_provider_params():
        target_path = os.path.join(AZURE_DIRECTORY, params.app_name)
        dir_util.mkpath(target_path)
        azure_package.prepare_azure_package(params, target_path)

if __name__ == '__main__':
    main()
