from src.regionify.app_invoice import AppInvoice
from src.regionify.cloudshell_package import CloudshellPackage
from distutils import dir_util
import os
import shutil

AZURE_INVOICE = '../regionify/invoices/azure_app_invoice.xlsx'

AWS_INVOICE = '../regionify/invoices/aws_app_invoice.xlsx'

AZURE_SOURCE_CLOUDSHELL_PACKAGE = '../cloudshell_package/azure'

AWS_SOURCE_CLOUDSHELL_PACKAGE = '../cloudshell_package/aws'

AWS_DIRECTORY = '..\\..\\Packages\\Amazon'
AZURE_DIRECTORY = '..\\..\\Packages\\Azure'


def main():
    shutil.rmtree(AWS_DIRECTORY)
    aws_package = CloudshellPackage(AWS_SOURCE_CLOUDSHELL_PACKAGE)
    aws_invoice = AppInvoice(AWS_INVOICE)
    for params in aws_invoice.aws_cloud_provider_params():
        target_path = os.path.join(AWS_DIRECTORY, params.app_name)
        dir_util.mkpath(target_path)
        aws_package.prepare_aws_package(params, target_path)

    shutil.rmtree(AZURE_DIRECTORY)
    azure_package = CloudshellPackage(AZURE_SOURCE_CLOUDSHELL_PACKAGE)
    azure_invoice = AppInvoice(AZURE_INVOICE)
    for params in azure_invoice.azure_cloud_provider_params():
        target_path = os.path.join(AZURE_DIRECTORY, params.app_name)
        dir_util.mkpath(target_path)
        azure_package.prepare_azure_package(params, target_path)

if __name__ == '__main__':
    main()
