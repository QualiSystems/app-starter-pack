class AwsParameters:
    def __init__(self, app_name, ami_id, instance_type, region_name):
        self._instance_type = instance_type
        self._ami_id = ami_id
        self._region_name = region_name
        self._app_name = app_name

    @property
    def app_name(self):
        return self._app_name

    @property
    def instance_type(self):
        return self._instance_type

    @property
    def ami_id(self):
        return self._ami_id

    @property
    def region_name(self):
        return self._region_name


class AzureParameters:
    def __init__(self, app_name, region_name, image_publisher, image_offer, image_sku, image_version='latest', vm_size='basic_A0'):
        self._region_name = region_name
        self._image_publisher = image_publisher
        self._image_offer = image_offer
        self._image_sku = image_sku
        self._image_version = image_version
        self._vm_size = vm_size
        self._app_name = app_name

    @property
    def app_name(self):
        return self._app_name

    @property
    def vm_size(self):
        return self._vm_size

    @property
    def region_name(self):
        return self._region_name

    @property
    def image_publisher(self):
        return self._image_publisher

    @property
    def image_offer(self):
        return self._image_offer

    @property
    def image_sku(self):
        return self._image_sku

    @property
    def image_version(self):
        return self._image_version