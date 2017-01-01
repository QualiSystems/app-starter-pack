import unittest
from src.regionify.build import CloudshellPackage, AwsParameters, AzureParameters


class TestBuild(unittest.TestCase):
    def test_build_aws_region_packages(self):
        aws_package = CloudshellPackage('../cloudshell_package/aws')
        aws_params = AwsParameters(ami_id='ami-6d1c2007', instance_type='basic', region_name='us-east-1')
        aws_package.prepare_aws_package(aws_params, 'windows loliflex', 'c:\\temp')

    def test_build_azure_region_packages(self):
        azure_package = CloudshellPackage('../cloudshell_package/azure')
        azure_params = AzureParameters(image_publisher='MicrosoftWindowsServer',
                                       image_offer='WindowsServer',
                                       image_sku='2012-R2-Datacenter',
                                       image_version='latest',
                                       region_name='us-east-1',
                                       vm_size='Basic_A0')
        azure_package.prepare_azure_package(azure_params, 'windows loliflex', 'c:\\temp')
