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

class AlarmRule(object):
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
        'alarm_details': 'str',
        'condition': 'AlarmCondition',
        'dashboard_id': 'DashboardId',
        'schedule': 'AlarmSchedule'
    }

    attribute_map = {
        'alarm_details': 'alarmDetails',
        'condition': 'condition',
        'dashboard_id': 'dashboardId',
        'schedule': 'schedule'
    }

    def __init__(self, alarm_details=None, condition=None, dashboard_id=None, schedule=None):  # noqa: E501
        """AlarmRule - a model defined in Swagger"""  # noqa: E501
        self._alarm_details = None
        self._condition = None
        self._dashboard_id = None
        self._schedule = None
        self.discriminator = None
        if alarm_details is not None:
            self.alarm_details = alarm_details
        if condition is not None:
            self.condition = condition
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if schedule is not None:
            self.schedule = schedule

    @property
    def alarm_details(self):
        """Gets the alarm_details of this AlarmRule.  # noqa: E501


        :return: The alarm_details of this AlarmRule.  # noqa: E501
        :rtype: str
        """
        return self._alarm_details

    @alarm_details.setter
    def alarm_details(self, alarm_details):
        """Sets the alarm_details of this AlarmRule.


        :param alarm_details: The alarm_details of this AlarmRule.  # noqa: E501
        :type: str
        """

        self._alarm_details = alarm_details

    @property
    def condition(self):
        """Gets the condition of this AlarmRule.  # noqa: E501


        :return: The condition of this AlarmRule.  # noqa: E501
        :rtype: AlarmCondition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this AlarmRule.


        :param condition: The condition of this AlarmRule.  # noqa: E501
        :type: AlarmCondition
        """

        self._condition = condition

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this AlarmRule.  # noqa: E501


        :return: The dashboard_id of this AlarmRule.  # noqa: E501
        :rtype: DashboardId
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this AlarmRule.


        :param dashboard_id: The dashboard_id of this AlarmRule.  # noqa: E501
        :type: DashboardId
        """

        self._dashboard_id = dashboard_id

    @property
    def schedule(self):
        """Gets the schedule of this AlarmRule.  # noqa: E501


        :return: The schedule of this AlarmRule.  # noqa: E501
        :rtype: AlarmSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AlarmRule.


        :param schedule: The schedule of this AlarmRule.  # noqa: E501
        :type: AlarmSchedule
        """

        self._schedule = schedule

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
        if issubclass(AlarmRule, dict):
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
        if not isinstance(other, AlarmRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
