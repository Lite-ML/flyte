# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.admin_system_metadata import AdminSystemMetadata  # noqa: F401,E501
from flyteadmin.models.core_node_execution_identifier import CoreNodeExecutionIdentifier  # noqa: F401,E501
from flyteadmin.models.core_workflow_execution_identifier import CoreWorkflowExecutionIdentifier  # noqa: F401,E501
from flyteadmin.models.execution_metadata_execution_mode import ExecutionMetadataExecutionMode  # noqa: F401,E501


class AdminExecutionMetadata(object):
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
        'mode': 'ExecutionMetadataExecutionMode',
        'principal': 'str',
        'nesting': 'int',
        'scheduled_at': 'datetime',
        'parent_node_execution': 'CoreNodeExecutionIdentifier',
        'reference_execution': 'CoreWorkflowExecutionIdentifier',
        'system_metadata': 'AdminSystemMetadata'
    }

    attribute_map = {
        'mode': 'mode',
        'principal': 'principal',
        'nesting': 'nesting',
        'scheduled_at': 'scheduled_at',
        'parent_node_execution': 'parent_node_execution',
        'reference_execution': 'reference_execution',
        'system_metadata': 'system_metadata'
    }

    def __init__(self, mode=None, principal=None, nesting=None, scheduled_at=None, parent_node_execution=None, reference_execution=None, system_metadata=None):  # noqa: E501
        """AdminExecutionMetadata - a model defined in Swagger"""  # noqa: E501

        self._mode = None
        self._principal = None
        self._nesting = None
        self._scheduled_at = None
        self._parent_node_execution = None
        self._reference_execution = None
        self._system_metadata = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if principal is not None:
            self.principal = principal
        if nesting is not None:
            self.nesting = nesting
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if parent_node_execution is not None:
            self.parent_node_execution = parent_node_execution
        if reference_execution is not None:
            self.reference_execution = reference_execution
        if system_metadata is not None:
            self.system_metadata = system_metadata

    @property
    def mode(self):
        """Gets the mode of this AdminExecutionMetadata.  # noqa: E501


        :return: The mode of this AdminExecutionMetadata.  # noqa: E501
        :rtype: ExecutionMetadataExecutionMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this AdminExecutionMetadata.


        :param mode: The mode of this AdminExecutionMetadata.  # noqa: E501
        :type: ExecutionMetadataExecutionMode
        """

        self._mode = mode

    @property
    def principal(self):
        """Gets the principal of this AdminExecutionMetadata.  # noqa: E501

        Identifier of the entity that triggered this execution. For systems using back-end authentication any value set here will be discarded in favor of the authenticated user context.  # noqa: E501

        :return: The principal of this AdminExecutionMetadata.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this AdminExecutionMetadata.

        Identifier of the entity that triggered this execution. For systems using back-end authentication any value set here will be discarded in favor of the authenticated user context.  # noqa: E501

        :param principal: The principal of this AdminExecutionMetadata.  # noqa: E501
        :type: str
        """

        self._principal = principal

    @property
    def nesting(self):
        """Gets the nesting of this AdminExecutionMetadata.  # noqa: E501

        Indicates the nestedness of this execution. If a user launches a workflow execution, the default nesting is 0. If this execution further launches a workflow (child workflow), the nesting level is incremented by 0 => 1 Generally, if workflow at nesting level k launches a workflow then the child workflow will have nesting = k + 1.  # noqa: E501

        :return: The nesting of this AdminExecutionMetadata.  # noqa: E501
        :rtype: int
        """
        return self._nesting

    @nesting.setter
    def nesting(self, nesting):
        """Sets the nesting of this AdminExecutionMetadata.

        Indicates the nestedness of this execution. If a user launches a workflow execution, the default nesting is 0. If this execution further launches a workflow (child workflow), the nesting level is incremented by 0 => 1 Generally, if workflow at nesting level k launches a workflow then the child workflow will have nesting = k + 1.  # noqa: E501

        :param nesting: The nesting of this AdminExecutionMetadata.  # noqa: E501
        :type: int
        """

        self._nesting = nesting

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this AdminExecutionMetadata.  # noqa: E501

        For scheduled executions, the requested time for execution for this specific schedule invocation.  # noqa: E501

        :return: The scheduled_at of this AdminExecutionMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this AdminExecutionMetadata.

        For scheduled executions, the requested time for execution for this specific schedule invocation.  # noqa: E501

        :param scheduled_at: The scheduled_at of this AdminExecutionMetadata.  # noqa: E501
        :type: datetime
        """

        self._scheduled_at = scheduled_at

    @property
    def parent_node_execution(self):
        """Gets the parent_node_execution of this AdminExecutionMetadata.  # noqa: E501


        :return: The parent_node_execution of this AdminExecutionMetadata.  # noqa: E501
        :rtype: CoreNodeExecutionIdentifier
        """
        return self._parent_node_execution

    @parent_node_execution.setter
    def parent_node_execution(self, parent_node_execution):
        """Sets the parent_node_execution of this AdminExecutionMetadata.


        :param parent_node_execution: The parent_node_execution of this AdminExecutionMetadata.  # noqa: E501
        :type: CoreNodeExecutionIdentifier
        """

        self._parent_node_execution = parent_node_execution

    @property
    def reference_execution(self):
        """Gets the reference_execution of this AdminExecutionMetadata.  # noqa: E501

        Optional, a reference workflow execution related to this execution. In the case of a relaunch, this references the original workflow execution.  # noqa: E501

        :return: The reference_execution of this AdminExecutionMetadata.  # noqa: E501
        :rtype: CoreWorkflowExecutionIdentifier
        """
        return self._reference_execution

    @reference_execution.setter
    def reference_execution(self, reference_execution):
        """Sets the reference_execution of this AdminExecutionMetadata.

        Optional, a reference workflow execution related to this execution. In the case of a relaunch, this references the original workflow execution.  # noqa: E501

        :param reference_execution: The reference_execution of this AdminExecutionMetadata.  # noqa: E501
        :type: CoreWorkflowExecutionIdentifier
        """

        self._reference_execution = reference_execution

    @property
    def system_metadata(self):
        """Gets the system_metadata of this AdminExecutionMetadata.  # noqa: E501

        Optional, platform-specific metadata about the execution. In this the future this may be gated behind an ACL or some sort of authorization.  # noqa: E501

        :return: The system_metadata of this AdminExecutionMetadata.  # noqa: E501
        :rtype: AdminSystemMetadata
        """
        return self._system_metadata

    @system_metadata.setter
    def system_metadata(self, system_metadata):
        """Sets the system_metadata of this AdminExecutionMetadata.

        Optional, platform-specific metadata about the execution. In this the future this may be gated behind an ACL or some sort of authorization.  # noqa: E501

        :param system_metadata: The system_metadata of this AdminExecutionMetadata.  # noqa: E501
        :type: AdminSystemMetadata
        """

        self._system_metadata = system_metadata

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
        if issubclass(AdminExecutionMetadata, dict):
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
        if not isinstance(other, AdminExecutionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
