import os
import shutil
import xml.etree.ElementTree as ET
from tempfile import mkdtemp

from src.regionify.constants import EXTENSION_SCRIPT_FILE, VM_SIZE, IMAGE_VERSION, IMAGE_SKU, IMAGE_OFFER, \
    IMAGE_PUBLISHER, INSTANCE_TYPE, AMI_ID, AWS_AMI_ID
from src.regionify.utilities import zippit, get_files


class CloudshellPackage:
    def __init__(self, src_package_path):
        self.src = src_package_path

    def prepare_aws_package(self, aws_parameters, dst_path):
        cp_modifications = {AMI_ID: aws_parameters.ami_id,
                            INSTANCE_TYPE: aws_parameters.instance_type}
        short_provider_name = 'aws'
        self._prepare_package(cp_modifications, aws_parameters.app_name, dst_path,
                              aws_parameters.region_name,
                              short_provider_name, CloudshellPackage._aws_specific_modifications)

    def prepare_azure_package(self, azure_parameters, dst_path):
        short_provider_name = 'azure'
        self._prepare_package(azure_parameters, azure_parameters.app_name, dst_path,
                              azure_parameters.region_name,
                              short_provider_name, CloudshellPackage._azure_specific_modifications)

    def _prepare_package(self, cp_modifications, app_name, dst_path, region_name,
                         short_provider_name, cp_modifier_func):
        source_dir = os.path.join(mkdtemp(), short_provider_name)
        try:
            shutil.copytree(self.src, source_dir)
            datamodel_path = self._get_app_datamodel_file(source_dir)
            self._modify_datamodel_file(cp_modifications, app_name, datamodel_path, region_name,
                                        cp_modifier_func)
            self._prepare_package_archive(app_name, source_dir, dst_path, region_name, short_provider_name)
        except Exception as e:
            shutil.rmtree(source_dir)
            raise e

    def _prepare_package_archive(self, app_name, package_source_path, dst_path, region_name, short_provider_name):
        archive_name = self._get_package_archive_name(app_name, region_name, short_provider_name)
        package_files = get_files(package_source_path)
        zippit(package_source_path, archive_name, package_files, dst_path)

    @staticmethod
    def _get_package_archive_name(app_name, region_name, short_provider_name):
        return '{0}_{1}_{2}.zip'.format(app_name, short_provider_name, region_name).replace(' ', '_')

    @staticmethod
    def _modify_datamodel_file(cp_values, app_name, datamodel_path, region_name,
                               cp_modifier_func):
        tree = ET.parse(datamodel_path)
        app_root = tree.getroot()
        app_resource_info = app_root.find('./AppResourceInfo')
        app_resource_info.attrib['Name'] = app_name
        deployment_path = app_root.findall('.//DeploymentPath')[0]
        deployment_service = deployment_path.find('./DeploymentService')
        deployment_service.attrib['CloudProvider'] = '{0}_{1}'.format(deployment_service.attrib['CloudProvider'],
                                                                      region_name)
        deployment_path.attrib['Name'] = '{0} - {1}'.format(deployment_service.attrib['CloudProvider'],
                                                            deployment_service.attrib['Name'])
        cp_modifier_func(cp_values, deployment_path)
        with open(datamodel_path, 'w') as f:
            tree.write(f)

    @staticmethod
    def _aws_specific_modifications(cp_modifications, deployment_path):
        ami_id_element = deployment_path.findall("./DeploymentService//Attribute[@Name='%s']" % AWS_AMI_ID)[0]
        ami_id_element.attrib['Value'] = cp_modifications[AMI_ID]
        ami_id_element = deployment_path.findall("./DeploymentService//Attribute[@Name='%s']" % INSTANCE_TYPE)[0]
        ami_id_element.attrib['Value'] = cp_modifications[INSTANCE_TYPE]

    @staticmethod
    def _azure_specific_modifications(azure_params, deployment_path):
        """
        :type azure_params: src.regionify.cp_parameters.AzureParameters
        :type deployment_path: xml.etree.Element
        :return:
        """
        cp = CloudshellPackage
        cp._modify_deployment_path_attribute(deployment_path, IMAGE_PUBLISHER, azure_params.image_publisher)
        cp._modify_deployment_path_attribute(deployment_path, IMAGE_OFFER, azure_params.image_offer)
        cp._modify_deployment_path_attribute(deployment_path, IMAGE_SKU, azure_params.image_sku)
        cp._modify_deployment_path_attribute(deployment_path, IMAGE_VERSION, azure_params.image_version)
        cp._modify_deployment_path_attribute(deployment_path, VM_SIZE, azure_params.vm_size)
        if azure_params.extension_script_file:
            cp._modify_deployment_path_attribute(deployment_path, EXTENSION_SCRIPT_FILE,
                                                 azure_params.extension_script_file)

    @staticmethod
    def _modify_deployment_path_attribute(deployment_path, attribute, value):
        element = deployment_path.findall("./DeploymentService//Attribute[@Name='{0}']".format(attribute))[0]
        element.attrib['Value'] = value
        return deployment_path

    @staticmethod
    def _get_app_datamodel_file(aws_dir):
        app_xml_path = os.path.join(aws_dir, 'App Templates', 'app.xml')
        return app_xml_path
