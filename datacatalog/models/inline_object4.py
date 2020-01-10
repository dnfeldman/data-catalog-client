# coding: utf-8

"""
    MINT Data Catalog

    API Documentation for MINT Data Catalog  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: danf@usc.edu
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineObject4(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'dataset_id': 'str'
    }

    attribute_map = {
        'dataset_id': 'dataset_id'
    }

    def __init__(self, dataset_id=None):  # noqa: E501
        """InlineObject4 - a model defined in OpenAPI"""  # noqa: E501

        self._dataset_id = None
        self.discriminator = None

        if dataset_id is not None:
            self.dataset_id = dataset_id

    @property
    def dataset_id(self):
        """Gets the dataset_id of this InlineObject4.  # noqa: E501

        record_id of the dataset  # noqa: E501

        :return: The dataset_id of this InlineObject4.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this InlineObject4.

        record_id of the dataset  # noqa: E501

        :param dataset_id: The dataset_id of this InlineObject4.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other