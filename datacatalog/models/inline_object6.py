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


class InlineObject6(object):
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
        'dataset_names__in': 'list[str]',
        'dataset_ids__in': 'list[str]',
        'standard_variable_ids__in': 'list[str]',
        'standard_variable_names__in': 'list[str]'
    }

    attribute_map = {
        'dataset_names__in': 'dataset_names__in',
        'dataset_ids__in': 'dataset_ids__in',
        'standard_variable_ids__in': 'standard_variable_ids__in',
        'standard_variable_names__in': 'standard_variable_names__in'
    }

    def __init__(self, dataset_names__in=None, dataset_ids__in=None, standard_variable_ids__in=None, standard_variable_names__in=None):  # noqa: E501
        """InlineObject6 - a model defined in OpenAPI"""  # noqa: E501

        self._dataset_names__in = None
        self._dataset_ids__in = None
        self._standard_variable_ids__in = None
        self._standard_variable_names__in = None
        self.discriminator = None

        if dataset_names__in is not None:
            self.dataset_names__in = dataset_names__in
        if dataset_ids__in is not None:
            self.dataset_ids__in = dataset_ids__in
        if standard_variable_ids__in is not None:
            self.standard_variable_ids__in = standard_variable_ids__in
        if standard_variable_names__in is not None:
            self.standard_variable_names__in = standard_variable_names__in

    @property
    def dataset_names__in(self):
        """Gets the dataset_names__in of this InlineObject6.  # noqa: E501


        :return: The dataset_names__in of this InlineObject6.  # noqa: E501
        :rtype: list[str]
        """
        return self._dataset_names__in

    @dataset_names__in.setter
    def dataset_names__in(self, dataset_names__in):
        """Sets the dataset_names__in of this InlineObject6.


        :param dataset_names__in: The dataset_names__in of this InlineObject6.  # noqa: E501
        :type: list[str]
        """

        self._dataset_names__in = dataset_names__in

    @property
    def dataset_ids__in(self):
        """Gets the dataset_ids__in of this InlineObject6.  # noqa: E501


        :return: The dataset_ids__in of this InlineObject6.  # noqa: E501
        :rtype: list[str]
        """
        return self._dataset_ids__in

    @dataset_ids__in.setter
    def dataset_ids__in(self, dataset_ids__in):
        """Sets the dataset_ids__in of this InlineObject6.


        :param dataset_ids__in: The dataset_ids__in of this InlineObject6.  # noqa: E501
        :type: list[str]
        """

        self._dataset_ids__in = dataset_ids__in

    @property
    def standard_variable_ids__in(self):
        """Gets the standard_variable_ids__in of this InlineObject6.  # noqa: E501


        :return: The standard_variable_ids__in of this InlineObject6.  # noqa: E501
        :rtype: list[str]
        """
        return self._standard_variable_ids__in

    @standard_variable_ids__in.setter
    def standard_variable_ids__in(self, standard_variable_ids__in):
        """Sets the standard_variable_ids__in of this InlineObject6.


        :param standard_variable_ids__in: The standard_variable_ids__in of this InlineObject6.  # noqa: E501
        :type: list[str]
        """

        self._standard_variable_ids__in = standard_variable_ids__in

    @property
    def standard_variable_names__in(self):
        """Gets the standard_variable_names__in of this InlineObject6.  # noqa: E501


        :return: The standard_variable_names__in of this InlineObject6.  # noqa: E501
        :rtype: list[str]
        """
        return self._standard_variable_names__in

    @standard_variable_names__in.setter
    def standard_variable_names__in(self, standard_variable_names__in):
        """Sets the standard_variable_names__in of this InlineObject6.


        :param standard_variable_names__in: The standard_variable_names__in of this InlineObject6.  # noqa: E501
        :type: list[str]
        """

        self._standard_variable_names__in = standard_variable_names__in

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
        if not isinstance(other, InlineObject6):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other