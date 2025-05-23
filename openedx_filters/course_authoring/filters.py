"""
Package where filters related to the Course Authoring architectural subdomain are implemented.
"""

from openedx_filters.tooling import OpenEdxPublicFilter


class LMSPageURLRequested(OpenEdxPublicFilter):
    """
    Custom class used to get lms page url filters and its custom methods.
    """

    filter_type = "org.openedx.course_authoring.lms.page.url.requested.v1"

    @classmethod
    def run_filter(cls, url, org):
        """
        Execute a filter with the signature specified.

        Arguments:
            url (str): the URL of the page to be modified.
            org (str): Course org filter used as context data to get LMS configurations.
        """
        data = super().run_pipeline(url=url, org=org)
        return data.get("url"), data.get("org")


class OrganizationListRequested(OpenEdxPublicFilter):
    """
    Filter used to modify the organization list based on site-specific configuration.

    Purpose:
        This filter is triggered when course authoring MFE requests the organization list,
        allowing the filter to modify the returned.

    Filter Type:
        org.openedx.content_authoring.organization.list.requested.v1

    Trigger:
        - Repository: openedx/edx-platform
        - Path: cms/djangoapps/contentstore/views/organization.py
        - Function or Method: OrganizationListView.get
    """

    filter_type = "org.openedx.content_authoring.organization.list.requested.v1"

    @classmethod
    def run_filter(cls, organizations: list, request=None) -> dict:
        """
        Process the organization list using configured pipeline steps.

        Arguments:
            organizations (list): List of all organizations from get_organizations()
            request: Django request object for additional context

        Returns:
            data (dict): Dictionary containing filtered organizations and request contexts
        """
        data = super().run_pipeline(
            organizations=organizations,
            request=request
        )
        return data
