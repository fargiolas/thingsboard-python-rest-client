# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SchedulerEventId(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'entity_type': 'entityType',
        'id': 'id'
    }

    def __init__(self, entity_type=None, id=None):  # noqa: E501
        """EntityId - a model defined in Swagger"""  # noqa: E501

        self._entity_type = None
        self._id = None
        self.discriminator = None

        if entity_type is not None:
            self.entity_type = entity_type
        if id is not None:
            self.id = id

    @property
    def entity_type(self):
        """Gets the entity_type of this EntityId.  # noqa: E501


        :return: The entity_type of this EntityId.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EntityId.


        :param entity_type: The entity_type of this EntityId.  # noqa: E501
        :type: str
        """
        allowed_values = ["TENANT", "CUSTOMER", "USER", "DASHBOARD", "ASSET", "DEVICE", "ALARM", "ENTITY_GROUP", "CONVERTER", "INTEGRATION", "RULE_CHAIN", "RULE_NODE", "SCHEDULER_EVENT", "BLOB_ENTITY", "ENTITY_VIEW", "WIDGETS_BUNDLE", "WIDGET_TYPE", "ROLE", "GROUP_PERMISSION"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def id(self):
        """Gets the id of this EntityId.  # noqa: E501


        :return: The id of this EntityId.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityId.


        :param id: The id of this EntityId.  # noqa: E501
        :type: str
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(self.__class__, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
