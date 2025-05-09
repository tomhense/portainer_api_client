# coding: utf-8

# flake8: noqa

"""
    PortainerCE API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://documentation.portainer.io/api/api-examples/ You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API environments(endpoints) require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example:  ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API environment(endpoint) has an associated access policy, it is documented in the description of each environment(endpoint).  Different access policies are available:  - Public access - Authenticated access - Restricted access - Administrator access  ### Public access  No authentication is required to access the environments(endpoints) with this access policy.  ### Authenticated access  Authentication is required to access the environments(endpoints) with this access policy.  ### Restricted access  Authentication is required to access the environments(endpoints) with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the environments(endpoints) with this access policy.  # Execute Docker requests  Portainer **DO NOT** expose specific environments(endpoints) to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API environment(endpoint) (which is not documented below due to Swagger limitations). This environment(endpoint) has a restricted access policy so you still need to be authenticated to be able to query this environment(endpoint). Any query on this environment(endpoint) will be proxied to the Docker API of the associated environment(endpoint) (requests and responses objects are the same as documented in the Docker API).  # Private Registry  Using private registry, you will need to pass a based64 encoded JSON string ‘{\"registryId\":\\<registryID value\\>}’ inside the Request Header. The parameter name is \"X-Registry-Auth\". \\<registryID value\\> - The registry ID where the repository was created.  Example:  ``` eyJyZWdpc3RyeUlkIjoxfQ== ```  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://documentation.portainer.io/api/api-examples/).   # noqa: E501

    OpenAPI spec version: 2.21.5
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.auth_api import AuthApi
from swagger_client.api.backup_api import BackupApi
from swagger_client.api.custom_templates_api import CustomTemplatesApi
from swagger_client.api.docker_api import DockerApi
from swagger_client.api.edge_api import EdgeApi
from swagger_client.api.edge_groups_api import EdgeGroupsApi
from swagger_client.api.edge_jobs_api import EdgeJobsApi
from swagger_client.api.edge_stacks_api import EdgeStacksApi
from swagger_client.api.edge_templates_api import EdgeTemplatesApi
from swagger_client.api.endpoint_groups_api import EndpointGroupsApi
from swagger_client.api.endpoints_api import EndpointsApi
from swagger_client.api.gitops_api import GitopsApi
from swagger_client.api.helm_api import HelmApi
from swagger_client.api.intel_api import IntelApi
from swagger_client.api.kubernetes_api import KubernetesApi
from swagger_client.api.ldap_api import LdapApi
from swagger_client.api.motd_api import MotdApi
from swagger_client.api.rbac_enabled_api import RbacEnabledApi
from swagger_client.api.registries_api import RegistriesApi
from swagger_client.api.resource_controls_api import ResourceControlsApi
from swagger_client.api.roles_api import RolesApi
from swagger_client.api.settings_api import SettingsApi
from swagger_client.api.ssl_api import SslApi
from swagger_client.api.stacks_api import StacksApi
from swagger_client.api.status_api import StatusApi
from swagger_client.api.system_api import SystemApi
from swagger_client.api.tags_api import TagsApi
from swagger_client.api.team_memberships_api import TeamMembershipsApi
from swagger_client.api.teams_api import TeamsApi
from swagger_client.api.templates_api import TemplatesApi
from swagger_client.api.upload_api import UploadApi
from swagger_client.api.users_api import UsersApi
from swagger_client.api.webhooks_api import WebhooksApi
from swagger_client.api.websocket_api import WebsocketApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.auth_authenticate_payload import AuthAuthenticatePayload
from swagger_client.models.auth_authenticate_response import AuthAuthenticateResponse
from swagger_client.models.auth_oauth_payload import AuthOauthPayload
from swagger_client.models.backup_backup_payload import BackupBackupPayload
from swagger_client.models.backup_restore_payload import BackupRestorePayload
from swagger_client.models.containers_container_gpus_response import ContainersContainerGpusResponse
from swagger_client.models.customtemplates_custom_template_from_file_content_payload import CustomtemplatesCustomTemplateFromFileContentPayload
from swagger_client.models.customtemplates_custom_template_from_git_repository_payload import CustomtemplatesCustomTemplateFromGitRepositoryPayload
from swagger_client.models.customtemplates_custom_template_update_payload import CustomtemplatesCustomTemplateUpdatePayload
from swagger_client.models.customtemplates_file_response import CustomtemplatesFileResponse
from swagger_client.models.demo_environment_details import DemoEnvironmentDetails
from swagger_client.models.edge_registry_credentials import EdgeRegistryCredentials
from swagger_client.models.edge_stack_payload import EdgeStackPayload
from swagger_client.models.edgegroups_decorated_edge_group import EdgegroupsDecoratedEdgeGroup
from swagger_client.models.edgegroups_edge_group_create_payload import EdgegroupsEdgeGroupCreatePayload
from swagger_client.models.edgegroups_edge_group_update_payload import EdgegroupsEdgeGroupUpdatePayload
from swagger_client.models.edgejobs_edge_job_create_from_file_content_payload import EdgejobsEdgeJobCreateFromFileContentPayload
from swagger_client.models.edgejobs_edge_job_file_response import EdgejobsEdgeJobFileResponse
from swagger_client.models.edgejobs_edge_job_update_payload import EdgejobsEdgeJobUpdatePayload
from swagger_client.models.edgejobs_file_response import EdgejobsFileResponse
from swagger_client.models.edgejobs_task_container import EdgejobsTaskContainer
from swagger_client.models.edgestacks_edge_stack_from_git_repository_payload import EdgestacksEdgeStackFromGitRepositoryPayload
from swagger_client.models.edgestacks_edge_stack_from_string_payload import EdgestacksEdgeStackFromStringPayload
from swagger_client.models.edgestacks_stack_file_response import EdgestacksStackFileResponse
from swagger_client.models.edgestacks_update_edge_stack_payload import EdgestacksUpdateEdgeStackPayload
from swagger_client.models.edgestacks_update_status_payload import EdgestacksUpdateStatusPayload
from swagger_client.models.endpointedge_edge_job_response import EndpointedgeEdgeJobResponse
from swagger_client.models.endpointedge_endpoint_edge_status_inspect_response import EndpointedgeEndpointEdgeStatusInspectResponse
from swagger_client.models.endpointedge_stack_status_response import EndpointedgeStackStatusResponse
from swagger_client.models.endpointgroups_endpoint_group_create_payload import EndpointgroupsEndpointGroupCreatePayload
from swagger_client.models.endpointgroups_endpoint_group_update_payload import EndpointgroupsEndpointGroupUpdatePayload
from swagger_client.models.endpoints_dockerhub_status_response import EndpointsDockerhubStatusResponse
from swagger_client.models.endpoints_endpoint_create_global_key_response import EndpointsEndpointCreateGlobalKeyResponse
from swagger_client.models.endpoints_endpoint_delete_batch_partial_response import EndpointsEndpointDeleteBatchPartialResponse
from swagger_client.models.endpoints_endpoint_delete_batch_payload import EndpointsEndpointDeleteBatchPayload
from swagger_client.models.endpoints_endpoint_delete_request import EndpointsEndpointDeleteRequest
from swagger_client.models.endpoints_endpoint_settings_update_payload import EndpointsEndpointSettingsUpdatePayload
from swagger_client.models.endpoints_endpoint_update_payload import EndpointsEndpointUpdatePayload
from swagger_client.models.endpoints_endpoint_update_relations_payload import EndpointsEndpointUpdateRelationsPayload
from swagger_client.models.endpoints_endpoint_update_relations_payload_relations import EndpointsEndpointUpdateRelationsPayloadRelations
from swagger_client.models.endpoints_force_update_service_payload import EndpointsForceUpdateServicePayload
from swagger_client.models.endpoints_registry_access_payload import EndpointsRegistryAccessPayload
from swagger_client.models.fdo_device_configure_payload import FdoDeviceConfigurePayload
from swagger_client.models.fdo_fdo_configure_payload import FdoFdoConfigurePayload
from swagger_client.models.filesystem_dir_entry import FilesystemDirEntry
from swagger_client.models.gitops_file_response import GitopsFileResponse
from swagger_client.models.gitops_repository_file_preview_payload import GitopsRepositoryFilePreviewPayload
from swagger_client.models.gittypes_git_authentication import GittypesGitAuthentication
from swagger_client.models.gittypes_repo_config import GittypesRepoConfig
from swagger_client.models.helm_add_helm_repo_url_payload import HelmAddHelmRepoUrlPayload
from swagger_client.models.helm_helm_user_repository_response import HelmHelmUserRepositoryResponse
from swagger_client.models.helm_install_chart_payload import HelmInstallChartPayload
from swagger_client.models.images_image_response import ImagesImageResponse
from swagger_client.models.kubernetes_k8s_application import KubernetesK8sApplication
from swagger_client.models.kubernetes_k8s_config_map_or_secret import KubernetesK8sConfigMapOrSecret
from swagger_client.models.kubernetes_k8s_ingress_controller import KubernetesK8sIngressController
from swagger_client.models.kubernetes_k8s_ingress_delete_requests import KubernetesK8sIngressDeleteRequests
from swagger_client.models.kubernetes_k8s_ingress_info import KubernetesK8sIngressInfo
from swagger_client.models.kubernetes_k8s_ingress_path import KubernetesK8sIngressPath
from swagger_client.models.kubernetes_k8s_ingress_tls import KubernetesK8sIngressTLS
from swagger_client.models.kubernetes_k8s_namespace_details import KubernetesK8sNamespaceDetails
from swagger_client.models.kubernetes_k8s_resource_quota import KubernetesK8sResourceQuota
from swagger_client.models.kubernetes_k8s_service_delete_requests import KubernetesK8sServiceDeleteRequests
from swagger_client.models.kubernetes_k8s_service_info import KubernetesK8sServiceInfo
from swagger_client.models.kubernetes_k8s_service_ingress import KubernetesK8sServiceIngress
from swagger_client.models.kubernetes_k8s_service_port import KubernetesK8sServicePort
from swagger_client.models.kubernetes_namespaces_toggle_system_payload import KubernetesNamespacesToggleSystemPayload
from swagger_client.models.ldap_check_payload import LdapCheckPayload
from swagger_client.models.motd_motd_response import MotdMotdResponse
from swagger_client.models.openamt_device_action_payload import OpenamtDeviceActionPayload
from swagger_client.models.openamt_device_features_payload import OpenamtDeviceFeaturesPayload
from swagger_client.models.openamt_open_amt_configure_payload import OpenamtOpenAMTConfigurePayload
from swagger_client.models.portainer_api_key import PortainerAPIKey
from swagger_client.models.portainer_access_policy import PortainerAccessPolicy
from swagger_client.models.portainer_authorizations import PortainerAuthorizations
from swagger_client.models.portainer_auto_update_settings import PortainerAutoUpdateSettings
from swagger_client.models.portainer_azure_credentials import PortainerAzureCredentials
from swagger_client.models.portainer_custom_template import PortainerCustomTemplate
from swagger_client.models.portainer_custom_template_variable_definition import PortainerCustomTemplateVariableDefinition
from swagger_client.models.portainer_docker_snapshot import PortainerDockerSnapshot
from swagger_client.models.portainer_docker_snapshot_raw import PortainerDockerSnapshotRaw
from swagger_client.models.portainer_ecr_data import PortainerEcrData
from swagger_client.models.portainer_edge_group import PortainerEdgeGroup
from swagger_client.models.portainer_edge_job import PortainerEdgeJob
from swagger_client.models.portainer_edge_job_endpoint_meta import PortainerEdgeJobEndpointMeta
from swagger_client.models.portainer_edge_stack import PortainerEdgeStack
from swagger_client.models.portainer_edge_stack_deployment_status import PortainerEdgeStackDeploymentStatus
from swagger_client.models.portainer_edge_stack_status import PortainerEdgeStackStatus
from swagger_client.models.portainer_edge_stack_status_details import PortainerEdgeStackStatusDetails
from swagger_client.models.portainer_endpoint import PortainerEndpoint
from swagger_client.models.portainer_endpoint_agent import PortainerEndpointAgent
from swagger_client.models.portainer_endpoint_authorizations import PortainerEndpointAuthorizations
from swagger_client.models.portainer_endpoint_group import PortainerEndpointGroup
from swagger_client.models.portainer_endpoint_post_init_migrations import PortainerEndpointPostInitMigrations
from swagger_client.models.portainer_endpoint_security_settings import PortainerEndpointSecuritySettings
from swagger_client.models.portainer_environment_edge_settings import PortainerEnvironmentEdgeSettings
from swagger_client.models.portainer_fdo_configuration import PortainerFDOConfiguration
from swagger_client.models.portainer_gitlab_registry_data import PortainerGitlabRegistryData
from swagger_client.models.portainer_global_deployment_options import PortainerGlobalDeploymentOptions
from swagger_client.models.portainer_helm_user_repository import PortainerHelmUserRepository
from swagger_client.models.portainer_internal_auth_settings import PortainerInternalAuthSettings
from swagger_client.models.portainer_k8s_namespace_info import PortainerK8sNamespaceInfo
from swagger_client.models.portainer_k8s_node_limits import PortainerK8sNodeLimits
from swagger_client.models.portainer_k8s_nodes_limits import PortainerK8sNodesLimits
from swagger_client.models.portainer_kubernetes_configuration import PortainerKubernetesConfiguration
from swagger_client.models.portainer_kubernetes_data import PortainerKubernetesData
from swagger_client.models.portainer_kubernetes_flags import PortainerKubernetesFlags
from swagger_client.models.portainer_kubernetes_ingress_class_config import PortainerKubernetesIngressClassConfig
from swagger_client.models.portainer_kubernetes_snapshot import PortainerKubernetesSnapshot
from swagger_client.models.portainer_kubernetes_storage_class_config import PortainerKubernetesStorageClassConfig
from swagger_client.models.portainer_ldap_group_search_settings import PortainerLDAPGroupSearchSettings
from swagger_client.models.portainer_ldap_search_settings import PortainerLDAPSearchSettings
from swagger_client.models.portainer_ldap_settings import PortainerLDAPSettings
from swagger_client.models.portainer_o_auth_settings import PortainerOAuthSettings
from swagger_client.models.portainer_open_amt_configuration import PortainerOpenAMTConfiguration
from swagger_client.models.portainer_open_amt_device_enabled_features import PortainerOpenAMTDeviceEnabledFeatures
from swagger_client.models.portainer_pair import PortainerPair
from swagger_client.models.portainer_quay_registry_data import PortainerQuayRegistryData
from swagger_client.models.portainer_registry import PortainerRegistry
from swagger_client.models.portainer_registry_access_policies import PortainerRegistryAccessPolicies
from swagger_client.models.portainer_registry_accesses import PortainerRegistryAccesses
from swagger_client.models.portainer_registry_management_configuration import PortainerRegistryManagementConfiguration
from swagger_client.models.portainer_resource_control import PortainerResourceControl
from swagger_client.models.portainer_role import PortainerRole
from swagger_client.models.portainer_ssl_settings import PortainerSSLSettings
from swagger_client.models.portainer_settings import PortainerSettings
from swagger_client.models.portainer_settings_edge import PortainerSettingsEdge
from swagger_client.models.portainer_stack import PortainerStack
from swagger_client.models.portainer_stack_deployment_info import PortainerStackDeploymentInfo
from swagger_client.models.portainer_stack_option import PortainerStackOption
from swagger_client.models.portainer_tls_configuration import PortainerTLSConfiguration
from swagger_client.models.portainer_tag import PortainerTag
from swagger_client.models.portainer_team import PortainerTeam
from swagger_client.models.portainer_team_access_policies import PortainerTeamAccessPolicies
from swagger_client.models.portainer_team_membership import PortainerTeamMembership
from swagger_client.models.portainer_team_resource_access import PortainerTeamResourceAccess
from swagger_client.models.portainer_template import PortainerTemplate
from swagger_client.models.portainer_template_env import PortainerTemplateEnv
from swagger_client.models.portainer_template_env_select import PortainerTemplateEnvSelect
from swagger_client.models.portainer_template_repository import PortainerTemplateRepository
from swagger_client.models.portainer_template_volume import PortainerTemplateVolume
from swagger_client.models.portainer_user import PortainerUser
from swagger_client.models.portainer_user_access_policies import PortainerUserAccessPolicies
from swagger_client.models.portainer_user_resource_access import PortainerUserResourceAccess
from swagger_client.models.portainer_user_theme_settings import PortainerUserThemeSettings
from swagger_client.models.portainer_webhook import PortainerWebhook
from swagger_client.models.registries_registry_configure_payload import RegistriesRegistryConfigurePayload
from swagger_client.models.registries_registry_create_payload import RegistriesRegistryCreatePayload
from swagger_client.models.registries_registry_update_payload import RegistriesRegistryUpdatePayload
from swagger_client.models.release_chart import ReleaseChart
from swagger_client.models.release_dependency import ReleaseDependency
from swagger_client.models.release_file import ReleaseFile
from swagger_client.models.release_hook import ReleaseHook
from swagger_client.models.release_hook_execution import ReleaseHookExecution
from swagger_client.models.release_lock import ReleaseLock
from swagger_client.models.release_maintainer import ReleaseMaintainer
from swagger_client.models.release_metadata import ReleaseMetadata
from swagger_client.models.release_release import ReleaseRelease
from swagger_client.models.release_release_element import ReleaseReleaseElement
from swagger_client.models.resource_quantity import ResourceQuantity
from swagger_client.models.resourcecontrols_resource_control_create_payload import ResourcecontrolsResourceControlCreatePayload
from swagger_client.models.resourcecontrols_resource_control_update_payload import ResourcecontrolsResourceControlUpdatePayload
from swagger_client.models.settings_public_settings_response import SettingsPublicSettingsResponse
from swagger_client.models.settings_public_settings_response_edge import SettingsPublicSettingsResponseEdge
from swagger_client.models.settings_settings_update_payload import SettingsSettingsUpdatePayload
from swagger_client.models.ssl_ssl_update_payload import SslSslUpdatePayload
from swagger_client.models.stacks_compose_stack_from_file_content_payload import StacksComposeStackFromFileContentPayload
from swagger_client.models.stacks_compose_stack_from_git_repository_payload import StacksComposeStackFromGitRepositoryPayload
from swagger_client.models.stacks_kubernetes_git_deployment_payload import StacksKubernetesGitDeploymentPayload
from swagger_client.models.stacks_kubernetes_manifest_url_deployment_payload import StacksKubernetesManifestURLDeploymentPayload
from swagger_client.models.stacks_kubernetes_string_deployment_payload import StacksKubernetesStringDeploymentPayload
from swagger_client.models.stacks_stack_file_response import StacksStackFileResponse
from swagger_client.models.stacks_stack_git_redploy_payload import StacksStackGitRedployPayload
from swagger_client.models.stacks_stack_git_update_payload import StacksStackGitUpdatePayload
from swagger_client.models.stacks_stack_migrate_payload import StacksStackMigratePayload
from swagger_client.models.stacks_swarm_stack_from_file_content_payload import StacksSwarmStackFromFileContentPayload
from swagger_client.models.stacks_swarm_stack_from_git_repository_payload import StacksSwarmStackFromGitRepositoryPayload
from swagger_client.models.stacks_update_swarm_stack_payload import StacksUpdateSwarmStackPayload
from swagger_client.models.swarm_service_update_response import SwarmServiceUpdateResponse
from swagger_client.models.system_build_info import SystemBuildInfo
from swagger_client.models.system_nodes_count_response import SystemNodesCountResponse
from swagger_client.models.system_status import SystemStatus
from swagger_client.models.system_system_info_response import SystemSystemInfoResponse
from swagger_client.models.system_version_response import SystemVersionResponse
from swagger_client.models.tags_tag_create_payload import TagsTagCreatePayload
from swagger_client.models.teammemberships_team_membership_create_payload import TeammembershipsTeamMembershipCreatePayload
from swagger_client.models.teammemberships_team_membership_update_payload import TeammembershipsTeamMembershipUpdatePayload
from swagger_client.models.teams_team_create_payload import TeamsTeamCreatePayload
from swagger_client.models.teams_team_update_payload import TeamsTeamUpdatePayload
from swagger_client.models.templates_file_payload import TemplatesFilePayload
from swagger_client.models.templates_file_response import TemplatesFileResponse
from swagger_client.models.templates_list_response import TemplatesListResponse
from swagger_client.models.users_access_token_response import UsersAccessTokenResponse
from swagger_client.models.users_add_helm_repo_url_payload import UsersAddHelmRepoUrlPayload
from swagger_client.models.users_admin_init_payload import UsersAdminInitPayload
from swagger_client.models.users_helm_user_repository_response import UsersHelmUserRepositoryResponse
from swagger_client.models.users_theme_payload import UsersThemePayload
from swagger_client.models.users_user_access_token_create_payload import UsersUserAccessTokenCreatePayload
from swagger_client.models.users_user_create_payload import UsersUserCreatePayload
from swagger_client.models.users_user_update_password_payload import UsersUserUpdatePasswordPayload
from swagger_client.models.users_user_update_payload import UsersUserUpdatePayload
from swagger_client.models.v1_duration import V1Duration
from swagger_client.models.v1_fields_v1 import V1FieldsV1
from swagger_client.models.v1_managed_fields_entry import V1ManagedFieldsEntry
from swagger_client.models.v1_owner_reference import V1OwnerReference
from swagger_client.models.v1_resource_list import V1ResourceList
from swagger_client.models.v1beta1_container_metrics import V1beta1ContainerMetrics
from swagger_client.models.v1beta1_node_metrics import V1beta1NodeMetrics
from swagger_client.models.v1beta1_node_metrics_list import V1beta1NodeMetricsList
from swagger_client.models.v1beta1_pod_metrics import V1beta1PodMetrics
from swagger_client.models.v1beta1_pod_metrics_list import V1beta1PodMetricsList
from swagger_client.models.webhooks_webhook_create_payload import WebhooksWebhookCreatePayload
from swagger_client.models.webhooks_webhook_update_payload import WebhooksWebhookUpdatePayload
