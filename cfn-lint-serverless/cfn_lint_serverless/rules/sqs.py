"""
Rules for SQS resources
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


class SqsNoRedrivePolicyRule(CloudFormationLintRule):
    """
    Ensure SQS queues have a redrive policy configured
    """

    id = "ES6000"  # noqa: VNE003
    shortdesc = "SQS No Redrive Policy"
    description = "Ensure SQS queues have a redrive policy configured"
    tags = ["sqs"]

    _message = "SQS Queue {} should have a RedrivePolicy property configured."

    def match(self, cfn):
        """
        Match against SQS queues without RedrivePolicy
        """

        matches = []

        for key, value in cfn.get_resources(["AWS::SQS::Queue"]).items():
            redrive_policy = value.get("Properties", {}).get("RedrivePolicy", None)

            if redrive_policy is None:
                matches.append(RuleMatch(["Resources", key], self._message.format(key)))

        return matches