import unittest
from regionify.cloudshell_package import CloudshellPackage
from regionify.cp_parameters import AwsParameters, AzureParameters
from regionify.app_invoice import AppInvoice


class TestBuild(unittest.TestCase):
    def test_build_aws_region_packages(self):
        aws_package = CloudshellPackage('../cloudshell_package/aws')
        aws_params = AwsParameters(ami_id='ami-6d1c2007', instance_type='basic', region_name='us-east-1',
                                   app_name='windows 12')
        aws_package.prepare_aws_package(aws_params, 'c:\\temp')

    def test_build_azure_region_packages(self):
        azure_package = CloudshellPackage('../cloudshell_package/azure')
        azure_params = AzureParameters(image_publisher='MicrosoftWindowsServer',
                                       image_offer='WindowsServer',
                                       image_sku='2012-R2-Datacenter',
                                       image_version='latest',
                                       region_name='us-east-1',
                                       vm_size='Basic_A0',
                                       app_name='windows 13')
        azure_package.prepare_azure_package(azure_params, 'c:\\temp')

    def test_app_invoice_get_aws_cp_params(self):
        invoice = AppInvoice('aws_app_invoice.xlsx')
        records = invoice.aws_cloud_provider_params()
        print records

    def test_app_invoice_get_azure_cp_params(self):
        invoice = AppInvoice('azure_app_invoice.xlsx')
        records = invoice.azure_cloud_provider_params()
        print records

    def test_build_packages_from_aws_invoice(self):
        aws_package = CloudshellPackage('../cloudshell_package/aws')
        aws_invoice = AppInvoice('../regionify/invoices/aws_app_invoice.xlsx')
        for params in aws_invoice.aws_cloud_provider_params():
            aws_package.prepare_aws_package(params, 'c:\\temp2')

    def test_build_packages_from_azure_invoice(self):
        azure_package = CloudshellPackage('../cloudshell_package/azure')
        azure_invoice = AppInvoice('../regionify/invoices/azure_app_invoice.xlsx')
        for params in azure_invoice.azure_cloud_provider_params():
            azure_package.prepare_azure_package(params, 'c:\\temp2')

