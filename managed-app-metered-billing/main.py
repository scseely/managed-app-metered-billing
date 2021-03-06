# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------


import argparse
import os
import sys

path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append("")
import pprint
from datetime import datetime, timedelta

from azure.identity import ClientSecretCredential
from azure.mgmt.resource import managedapplications
from azure.mgmt.subscription import SubscriptionClient
from msrestazure.azure_active_directory import ServicePrincipalCredentials
from microsoft.marketplace.meter import MeteringAPI
from microsoft.marketplace.meter.models import UsageEvent


def handle_usage_event_response(response, data, other):
    # data will be the UsageOKEvent and needs to also be returned to the original caller.
    return data


def send_usage_data(args=None):
    cred = ServicePrincipalCredentials(
        client_id=args.client_id,
        secret=args.client_secret,
        tenant=args.tenant_id)
    subscription_client = SubscriptionClient(cred)

    subs = subscription_client.subscriptions.list()

    managed_app_credential = ClientSecretCredential(
        client_id=args.client_id,
        client_secret=args.client_secret,
        tenant_id=args.tenant_id)

    metering = MeteringAPI(managed_app_credential)
    pretty_printer = pprint.PrettyPrinter(indent=4)
    for sub in subs:
        managed_app_client = managedapplications.ApplicationClient(credential=managed_app_credential,
                                                                   subscription_id=sub.subscription_id)
        apps = managed_app_client.applications.list_by_subscription()

        for app in apps:
            # At this point, we need to construct a raw URL to get the billing ID if one exists
            # This could be detected by the Offer ID (app.plan.product) and Plan ID (app.plan.name)
            if app.plan.product != args.offer_id.lower() and app.plan.name != args.plan_id.lower():
                continue

            timestamp = (datetime.now() - timedelta(hours=1)).isoformat()
            print("Sending usage event to app id {}".format(app.id))
            usage_event = UsageEvent(
                resource_uri=app.id,
                quantity=10,
                dimension='dim1',
                effective_start_time=timestamp,
                plan_id=app.plan.name
            )

            # Make sure your cls implementation returns the second parameter so that the result also appears
            # here. Otherwise, resp will always be None.
            resp = metering.metering_operations.post_usage_event(body=usage_event, cls=handle_usage_event_response)


# --tenant-id <tenant id> --client-id <client id> --client-secret <client secret>
def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Send metered charges to subscribers")
    parser.add_argument('--tenant-id', type=str, help='The Azure AD Tenant ID for the identity', required=True)
    parser.add_argument('--client-id', type=str, help='The Azure AD Service Principal client ID', required=True)
    parser.add_argument('--client-secret', type=str, help='The Azure AD Service Principal client secret', required=True)
    parser.add_argument('--offer-id', type=str, help='The Partner Center offer ID for the Managed Application offer',
                        required=True)
    parser.add_argument('--plan-id', type=str,
                        help='The Partner Center plan ID for the plan within the Managed Application offer',
                        required=True)

    try:
        args = parser.parse_args(args)
        send_usage_data(args)
    except:
        parser.print_usage()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())
